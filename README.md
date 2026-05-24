# AI Prompt CLI

A simple Python command-line application that sends prompts to the OpenRouter AI API and returns AI-generated responses.

## Features

- Easy-to-use CLI interface for interacting with AI models
- Supports any model available through OpenRouter
- Error handling for API failures, timeouts, and missing configuration
- Environment variable configuration for secure API key management

## Prerequisites

- Python 3.7 or higher
- An OpenRouter API key (get one at https://openrouter.ai)

## Installation

1. Clone or download this project
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a .env file in the project root with your configuration:
```
OPENROUTER_API_KEY=your_api_key_here
MODEL_NAME=your-model-name-here
```

## Usage
Run the application with a prompt as an argument:

```
python main.py "What is the capital of France?"
```
Example Output

Sending prompt to AI: "What is the capital of France?"

──────────────────────────────────────────────────

AI Response:

The capital of France is Paris.

──────────────────────────────────────────────────

## Configuration

### Environment Variables
```
OPENROUTER_API_KEY (required): Your OpenRouter API key for authentication
MODEL_NAME (required): The AI model to use
(See OpenRouter Models for available models.)
```
### Error Handling
The application handles the following errors gracefully:

- Missing API Key: Displays error if OPENROUTER_API_KEY is not set
- Missing Model: Displays error if MODEL_NAME is not set
- Network Timeout: Handles requests that exceed 30 seconds
- API Errors: Displays HTTP error messages from the API
- Missing Prompt: Shows usage instructions if no prompt is provided

## License
MIT
   