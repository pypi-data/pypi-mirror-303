"""Completion implementation for the OpenAI API."""

import logging
import os
import timeit

import openai
import opentelemetry.trace
from openai import OpenAI

from promptarchitect.completions.core import Completion

# Configuring logging
logger = logging.getLogger(__name__)
tracer = opentelemetry.trace.get_tracer(__name__)


class OpenAICompletion(Completion):
    """Completion logic for the OpenAI API."""

    is_json = False
    is_markdown = False

    def __init__(
        self,
        system_role: str = "",
        model: str = None,
        parameters: dict = None,
    ) -> None:
        """Initialize a new instance of the OpenAICompletion class.

        Arguments
        ---------
        system_role: str
            The role of the system in the conversation.
        model: str
            The model to use for the completion.
        parameters: dict
            Additional parameters for the completion request.
        """
        super().__init__(system_role, model, parameters, "openai.json")
        self.api_key = None

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
        with tracer.start_as_current_span("OpenAICompletion.completion") as span:
            span.set_attribute("promptarchitect.provider.id", "openai")
            span.set_attribute("promptarchitect.model.id", self.model)

            self.api_key = os.getenv("OPENAI_API_KEY")
            self.client = OpenAI()  # Instance of the OpenAI class initialized
            self.prompt = prompt

            request = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": self.system_role},
                    {"role": "user", "content": self.prompt},
                ],
            }

            # We need to map output_format to response_format for openai.
            if (
                "output_format" in self.parameters
                and self.parameters["output_format"] is not None
            ):
                if self.parameters["output_format"].strip() in [
                    "json",
                    "json_object",
                ]:
                    response_format = {"type": "json_object"}
                    self.parameters["response_format"] = response_format
                    self.is_json = True
                elif self.parameters["output_format"].strip() == "markdown":
                    self.is_markdown = True

            # Add the parameters to the request
            if self.parameters is not None:
                for key, value in self.parameters.items():
                    if key in [
                        "temperature",
                        "top_p",
                        "max_tokens",
                        "frequency_penalty",
                        "presence_penalty",
                        "response_format",
                    ]:
                        if key in ["temperature", "top_p"] and value:
                            request[key] = float(value)
                        elif key in ["max_tokens"] and value:
                            request[key] = int(value)
                        else:
                            request[key] = value

            try:
                # Calculate the duration of the completion
                start = timeit.default_timer()
                response = self.client.chat.completions.create(**request)
                end = timeit.default_timer()
                self.duration = end - start
            except openai.BadRequestError as e:
                error_message = f"Bad Request Error (wrong parameters): {e}"
                raise ValueError(error_message) from e

            self._response = dict(response)

            # Calculate the cost of the completion
            self.cost = self._calculate_cost(
                self._response["usage"].prompt_tokens,
                self._response["usage"].completion_tokens,
            )

            self.input_tokens = self._response["usage"].prompt_tokens
            self.output_tokens = self._response["usage"].completion_tokens

            span.set_attribute("promptarchitect.prompt.input_tokens", self.input_tokens)

            span.set_attribute(
                "promptarchitect.prompt.output_tokens",
                self.output_tokens,
            )

            span.set_attribute("promptarchitect.prompt.costs", self.cost)

            self.response_message = response.choices[0].message.content

            if self.is_json:
                # OpenAI has the quirks of returning JSON in a weird format
                # With starting and ending quotes. So we need to extract the JSON
                self.response_message = self._extract_json(self.response_message)

            return self.response_message.strip()

    def to_dict(self) -> dict:
        """Convert the object to a dictionary."""
        data = super().to_dict()
        data.update(
            {
                "provider_file": "openai.json",
            },
        )
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "OpenAICompletion":
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
