
#**********************************************************************************************************************
# Created by Laxman Khatri - 20 Oct 2024 (JKL404)
#**********************************************************************************************************************

import os
from pmagent import LLMInteractionManager


def main():
    #  calling the agent
    import argparse

    parser = argparse.ArgumentParser(description="PMAgent: A Python agent for refactoring and modifying code using OpenAI.")
    parser.add_argument('user_message', type=str, help="The message describing what needs to be done.")
    parser.add_argument('path', type=str, help="The path to the file or folder to modify.")

    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")  # Make sure your API key is in the environment variables
    if not api_key:
        print("Error: API key is not set. Please set the environment variable OPENAI_API_KEY.")
        exit(1)
    llm_interaction_manager = LLMInteractionManager(api_key=api_key)

    llm_interaction_manager.interact_with_llm(user_message=args.user_message, path=args.path)


if __name__ == "__main__":
    main()
