from docutils import nodes

from .helper import cat_name2level, create_ref_node
from .directives import DoxTraceDirective

from sphinx.util import logging

logger = logging.getLogger(__name__)


def calc_parents(spec_options, target_ref_id):
    current = spec_options[target_ref_id]
    if "parents" not in current:
        parents = set()
        current["parents"] = parents
        for r in current["upstream_refs"]:
            opt = spec_options[r]
            if r not in parents and opt["role"] != "information" and not opt["strike"]:
                if opt["role"] == "requirement" and opt["category"] == "input":
                    parents.add(r)
                grandparents = calc_parents(spec_options, r)
                parents.update(grandparents)
    return current["parents"]


def calc_backward(_app, env):
    std = env.domaindata["std"]

    spec_options = std["spec_options"]
    for ref_id, options in spec_options.items():
        options["upstream_refs"] = set()
        options["downstream_refs"] = set()

    # direct parents
    for source_ref_id, source_options in spec_options.items():
        if "refs" in source_options:
            source_cat_level = cat_name2level[source_options["category"]]

            for target_spec_id in source_options["refs"]:
                target_ref_id = target_spec_id.lower()
                if target_ref_id in spec_options:
                    target_options = spec_options[target_ref_id]
                    target_cat_level = cat_name2level[target_options["category"]]
                    if target_cat_level > source_cat_level:
                        source_options["upstream_refs"].add(target_ref_id)
                        target_options["downstream_refs"].add(source_ref_id)
                    else:
                        source_options["downstream_refs"].add(target_ref_id)
                        target_options["upstream_refs"].add(source_ref_id)
                else:
                    source_options["downstream_refs"].add(target_spec_id)
        else:
            spec_options[source_ref_id]["refs"] = []

    # all parents (without information)
    for target_ref_id in spec_options:
        calc_parents(spec_options, target_ref_id)

    return None


def upstream_missing_trace(options):
    return not options["strike"] and ("tags" not in options or "tool" not in options["tags"])


def upstream_missing(options):
    return (
        upstream_missing_trace(options)
        and options["category"] != "input"
        and options["role"] != "information"
    )


def downstream_missing_trace(options):
    return (
        not options["strike"]
        and not ("tags" in options and "covered" in options["tags"])
        and not (options["category"] == "module" and options["role"] == "interface")
    )


def downstream_missing(options):
    return downstream_missing_trace(options) and not options["role"] in ["unit", "information"]


def inject_backward_references(app, doctree, fromdocname):
    std = app.env.domaindata["std"]
    allow_undefined_refs = app.env.config.dox_trace_allow_undefined_refs
    spec_options = std["spec_options"]
    for node in doctree.traverse(nodes.comment):
        if "backward_ref_id" in node.attributes and "backward_attr" in node.attributes:
            target_ref_id = node.attributes["backward_ref_id"]
            target_attribute = node.attributes["backward_attr"]

            if target_attribute == "upstream":
                rs = []
                options = spec_options[target_ref_id]
                attr_formatted = node.attributes["backward_attr_formatted"]
                inline = nodes.inline()
                inline.set_class("dox-trace-grey")
                for source_ref_id in sorted(spec_options[target_ref_id]["upstream_refs"]):
                    ref_node = create_ref_node(app, source_ref_id, fromdocname)
                    if len(rs) == 0:
                        rs.append(nodes.raw("", attr_formatted, format="html"))
                    else:
                        rs.append(nodes.Text(", "))
                    rs.append(ref_node)
                if len(rs) == 0:
                    if upstream_missing(options):
                        inline.set_class("dox-trace-attribute-missing")
                        html = f"{attr_formatted}[missing]<br>"
                    else:
                        inline.set_class("dox-trace-attribute-empty")
                        html = f"{attr_formatted}-<br>"
                    rs.append(nodes.raw("", html, format="html"))
                else:
                    rs.append(nodes.raw("", "<br>", format="html"))
                for n in rs:
                    inline.append(n)
                node.replace_self(inline)
            elif target_attribute == "downstream":
                rs = []
                options = spec_options[target_ref_id]
                attr_formatted = node.attributes["backward_attr_formatted"]
                inline = nodes.inline()
                inline.set_class("dox-trace-grey")
                for source_ref_id in sorted(spec_options[target_ref_id]["downstream_refs"]):
                    if source_ref_id in spec_options:
                        ref_node = create_ref_node(app, source_ref_id, fromdocname)
                    else:
                        # source_ref_id is spec_id in this case (not lower-cased)
                        if allow_undefined_refs:
                            html = DoxTraceDirective.red + source_ref_id + DoxTraceDirective.colEnd
                            ref_node = nodes.raw("", html, format="html")
                        else:
                            spec_node = std["spec_node"][target_ref_id]
                            target_spec_id = std["spec_id"][target_ref_id]
                            logger.error(
                                f"{spec_node.source}.rst:{spec_node.line}: {target_spec_id} refers to non-existing {source_ref_id}"
                            )
                            continue
                    if len(rs) == 0:
                        rs.append(nodes.raw("", attr_formatted, format="html"))
                    else:
                        rs.append(nodes.Text(", "))
                    rs.append(ref_node)
                if len(rs) == 0:
                    if downstream_missing(options):
                        inline.set_class("dox-trace-attribute-missing")
                        html = f"{attr_formatted}[missing]<br>"
                    else:
                        inline.set_class("dox-trace-attribute-empty")
                        html = f"{attr_formatted}-<br>"
                    rs.append(nodes.raw("", html, format="html"))
                else:
                    rs.append(nodes.raw("", "<br>", format="html"))
                for n in rs:
                    inline.append(n)
                node.replace_self(inline)
            elif target_attribute in [
                "parent_asil",
                "parent_security",
                "parent_cal",
                "parent_tags",
            ]:
                inline = nodes.inline()
                inline.set_class("dox-trace-grey")
                node.replace_self(inline)
                attr_formatted = node.attributes["backward_attr_formatted"]
                if (
                    "upstream_refs" not in spec_options[target_ref_id]
                    or len(spec_options[target_ref_id]["upstream_refs"]) == 0
                ):
                    inline.set_class("dox-trace-attribute-empty")
                    html = f"{attr_formatted}-"
                    inline.append(nodes.raw("", html, format="html"))
                else:
                    opt = target_attribute[7:]
                    elems = set()
                    for p in sorted(spec_options[target_ref_id]["upstream_refs"]):
                        obw = spec_options[p]
                        if obw["role"] != "information" and not obw["strike"] and opt in obw:
                            attr = spec_options[p][opt]
                            if isinstance(attr, list):
                                elems.update(attr)
                            else:
                                elems.add(attr)
                    if len(elems) == 0:
                        inline.set_class("dox-trace-attribute-empty")
                        html = f"{attr_formatted}-"
                        inline.append(nodes.raw("", html, format="html"))
                    else:
                        inline.append(
                            nodes.raw("", attr_formatted + ", ".join(sorted(elems)), format="html")
                        )

            else:  # target_attribute in ["parent_feature", "parent_change_request"]
                inline = nodes.inline()
                inline.set_class("dox-trace-grey")
                node.replace_self(inline)
                attr_formatted = node.attributes["backward_attr_formatted"]
                if (
                    "parents" not in spec_options[target_ref_id]
                    or len(spec_options[target_ref_id]["parents"]) == 0
                ):
                    inline.set_class("dox-trace-attribute-empty")
                    html = f"{attr_formatted}-<br>"
                    inline.append(nodes.raw("", html, format="html"))
                else:
                    opt = target_attribute[7:]
                    elems = set()
                    raw_nodes = []

                    for p in sorted(spec_options[target_ref_id]["parents"]):
                        v = spec_options[p][opt]
                        if v in elems or v == "":
                            continue
                        elems.add(v)
                        if len(raw_nodes) > 0:
                            raw_nodes.append(nodes.Text(", "))
                        val = v.strip()
                        parent_node_key = opt + "_nodes"
                        if parent_node_key in spec_options[p]:
                            for n in spec_options[p][parent_node_key]:
                                raw_nodes.append(n.deepcopy())
                        else:
                            # ensured in directives.py:
                            # len(val) > 12 and val.startswith(":raw-html:")
                            # otherwise this would be an alternative:
                            # raw_nodes.append(nodes.Text(val.replace("\n", " ")))
                            raw_nodes.append(nodes.raw("", val[11:-1], format="html"))

                    if len(elems) == 0:
                        inline.set_class("dox-trace-attribute-empty")
                        html = f"{attr_formatted}-<br>"
                        inline.append(nodes.raw("", html, format="html"))
                    else:
                        inline.append(nodes.raw("", attr_formatted, format="html"))
                        for n in raw_nodes:
                            inline.append(n)
                        inline.append(nodes.raw("", "<br>", format="html"))
