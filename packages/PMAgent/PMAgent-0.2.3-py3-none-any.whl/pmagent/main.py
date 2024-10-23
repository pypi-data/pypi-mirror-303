# **********************************************************************************************************************
# Created by Laxman Khatri - 20 Oct 2024 (JKL404)
# Updated by Laxman Khatri - 23 Oct 2024 (JKL404) - Added Groq API KEY SUPPORT AND OPTIMIZATION
# **********************************************************************************************************************

import os
import argparse
from pmagent import LLMInteractionManager


def setup_argument_parser():
    """Setup and return the argument parser with all necessary arguments."""
    parser = argparse.ArgumentParser(
        description="A PMAgent is an Expert Technical Professional with comprehensive knowledge across "
                   "multiple domains including Full Stack Development, Data Science, Data Analysis, "
                   "DevOps, and Machine Learning."
    )
    
    # Mandatory message argument - can be provided either positionally or with --message/-m
    message_group = parser.add_mutually_exclusive_group(required=True)
    message_group.add_argument('message', type=str, nargs='?',
                             help="The message describing what needs to be done.")
    message_group.add_argument('--message', '-m', type=str,
                             help="The message describing what needs to be done.")
    
    # Optional path argument - can be provided either positionally or with --path/-p
    parser.add_argument('--path', '-p', type=str,
                       default="",  # Default to current directory
                       help="The path to the file or folder to modify. Defaults to current directory.")
    
    return parser


def validate_api_keys():
    """Validate that at least one API key is present."""
    openai_api_key = os.getenv("OPENAI_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")
    
    if not openai_api_key and not groq_api_key:
        raise ValueError(
            "Error: API key is not set. Please set either OPENAI_API_KEY or GROQ_API_KEY "
            "environment variable."
        )
    
    return openai_api_key, groq_api_key


def main():
    # Parse arguments
    parser = setup_argument_parser()
    args = parser.parse_args()
    
    # Get the message from either positional or named argument
    message = args.message if args.message is not None else args.message
    
    # Validate API keys
    try:
        openai_api_key, groq_api_key = validate_api_keys()
    except ValueError as e:
        print(str(e))
        return 1
    
    # Initialize and run the LLM interaction
    llm_interaction_manager = LLMInteractionManager(
        openai_api_key=openai_api_key,
        groq_api_key=groq_api_key,
    )

    llm_interaction_manager.interact_with_llm(
        user_message=message,
        path=args.path
    )
    
    print("\nDONE :)")
    return 0


if __name__ == "__main__":
    exit(main())