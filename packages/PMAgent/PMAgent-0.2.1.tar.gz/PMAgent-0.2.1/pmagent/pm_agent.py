# **********************************************************************************************************************
# Created by Laxman Khatri - 20 Oct 2024 (JKL404)
# Updated by Laxman Khatri - 23 Oct 2024 (JKL404) - Added Groq API KEY SUPPORT AND OPTIMIZATION
# **********************************************************************************************************************

import os
import mistune  # add this library
import re
import logging
import tempfile
import subprocess
import traceback
from openai import OpenAI
from groq import Groq
from typing import Tuple, Optional, Dict, List
from .pm_script import (
    SYSTEM_PROMPT,
    PRE_DEFINED_FILE_TYPE,
    dedent_text,
)

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
# List of libraries to suppress DEBUG messages
libraries_to_suppress = ['openai._base_client', 'groq._base_client', 'httpcore', 'httpx']
for library in libraries_to_suppress:
    logging.getLogger(library).setLevel(logging.WARNING)
# Your application's logger
logger = logging.getLogger(__name__)

# From ENV
OPENAI_DEFAULT_CONFIG = {
    "model": "gpt-4o"
}
GROQ_DEFAULT_CONFIG = {
    "model": "llama-3.1-70b-versatile"
}

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")
TEMPERATURE = os.getenv("TEMPERATURE")
TOP_P = os.getenv("TOP_P")
MAX_TOKENS = os.getenv("MAX_TOKENS")


class CodeRefactorManager:
    def __init__(self, open_ai_key, grop_api_key, config:dict = {}):
        self.logger = logger
        self.config = config
        # Dictionary to map language to file extension and interpreter
        self.language_map = {
            'python': {'file_extension': '.py', 'interpreter': 'python'},
            'bash': {'file_extension': '.sh', 'interpreter': 'bash'}
        }
        self.client, self.default_model = self._create_client_and_model(open_ai_key, grop_api_key)

    def _create_client_and_model(self, open_ai_key: Optional[str], grop_api_key: Optional[str]) -> Tuple:
        """
        Creates and returns the appropriate client and default model based on the provided API keys.

        Args:
            open_ai_key (Optional[str]): API key for OpenAI.
            grop_api_key (Optional[str]): API key for Groq.

        Returns:
            Tuple: A tuple containing the client instance and the default model string.

        Raises:
            ValueError: If neither API key is provided.
        """
        options: Dict[str, Tuple] = {
            'openai': (OpenAI(api_key=open_ai_key), OPENAI_DEFAULT_CONFIG['model']) if open_ai_key else (None, None),
            'groq': (Groq(api_key=grop_api_key), GROQ_DEFAULT_CONFIG['model']) if grop_api_key else (None, None)
        }

        for key in ['openai', 'groq']:
            client, model = options[key]
            if client:
                self.logger.info(f"** LLM Type ** : {key.upper()}")
                return client, model

    def code_interpret(self, code):
        """
        Detect and execute multiple code blocks (Python, Bash, etc.) from the input code.
        Automatically detects language from markdown-style code blocks and handles both.
        """
        temp_file_name = ""
        try:

            # Find all code blocks with the language and the content
            code_blocks = re.findall(r"```(\w+)\n(.*?)\n```", code, re.DOTALL)

            if not code_blocks:
                raise ValueError("No valid code blocks found")

            for language, code_content in code_blocks:
                language = language.lower()

                if language in self.language_map:
                    file_extension = self.language_map[language]['file_extension']
                    interpreter = self.language_map[language]['interpreter']
                else:
                    raise ValueError(f"Unsupported language: {language}")

                # Create a temporary file for the code
                with tempfile.NamedTemporaryFile(mode='w', suffix=file_extension, delete=False) as temp_file:
                    temp_file.write(code_content)
                    temp_file.flush()
                    temp_file_name = temp_file.name

                # Execute the code in a subprocess and capture output
                result = subprocess.run([interpreter, temp_file_name], capture_output=True, text=True)

                # Output results
                if result.returncode != 0:
                    self.logger.info(f"Execution failed for {language} with error:\n{result.stderr}")
                else:
                    self.logger.info(f"Execution succeeded for {language} with output:\n{result.stdout}")

        except Exception as e:
            self.logger.info(f"Error occurred: {e}")
            traceback.print_exc()
        finally:
            # Optionally, delete the temporary file after execution
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)

    def run_model(self, messages: List[dict]):
        """
        Execute Query with LLM
        """
        # NOTE: DONOT CHANGE THIS PART
        params = {
            "model": self.config.get('model') or self.default_model,
            "temperature": float(self.config.get('temperature')) if self.config.get('temperature') else None,
            "top_p": float(self.config.get('top_p')) if self.config.get('top_p') else None,
            "max_tokens": int(self.config.get('max_tokens')) if self.config.get('max_tokens') else None,
            "messages": messages,
            
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.chat.completions.create(
            **params
        )
        # END NOTE
        return response

    def extract_code_to_dict(self, markdown_content):
        """
        Extract code blocks and return them in a dictionary where the keys are file paths
        and the values are the code block content.
        
        Args:
            markdown_content (str): The full Markdown content containing file paths and code blocks.
        
        Returns:
            dict: A dictionary with file paths as keys and code block content as values.
        
        Expected response format:
        ```python
        # File: path/to/file1.py
        {code}

        # File: path/to/file2.py
        {code}
        ```
        """
        # Create a Markdown parser instance that outputs an AST
        markdown = mistune.create_markdown(renderer='ast')

        # Parse the Markdown content into an AST (list of tokens)
        parsed_blocks = markdown(markdown_content)
        
        # Initialize the result dictionary
        files_dict = {}
        current_file_path = None
        current_code = []

        for block in parsed_blocks:
            # Check if this block is specifying a new file (heading)
            if block['type'] == 'heading' and 'children' in block:
                heading_text = "".join(child.get('raw', '') for child in block['children'] if child['type'] == 'text')
                self.logger.info(f"Detected heading: {heading_text}")  # Debugging print

                # Match file heading and extract file path
                file_match = re.match(r"File:\s*(.+)", heading_text)  # Updated regex
                if file_match:
                    self.logger.info(f"File matched: {file_match.group(1)}")  # Debugging print

                    # If a current file is being collected, save it to the dictionary
                    if current_file_path and current_code:
                        self.logger.info(f"Saving code for: {current_file_path}")  # Debugging print
                        files_dict[current_file_path] = "\n".join(current_code)

                    # Set the new file path and reset current_code
                    current_file_path = file_match.group(1).strip()
                    current_code = []  # Reset code block collection for the new file

            elif block['type'] == 'block_code':
                # Append the code block content to current_code
                if current_file_path:
                    current_code.append(block.get('raw', ''))

        # After looping through, save the final collected file if any
        if current_file_path and current_code:
            self.logger.info(f"Saving final code for: {current_file_path}")  # Debugging print
            files_dict[current_file_path] = "\n".join(current_code)

        return files_dict


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
                    file_type = FileManager.get_file_type(file_path)
                    if file_content is not None:
                        folder_contents.append(f"File: {file_path}\n```{file_type}\n{file_content}\n```")
            return "\n\n".join(folder_contents)
        except Exception as e:
            self.logger.error(f"Error reading folder contents from {folder_path}: {e}")
            return None

    def _validate_and_create_directory(self, dir_path):
        """
        Validate and create directory if it doesn't exist.
        If dir_path is a file, it will remove the file part and create only the directory.

        Args:
            dir_path (str): The directory path or file path to validate.

        Returns:
            str: The validated directory path.
        
        Raises:
            OSError: If there's an OS-related error in creating the directory.
        """
        # Remove any leading/trailing whitespace
        dir_path = dir_path.strip()
        
        # Check if dir_path points to a file (i.e., if the base name contains a file extension)
        if os.path.isfile(dir_path) or os.path.splitext(dir_path)[1]:
            # Extract directory part from the file path
            dir_path = os.path.dirname(dir_path)

        if not os.path.exists(dir_path):
            try:
                os.makedirs(dir_path, exist_ok=True)  # Create the directory
                self.logger.info(f"Directory {dir_path} created.")
            except OSError as e:
                error_msg = f"OS error occurred while creating directory {dir_path}"
                self.logger.error(f"{error_msg}: {e}")
                raise OSError(error_msg) from e
        else:
            self.logger.info(f"Directory {dir_path} already exists.")
        return dir_path

    def write_to_file(self, file_path, content, default_directory=None):
        """
        Helper function to write content to a file.
        
        Args:
            file_path (str): The path to the file.
            content (str): The content to write to the file.
            default_directory (str, optional): Default directory to use if no directory is specified in file_path.
                                            Will be created if it doesn't exist.
            
        Returns:
            str: The actual path where the file was written.
            
        Raises:
            ValueError: If file_path is empty or None.
            ValueError: If default_directory is not a valid string.
            ValueError: If no filename is specified in file_path.
            PermissionError: If there are permission issues.
            OSError: If there are other OS-level errors.
        """
        # Validate file_path
        if not file_path:
            raise ValueError("file_path cannot be empty or None")
        
        # Get the filename and directory path
        filename = os.path.basename(file_path)
        if not filename:
            raise ValueError("No filename specified in file_path")
        
        dir_path = os.path.dirname(file_path)
        
        try:
            # If no directory path and default_directory is provided, use default_directory
            if not dir_path and default_directory:
                # Validate and create default directory
                validated_dir = self._validate_and_create_directory(default_directory)
                file_path = os.path.join(validated_dir, filename)
                dir_path = validated_dir
            # If directory path exists in file_path, create it
            elif dir_path:
                # Validate and create the directory path
                validated_dir = self._validate_and_create_directory(dir_path)
                file_path = os.path.join(validated_dir, filename)
            
            # Write the content to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            self.logger.info(f"New changes have been successfully written to {file_path}")
            return file_path
        
        except PermissionError as e:
            error_msg = f"Permission denied when accessing {file_path}"
            self.logger.error(f"{error_msg}: {e}")
            raise PermissionError(error_msg) from e
        
        except OSError as e:
            error_msg = f"OS error occurred while writing to {file_path}"
            self.logger.error(f"{error_msg}: {e}")
            raise OSError(error_msg) from e
        
        except Exception as e:
            error_msg = f"Unexpected error occurred while writing to {file_path}"
            self.logger.error(f"{error_msg}: {e}")
            raise Exception(error_msg) from e

    @staticmethod
    def get_file_type(file_name):
        if not file_name:
            return ""
        file_extension = file_name.split('.')[-1].lower()
        return PRE_DEFINED_FILE_TYPE.get(file_extension, file_extension)


class LLMInteractionManager:
    def __init__(self, openai_api_key=None, groq_api_key=None, config: dict = {}):
        self.logger = logger
        self.code_refactor_manager = CodeRefactorManager(
            open_ai_key=OPENAI_API_KEY or openai_api_key,
            grop_api_key=GROQ_API_KEY or groq_api_key,
            config=self.prepare_config(
                config=config,
            )
        )
        self.file_manager = FileManager()

    def prepare_config(self, config:dict = {}):
        """
        Prepare Config for LLM
        """
        if config:
            self.logger.info(f"Using User LLM Config {config}")
            return config
        # FROM ENV
        config = {
            "temperature": float(TEMPERATURE) if TEMPERATURE else None,
            "top_p": float(TOP_P) if TOP_P else None,
            "max_tokens": int(MAX_TOKENS) if MAX_TOKENS else None,
            "model": MODEL,
        }
        # Remove unnecessary None
        config = {k: v for k, v in config.items() if v is not None}
        self.logger.info(f"Using Default Config {config}")
        return config

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
                    file_type = FileManager.get_file_type(path)
                    user_message = f"{user_message}\n\nThe current content of the file is:\n```{file_type}\n{file_content}\n```"
                else:
                    self.logger.error("Failed to read file content.")
                    return None
            else:
                self.logger.error(f"Provided path {path} does not exist.")
        else:
            self.logger.error("No file or folder path provided., Skipping Reading..")
        return user_message

    def interact_with_llm(self, user_message, path=None):
        """
        Communicate with the LLM to fulfill the user request.
        """
        self.logger.info(f"Received user message: {user_message}")

        # Prepare user message with file or folder content
        prepared_message = self.prepare_user_message(user_message, path)
        if prepared_message is None:
            return

        messages = [
            {"role": "system", "content": dedent_text(SYSTEM_PROMPT)},
            {"role": "user", "content": prepared_message},
        ]

        # NOTE: DONOT CHANGE THIS PART
        response = self.code_refactor_manager.run_model(
            messages=messages,
        )
        # END NOTE

        response_message = response.choices[0].message
        response_content = response_message.content
        # self.logger.debug(response_content)
        file_modifications = self.code_refactor_manager.extract_code_to_dict(
            markdown_content=response_content
        )
        # If File FOund: Save it
        if file_modifications:
            # Apply changes to individual files
            for file_path, code in file_modifications.items():
                self.file_manager.write_to_file(
                    file_path=file_path,
                    content=code,
                    default_directory=path
                )
            self.logger.info("File Saved DONE :)")
            return
        
        # If no modifications are returned, execute the code interpretation
        self.code_refactor_manager.code_interpret(response_content)
