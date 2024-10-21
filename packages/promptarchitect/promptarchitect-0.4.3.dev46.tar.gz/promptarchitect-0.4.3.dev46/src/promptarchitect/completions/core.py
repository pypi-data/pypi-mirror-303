"""Core types for completions."""

import json
import logging
import re
from abc import ABC, abstractmethod
from pathlib import Path

import dotenv
import marko
from marko.block import FencedCode

logger = logging.getLogger(__name__)


class Completion(ABC):
    """Abstract base class for completions."""

    def __init__(
        self,
        system_role: str,
        model: str,
        parameters: dict,
        provider_file: str,
    ) -> None:
        """Initialize the CompletionBase class with necessary configuration.

        Args:
        ----
            system_role (str): The role assigned to the system in the conversation.
            model (str): The model used for the API calls.
            parameters (dict): Additional parameters for the completion request.
            model_provider_config (str): Path to the model provider configuration file.

        """
        parameters = {} if parameters is None else parameters
        # Load all API keys from the .env file
        dotenv.load_dotenv()
        provider_file_path = Path(__file__).parent.parent / "provider" / provider_file

        with open(provider_file_path, "r") as config_pricing_file:
            self.provider_file = json.load(config_pricing_file)

        if model is None:
            # Search for the model name where the default is True
            model = self.get_default_model()

        # Check if the model is supported in the provider file as key or as alias
        self.model = self._get_model_name(self.provider_file, model)

        if self.model is None:
            error_message = (
                f"Model {model} not supported. "
                f"Check the provider file {provider_file}."
            )

            raise ValueError(error_message)

        self.system_role = system_role
        self.prompt = ""
        self.parameters = parameters
        self.cost = 0.0
        self.is_json = False
        self.test_path = ""
        self.response_message = ""
        self.duration = 0.0

    def _get_model_name(self, data: dict, search_string: str) -> str | None:
        for key, value in data.items():
            if key == search_string or value.get("alias") == search_string:
                return key
        return None

    def _calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        return (
            input_tokens * self.provider_file[self.model]["input_tokens"]
            + output_tokens * self.provider_file[self.model]["output_tokens"]
        )

    def get_default_model(self) -> str:
        """Get the default model from the provider file."""
        for model_name, model_config in self.provider_file.items():
            if model_config.get("default", False):
                return model_name
        return None

    @abstractmethod
    def completion(self, prompt: str) -> str:
        """Fetch the response for the provided prompt.

        Parameters
        ----------
        prompt: str
            The prompt to send to the API.

        Returns
        -------
        str
            The response from the API.

        """
        raise NotImplementedError()

    def to_dict(self) -> dict:
        """Convert the completion to a dictionary."""
        return {
            "system_role": self.system_role,
            "prompt": self.prompt,
            "model": self.model,
            "parameters": self.parameters if self.parameters else {},
            "cost": self.cost,
            "is_json": self.is_json,
            "test_path": self.test_path,
            "response_message": self.response_message,
            "duration": self.duration,
            "provider_file": self.provider_file,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Completion":
        """Create a completion from a dictionary."""
        completion = cls(
            system_role=data["system_role"],
            model=data["model"],
            parameters=data["parameters"],
            provider_file=data["provider_file"],
        )
        completion.prompt = data["prompt"]
        completion.cost = data["cost"]
        completion.is_json = data["is_json"]
        completion.test_path = data["test_path"]
        completion.response_message = data["response_message"]
        completion.duration = data["duration"]
        return completion

    def _extract_json(self, text: str) -> str:
        # Remove block quote characters
        text = text.replace('```json', '').replace('```', '').strip()

        # Regular expression pattern to find text that looks like JSON
        # This pattern assumes JSON starts with '[' or '{' and ends with ']' or '}'
        pattern = r"\{[\s\S]*\}|\[[\s\S]*\]"

        # Searching the text for JSON pattern
        match = re.search(pattern, text)

        if match:
            json_text = match.group(0)
            try:
                # Validating and returning the JSON object
                _ = json.loads(json_text)
                return json_text
            except json.JSONDecodeError:
                return "The extracted text is not valid JSON."
        else:
            return "No JSON found in the text."

    def _extract_markdown(self, markdown: str) -> str:
        ast = marko.parse(markdown)

        for element in ast.children:
            if isinstance(element, FencedCode):
                raw_text_element = element.children[0]
                return raw_text_element.children.strip()

        return markdown
