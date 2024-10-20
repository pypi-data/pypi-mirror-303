import time
from typing import Dict, List, Literal, Optional, Text, Tuple, Union

from openai.types.beta.assistant import ToolResources
from openai.types.beta.assistant_response_format_option import (
    AssistantResponseFormatOption,
)
from openai.types.beta.assistant_tool import AssistantTool
from openai.types.beta.assistant_tool_choice_option import AssistantToolChoiceOption
from openai.types.beta.thread import Thread
from openai.types.beta.threads.annotation import Annotation as OpenaiAnnotation
from openai.types.beta.threads.image_file import ImageFile
from openai.types.beta.threads.image_url import ImageURL
from openai.types.beta.threads.message import AttachmentTool
from openai.types.beta.threads.message import Message as OpenaiMessage
from openai.types.beta.threads.run import IncompleteDetails, LastError, RequiredAction
from openai.types.beta.threads.run import Run as OpenaiRun
from openai.types.beta.threads.run import TruncationStrategy, Usage
from openai.types.beta.threads.run_status import RunStatus
from openai.types.beta.threads.text import Text as OpenaiText
from openai.types.beta.threads.text_content_block import (
    TextContentBlock as OpenaiTextContentBlock,
)
from pydantic import BaseModel, Field

from languru.utils.openai_utils import rand_openai_id


def to_openai_threads_message(
    thread_id: Text,
    *,
    role: Literal["user", "assistant"],
    content: Optional[Union[Text, List["MessageContent"]]] = None,
    message_id: Optional[Text] = None,
    attachments: Optional[List["AttachmentTool"]] = None,
    metadata: Optional[Dict[Text, Text]] = None,
    status: Literal["in_progress", "incomplete", "completed"] = "completed",
    created_at: Optional[int] = None,
) -> OpenaiMessage:
    """Converts a message to an OpenAI Threads message."""

    data = {
        "id": message_id or rand_openai_id("message"),
        "thread_id": thread_id,
        "role": role,
        "content": (
            [TextContentBlock.model_validate({"text": {"value": content}})]
            if isinstance(content, Text)
            else content
        ),
        "attachments": attachments,
        "metadata": metadata or {},
        "status": status,
        "object": "thread.message",
        "created_at": created_at or int(time.time()),
    }
    return OpenaiMessage.model_validate(data)


class TextContentBlockText(OpenaiText):
    annotations: List[OpenaiAnnotation] = Field(
        default_factory=list, description="A list of annotations for the text."
    )


class TextContentBlock(OpenaiTextContentBlock):
    text: TextContentBlockText
    type: Literal["text"] = Field(default="text", description="Always `text`.")


MessageContent = Union[ImageFile, ImageURL, TextContentBlockText]


class ThreadsMessageCreate(BaseModel):
    content: Optional[Union[Text, List[MessageContent]]] = Field(
        default=None, description="The text contents of the message."
    )
    role: Literal["user", "assistant"] = Field(
        ..., description="The role of the entity that is creating the message."
    )
    attachments: Optional[List[AttachmentTool]] = Field(
        default=None,
        description=(
            "A list of files attached to the message, "
            + "and the tools they should be added to."
        ),
    )
    metadata: Optional[Dict[Text, Text]] = Field(
        default=None,
        description="Set of 16 key-value pairs that can be attached to an object.",
    )

    def to_openai_message(
        self,
        thread_id: Text,
        message_id: Optional[Text] = None,
        status: Literal["in_progress", "incomplete", "completed"] = "completed",
    ) -> OpenaiMessage:
        data = self.model_dump()
        data["id"] = message_id or rand_openai_id("message")
        data["thread_id"] = thread_id
        data["status"] = status
        data["object"] = "thread.message"
        data["created_at"] = int(time.time())
        if isinstance(data["content"], Text):
            data["content"] = [
                TextContentBlock.model_validate({"text": {"value": data["content"]}})
            ]
        return OpenaiMessage.model_validate(data)


class ThreadsMessageUpdate(BaseModel):
    metadata: Optional[Dict[Text, Text]] = Field(
        default=None,
        description="Set of 16 key-value pairs that can be attached to an object.",
    )


class ThreadCreateRequest(BaseModel):
    messages: Optional[List[ThreadsMessageCreate]] = Field(
        default=None,
        description="A list of messages to start the thread with.",
    )
    metadata: Optional[Dict[Text, Text]] = Field(
        default=None,
        description="Set of 16 key-value pairs that can be attached to an object.",
    )
    tool_resources: Optional[ToolResources] = Field(
        default=None,
        description=(
            "A set of resources that are made available to "
            + "the assistant's tools in this thread."
        ),
    )

    def to_openai_thread(self, thread_id: Optional[Text] = None) -> Thread:
        data = self.model_dump()
        data["id"] = thread_id or rand_openai_id("thread")
        data["object"] = "thread"
        data["created_at"] = int(time.time())
        return Thread.model_validate(data)


class ThreadUpdateRequest(BaseModel):
    metadata: Optional[Dict[Text, Text]] = Field(
        default=None,
        description="Set of 16 key-value pairs that can be attached to an object.",
    )
    tool_resources: Optional[ToolResources] = Field(
        default=None,
        description=(
            "A set of resources that are made available to "
            + "the assistant's tools in this thread."
        ),
    )


class ThreadsRunCreate(BaseModel):
    assistant_id: Text
    additional_instructions: Optional[Text] = Field(
        default=None,
        description="Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.",  # noqa: E501
    )
    additional_messages: Optional[List[ThreadsMessageCreate]] = Field(
        default=None,
        description="Adds additional messages to the thread before creating the run.",
    )
    instructions: Optional[Text] = Field(
        default=None,
        description="Overrides the instructions of the assistant. This is useful for modifying the behavior on a per-run basis.",  # noqa: E501
    )
    max_completion_tokens: Optional[int] = Field(
        default=None,
        description="The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.",  # noqa: E501
    )
    max_prompt_tokens: Optional[int] = Field(
        default=None,
        description="The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.",  # noqa: E501
    )
    metadata: Optional[Dict[Text, Text]] = Field(
        default=None,
        description="Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.",  # noqa: E501
    )
    model: Optional[Text] = Field(
        default=None,
        description="The ID of the Model to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.",  # noqa: E501
    )
    parallel_tool_calls: Optional[bool] = Field(
        default=None,
        description="Whether to enable parallel function calling during tool use.",
    )
    response_format: Optional[AssistantResponseFormatOption] = Field(
        default=None,
        description="Specifies the format that the model must output.",
    )
    stream: Optional[Literal[False]] = Field(
        default=None,
        description="If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.",  # noqa: E501
    )
    temperature: Optional[float] = Field(
        default=None,
        description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.",  # noqa: E501
    )
    tool_choice: Optional[AssistantToolChoiceOption] = Field(
        default=None,
        description="Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user. Specifying a particular tool like `{'type': 'file_search'}` or `{'type': 'function', 'function': {'name': 'my_function'}}` forces the model to call that tool.",  # noqa: E501
    )
    tools: Optional[List[AssistantTool]] = Field(
        default=None,
        description="Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.",  # noqa: E501
    )
    top_p: Optional[float] = Field(
        default=None,
        description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.",  # noqa: E501
    )
    truncation_strategy: Optional[Literal["auto", "last_messages"]] = Field(
        default=None,
        description="The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.",  # noqa: E501
    )

    def to_openai_run(
        self,
        thread_id: Text,
        run_id: Optional[Text] = None,
        status: RunStatus = "queued",
        default_instructions: Optional[Text] = None,
        default_temperature: Optional[float] = None,
        enable_additional_instructions: bool = True,
        additional_instructions_separator: Text = "\n",
    ) -> OpenaiRun:
        data = self.model_dump(exclude_none=True)
        data["id"] = run_id or rand_openai_id("run")
        data["object"] = "thread.run"
        data["created_at"] = int(time.time())
        data["thread_id"] = thread_id
        data["status"] = status
        data["instructions"] = self.instructions or default_instructions or ""
        if enable_additional_instructions and self.additional_instructions:
            data["instructions"] += additional_instructions_separator
            data["instructions"] += self.additional_instructions or ""
        data["temperature"] = self.temperature or default_temperature
        data["parallel_tool_calls"] = self.parallel_tool_calls or False
        data["tools"] = self.tools or []
        return OpenaiRun.model_validate(data)


class ThreadsRunUpdate(BaseModel):
    metadata: Optional[Dict[Text, Text]] = Field(
        default=None,
        description="Set of 16 key-value pairs that can be attached to an object.",
    )
    cancelled_at: Optional[int] = Field(
        default=None,
        description="The time at which the run was cancelled.",
    )
    completed_at: Optional[int] = Field(
        default=None,
        description="The time at which the run was completed.",
    )
    expires_at: Optional[int] = Field(
        default=None,
        description="The time at which the run expires.",
    )
    failed_at: Optional[int] = Field(
        default=None,
        description="The time at which the run failed.",
    )
    incomplete_details: Optional[IncompleteDetails] = Field(
        default=None,
        description="Details on why the run is incomplete.",
    )
    instructions: Optional[Text] = Field(
        default=None,
        description="The instructions the assistant used for this run.",
    )
    last_error: Optional[LastError] = Field(
        default=None,
        description="The last error associated with this run.",
    )
    max_completion_tokens: Optional[int] = Field(
        default=None,
        description="The maximum number of completion tokens specified to have been used over the course of the run.",  # noqa: E501
    )
    max_prompt_tokens: Optional[int] = Field(
        default=None,
        description="The maximum number of prompt tokens specified to have been used over the course of the run.",  # noqa: E501
    )
    model: Optional[Text] = Field(
        default=None,
        description="The model that the assistant used for this run.",
    )
    parallel_tool_calls: Optional[bool] = Field(
        default=None,
        description="Whether to enable parallel function calling during tool use.",
    )
    required_action: Optional[RequiredAction] = Field(
        default=None,
        description="The required action for the run.",
    )
    response_format: Optional[AssistantResponseFormatOption] = Field(
        default=None,
        description="Specifies the format that the model must output.",
    )
    started_at: Optional[int] = Field(
        default=None,
        description="The time at which the run started.",
    )
    status: Optional[RunStatus] = Field(
        default=None,
        description="The status of the run.",
    )
    tool_choice: Optional[AssistantToolChoiceOption] = Field(
        default=None,
        description="Controls which (if any) tool is called by the model.",
    )
    tools: Optional[List[AssistantTool]] = Field(
        default=None,
        description="The list of tools that the assistant used for this run.",
    )
    truncation_strategy: Optional[TruncationStrategy] = Field(
        default=None,
        description="Controls for how a thread will be truncated prior to the run.",
    )
    usage: Optional[Usage] = Field(
        default=None,
        description="Usage statistics related to the run.",
    )
    temperature: Optional[float] = Field(
        default=None,
        description="The sampling temperature used for this run.",
    )
    top_p: Optional[float] = Field(
        default=None,
        description="The nucleus sampling value used for this run.",
    )


class ThreadCreateAndRunRequest(BaseModel):
    assistant_id: Text
    instructions: Optional[Text] = Field(
        default=None,
        description="Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.",  # noqa: E501
    )
    max_completion_tokens: Optional[int] = Field(
        default=None,
        description="The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.",  # noqa: E501
    )
    max_prompt_tokens: Optional[int] = Field(
        default=None,
        description="The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.",  # noqa: E501
    )
    metadata: Optional[Dict[Text, Text]] = Field(
        default=None,
        description="Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.",  # noqa: E501
    )
    model: Optional[Text] = Field(
        default=None,
        description="The ID of the Model to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.",  # noqa: E501
    )
    parallel_tool_calls: Optional[bool] = Field(
        default=None,
        description="Whether to enable parallel function calling during tool use.",
    )
    response_format: Optional[AssistantResponseFormatOption] = Field(
        default=None,
        description="Specifies the format that the model must output.",
    )
    stream: Optional[Literal[False]] = Field(
        default=None,
        description="If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.",  # noqa: E501
    )
    temperature: Optional[float] = Field(
        default=None,
        description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.",  # noqa: E501
    )
    thread: Optional[ThreadCreateRequest] = Field(
        default=None,
        description="If no thread is provided, an empty thread will be created.",
    )
    tool_choice: Optional[AssistantToolChoiceOption] = Field(
        default=None,
        description="Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user. Specifying a particular tool like `{'type': 'file_search'}` or `{'type': 'function', 'function': {'name': 'my_function'}}` forces the model to call that tool.",  # noqa: E501
    )
    tool_resources: Optional[ToolResources] = Field(
        default=None,
        description="A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.",  # noqa: E501
    )
    tools: Optional[List[AssistantTool]] = Field(
        default=None,
        description="Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.",  # noqa: E501
    )
    top_p: Optional[float] = Field(
        default=None,
        description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.",  # noqa: E501
    )
    truncation_strategy: Optional[Literal["auto", "last_messages"]] = Field(
        default=None,
        description="Controls for how a thread will be truncated prior to the run. Use this to control the intial context window of the run.",  # noqa: E501
    )

    def to_openai_thread_and_messages(
        self, thread_id: Optional[Text] = None
    ) -> Tuple[Thread, List[OpenaiMessage]]:
        thread = (
            self.thread or ThreadCreateRequest.model_validate({})
        ).to_openai_thread(thread_id)
        messages = (
            [m.to_openai_message(thread_id=thread.id) for m in self.thread.messages]
            if self.thread and self.thread.messages
            else []
        )
        return (thread, messages)

    def to_openai_run(
        self,
        thread_id: Text,
        *,
        run_id: Optional[Text] = None,
        status: RunStatus = "queued",
        default_instructions: Optional[Text] = None,
        default_temperature: Optional[float] = None,
    ) -> OpenaiRun:
        data = self.model_dump()
        data["id"] = run_id or rand_openai_id("run")
        data["object"] = "thread.run"
        data["created_at"] = int(time.time())
        data["thread_id"] = thread_id
        data["status"] = status
        data["instructions"] = data["instructions"] or default_instructions or ""
        data["temperature"] = data["temperature"] or default_temperature
        data["parallel_tool_calls"] = data["parallel_tool_calls"] or False
        data["tools"] = data["tools"] or []
        return OpenaiRun.model_validate(data)


class ToolOutput(BaseModel):
    output: Text = Field(
        ...,
        description="The output of the tool call to be submitted to continue the run.",
    )
    tool_call_id: Text = Field(
        ...,
        description=(
            "The ID of the tool call in the `required_action` object within "
            + "the run object the output is being submitted for."
        ),
    )


class RunSubmitToolOutputsRequest(BaseModel):
    tool_outputs: List[ToolOutput] = Field(
        ..., description="A list of tools for which the outputs are being submitted."
    )
    stream: Optional[bool] = Field(
        default=False,
        description=(
            "If `true`, returns a stream of events that happen during the Run as "
            + "server-sent events, terminating when the Run enters a terminal "
            + "state with a `data: [DONE]` message."
        ),
    )
