from docutils import nodes


def todo_role(_role, rawtext, text, _lineno, _inliner, _options={}, _content=[]):
    node = nodes.literal(rawtext, text)
    node.set_class("highlight")
    node.set_class("highlight-todo")
    return [node], []
