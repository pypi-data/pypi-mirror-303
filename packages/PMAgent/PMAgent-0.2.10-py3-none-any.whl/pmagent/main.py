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
    parser.add_argument('path', type=str, nargs='?', default="", 
                        help="The path to the file or folder to modify.")
    parser.add_argument('--path', '-p', type=str, 
                        help="The path to the file or folder to modify.")
    
    # Add LLM type selection argument - default will be determined based on available API keys
    parser.add_argument('--llm-type', '-l', type=str, choices=['openai', 'groq'], 
                        help="Choose the LLM provider (openai or groq). If not specified, "
                             "uses whichever API key is available.")
    
    return parser


def detect_available_llm():
    """
    Detect which LLM API keys are available and choose the default.
    
    Returns:
        tuple: (default_llm_type, api_key)
    """
    # Check for available API keys
    openai_key = os.getenv("OPENAI_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")
    
    if not openai_key and not groq_key:
        raise ValueError(
            "Error: No API keys found. Please set either OPENAI_API_KEY or GROQ_API_KEY "
            "environment variable."
        )
    
    # If both keys are available and no specific type is requested,
    # prefer OpenAI (you can change this default preference)
    if openai_key:
        return 'openai', openai_key
    return 'groq', groq_key


def get_api_key(llm_type):
    """
    Get the appropriate API key based on LLM type.
    
    Args:
        llm_type (str): The LLM provider type ('openai' or 'groq')
        
    Returns:
        str: The API key
    """
    api_key = os.getenv(f"{llm_type.upper()}_API_KEY")
    
    if not api_key:
        raise ValueError(
            f"Error: {llm_type.upper()}_API_KEY environment variable is not set."
        )
    
    return api_key


def main():
    # Parse arguments
    parser = setup_argument_parser()
    args = parser.parse_args()
    
    # Get the message and path from either positional or named argument
    message = args.message
    path = args.path
    llm_type = args.llm_type
    
    try:
        if llm_type:
            # If LLM type is specified, use that
            api_key = get_api_key(llm_type)
        else:
            # Otherwise, auto-detect based on available API keys
            llm_type, api_key = detect_available_llm()
            
    except ValueError as e:
        print(str(e))
        return 1
    
    # Initialize and run the LLM interaction
    kwargs = {
        f"{llm_type}_api_key": api_key,  # Only pass the relevant API key
        "llm_type": llm_type  # Pass the LLM type to the manager
    }
    
    llm_interaction_manager = LLMInteractionManager(**kwargs)

    llm_interaction_manager.interact_with_llm(
        user_message=message,
        path=path
    )
    
    print(f"\nDONE :) (Using {llm_type.upper()})")
    return 0


if __name__ == "__main__":
    exit(main())
