import os
import sys
import requests 

from dotenv import load_dotenv  

# ── STEP 1: LOAD ENVIRONMENT VARIABLES ───
load_dotenv()


# ── STEP 2: THE CORE FUNCTION ──

def ask_ai(prompt: str) -> str:
    """
    Accepts a user prompt, sends it to the OpenRouter AI API,
    extracts the AI's response, and returns it as a string.

    Args:
        prompt (str): The user's question or instruction.

    Returns:
        str: The AI-generated response text.
    """

    api_key = os.getenv("OPENROUTER_API_KEY")
    "meta-llama/llama-3-8b-instruct"
    model = os.getenv("MODEL_NAME")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found."
            "Make sure it is set in your .env file."
        )

    if not model:
        raise ValueError(
            "MODEL_NAME not found."
            "Make sure it is set in your .env file."
        )

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",  
        "Content-Type": "application/json",     
    }


    payload = {
        "model": model,   
        "messages": [
            {
                "role": "user",  
                "content": prompt     
            }
        ]
    }

    # ── Send the request and handle errors ──
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        raise TimeoutError("The request timed out. Please try again.")

    except requests.exceptions.HTTPError as e:
        raise ConnectionError(f"API request failed: {e}")

    data = response.json()

    ai_response = data["choices"][0]["message"]["content"]

    return ai_response


# ── STEP 3: CLI (COMMAND LINE INTERFACE) ENTRY POINT ──

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(" Error: Please provide a prompt as a command-line argument.")
        print("  Usage: python main.py \"Your question here\"")
        sys.exit(1)  
    
    user_prompt = sys.argv[1]

    print(f"\nSending prompt to AI: \"{user_prompt}\"\n")
    print("─" * 50)


    try:
        result = ask_ai(user_prompt)
        print(f"AI Response:\n\n{result}")

    except (ValueError, ConnectionError, TimeoutError) as e:
        print(e)
        sys.exit(1)

    print("\n" + "─" * 50)
