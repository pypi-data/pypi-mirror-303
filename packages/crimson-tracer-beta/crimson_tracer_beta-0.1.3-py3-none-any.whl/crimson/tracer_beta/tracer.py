import sys
from types import FrameType
from typing import Optional, Callable, Any, List, Dict, Literal, Generic, TypeVar
from pydantic import BaseModel, ConfigDict

Custom = TypeVar("Custom")


class TraceEvent(BaseModel, Generic[Custom]):
    function: str
    filename: str
    lineno: int
    event: Literal["call", "line", "return"]
    arg: Any | None
    level: int
    locals: Dict[str, Any] = {}
    custom: Custom | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)


class EventEditor(Callable[[TraceEvent], TraceEvent]):
    """
    Edit the `TraceEvent` to be stored during tracing.
    """

    def default(trace_event: TraceEvent) -> TraceEvent:
        return trace_event


class TraceManager:
    traces: Dict[str, List[TraceEvent]] = {}
    current_trace_name: Optional[str] = None
    stack_count: int = -1
    frame_filter: Callable[[FrameType], bool] = lambda frame: True
    event_editor: Callable[[TraceEvent], TraceEvent] = None

    @classmethod
    def set_frame_filter(cls, frame_filter: Callable[[FrameType], bool]):
        cls.frame_filter = frame_filter

    @classmethod
    def set_event_editor(cls, event_editor: Callable[[TraceEvent], TraceEvent]):
        cls.event_editor = event_editor

    @classmethod
    def tracer(cls, frame: FrameType, event: str, arg: Any) -> Optional[Callable]:
        if cls.frame_filter(frame):
            if event == "call":
                cls.stack_count += 1
                cls._update_trace_event(frame, event, arg)
            elif event == "line":
                cls._update_trace_event(frame, event, arg)
            elif event == "return":
                cls._update_trace_event(frame, event, arg)
                cls.stack_count -= 1
        return cls.tracer

    @classmethod
    def _update_trace_event(cls, frame, event, arg):
        trace_event = cls.generate_trace_event(frame, event, arg)
        cls.traces[cls.current_trace_name].append(trace_event)

    @classmethod
    def run_trace(
        cls,
        func: Callable,
        name: Optional[str] = None,
        frame_filter: Callable[[FrameType], bool] = None,
    ):
        if frame_filter is not None:
            cls.set_frame_filter(frame_filter)

        if name is None:
            name = func.__name__

        cls.current_trace_name = name
        cls.traces[name] = []
        cls.stack_count = -1

        sys.settrace(cls.tracer)
        result = func()
        sys.settrace(None)

        cls.current_trace_name = None
        return result

    @classmethod
    def get_trace(
        cls, name: str, custom_type: Custom = Custom
    ) -> List[TraceEvent[Custom]]:
        return cls.traces.get(name, [])

    @classmethod
    def generate_trace_event(cls, frame: FrameType, event: str, arg: Any) -> TraceEvent:
        trace_event = TraceEvent(
            function=frame.f_code.co_name,
            filename=frame.f_code.co_filename,
            lineno=frame.f_lineno,
            event=event,
            arg=arg,
            level=cls.stack_count,
            locals=frame.f_locals if event == "call" else {},
        )
        if cls.event_editor is not None:
            trace_event = cls.event_editor(trace_event)
        return trace_event
