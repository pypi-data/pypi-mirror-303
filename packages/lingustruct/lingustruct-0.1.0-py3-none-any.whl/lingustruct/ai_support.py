import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AISupport:
    def __init__(self, api_key=None, default_model="llama-3.2-90b-text-preview"):
        # Get API key from argument or environment variable
        self.api_key = api_key or os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError(
                "Groq API key must be provided or set in the GROQ_API_KEY environment variable."
            )

        # Set the API endpoint (Replace with actual endpoint)
        self.endpoint = "https://api.groq.com/v1/completions"
        self.default_model = default_model

    def complete_design(
        self,
        section: str,
        content: str,
        model: str = None,
        max_tokens: int = 150,
        temperature: float = 0.7,
        prompt_template: str = None
    ):
        # Use the specified model or the default model
        selected_model = model or self.default_model

        # Build the prompt using the provided template or the default one
        prompt = prompt_template or (
            f"Complete the following section for system design:\n"
            f"Section: {section}\nContent: {content}\n"
        )

        # Set request headers and payload
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": selected_model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        try:
            # Send POST request to the Groq API
            response = requests.post(self.endpoint, json=payload, headers=headers)
            response.raise_for_status()  # Raise exception for non-200 status

            # Parse the response
            data = response.json()
            completion = data.get("choices", [{}])[0].get("text", "").strip()
            return completion
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.ConnectionError:
            return "Connection error: Failed to connect to the API."
        except requests.exceptions.Timeout:
            return "Timeout error: The request timed out."
        except requests.exceptions.RequestException as req_err:
            return f"An error occurred: {req_err}"
        except Exception as err:
            return f"An unexpected error occurred: {err}"
