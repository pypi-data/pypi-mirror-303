import re
import os

from sphinx.directives.other import TocTree
from sphinx.util import docname_join
from sphinx.util.matching import patfilter

from sphinx.util.docutils import SphinxDirective
from docutils import nodes
from docutils.statemachine import ViewList

from typing import List

glob_re = re.compile(r".*[*?\[].*")


class TolerantTocTree(TocTree):
    content: List[str]

    def run(self):
        new_content = []
        all_docnames = self.env.found_docs.copy()
        all_docnames.remove(self.env.docname)

        for entry in self.content:
            patname = docname_join(self.env.docname, entry)
            if patname in all_docnames:
                new_content.append(entry)
            elif "glob" in self.options and glob_re.match(entry):
                if len(patfilter(all_docnames, patname)) > 0:
                    new_content.append(entry)
        self.content = new_content
        return super().run()


class DocList(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        all_docnames = self.env.found_docs.copy()
        filename = self.get_source_info()[0]
        line_number = self.get_source_info()[1]

        docs = []
        for entry in self.content:
            if not entry:
                continue
            if glob_re.match(entry):
                patname = docname_join(self.env.docname, entry)
                docnames = sorted(patfilter(all_docnames, patname))
                docs.extend(docnames)
                if not docnames:
                    raise AttributeError(
                        "%s.rst:%d: doclist glob pattern %r didn't match any documents"
                        % (self.env.docname, line_number, entry)
                    )
            else:
                docs.append(docname_join(self.env.docname, entry))

        rst = ViewList()
        for docname in docs:
            dir_docname = os.path.dirname(self.env.docname)
            rel_docname = os.path.relpath(docname, dir_docname).replace("\\", "/")
            entry = f"- :doc:`{rel_docname}`"
            rst.append(entry, filename, line_number)

        node = nodes.section()
        node.document = self.state.document
        self.state.nested_parse(rst, 0, node)

        for generated_node in node.traverse():
            generated_node.source = self.env.docname + ".rst"
            generated_node.line = line_number

        return node.children
