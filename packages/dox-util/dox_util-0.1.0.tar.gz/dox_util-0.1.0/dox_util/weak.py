import re

from docutils import nodes
from sphinx import addnodes
from sphinx.util import logging

logger = logging.getLogger(__name__)
weakref_pattern = re.compile("^([^<]+)(<([^>]+)>|)$")


def weak_role(role, _rawtext, text, lineno, inliner, _options={}, _content=[]):
    text = text.strip()
    ref = weakref_pattern.findall(text)
    if len(ref) == 0:
        logger.warning(
            "%s.rst:%d: invalid ref pattern %s"
            % (inliner.document.settings.env.docname, lineno, text)
        )

    ref_text = ref[0][0].strip()
    explicit = ref[0][1] != ""
    target = ref[0][2].strip() if explicit else ref_text

    ref_node = addnodes.pending_xref(
        "",
        refdomain="std",
        refexplicit=explicit,
        reftarget=target.lower(),
        reftype="ref" if role == "weakref" else "doc",
        refwarn=inliner.document.settings.env.app.config.enable_weak_warnings,
    )

    ref_node += nodes.Text(ref_text)
    return [ref_node], []
