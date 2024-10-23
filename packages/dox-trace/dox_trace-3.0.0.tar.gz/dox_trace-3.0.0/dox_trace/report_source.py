from .helper import create_ref_node

from docutils import nodes
from sphinx.util import logging

logger = logging.getLogger(__name__)


def calc_source_backward(std):
    sources = {}
    for docname, ref_ids in std["local_ordered"].items():
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            if "sources_base" in options:
                for f in options["sources_base"]:
                    if f not in sources:
                        sources[f] = []
                    sources[f].append(ref_id)
    return sources


def calc_source_list(app, _category, fromdocname, _modules, _developer):
    std = app.env.domaindata["std"]
    sources = calc_source_backward(std)

    if len(sources) == 0:
        return None

    node_list = nodes.bullet_list()
    for source in sorted(sources.keys()):
        ref_ids = sources[source]
        ref_ids.sort()
        rs = []
        for ref_id in ref_ids:
            ref_node = create_ref_node(app, ref_id, fromdocname)
            if len(rs) > 0:
                rs.append(nodes.Text(", "))
            rs.append(ref_node)
        node_para_source = nodes.paragraph("", "", nodes.literal("", source))
        node_para_refs = nodes.paragraph()
        node_para_refs += rs

        node_item = nodes.list_item()
        node_list.append(node_item)
        node_item.append(node_para_source)
        node_item.append(node_para_refs)

    return node_list
