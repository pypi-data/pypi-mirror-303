"""Completion implementation for the Ollama API."""

import logging
import re
import timeit
from typing import List

import ollama
import opentelemetry.trace
import requests

from promptarchitect.completions.core import Completion

# Configuring logging
logger = logging.getLogger(__name__)
tracer = opentelemetry.trace.get_tracer(__name__)


class OllamaCompletion(Completion):
    """Completion logic for the Ollama API."""

    is_markdown = False
    is_json = False

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
        super().__init__(system_role, model, parameters, "ollama.json")

        # Check if the model is downloaded and available
        self.model = self._resolve_model(model)

        self.api_key = None

    def _is_ollama_server_running(self, url: str = "http://localhost:11434") -> bool:
        try:
            response = requests.get(url, timeout=1)
            return response.status_code == requests.codes.ok
        except requests.ConnectionError:
            return False

    def _list_models(self) -> List[str]:
        result = ollama.list()
        return [model["name"] for model in result["models"]]

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
        with tracer.start_as_current_span("OllamaCompletion.completion") as span:
            span.set_attribute("promptarchitect.provider.id", "ollama")
            span.set_attribute("promptarchitect.model.id", self.model)

            # Check if Ollama server is running
            if not self._is_ollama_server_running():
                error_message = (
                    "Ollama server is not running. Please start the server or install "
                    "the Ollama package. Visit https://ollama.com/ for more "
                    "information."
                )

                raise ValueError(error_message)

            self.prompt = prompt

            request = {
                "model": self.model,
                "messages": [
                    {"role": "user", "content": self.system_role + " " + self.prompt},
                ],
            }

            if "response_format" in self.parameters:
                if self.parameters["response_format"].strip() in ["json"]:
                    response_format = {"format": "json"}
                    self.parameters["response_format"] = response_format
                    self.is_json = True
                elif self.parameters["response_format"].strip() == "markdown":
                    self.is_markdown = True

            # # Add the parameters to the request
            if self.parameters is not None:
                options = {}
                for key, value in self.parameters.items():
                    allowed_keys = ["temperature", "top_p", "max_tokens"]

                    if key in allowed_keys and value:
                        # Add the parameters to the request
                        if key == "max_tokens":
                            options[key] = int(value)
                        else:
                            options[key] = float(value)

                request["options"] = options

            try:
                # Calculate the duration of the completion
                start = timeit.default_timer()

                # Calling the local model
                response = ollama.chat(**request)

                end = timeit.default_timer()
                self.duration = end - start
            except ollama.ResponseError as e:
                error_message = f"Ollama error: {e.error}"
                raise ValueError(error_message) from e

            self._response = dict(response)
            # Calculate the cost of the completion
            # For now we calculate the cost as 0.0
            self.cost = self._calculate_cost(0.0, 0.0)

            self.input_tokens = response["prompt_eval_count"]
            self.output_tokens = response["eval_count"]

            self.response_message = response["message"]["content"]

            if self.is_json:  # noqa SIM114
                self.response_message = self._extract_json(self.response_message)
            elif self.is_markdown:
                self.response_message = self._extract_json(self.response_message)

            return self.response_message

    def _resolve_model(self, model: str) -> str:
        resolved_model = model

        # Automatically resolve the model to its latest version
        # if the version is not specified
        if not re.match(r"(\S+):(\S+)", model):
            resolved_model = f"{model}:latest"

        available_models = self._list_models()

        if resolved_model not in available_models:
            error_message = (
                f"Model {model} is not available. Available models are: "
                f"{available_models}. Please download the model with "
                f"`ollama pull {model}`."
            )

            raise ValueError(error_message)

        # Currently, we are not returning models with a specific tag. We assume that
        # we always use the latest version of the model.

        # TODO: Make it possible to use a specific tag with ollama.

        return model

    def download_model(self, model: str) -> None:
        """Download the specified model."""
        ollama.pull(model)

    def to_dict(self) -> dict:
        """Convert the object to a dictionary."""
        data = super().to_dict()
        data.update(
            {
                "provider_file": "ollama.json",
            },
        )
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "OllamaCompletion":
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
