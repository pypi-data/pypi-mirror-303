from crimson.anytree_extension.unique_node import UniqueNode
from dataclasses import asdict
from typing import Any, List, Dict, Optional
from dataclasses import dataclass
from crimson.tracer_beta.tracer import TraceEvent


@dataclass
class NodeBody:
    function: str
    level: int
    filename: str
    lineno: int
    args: Dict[str, Any]
    return_lineno: int | None = None
    return_value: Any = None
    called_filename: str | None = None
    called_lineno: int | None = None


class TraceNode(UniqueNode['TraceNode']):
    def __init__(
        self,
        name,
        body: NodeBody | None = None,
        parent: "TraceNode" = None,
        children: List["TraceNode"] = None,
        **kwargs_dummy,
    ):
        super().__init__(name, parent, children)
        self.body = body

    def to_dict(self):
        result = {
            "type": "root" if self.is_root else "node",
            "name": self.name,
            "children": [child.to_dict() for child in self.children],
        }

        if self.body:
            result["body"] = asdict(self.body)

        return result


def generate_trace_tree(trace_result: List[TraceEvent]) -> TraceNode:
    root = TraceNode("root")
    stack = [root]
    last_line = {}
    call_events = {}

    def create_node_body(
        trace_event: TraceEvent, parent: TraceNode, called_lineno: Optional[int] = None
    ) -> NodeBody:
        shared_fields = {
            field: getattr(trace_event, field)
            for field in ["function", "filename", "lineno", "level"]
        }

        called_filename = (
            parent.body.filename if hasattr(parent.body, "filename") else None
        )

        return NodeBody(
            **shared_fields,
            args=trace_event.locals,
            called_filename=called_filename,
            called_lineno=called_lineno,
        )

    for trace_event in trace_result:
        if trace_event.event == "call":
            parent = stack[-1] if len(stack) > trace_event.level else root
            called_lineno = last_line.get(trace_event.level - 1)

            node_body = create_node_body(trace_event, parent, called_lineno)

            node = TraceNode(
                name=f"{trace_event.function}_{trace_event.lineno}",
                parent=parent,
                body=node_body,
            )

            stack.append(node)
            call_events[trace_event.level] = node

        elif trace_event.event == "return":
            if stack:
                call_node: TraceNode = call_events.get(trace_event.level)
                if call_node:
                    call_node.body.return_value = trace_event.arg
                    call_node.body.return_lineno = trace_event.lineno
                stack.pop()
                del call_events[trace_event.level]

        last_line[trace_event.level] = trace_event.lineno

    return root
