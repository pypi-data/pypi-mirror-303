from docutils import nodes
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

logger = logging.getLogger(__name__)


def prop_read(config, module, attribute):
    if (
        isinstance(config.properties, dict)
        and module in config.properties
        and isinstance(config.properties[module], dict)
        and attribute in config.properties[module]
    ):
        return config.properties[module][attribute]
    return None


def prop_value(config, text, filename, line_number):
    value = None
    if hasattr(config, "properties"):
        split = text.split(":")
        if len(split) == 2:
            module = split[0]
            attribute = split[1]
            value = prop_read(config, module, attribute)
            if not value:
                value = prop_read(config, "_default_", attribute)
            if not value:
                logger.error(f"{filename}.rst:{line_number}: property {text} not found")
        else:
            logger.error(
                f'{filename}.rst:{line_number}: property {text} does not include exactly one ":"'
            )
    else:
        logger.error(
            f"{filename}.rst:{line_number}: dox_trace_properties_file not specified in configuration"
        )
    return value


def prop_role(_role, rawtext, text, lineno, inliner, _options={}, _content=[]):
    env = inliner.document.settings.env
    config = env.app.config
    value = prop_value(config, text, env.docname, lineno)

    node = nodes.literal(rawtext, value)
    node.set_class("highlight")
    node.set_class("highlight-prop")

    return [node], []


class PropDirective(SphinxDirective):
    required_arguments = 1
    has_content = False

    def run(self):
        spec_id = self.arguments[0]
        filename = self.get_source_info()[0]
        document = self.state.document
        line_number = self.get_source_info()[1]

        value = prop_value(self.env.app.config, spec_id, document.settings.env.docname, line_number)

        rst = ViewList()
        for line in value.split("\n"):
            rst.append(line, filename, line_number)

        node = nodes.section()
        node.document = document
        nested_parse_with_titles(self.state, rst, node)
        return node.children
