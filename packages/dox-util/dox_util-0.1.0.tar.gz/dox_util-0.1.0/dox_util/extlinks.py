import os
from sphinx.util.nodes import split_explicit_title
from docutils import nodes, utils


def make_link_role(_name: str, base_url: str, caption: str):
    def role(_role, _rawtext, text, _lineno, inliner, _options={}, _content=[]):
        text = utils.unescape(text)
        has_explicit_title, title, part = split_explicit_title(text)
        if base_url.startswith(".."):
            doc = os.path.dirname(inliner.document.current_source)
            src = inliner.document.settings.env.app.srcdir
            to_src = os.path.relpath(src, doc)
            full_url = os.path.join(str(to_src), base_url % part).replace("\\", "/")
        else:
            full_url = base_url % part
        if not has_explicit_title:
            if caption is None:
                title = full_url
            else:
                title = caption % part
        ref_node = nodes.reference(title, title, internal=False, refuri=full_url)
        return [ref_node], []

    return role


def setup_link_roles(app):
    if "extlinks" in app.config:
        for name, (base_url, caption) in app.config.extlinks.items():
            app.add_role(name, make_link_role(name, base_url, caption), override=True)
