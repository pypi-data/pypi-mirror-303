# **********************************************************************************************************************
# Created by Laxman Khatri - 20 Oct 2024 (JKL404)
# Updated by Laxman Khatri - 23 Oct 2024 (JKL404) - Added Groq API KEY SUPPORT AND OPTIMIZATION
# **********************************************************************************************************************

import os
from pmagent import LLMInteractionManager


def main():
    #  calling the agent
    import argparse

    parser = argparse.ArgumentParser(description="PMAgent: A Python agent for refactoring and modifying code using OpenAI.")
    parser.add_argument('user_message', type=str, help="The message describing what needs to be done.")
    parser.add_argument('path', type=str, help="The path to the file or folder to modify.")

    args = parser.parse_args()
    
    # Make sure your API key is in the environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not openai_api_key and not groq_api_key:
        print("Error: API key is not set. Please set the environment variable OPENAI_API_KEY | GROQ_API_KEY.")
        exit(1)
    llm_interaction_manager = LLMInteractionManager(
        openai_api_key=openai_api_key,
        groq_api_key=groq_api_key,
    )

    llm_interaction_manager.interact_with_llm(
        user_message=args.user_message,
        path=args.path
    )
    print("\nDONE :)")


if __name__ == "__main__":
    main()
