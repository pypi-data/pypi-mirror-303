from docutils import nodes

from .env import add_node_to_env


def spec_role(role, rawtext, text, lineno, inliner, _options={}, _content=[]):
    env = inliner.document.settings.env

    spec_id = text
    ref_id = spec_id.lower()
    role = role.replace("_generated", "")

    node = nodes.literal(rawtext, "[" + role + "] ")
    node.set_class("highlight")
    node.set_class("highlight-%s" % role)
    node.line = lineno

    self_ref = nodes.reference(spec_id, spec_id, refdocname=env.docname, refid=ref_id)
    node.append(self_ref)

    target_node = nodes.target("", "", ids=[ref_id])

    add_node_to_env(inliner.document, spec_id, node)

    return [target_node, node], []
