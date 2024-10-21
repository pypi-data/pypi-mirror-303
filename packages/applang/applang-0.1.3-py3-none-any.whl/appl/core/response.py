import json
import os
import shutil
import time

from litellm import CustomStreamWrapper, completion_cost, stream_chunk_builder
from litellm.exceptions import NotFoundError
from openai import Stream
from pydantic import model_validator
from rich.live import Live
from rich.panel import Panel
from rich.syntax import Syntax
from tqdm import tqdm

from .config import configs
from .tool import ToolCall
from .types import *
from .utils import make_panel


class CompletionResponse(BaseModel):
    """A class wrapping the response from the LLM model.

    For a streaming response, it tracks the chunks of the response and
    builds the complete response when the streaming is finished.
    """

    raw_response: Any = Field(None, description="The raw response from the model")
    """The raw response from the model."""
    cost: Optional[float] = Field(None, description="The cost of the completion")
    """The cost of the completion."""
    usage: Optional[CompletionUsage] = Field(
        None, description="The usage of the completion"
    )
    """The usage of the completion."""
    chunks: List[Union[ModelResponse, ChatCompletionChunk]] = Field(
        [], description="The chunks of the response when streaming"
    )
    """The chunks of the response when streaming."""
    is_stream: bool = Field(False, description="Whether the response is a stream")
    """Whether the response is a stream."""
    is_finished: bool = Field(
        False, description="Whether the response stream is finished"
    )
    """Whether the response stream is finished."""
    post_finish_callbacks: List[Callable] = Field(
        [], description="The post finish callbacks"
    )
    """The post finish callbacks."""
    response_model: Any = Field(
        None, description="The BaseModel's subclass specifying the response format."
    )
    """The BaseModel's subclass specifying the response format."""
    response_obj: Any = Field(
        None, description="The response object of response model, could be a stream"
    )
    """The response object of response model, could be a stream."""
    message: Optional[str] = Field(
        None, description="The top-choice message from the completion"
    )
    """The top-choice message from the completion."""
    tool_calls: List[ToolCall] = Field([], description="The tool calls")
    """The tool calls."""

    @model_validator(mode="after")
    def _post_init(self) -> "CompletionResponse":
        self._complete_response = None

        if isinstance(self.raw_response, (CustomStreamWrapper, Stream)):
            # ? supports for Async Steam?
            self.is_stream = True
        else:
            self._finish(self.raw_response)  # type: ignore
        return self

    def set_response_obj(self, response_obj: Any) -> None:
        """Set the response object."""
        self.response_obj = response_obj

    @property
    def complete_response(self) -> Union[ModelResponse, ChatCompletion]:
        """The complete response from the model. This will block until the response is finished."""
        if self.is_finished:
            return self._complete_response  # type: ignore
        self.streaming()  # ? when we should set display to False?
        assert self.is_finished, "Response should be finished after streaming"
        return self._complete_response  # type: ignore

    @property
    def results(self) -> Any:
        """The results of the response.

        Returns:
            message (str):
                The message if the response is a text completion.
            tool_calls (List[ToolCall]):
                The tool calls if the response is a list of tool calls.
            response_obj (Any):
                The object if the response is a response object.
        """
        if self.is_stream and not self.is_finished:
            self.streaming()  # display the stream and finish the response
        results: Any = self.message
        if self.response_obj is not None:
            results = self.response_obj
        elif len(self.tool_calls):
            results = self.tool_calls
        return results

    @property
    def type(self) -> ResponseType:
        """The type of the response."""
        if not self.is_finished:
            return ResponseType.UNFINISHED
        if self.response_model is not None and self.response_obj is not None:
            return ResponseType.OBJECT
        if len(self.tool_calls):
            return ResponseType.TOOL_CALL
        return ResponseType.TEXT

    def streaming(
        self, display: bool = True, title: str = "APPL Streaming"
    ) -> "CompletionResponse":
        """Stream the response object and finish the response."""
        if not self.is_stream:
            raise ValueError("Cannot iterate over non-streaming response")
        if self.is_finished:
            return self

        if self.response_obj is not None:
            target = self.response_obj
        else:
            target = self.format_stream()
        if display:
            refresh_interval = configs.getattrs(
                "settings.logging.display.stream_interval", 1.0
            )
            start_time = time.time()

            def panel(
                content: str, iter_index: Optional[int] = None, truncate: bool = False
            ) -> Panel:
                style = "magenta"
                display_title = title
                if iter_index is not None:
                    time_elapsed = time.time() - start_time
                    avg_iters_per_sec = (iter_index + 1) / time_elapsed
                    stream_info = (
                        f"[{time_elapsed:.3f}s ({avg_iters_per_sec:.2f} it/s)]"
                    )
                    display_title += f" - {stream_info}"
                return make_panel(
                    content, title=display_title, style=style, truncate=truncate
                )

            with Live(
                panel("Waiting for Response ..."),
                refresh_per_second=refresh_interval,
                # vertical_overflow="visible", # manually display the tail lines instead
            ) as live:
                content = ""
                for i, chunk in enumerate(iter(target)):
                    if isinstance(chunk, BaseModel):
                        content = json.dumps(chunk.model_dump(), indent=2)
                    else:
                        content += str(chunk)
                    live.update(panel(content, i, truncate=True))
                    # live.refresh() # might be too frequent
                # display untruncated content at the end
                live.update(panel(content, i))
                live.refresh()
        else:
            for chunk in iter(target):
                pass
        if self.response_obj is not None:
            self.set_response_obj(chunk)
        return self

    def register_post_finish_callback(self, callback: Callable) -> None:
        """Register a post finish callback.

        The callback will be called after the response is finished.
        """
        if self.is_finished:
            callback(self)
        else:
            self.post_finish_callbacks.append(callback)

    def format_stream(self):
        """Format the stream response as a text generator."""
        suffix = ""
        for chunk in iter(self):
            # chunk: Union[ModelResponse, ChatCompletionChunk]
            delta: Union[Delta, ChoiceDelta] = chunk.choices[0].delta  # type: ignore

            if delta is not None:
                if delta.content is not None:
                    yield delta.content
                elif getattr(delta, "tool_calls", None):
                    f: Union[Function, ChoiceDeltaToolCallFunction] = delta.tool_calls[
                        0
                    ].function  # type: ignore
                    if f.name is not None:
                        if suffix:
                            yield f"{suffix}, "
                        yield f"{f.name}("
                        suffix = ")"
                    if f.arguments is not None:
                        yield f.arguments
        yield suffix

    def _finish(self, response: Any) -> None:
        if self.is_finished:
            logger.warning("Response already finished. Ignoring finish call.")
            return
        self.is_finished = True
        self._complete_response = response
        self.usage = getattr(response, "usage", None)
        self.cost = 0.0
        try:
            self.cost = completion_cost(response)
        except Exception:
            pass
        # parse the message and tool calls
        if isinstance(response, (ModelResponse, ChatCompletion)):
            message = response.choices[0].message  # type: ignore
            if tool_calls := getattr(message, "tool_calls", None):
                for call in tool_calls:
                    self.tool_calls.append(ToolCall.from_openai_tool_call(call))
            elif message.content is not None:
                self.message = message.content
            else:
                raise ValueError(f"Invalid response: {response}")
        # post finish hook
        for callback in self.post_finish_callbacks:
            try:
                callback(self)
            except Exception as e:
                logger.error(
                    f"Error when calling post finish callback {callback.__name__}: {e}"
                )
                raise e

    def _finish_stream(self) -> None:
        try:
            response = stream_chunk_builder(self.chunks)
        except Exception:
            logger.error("Error when building the response from the stream")
            raise
        self._finish(response)

    def __str__(self):
        if self.is_stream and not self.is_finished:
            return repr(self)
        return str(self.results)

    def __next__(self):
        if not self.is_stream:
            raise ValueError("Cannot iterate over non-streaming response")
        try:
            chunk = next(self.raw_response)
            self.chunks.append(chunk)
            return chunk
        except StopIteration:
            self._finish_stream()
            raise StopIteration

    def __iter__(self):
        if not self.is_stream:
            raise ValueError("Cannot iterate over non-streaming response")
        return self

    def __getattr__(self, name: str) -> Any:
        if not self.is_finished:
            logger.warning(
                f"Cannot get {name} attribute before the response is finished. "
                "Returning None."
            )
            return None
        return getattr(self.complete_response, name)
