"""Completion implementation for the Anthropic API."""

import json
import logging
import os
import timeit

import anthropic
import opentelemetry.trace

from promptarchitect.completions.core import Completion

# Configuring logging
logger = logging.getLogger(__name__)
tracer = opentelemetry.trace.get_tracer(__name__)


class AnthropicCompletion(Completion):
    """Completion logic for the Anthropic API."""

    is_json: bool = False
    is_markdown: bool = False

    def __init__(
        self,
        system_role: str = "",
        model: str = None,
        parameters: dict = None,
    ) -> None:
        """Initialize a new instance of the OllamaCompletion class.

        Arguments
        ---------
        system_role: str
            The role of the system in the conversation.
        model: str
            The model to use for the completion.
        parameters: dict
            Additional parameters for the completion request.
        """
        super().__init__(system_role, model, parameters, "anthropic.json")
        self.api_key = None

    def _get_api_key(self) -> str:
        api_key = os.getenv("CLAUDE_API_KEY")
        if not api_key:
            error_message = "API key for Claude.ai is required. Set CLAUDE_API_KEY."
            raise ValueError(error_message)
        return api_key

    def _prepare_request(self, prompt: str) -> dict:
        request = {
            "model": self.model,
            "messages": [{"role": "user", "content": f"{self.system_role} {prompt}"}],
        }

        self._handle_response_format()

        for key, value in self.parameters.items():
            if key in ["temperature", "top_p", "max_tokens"] and value is not None:
                request[key] = self._cast_parameter_value(key, value)

        request["max_tokens"] = request.get("max_tokens", self._default_max_tokens())

        return request

    def _handle_response_format(self) -> None:
        if "response_format" in self.parameters:
            if self.parameters["response_format"].strip() in ["json", "json_object"]:
                self.parameters["response_format"] = {"type": "json_object"}
                self.is_json = True
            elif self.parameters["response_format"].strip() == "markdown":
                self.is_markdown = True

    def _cast_parameter_value(self, key: str, value: any) -> int | float:
        if value is None:
            return None

        if key in ["temperature", "top_p"]:
            return float(value)

        if key == "max_tokens":
            return int(value)

        error_message = f"Invalid parameter value for {key}: {value}"
        raise ValueError(error_message)

    def _default_max_tokens(self) -> int:
        if "claude-3-5-sonnet-20240620" in self.model:
            return 8129
        return 4096

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
        with tracer.start_as_current_span("ClaudeCompletion.completion") as span:
            span.set_attribute("promptarchitect.provider.id", "antrhopic")
            span.set_attribute("promptarchitect.model.id", self.model)

            self.api_key = self._get_api_key()
            self.prompt = prompt
            self.client = anthropic.Client(api_key=self.api_key)

            request = self._prepare_request(prompt)

            try:
                self._execute_request(request)
            except anthropic.BadRequestError as e:
                self._handle_bad_request(e)
            except anthropic.AnthropicError as e:
                self._handle_anthropic_error(e)
            except Exception as e:
                error_message = f"An unexpected error occurred: {str(e)}"
                raise RuntimeError(error_message) from e

            return self._process_response()

    def _execute_request(self, request: dict) -> None:
        start = timeit.default_timer()
        response = self.client.messages.create(**request)
        end = timeit.default_timer()

        self.duration = end - start
        self._response = dict(response)

    def _handle_bad_request(self, error: anthropic.BadRequestError) -> None:
        error_data = json.loads(error.response.text)
        error_message = error_data.get("error", {}).get(
            "message",
            "An unknown error occurred.",
        )
        error_type = error_data.get("error", {}).get("type", "unknown_error")
        error_message = f"Error Type: {error_type} - {error_message}"

        raise ValueError(error_message)

    def _handle_anthropic_error(self, error: anthropic.AnthropicError) -> None:
        error_data = json.loads(error.response.text)
        error_message = error_data.get("error", {}).get(
            "message",
            "An unknown error occurred.",
        )
        error_type = error_data.get("error", {}).get("type", "unknown_error")
        error_message = f"Error Type: {error_type} - {error_message}"
        raise RuntimeError(error_message)

    def _process_response(self) -> str:
        self.cost = self._calculate_cost(
            self._response["usage"].input_tokens,
            self._response["usage"].output_tokens,
        )

        self.input_tokens = self._response["usage"].input_tokens
        self.output_tokens = self._response["usage"].output_tokens

        self.response_message = self._response["content"][0].text

        if self.is_markdown:
            self.response_message = self._extract_markdown(self.response_message)

        if self.is_json:
            self.response_message = self._extract_json(self.response_message)

        return self.response_message

    def to_dict(self) -> dict:
        """Convert the object to a dictionary."""
        data = super().to_dict()
        data.update(
            {
                "provider_file": "claude.json",
            },
        )
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "AnthropicCompletion":
        """Create an instance of the class from a dictionary."""
        obj = cls(
            system_role=data["system_role"],
            model=data["model"],
            parameters=data["parameters"],
        )
        obj.prompt = data.get("prompt", "")
        obj.cost = data.get("cost", 0.0)
        obj.is_json = data.get("is_json", False)
        obj.test_path = data.get("test_path", "")
        obj.response_message = data.get("response_message", "")
        obj.duration = data.get("duration", 0.0)
        return obj
