"""
Engineered prompting.

This module contains the EngineeredPrompt class that is used to run the prompt in
production.

See Also
--------
promptarchitect.specification : Specifications used by this module.
promptarchitect.validation : Validation of the prompt.

"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, Optional
from uuid import uuid4

import chevron
import opentelemetry.trace

from promptarchitect.completions import create_completion
from promptarchitect.specification import EngineeredPromptSpecification, PromptInput

logger = logging.getLogger(__name__)
tracer = opentelemetry.trace.get_tracer(__name__)


class EngineeredPrompt:
    """The engineered prompt. A validated, well thought-out prompt that is easy to use.

    We support running and rendering the prompt in the specification in your
    application. This class is also used during validation to run the prompt.

    Attributes
    ----------
    specification : EngineeredPromptSpecification
        The specification for the prompt.

    """

    specification: EngineeredPromptSpecification

    def __init__(
        self,
        specification: EngineeredPromptSpecification | None = None,
        prompt_file: str | None = None,
        output_path: str | None = None,
    ) -> None:
        """Initialize the engineered prompt with the specification.

        Parameters
        ----------
        specification : EngineeredPromptSpecification
            The specification for the prompt.

        prompt_file : str
            The path to a prompt file.

        output_path : str
            The path to the output directory if you want to save the response to a file.

        """
        self.id = str(uuid4())

        # Convert in the case of a Path object
        self.prompt_file = str(prompt_file) if prompt_file is not None else None
        self.output_path = str(output_path) if output_path is not None else None

        if specification is None and prompt_file is None:
            error_message = "Either specification or prompt_file must be provided."
            raise ValueError(error_message)

        if specification is not None and prompt_file is not None:
            error_message = "Only one of specification or prompt_file can be provided."
            raise ValueError(
                error_message,
            )

        if self.prompt_file is not None:
            self.specification = EngineeredPromptSpecification.from_file(
                self.prompt_file,
            )
        else:
            self.specification = specification

        # If the system role is provided in the specification, we'll use that
        # and read it from the file specified in the metadata
        # Otherwise we'll use the default system role
        if self.specification.metadata.system_role is not None:
            if Path(self.specification.metadata.system_role).is_absolute():
                system_role_path = Path(self.specification.metadata.system_role)
            else:
                system_role_path = (
                    Path(self.specification.filename).parent
                    / self.specification.metadata.system_role
                )

            with open(system_role_path, "r") as file:
                self.specification.metadata.system_role_text = file.read().strip()

        # Initialize the completion, so for Open Source models we can download the model
        self.completion = create_completion(
            self.specification.metadata.provider,
            self.specification.metadata.model,
            self.specification.metadata,
            self.specification.metadata.system_role_text,
        )

    def execute(
        self,
        input_text: Optional[str] = None,
        input_file: Optional[str] = None,
        properties: Optional[Dict[str, object]] = None,
    ) -> str:
        """Execute the prompt with the input text or input file.

        This function is for backwards compatibility with the previous version of the
        library.

        Returns
        -------
        str
            The output of the prompt.

        """
        logger.warning("The execute method is deprecated. Use run instead.")

        return self.run(input_text, input_file, properties)

    def run(
        self,
        input_text: Optional[str] = None,
        input_file: Optional[str] = None,
        properties: Optional[Dict[str, object]] = None,
    ) -> str:
        """Run the prompt with the input text or input file.

        The output of this operation is automatically cached until the application is
        closed.

        Parameters
        ----------
        input_text : str, optional
            The input text to the prompt.
        input_file : str, optional
            The path to the input file.
        properties : Dict[str, object], optional
            Additional properties for the prompt input to render the prompt with
            variables.

        Returns
        -------
        str
            The output of the prompt.

        """
        with tracer.start_as_current_span("EngineeredPrompt.run") as span:
            rendered_input = self.render(input_text, input_file, properties)
            response = self.completion.completion(rendered_input)

            span.set_attribute("prompt.rendered_input", rendered_input)
            span.set_attribute("prompt.response", response)
            span.set_attribute("prompt.cost", self.completion.cost)
            span.set_attribute("prompt.input_tokens", self.completion.input_tokens)
            span.set_attribute("prompt.output_tokens", self.completion.output_tokens)
            span.set_attribute("prompt.filename", self.specification.filename)
            span.set_attribute("prompt.author", self.specification.metadata.author)
            span.set_attribute(
                "prompt.date_created", self.specification.metadata.date_created
            )
            span.set_attribute(
                "prompt.description", self.specification.metadata.description
            )

            if self.output_path is not None:
                output_file = os.path.join(
                    self.output_path,
                    self.specification.metadata.output,
                )
                self._write_output_to_file(response, output_file)

            return response

    def _number_of_mustaches_in_prompt(self) -> int:
        mustaches = set(chevron.tokenizer.tokenize(self.specification.prompt))

        # filter on literal mustaches
        number_of_mustaches = len([m for m in mustaches if m[0] == "variable"])
        # If the mustache {{input}} is in the prompt, we'll remove it from the count
        if "{{input}}" in self.specification.prompt:
            number_of_mustaches -= 1
        return number_of_mustaches

    def _write_output_to_file(self, response: str, output_file: str) -> None:
        # Create base path if it does not exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Check the output format in the specification
        if self.specification.metadata.output_format == "json":
            # Consider the output format to be JSON
            # Load the response as JSON so we can write it to a file
            # in the right format. Otherwise, we get all the escape characters
            json_data = json.loads(response)
            # Write the response to a JSON file
            with open(output_file, "w") as file:
                json.dump(json_data, file)

        else:
            # Consider the output format to be text
            with open(output_file, "w") as file:
                file.write(response)

    def render(
        self,
        input_text: Optional[str] = None,
        input_file: Optional[str] = None,
        properties: Optional[Dict[str, object]] = None,
    ) -> str:
        """Render the prompt to a string.

        Use this method if you need to support chat interfaces or other interfaces
        that require you to interact with the language model yourself.

        We'll read the input_file if is is provided. The input file will provide this
        method with the input_text and properties. If you specify the input_text you
        can optionally include extra properties you need to render the prompt.

        Specifying properties with an `input_file` is not supported. You also can't
        provide both `input_text` and `input_file`. You must provide one or the other.

        Parameters
        ----------
        input_text : str, optional
            The input text to the prompt.
        input_file : str, optional
            The path to the input file.
        properties : Dict[str, object], optional
            Additional properties for the prompt input.

        Returns
        -------
        str
            The rendered prompt.

        """
        with tracer.start_as_current_span("EngineeredPrompt.render") as span:
            input_text = self._determine_input_text_order(input_text, input_file)

            if properties is not None:
                mustaches = self._number_of_mustaches_in_prompt()

                if mustaches != len(properties):
                    warning_message = (
                        "Mustaches mismatch: The number of mustaches in the prompt "
                        f"({mustaches}) is not equal to the number of properties "
                        f"({len(properties)}). This might result in the prompt not "
                        "rendering correctly."
                    )

                    logger.warning(warning_message)

            prompt = self.specification.prompt
            # Add a input property to prompt if it is not already in the prompt
            # Otherwise the input will not be rendered in the prompt
            if "{{input}}" not in self.specification.prompt:
                prompt = f"{self.specification.prompt} {{{{input}}}}"

            # We'll render the prompt with the input_text and properties
            template_properties = properties.copy() if properties is not None else {}
            template_properties["input"] = input_text

            rendered_prompt = chevron.render(prompt, template_properties)
            span.set_attribute("prompt.rendered_prompt", rendered_prompt)

            return rendered_prompt

    def _determine_input_text_order(self, input_text: str, input_file: str) -> str:
        if input_text is not None and input_file is not None:
            error_message = "Only one of input_text or input_file can be provided."
            raise ValueError(error_message)

        # This is the order to pick the input for the rendering of the prompt
        # 1. input_text
        # 2. input_file
        # 3. self.specification.metadata.input

        if (
            input_text is None
            and input_file is None
            and self.specification.metadata.input is None
        ):
            input_text = ""

        elif input_text is None:
            input_file = (
                input_file
                if input_file is not None
                else self.specification.metadata.input
            )

            if input_file is not None:
                prompt_input = PromptInput.from_file(input_file)

                # properties = prompt_input.properties
                input_text = prompt_input.input

        return input_text

    def to_dict(self) -> Dict:
        """Convert the EngineeredPrompt instance to a dictionary.

        Returns
        -------
        dict
            A dictionary representation of the EngineeredPrompt instance.

        """
        return {
            "id": self.id,
            "specification": self.specification.dict() if self.specification else None,
            "prompt_file": self.prompt_file,
            "output_path": self.output_path,
            "completion": self.completion.to_dict() if self.completion else None,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "EngineeredPrompt":
        """Create an EngineeredPrompt instance from a dictionary.

        Parameters
        ----------
        data : dict
            A dictionary containing the data to create an EngineeredPrompt instance.

        Returns
        -------
        EngineeredPrompt
            An EngineeredPrompt instance created from the provided dictionary.

        """
        specification = (
            EngineeredPromptSpecification(**data["specification"])
            if data["specification"]
            else None
        )

        return cls(
            id=data.get("id"),
            specification=specification,
            prompt_file=data.get("prompt_file"),
            output_path=data.get("output_path"),
        )
