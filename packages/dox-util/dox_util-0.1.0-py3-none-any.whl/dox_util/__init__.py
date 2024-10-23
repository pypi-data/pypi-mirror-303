from .extlinks import *
from .linkcheck import *
from .rule import *
from .source import *
from .toctree import *
from .todo import *
from .weak import *
from .version import __version__

from pathlib import Path


def config_inited(app, config):
    static = Path.joinpath(Path(__file__).parent, "_static").as_posix()
    config.html_static_path.append(static)
    app.add_css_file("dox_util_colors.css")


def setup(app):
    # extlinks
    app.connect("builder-inited", setup_link_roles)

    # linkcheck
    app.add_builder(builder=LinkChecker, override=True)

    # rule
    app.add_role("rule", rule_role)

    # source
    app.add_role("source", source_role)
    app.add_directive("sourceinclude", SourceInclude)

    # toctree
    app.add_directive("tolerant-toctree", TolerantTocTree)
    app.add_directive("doclist", DocList)

    # todo
    app.add_role("todo", todo_role)

    # weak
    app.add_role("weakref", weak_role)
    app.add_role("weakdoc", weak_role)
    app.add_config_value("enable_weak_warnings", False, "html")

    # common CSS definitions
    app.connect("config-inited", config_inited)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
