import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

from .helper import DimViewList
from .report_input import calc_table_input_developer, calc_table_input_review_status
from .report_architecture import calc_table_architecture_type
from .report_module import calc_table_module_type
from .report_source import calc_source_list
from .report_generic import (
    calc_table_status,
    calc_table_safety,
    calc_table_stream,
    calc_table_list,
    calc_table_security,
    calc_table_cal,
)


logger = logging.getLogger(__name__)


class DoxTraceTraceabilityDirective(SphinxDirective):
    required_arguments = 1  # ID
    has_content = False
    option_spec = {"developer": directives.unchanged_required}

    def add_chapter(self, category, function_name, title, text=""):
        if title:
            title_node = DimViewList.string_to_nodes(
                [title, len(title) * "-", text], self.content_offset, self
            )
        else:
            title_node = [nodes.inline()]
        report_node = nodes.comment()
        report_node.attributes["traceability_report"] = category
        report_node.attributes["traceability_report_function"] = function_name
        report_node.attributes["developer"] = (
            self.options["developer"] if category != "source" else None
        )
        title_node[0] += report_node
        return title_node

    def run(self):
        category = self.arguments[0]
        document = self.state.document
        line_number = self.get_source_info()[1]

        if category not in ["input", "software", "architecture", "module", "source"]:
            logger.error(
                f"{document.settings.env.docname}.rst:{line_number}: category must be input, software, architecture, module or source"
            )

        if category != "source":
            if "developer" not in self.options:
                raise Exception(
                    f"{document.settings.env.docname}.rst:{line_number}: developer option not specified"
                )
            else:
                developer = self.options["developer"]
        else:
            developer = None

        if self.env.config.dox_trace_security_backward:
            calc_table_security_cal = calc_table_security
        else:
            calc_table_security_cal = calc_table_cal

        # fmt: off
        filter_heading    = "**Filter:** |br| "
        upstream_sufficiency   = " |br| |br| **Upstream Sufficiency:** |br| "
        downstream_sufficiency = " |br| |br| **Downstream Sufficiency:** |br| "

        srs_up = upstream_sufficiency + "Either an upstream reference exists or the element is tagged with *tool*."
        swa_up = upstream_sufficiency + "Either an upstream reference exists to SRS/SWA or the element is tagged with *tool*."
        smd_up = upstream_sufficiency + "Either an upstream reference exists to SWA/SMD or the element is tagged with *tool*."

        inp_down = downstream_sufficiency + "Either a downstream reference exists, the element is not *rejected* or the element is tagged with *covered*."
        srs_down = downstream_sufficiency + "Either a downstream reference exists, the element is tagged with *covered* or a source is specified."
        swa_down = downstream_sufficiency + "Either a downstream reference exists, the element is tagged with *covered* or a location/source is specified."
        smd_down = downstream_sufficiency + "Either a downstream reference exists, the element is tagged with *covered* or a source is specified."

        node_list = []
        if category == "input":
            node_list.extend(self.add_chapter(category, calc_table_input_developer,     "Developer", filter_heading + "type = requirement"))
            node_list.extend(self.add_chapter(category, calc_table_status,              "Status", filter_heading + f"type = requirement |br| developer = {developer}"))
            node_list.extend(self.add_chapter(category, calc_table_input_review_status, "Review Status", filter_heading + f"type = requirement |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_safety,              "Functional Safety", filter_heading + f"type = requirement |br| developer = {developer} |br| status = valid |br| review_status = accepted"))
            node_list.extend(self.add_chapter(category, calc_table_security_cal,        "Cyber Security", filter_heading + f"type = requirement |br| developer = {developer} |br| status = valid |br| review_status = accepted"))
            node_list.extend(self.add_chapter(category, calc_table_stream,              "Downstream", filter_heading + f"type = requirement |br| developer = {developer} |br| status = valid |br| review_status = accepted" + inp_down))
            node_list.extend(self.add_chapter(category, calc_table_list,                "List of Requirements", filter_heading + f"type = requirement |br| developer = {developer} |br| status = valid |br| review_status = accepted"))
        elif category == "software":
            node_list.extend(self.add_chapter(category, calc_table_status,              "Status", filter_heading + f"type = requirement / srs |br| developer = {developer}"))
            node_list.extend(self.add_chapter(category, calc_table_safety,              "Functional Safety", filter_heading + f"type = requirement / srs |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_security_cal,        "Cyber Security", filter_heading + f"type = requirement / srs |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_stream,              "Upstream and Downstream", filter_heading + f"type = requirement / srs |br| developer = {developer} |br| status = valid" + srs_up + srs_down))
            node_list.extend(self.add_chapter(category, calc_table_list,                "List of Requirements", filter_heading + f"type = requirement / srs |br| developer = {developer} |br| status = valid"))
        elif category == "architecture":
            node_list.extend(self.add_chapter(category, calc_table_status,              "Status", filter_heading + f"type = spec / interface / mod |br| developer = {developer}"))
            node_list.extend(self.add_chapter(category, calc_table_architecture_type,   "Type", filter_heading + f"type = spec / interface / mod |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_safety,              "Functional Safety", filter_heading + f"type = spec / interface / mod |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_security_cal,        "Cyber Security", filter_heading + f"type = spec / interface / mod |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_stream,              "Upstream and Downstream", filter_heading + f"type = spec / interface / mod |br| developer = {developer} |br| status = valid" + swa_up + swa_down))
            node_list.extend(self.add_chapter(category, calc_table_list,                "List of Specifications", filter_heading + f"type = spec / interface / mod |br| developer = {developer} |br| status = valid"))
        elif category == "module":
            smd_interface = "/ interface " if self.env.config.dox_trace_allow_deprecated else ""
            node_list.extend(self.add_chapter(category, calc_table_status,              "Status", filter_heading + f"type = spec {smd_interface}/ unit |br| developer = {developer}"))
            node_list.extend(self.add_chapter(category, calc_table_module_type,         "Type", filter_heading + f"type = spec {smd_interface}/ unit |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_safety,              "Functional Safety", filter_heading + f"type = spec {smd_interface}/ unit |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_security_cal,        "Cyber Security", filter_heading + f"type = spec {smd_interface}/ unit |br| developer = {developer} |br| status = valid"))
            node_list.extend(self.add_chapter(category, calc_table_stream,              "Upstream and Downstream", filter_heading + f"type = spec {smd_interface}/ unit |br| developer = {developer} |br| status = valid" + smd_up + smd_down))
            node_list.extend(self.add_chapter(category, calc_table_list,                "List of Specifications", filter_heading + f"type = spec {smd_interface}/ unit |br| developer = {developer} |br| status = valid"))
        else: # source
            node_list.extend(self.add_chapter(category, calc_source_list,               None,                     None))
        # fmt: on

        return node_list


def get_modules(app, requested_category):
    std = app.env.domaindata["std"]

    global dox_trace_modules
    if "dox_trace_modules" not in globals():
        dox_trace_modules = {}
        for ref_id, spec_id in sorted(std["spec_id"].items()):
            options = std["spec_options"][ref_id]
            if options["role"] in ["information"]:
                continue
            if "ignore_in_export" in options:
                continue

            if "module_name" in std["spec_options"][ref_id]:
                module_name = std["spec_options"][ref_id]["module_name"]
            else:
                m = re.match(r"^(([^_]+)_[^_]+)", spec_id)
                module_name = m.group(1)

            category = options["category"]
            if category not in dox_trace_modules:
                dox_trace_modules[category] = {}
            if module_name not in dox_trace_modules[category]:
                dox_trace_modules[category][module_name] = []
            dox_trace_modules[category][module_name].append(ref_id)

        for category in dox_trace_modules.keys():
            mdict = dox_trace_modules[category]
            dox_trace_modules[category] = {name: mdict[name] for name in sorted(mdict)}

    if requested_category in dox_trace_modules:
        return dox_trace_modules[requested_category]
    return None


def inject_report(app, doctree, fromdocname):
    for node in doctree.traverse(nodes.comment):
        if "traceability_report" in node.attributes:
            category = node.attributes["traceability_report"]
            function_name = node.attributes["traceability_report_function"]
            developer = node.attributes["developer"]

            modules = get_modules(app, category)
            if modules or category == "source":
                table = function_name(app, category, fromdocname, modules, developer)
            else:
                table = None
            if table:
                node.replace_self(table)
            else:
                node.replace_self(nodes.paragraph("", "", nodes.emphasis("", "No data yet")))
