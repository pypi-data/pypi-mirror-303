"""Class for representing a messages entry."""

import re
from string import Template
from typing import Dict, List, Optional


from guardrails.classes.templating.namespace_template import NamespaceTemplate
from guardrails.utils.constants import constants
from guardrails.utils.templating_utils import get_template_variables


class Messages:
    def __init__(
        self,
        source: List[Dict[str, str]],
        output_schema: Optional[str] = None,
        *,
        xml_output_schema: Optional[str] = None,
    ):
        self._source = source

        # FIXME: Why is this happening on init instead of on format?
        # Substitute constants in the prompt.
        for message in self._source:
            # if content is instance of Prompt class
            # call the substitute_constants method
            if isinstance(message["content"], str):
                message["content"] = self.substitute_constants(message["content"])

        # FIXME: Why is this happening on init instead of on format?
        # If an output schema is provided, substitute it in the prompt.
        if output_schema or xml_output_schema:
            for message in self._source:
                if isinstance(message["content"], str):
                    message["content"] = Template(message["content"]).safe_substitute(
                        output_schema=output_schema, xml_output_schema=xml_output_schema
                    )
        else:
            self.source = source

    def format(
        self,
        **kwargs,
    ):
        """Format the messages using the given keyword arguments."""
        formatted_messages = []
        for message in self.source:
            # Only use the keyword arguments that are present in the message.
            vars = get_template_variables(message["content"])
            filtered_kwargs = {k: v for k, v in kwargs.items() if k in vars}

            # Return another instance of the class with the formatted message.
            formatted_message = Template(message["content"]).safe_substitute(
                **filtered_kwargs
            )
            formatted_messages.append(
                {"role": message["role"], "content": formatted_message}
            )
        return Messages(formatted_messages)

    def substitute_constants(self, text):
        """Substitute constants in the prompt."""
        # Substitute constants by reading the constants file.
        # Regex to extract all occurrences of ${gr.<constant_name>}
        matches = re.findall(r"\${gr\.(\w+)}", text)

        # Substitute all occurrences of ${gr.<constant_name>}
        #   with the value of the constant.
        for match in matches:
            template = NamespaceTemplate(text)
            mapping = {f"gr.{match}": constants[match]}
            text = template.safe_substitute(**mapping)

        return text
