from sphinx.util import logging
from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from .helper import create_ref_node

logger = logging.getLogger(__name__)


def calc_unresolved_references(_app, env):
    std = env.domaindata["std"]
    spec_options = std["spec_options"]

    undefined_map = std["undefined_map"] = {}

    for ref_id, options in spec_options.items():
        resolved_refs = []
        for target_spec_id in spec_options[ref_id]["refs"]:
            target_spec_id_lower = target_spec_id.lower()
            if (
                target_spec_id_lower not in spec_options
                and target_spec_id_lower not in std["labels"]
            ):
                if ref_id not in undefined_map:
                    undefined_map[ref_id] = []
                undefined_map[ref_id].append(target_spec_id)
            else:
                # this adds invalid refs again which are reported in check_invalid_refs
                resolved_refs.append(target_spec_id)
        if len(resolved_refs) == 0:
            spec_options[ref_id]["refs"] = []
        else:
            spec_options[ref_id]["refs"] = resolved_refs


def inject_undefined_references(app, doctree, fromdocname):
    std = app.env.domaindata["std"]
    undefined_map = std["undefined_map"]

    for node in doctree.traverse(nodes.comment):
        if "undefined_refs" in node.attributes and node.attributes["undefined_refs"]:
            if len(undefined_map) == 0:
                node.replace_self(nodes.emphasis("", "No undefined references found."))
                continue

            node_list = nodes.bullet_list()
            refs_ids = undefined_map.keys()
            for ref_id in sorted(refs_ids):
                ref_node = create_ref_node(app, ref_id, fromdocname)

                node_para = nodes.paragraph("", "")
                node_para.append(ref_node)
                node_para.append(nodes.Text(": " + ", ".join(undefined_map[ref_id])))

                node_item = nodes.list_item()
                node_list.append(node_item)
                node_item.append(node_para)

            node.replace_self(node_list)


class UndefinedRefsDirective(SphinxDirective):
    def run(self):
        n = nodes.comment()
        n.attributes["undefined_refs"] = True
        return [n]
