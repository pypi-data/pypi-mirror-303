import re
from pathlib import Path
from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles
from sphinx.util import logging

from .directives import (
    UnitDirective,
    SpecDirective,
    InterfaceDirective,
    RequirementDirective,
    InformationDirective,
    ModDirective,
    SrsDirective,
    DoxTraceDirective,
)

logger = logging.getLogger(__name__)


def config_inited(app, config):
    static = Path.joinpath(Path(__file__).parent, "_static").as_posix()
    config.html_static_path.append(static)
    config.templates_path.append(static)

    app.add_css_file("dox_trace.css")
    config.html_js_files.append("dox_trace.js")

    project = config.project if "project" in config and config.project else "Default"
    project_clean = re.sub(r"\W+", "", project)

    config.rst_prolog += f"""
.. meta::
    :dox_trace_storage: {project_clean}
"""

    directive_map = {
        "unit": UnitDirective,
        "spec": SpecDirective,
        "interface": InterfaceDirective,
        "requirement": RequirementDirective,
        "information": InformationDirective,
        "mod": ModDirective,
        "srs": SrsDirective,
    }

    type_map = {
        # pylint: disable=unnecessary-lambda
        "text": lambda value: DoxTraceDirective.free_text(value),
        "enum": lambda value: DoxTraceDirective.multi_enum(value),
        "refs": lambda value: DoxTraceDirective.multi_enum(value),
        # pylint: enable=unnecessary-lambda
    }

    # fmt: off
    for name, attr in config.dox_trace_custom_attributes.items():
        # STEP 1: check input

        # name

        if not isinstance(name, str):
            logger.error("Names of custom attributes in config file must be strings")
        if name in list(DoxTraceDirective.attribute_functions.keys()) + ["text"]:
            logger.error(f"Custom attribute {name} in config file already exists")
        if not isinstance(attr, dict):
            logger.error(f"Custom attribute {name} in config file has wrong type")

        # type

        if "type" not in attr or not isinstance(attr["type"], str):
            logger.error(f"Custom attribute {name} in config file must have a valid type")
        if attr["type"] not in ["text", "enum", "refs"]:
            logger.error(f"Custom attribute {name} in config file has invalid type {attr['type']}")

        # directive

        if "directives" not in attr or not isinstance(attr["directives"], list) or len(attr["directives"]) == 0:
            logger.error(f"Custom attribute {name} in config file must be assigned to a list of at least one directive")
        for d in attr["directives"]:
            if d not in ["mod", "spec", "unit", "interface", "requirement", "information", "srs"]:
                logger.error(f"Custom attribute {name} in config file is assigned to invalid directive {d}")

        # category

        if "requirement" in attr["directives"] or "information" in attr["directives"]:
            if "categories" not in attr or not isinstance(attr["categories"], list) or len(attr["categories"]) == 0:
                logger.error(f"Custom attribute {name} in config file must be assigned to a list of at least one category")
            for c in attr["categories"]:
                if c not in ["input", "software", "system"]:
                    logger.error(f"Custom attribute {name} in config file is assigned to invalid category {c}")
        else:
            attr["categories"] = None

       # default

        if "default" in attr:
            if attr["type"] != "text":
                if not isinstance(attr["default"], list):
                    logger.error(f"Custom attribute {name} in config file must have type list for default")
                else:
                    attr["default"] = list(dict.fromkeys(attr["default"])) # make unique
            elif not isinstance(attr["default"], str):
                logger.error(f"Custom attribute {name} in config file must have type string for default")
            if attr["default"] in ["", []]:
                attr["default"] = None
        else:
            attr["default"] = None

        # export

        if "export" not in attr:
            attr["export"] = "no"
        else:
            if not isinstance(attr["export"], str):
                logger.error(f"Custom attribute {name} in config file has invalid type for export")
            if attr["export"] not in ["yes", "no"]:
                logger.error(f"Custom attribute {name} in config file has invalid value {attr['export']} for export")

        # STEP 2: add common_attribute data to directives

        if attr["export"] == "yes":
            DoxTraceDirective.attribute_mappings["valid_in_dim"].append(name)
        DoxTraceDirective.custom_attributes[name] = {
            "type": attr["type"],
            "default": attr["default"],
            "categories": attr["categories"],
        }

        for d in attr["directives"]:
            directive_map[d].option_spec[name] = type_map[attr["type"]]
    # fmt: on


class DoxTraceConfigDirective(SphinxDirective):
    def run(self):
        config = """.. raw:: html

            <p>Type, ID and content are always shown. Visibility of the other attributes:</p>

            <p>
            <input type="radio" id="dox_trace_config_none" checked="checked" name="dox_trace_config" onclick="dox_trace_config_changed(this)" value="none">
            Show all<br>
 
            <input type="radio" id="dox_trace_config_empty" name="dox_trace_config" onclick="dox_trace_config_changed(this)" value="empty">
            Hide empty<br>
 
            <input type="radio" id="dox_trace_config_missing" name="dox_trace_config" onclick="dox_trace_config_changed(this)" value="missing">
            Hide empty and "[missing]"<br>
 
            <input type="radio" id="dox_trace_config_all" name="dox_trace_config" onclick="dox_trace_config_changed(this)" value="all">
            Hide all
            </p>
        """

        filename = self.get_source_info()[0]
        line_number = self.get_source_info()[1]

        rst = ViewList()
        for line in config.split("\n"):
            rst.append(line, filename)

        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, rst, node)

        for generated_node in node.traverse():
            generated_node.line = line_number

        return node.children
