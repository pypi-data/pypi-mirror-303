
#**********************************************************************************************************************
# Created by Laxman Khatri - 20 Oct 2024 (JKL404)
#**********************************************************************************************************************

import os
import re
import logging
import tempfile
import traceback
from openai import OpenAI

# Setting up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# From ENV
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4o"


class CodeRefactorManager:
    SYSTEM_PROMPT = """
    You are a Python developer. Your task is to fulfill user requests related to Python code modification, enhancement, and generation. Only use a specific detailed prompt when provided by the user. The following are general instructions:

    - Format your response using Markdown with the appropriate code block notation.

    Generally, you follow these rules:
    - ALWAYS FORMAT YOUR RESPONSE IN MARKDOWN.
    - ALWAYS RESPOND ONLY WITH CODE IN CODE BLOCK LIKE THIS:
      ```python
      {code}
      ```
    - If you are changing any files, YOU MUST WRITE CODE THAT SAVES THE CHANGES TO THE SAME RESPECTIVE FILE. This is extremely important.
    - IF YOUR MODIFICATIONS ARE SPECIFIC TO A CERTAIN BLOCK OR FUNCTION, ONLY MODIFY THAT SPECIFIC BLOCK. DO NOT RETURN THE ENTIRE FILE UNLESS NECESSARY. ENSURE THAT THE RETURNED CODE CAN BE INTEGRATED INTO THE EXISTING SCRIPT WITHOUT BREAKING OTHER PARTS.
    - ENSURE THAT ANY CODE MODIFICATION SCRIPT IS IDEMPOTENT AND CAN BE EXECUTED MULTIPLE TIMES WITHOUT BREAKING EXISTING FUNCTIONALITY.
    - IF YOU ARE MODIFYING MULTIPLE FILES, RETURN THE RESPONSE IN THE FOLLOWING FORMAT FOR EACH FILE:
      # File: path/to/file.py
      ```python
      {modified_code}
      ```
    """

    def __init__(self, api_key=OPENAI_API_KEY):
        self.client = OpenAI(api_key=api_key)
        self.pattern = re.compile(r"```[a-zA-Z]*\n(.*?)\n```", re.DOTALL)
        self.logger = logger

    def save_code_to_file(self, code, file_path):
        """
        Save the given code to the specified file, removing any Markdown code block notation.
        """
        # Remove the Markdown code block notation if present
        code = re.sub(r"```[a-zA-Z]*\n(.*?)\n```", r"\1", code, flags=re.DOTALL)
        try:
            with open(file_path, 'w') as file:
                file.write(code)
            self.logger.info(f"Code has been successfully written to {file_path}")
        except Exception as e:
            self.logger.error(f"Error occurred while writing to the file {file_path}: {e}")

    def extract_code_block(self, llm_response):
        """
        Extract the Python code block from the LLM response.
        """
        match = self.pattern.search(llm_response)
        if match:
            code = match.group(1)
            self.logger.debug(f"Extracted code block: {code}")
            return code
        self.logger.warning("No Python code block found in LLM response.")
        return ""

    def code_interpret(self, code):
        """
        Execute the given code in a controlled environment.
        """
        try:
            # Remove the Markdown code block notation if present
            code = re.sub(r"```python\n(.*?)\n```", r"\1", code, flags=re.DOTALL)
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
                temp_file.write(code)
                temp_file.flush()
                os.system(f"python {temp_file.name}")
        except Exception as e:
            print(f"Error occurred: {e}")
            traceback.print_exc()


class FileManager:
    def __init__(self):
        self.logger = logger

    def read_file_contents(self, file_path):
        """
        Read the content from a given file path.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            self.logger.error(f"Error reading the file {file_path}: {e}")
            return None

    def read_folder_contents(self, folder_path):
        """
        Read the contents of all files in a directory.
        """
        folder_contents = []
        try:
            for root, _, files in os.walk(folder_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    file_content = self.read_file_contents(file_path)
                    if file_content is not None:
                        folder_contents.append(f"File: {file_path}\n```python\n{file_content}\n```")
            return "\n\n".join(folder_contents)
        except Exception as e:
            self.logger.error(f"Error reading folder contents from {folder_path}: {e}")
            return None


class LLMInteractionManager:
    def __init__(self, api_key=OPENAI_API_KEY):
        self.code_refactor_manager = CodeRefactorManager(api_key=api_key)
        self.file_manager = FileManager()
        self.logger = logger

    def prepare_user_message(self, user_message, path):
        """
        Prepare the user message by appending the file or folder content.
        """
        if path:
            if os.path.isdir(path):
                folder_contents = self.file_manager.read_folder_contents(path)
                if folder_contents is not None:
                    user_message = f"{user_message}\n\nThe current content of the files is:\n{folder_contents}"
                else:
                    self.logger.error("Failed to read folder contents.")
                    return None
            elif os.path.isfile(path):
                file_content = self.file_manager.read_file_contents(path)
                if file_content is not None:
                    user_message = f"{user_message}\n\nThe current content of the file is:\n```python\n{file_content}\n```"
                else:
                    self.logger.error("Failed to read file content.")
                    return None
            else:
                self.logger.error(f"Provided path {path} does not exist.")
                return None
        else:
            self.logger.error("No valid file or folder path provided.")
            return None
        return user_message

    def interact_with_llm(self, user_message, path=None, model_name=MODEL_NAME):
        """
        Communicate with the LLM to fulfill the user request.
        """
        self.logger.info(f"Received user message: {user_message}")

        # Prepare user message with file or folder content
        prepared_message = self.prepare_user_message(user_message, path)
        if prepared_message is None:
            return

        messages = [
            {"role": "system", "content": self.code_refactor_manager.SYSTEM_PROMPT},
            {"role": "user", "content": prepared_message},
        ]

        # NOTE: DONOT CHANGE THIS PART
        response = self.code_refactor_manager.client.chat.completions.create(
            model=model_name,
            messages=messages,
        )
        # END NOTE

        response_message = response.choices[0].message
        response_content = response_message.content
        file_modifications = self.parse_llm_response(response_content)

        if not file_modifications:
            # If no modifications are returned, execute the code interpretation
            self.code_refactor_manager.code_interpret(response_content)
        else:
            # Apply changes to individual files
            for file_path, code in file_modifications.items():
                if not os.path.exists(file_path):
                    # Create new file if it does not exist
                    self.code_refactor_manager.save_code_to_file(code, file_path)
                    self.logger.info(f"New file has been created: {file_path}")
                elif file_path.endswith('.py'):
                    self.code_refactor_manager.save_code_to_file(code, file_path)
                    # Execute the returned Python code if it does not contain the main block
                    # if "__name__ == \"__main__\"" not in code:
                    #     self.code_refactor_manager.code_interpret(code)

    def parse_llm_response(self, response_content):
        """
        Parse the LLM response to extract the changes for each file.
        Expected response format:
        ```python
        # File: path/to/file1.py
        {code}

        # File: path/to/file2.py
        {code}
        ```
        """
        file_modifications = {}
        current_file = None
        current_code_lines = []

        for line in response_content.splitlines():
            file_match = re.match(r"# File: (.+)", line)
            if file_match:
                # Save the current file's code if we're switching to a new file
                if current_file and current_code_lines:
                    file_modifications[current_file] = "\n".join(current_code_lines)

                # Start parsing the new file
                current_file = file_match.group(1).strip()
                current_code_lines = []
            elif current_file:
                current_code_lines.append(line)

        # Add the last file's code to the modifications
        if current_file and current_code_lines:
            file_modifications[current_file] = "\n".join(current_code_lines)

        return file_modifications
