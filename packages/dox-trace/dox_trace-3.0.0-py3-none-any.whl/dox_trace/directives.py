import re
import os.path
from pathlib import Path
from typing import Dict, List, Any

from docutils.parsers.rst import directives
from docutils import nodes
from sphinx import addnodes
from sphinx.util.docutils import SphinxDirective

from sphinx.util import logging

from .helper import DimViewList
from .roles import spec_role

logger = logging.getLogger(__name__)


class DoxTraceDirective(SphinxDirective):
    strike: bool
    isInputReq: bool
    isSRS: bool
    iface_back_comp: bool
    options: Dict[str, Any]
    content: List[str]

    required_arguments = 1  # ID
    has_content = True  # text
    final_argument_whitespace = True

    red = '<span class="dox-trace-red">'
    grey = '<span class="dox-trace-grey">'
    colEnd = "</span>"

    custom_attributes = {}

    @staticmethod
    def strip(value):
        if value is None:
            return ""
        value = value.strip()
        if len(value) > 1:
            if (value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'"):
                value = value[1:-1]
                return value.strip()
        return value

    @staticmethod
    def multi_enum(value):
        value = DoxTraceDirective.strip(value)
        if value is None or value.strip() in ['""', "''", ""]:
            return []
        stripped_list = []
        for s in value.split(","):
            s = DoxTraceDirective.strip(s)
            if s != "" and s not in stripped_list:
                stripped_list.append(s)
        if len(stripped_list) == 0:
            return []
        return stripped_list

    @staticmethod
    def free_text(value):
        value = DoxTraceDirective.strip(value)
        if value is None or value.strip() in ['""', "''", ""]:
            return ""
        return value

    # fmt: off
    attribute_functions = {
        # pylint: disable=unnecessary-lambda
        "status":                   lambda value: DoxTraceDirective.free_text(value),
        "review_status":            lambda value: DoxTraceDirective.free_text(value),
        "feature":                  lambda value: DoxTraceDirective.free_text(value),
        "change_request":           lambda value: DoxTraceDirective.free_text(value),
        "asil":                     lambda value: DoxTraceDirective.free_text(value),
        "security":                 lambda value: DoxTraceDirective.free_text(value),
        "cal":                      lambda value: DoxTraceDirective.free_text(value),
        "reuse":                    lambda value: DoxTraceDirective.free_text(value),
        "usage":                    lambda value: DoxTraceDirective.free_text(value),
        "tags":                     lambda value: DoxTraceDirective.multi_enum(value),

        "developer":                lambda value: DoxTraceDirective.free_text(value),
        "tester":                   lambda value: DoxTraceDirective.free_text(value),
        "test_setups":              lambda value: DoxTraceDirective.multi_enum(value),
        "verification_methods":     lambda value: DoxTraceDirective.multi_enum(value),

        "verification_criteria":    lambda value: DoxTraceDirective.free_text(value),
        "comment":                  lambda value: DoxTraceDirective.free_text(value),
        "miscellaneous":            lambda value: DoxTraceDirective.free_text(value),

        "sources":                  lambda value: DoxTraceDirective.multi_enum(value),
        "refs":                     lambda value: DoxTraceDirective.multi_enum(value),
        "location":                 lambda value: DoxTraceDirective.free_text(value),

        "category":                 lambda value: DoxTraceDirective.free_text(value),
        # pylint: enable=unnecessary-lambda
    }
    attribute_mappings = {
        # pylint: disable=line-too-long
        "mod":          ["status", "review_status", "asil", "security", "cal",         "developer",                                                                                                                                                                         "reuse", "usage", "location"],
        "spec":         ["status", "review_status", "asil", "security", "cal", "tags", "developer", "tester", "test_setups", "verification_methods", "verification_criteria",                                                          "sources", "refs"                                                ],
        "unit":         ["status", "review_status", "asil", "security", "cal", "tags", "developer", "tester", "test_setups", "verification_methods", "verification_criteria",                                                          "sources", "refs"                                                ],
        "interface":    ["status", "review_status", "asil", "security", "cal", "tags", "developer", "tester", "test_setups", "verification_methods", "verification_criteria",                                                          "sources", "refs"                                                ],
        "srs":          ["status", "review_status", "asil", "security", "cal", "tags", "developer", "tester", "test_setups", "verification_methods", "verification_criteria",                                                          "sources", "refs",                                               ],
        "requirement":  ["status", "review_status", "asil", "security", "cal", "tags", "developer", "tester", "test_setups", "verification_methods", "verification_criteria", "comment", "miscellaneous", "feature", "change_request", "sources", "refs", "category"                                    ],
        "information":  ["status", "review_status", "asil", "security", "cal", "tags",                                                                                        "comment", "miscellaneous",                                         "refs", "category"                                    ],
        "valid_in_dim": ["status", "review_status", "asil",                    "tags", "developer", "tester",                                        "verification_criteria", "comment", "miscellaneous", "feature", "change_request", "sources", "refs",            "text"                             ],
        # pylint: enable=line-too-long
    }
    # fmt: on

    @staticmethod
    def create_option_spec(role):
        option_spec_name = {"ignore_in_export": directives.flag}
        for attr in DoxTraceDirective.attribute_mappings[role]:
            option_spec_name[attr] = DoxTraceDirective.attribute_functions[attr]
        return option_spec_name

    def attr_name(self, name, value, first=False):
        separator = "" if first else " | "

        if value == "-":
            prefix = '<span class="dox-trace-attribute-empty">'
            postfix = "</span>"
        elif value == "[missing]":
            prefix = '<span class="dox-trace-attribute-missing">'
            postfix = "</span>"
        else:
            prefix = ""
            postfix = ""

        return f"{prefix}{separator}<strong>{name}:</strong> {value}{postfix}"

    def calc_status_attr(self):
        if "status" in self.options:
            status = self.options["status"]
        else:
            status = "draft"
            self.options["status"] = status
        if status == "invalid":
            self.strike = True

        if "review_status" in self.options:
            review_status = self.options["review_status"]
        else:
            if self.isInputReq:
                review_status = "not_reviewed"
            else:
                review_status = "accepted"
            self.options["review_status"] = review_status

        if review_status in ["rejected", "not_relevant"]:
            self.strike = True

        attr = ["<strong>Status:</strong> ", status]

        if self.isInputReq or review_status != "accepted":
            attr.append(f" | <strong>Review Status:</strong> {review_status}")

        return "".join(attr)

    def calc_test_dev_attr(self, spec_id):
        attr = []

        if self.role not in ["information"]:
            ref_id = spec_id.lower()

            developer = self.options["developer"] if "developer" in self.options else None
            if developer:
                developer = developer.replace("\n", " ")
            else:
                self.options["developer"] = ""
                if self.strike:
                    developer = "-"
                else:
                    developer = "[missing]"
            attr.append(self.attr_name("Developer", developer, True))

            self.options["developer_split"] = [
                d.strip() for d in self.options["developer"].split(",")
            ]

            if self.env.config.dox_trace_test_setups_backward:
                if "verification_methods" in self.options and "test_setups" not in self.options:
                    self.options["test_setups"] = self.options["verification_methods"]
                ts_attr_name = "test_setups"
                ts_display_name = "Test Setups"
            else:
                if "test_setups" in self.options and "verification_methods" not in self.options:
                    self.options["verification_methods"] = self.options["test_setups"]
                ts_attr_name = "verification_methods"
                ts_display_name = "Verification Methods"

            if (self.role != "mod") and not self.iface_back_comp:
                tester = self.options["tester"] if "tester" in self.options else None
                if tester:
                    tester = tester.replace("\n", " ")
                else:
                    self.options["tester"] = ""
                    if self.strike or (
                        ts_attr_name in self.options
                        and len(self.options[ts_attr_name]) == 1
                        and self.options[ts_attr_name][0] == "none"
                    ):
                        tester = "-"
                    else:
                        tester = "[missing]"
                attr.append(self.attr_name("Tester", tester))

                ts = None

                if ts_attr_name in self.options:
                    ts = self.options[ts_attr_name]
                if not ts:
                    if self.role in ["unit", "spec", "interface", "srs"]:
                        if ref_id.startswith("smd_"):
                            ts = ["off_target"]
                        else:  # must be swa_ or srs_
                            ts = ["on_target"]
                        self.options[ts_attr_name] = ts
                    else:
                        self.options[ts_attr_name] = "none"
                if ts:
                    test_setups = ", ".join(ts)
                else:
                    test_setups = "-"
                attr.append(self.attr_name(ts_display_name, test_setups))

                if (
                    developer not in ["-", "[missing]"]
                    or tester not in ["-", "[missing]"]
                    or test_setups != "-"
                ):
                    attr.append("<br>")
                elif developer == "[missing]" or tester == "[missing]":
                    attr.append('<span class="dox-trace-attribute-missing"><br></span>')
                else:
                    attr.append('<span class="dox-trace-attribute-empty"><br></span>')
            else:
                self.options["tester"] = ""
                self.options[ts_attr_name] = ["none"]

        return "".join(attr)

    def get_property(self, module_name, attribute_name):
        p = self.env.config.properties
        if module_name in p and attribute_name in p[module_name]:
            return p[module_name][attribute_name]
        return None

    def calc_asil_sec_review_attr(self):
        attr = ["<strong>Asil:</strong> "]

        if "asil" in self.options:
            asil = self.options["asil"]
        else:
            asil = "not_set"
            self.options["asil"] = asil
        attr.append(asil)

        if self.env.config.dox_trace_security_backward:
            if "security" in self.options:
                sec = self.options["security"]
            else:
                if "cal" in self.options:
                    if self.options["cal"] == "QM":
                        sec = "no"
                    elif self.options["cal"] in ["CAL_1", "CAL_2", "CAL_3", "CAL_4"]:
                        sec = "yes"
                    else:
                        sec = "not_set"
                else:
                    sec = "not_set"
                self.options["security"] = sec
            attr.append(f" | <strong>Security:</strong> {sec}")
        else:
            if "cal" in self.options:
                cal = self.options["cal"]
            else:
                if "security" in self.options:
                    if self.options["security"] == "yes":
                        cal = "CAL_4"
                    elif self.options["security"] == "no":
                        cal = "QM"
                    else:
                        cal = "not_set"
                else:
                    cal = "not_set"
                self.options["cal"] = cal
            attr.append(f" | <strong>Cal:</strong> {cal}")

        if self.role == "mod":
            if "reuse" in self.options and self.options["reuse"] != "":
                attr.append(" | <strong>Reuse:</strong> " + self.options["reuse"])
            else:
                attr.append(
                    '<span class="dox-trace-attribute-empty"> | <strong>Reuse:</strong> -</span>'
                )

            if "usage" in self.options and self.options["usage"] != "":
                attr.append(" | <strong>Usage:</strong> " + self.options["usage"])
            else:
                attr.append(
                    '<span class="dox-trace-attribute-empty"> | <strong>Usage:</strong> -</span>'
                )

        return "".join(attr)

    def calc_sources(self, document, line_number):
        sources = self.options["sources"]

        if self.role in ["unit", "spec", "interface", "srs"]:  # check for existence
            rst_file = document.settings.env.docname
            split = ("/" + rst_file).replace("\\", "/").split("/doc/")
            dir_source = os.path.dirname(document.get("source"))
            for s in sources:
                file = None
                if len(split) > 1:  # source referenced from regular module
                    path2mod = "../" * (split[-1].count("/") + 1)
                    file = os.path.join(dir_source, path2mod + s)
                if not file or not os.path.isfile(file):  # fallback for non-standard modules
                    file = os.path.join(dir_source, s)
                if not os.path.isfile(file):
                    logger.error(
                        f'{document.settings.env.docname}.rst:{line_number}: file "{s}" not found'
                    )

                file_res = Path(file).resolve()
                srcdir_res = Path(self.env.app.srcdir).resolve()
                rel_to_base = str(file_res.relative_to(srcdir_res)).replace("\\", "/")
                if "sources_base" not in self.options:
                    self.options["sources_base"] = {rel_to_base}
                else:
                    self.options["sources_base"].add(rel_to_base)
        else:  # role == "requirement", checked in Dim
            self.options["sources_base"] = sources

        return ", ".join(sources)

    def run(self):
        std = self.env.domaindata["std"]
        spec_id = self.arguments[0]
        ref_id = spec_id.lower()
        document = self.state.document
        docname = document.settings.env.docname
        line_number = self.get_source_info()[1]
        self.iface_back_comp = ref_id.startswith("smd_") and self.role == "interface"

        raw_nodes = []
        self.strike = False

        if "\n" in spec_id:
            spec_id_nl = spec_id.replace("\n", "\\n")
            logger.error(f"{docname}.rst:{line_number}: id {spec_id_nl} must not contain newlines")

        if hasattr(self.env.config, "properties"):
            parts = spec_id.split("_")
            module_name = "_".join(parts[0:2]) if len(parts) > 2 else None
            for attr in list(self.option_spec.keys()) + ["content"]:
                if attr == "content" and len(self.content) > 0:
                    continue
                if attr not in self.options:
                    val = self.get_property(spec_id, attr)  # e.g. SWA_MyModule_Abc
                    if val is None and module_name is not None:
                        val = self.get_property(module_name, attr)  # e.g. SWA_MyModule
                    if val is None:
                        val = self.get_property(parts[0], attr)  # e.g. SWA
                    if val is None:
                        val = self.get_property("_default_", attr)
                    if val:
                        if attr == "content":
                            self.content = val.split("\n")
                        else:
                            if isinstance(val, str) and attr in self.attribute_functions:
                                val = self.attribute_functions[attr](val)
                            self.options[attr] = val

        if self.role in ["requirement", "information"]:
            if "category" in self.options and self.options["category"] in ["software", "system"]:
                category = self.options["category"]
            else:
                category = "input"

            # Use the top level heading as module name, because elements from Dim, especially
            # customer requirements, do not follow a naming convention, which makes it impossible
            # to derive a module name.
            titles = document.traverse(nodes.title)
            if len(titles) > 0:
                self.options["module_name"] = titles[0].astext()
            else:
                self.options["module_name"] = "Unknown"
        else:
            if self.env.config.dox_trace_allow_deprecated:
                prefix = {
                    "srs": "SRS",
                    "spec": "SMD|SWA",
                    "unit": "SMD|SWA",
                    "mod": "SMD|SWA",
                    "interface": "SMD|SWA",
                }
            else:
                prefix = {
                    "srs": "SRS",
                    "spec": "SMD|SWA",
                    "unit": "SMD",
                    "mod": "SWA",
                    "interface": "SWA",
                }

            if self.env.config.dox_trace_tolerant_naming_convention and self.role != "srs":
                postfix = "_[^_]"
                postfix_readable = "_<string>"
            else:
                postfix = "_[^_]+_[^_]+$"
                postfix_readable = "_<string>_<string>"

            if not re.match(rf"^({prefix[self.role]}){postfix}", spec_id):
                logger.error(
                    f"{docname}.rst:{line_number}: id {spec_id} does not follow the form {prefix[self.role]}{postfix_readable}"
                )

            if spec_id.startswith("SRS_"):
                category = "software"
            elif spec_id.startswith("SWA_"):
                category = "architecture"
            else:  # SMD_
                category = "module"

        self.options["category"] = category

        self.isInputReq = self.role == "requirement" and self.options["category"] == "input"
        self.isSRS = self.role == "srs" or (
            self.role == "requirement" and self.options["category"] == "software"
        )

        self.options = {
            k: v for k, v in self.options.items() if v is not None or k == "ignore_in_export"
        }

        status_attr = self.calc_status_attr()
        test_dev_attr = self.calc_test_dev_attr(spec_id)
        # calcAsilSecReviewAttr must be called after calcTestDevAttr
        asil_sec_review_attr = self.calc_asil_sec_review_attr()

        self.options["strike"] = self.strike

        html = []
        if self.strike:
            html.append('<div style="position: relative">\n')
            opa = "; opacity: 0.5"
        else:
            opa = ""
        html.append(
            f'<table class="dox-trace-border dox-trace-initially-hidden docutils align-default" style="width: 100%; position: relative{opa}">\n'
            '    <colgroup><col style="width: 100%" /></colgroup>\n'
            "    <tbody>\n"
            '    <tr class="row-odd"><td><p>\n'
            "        "
        )
        raw_nodes.append(nodes.raw("", "".join(html), format="html"))

        spec_nodes, ign = spec_role(f"{self.role}_generated", "", spec_id, line_number, self.state)
        raw_nodes.extend(spec_nodes)

        html = [
            f'<span class="dox-trace-attribute"> &nbsp; {status_attr}</span>\n'
            "    </p></td></tr>\n"
            '    <tr class="row-even" hidden/>\n'
            f'    <tr class="row-odd dox-trace-attribute"><td><p>\n'
            f"        {asil_sec_review_attr}"
        ]

        if category != "input":
            raw_nodes.append(nodes.raw("", "".join(html), format="html"))

            attr_formatted = " | " + "<strong>Upstream Asil:</strong> "
            n = nodes.comment()
            n.attributes["backward_ref_id"] = ref_id
            n.attributes["backward_attr"] = "parent_asil"
            n.attributes["backward_attr_formatted"] = attr_formatted
            inline_node = nodes.inline()
            inline_node += n
            raw_nodes.append(inline_node)

            cal_str = "Security" if self.env.config.dox_trace_security_backward else "Cal"
            attr_formatted = " | " + f"<strong>Upstream {cal_str}:</strong> "
            n = nodes.comment()
            n.attributes["backward_ref_id"] = ref_id
            n.attributes["backward_attr"] = f"parent_{cal_str.lower()}"
            n.attributes["backward_attr_formatted"] = attr_formatted
            inline_node = nodes.inline()
            inline_node += n
            raw_nodes.append(inline_node)

            html = ["<br>\n"]
        else:
            html.append("<br>\n")

        if test_dev_attr != "":
            html.append(f"        {test_dev_attr}\n")

        if "tags" not in self.options:
            self.options["tags"] = []
        tags = self.options["tags"]
        if self.role != "mod":
            value = ", ".join(tags) if len(tags) > 0 else "-"
            html.append(f'        {self.attr_name("Tags", value, True)}')

            if category != "input":
                if len(tags) == 0:
                    html.append('<span class="dox-trace-grey dox-trace-attribute-empty"> | </span>')
                    bar = ""
                else:
                    bar = " | "
                attr_formatted = bar + "<strong>Upstream Tags:</strong> "

                raw_nodes.append(nodes.raw("", "".join(html), format="html"))
                n = nodes.comment()
                n.attributes["backward_ref_id"] = ref_id
                n.attributes["backward_attr"] = "parent_tags"
                n.attributes["backward_attr_formatted"] = attr_formatted
                inline_node = nodes.inline()
                inline_node += n
                raw_nodes.append(inline_node)
                html = ["\n"]
            else:
                html.append("\n")

        # the content
        html.append('    </p></td></tr>\n     <tr class="row-even"><td><p>\n')
        if len(self.content) == 0:
            html.append("        [missing]\n")
            self.options["text"] = ""
        else:
            if (
                self.role in ["requirement", "information"]
                and len(self.content) == 1
                and len(self.content[0]) > 12
                and self.content[0].startswith(":raw-html:")
            ):
                html.append(f"        {self.content[0][11:-1]}")
            else:
                html.append("        ")
                raw_nodes.append(nodes.raw("", "".join(html), format="html"))
                html = []
                text_nodes = DimViewList.string_to_nodes(self.content, self.content_offset, self)
                raw_nodes.extend(text_nodes)
            self.options["text"] = "See Sphinx documentation."
        html.append("    </p></td></tr>\n")

        additional_attributes = []
        if not ((self.role == "information" and category != "input") or (self.role == "mod")):
            additional_attributes.append({"name": "verification_criteria", "mode": "vc"})
            if self.options["category"] == "input":
                additional_attributes.append({"name": "comment", "mode": "comment"})
                additional_attributes.append({"name": "feature", "mode": "feature"})
                additional_attributes.append({"name": "change_request", "mode": "cr"})
                additional_attributes.append({"name": "miscellaneous", "mode": "misc"})
            else:
                additional_attributes.append({"name": "derived", "mode": "feature"})
                additional_attributes.append({"name": "derived", "mode": "change_request"})

        for name, ca in DoxTraceDirective.custom_attributes.items():
            if name in self.option_spec:
                if self.role in ["requirement", "information"]:
                    if self.options["category"] not in ca["categories"]:
                        continue
                if name not in self.options and ca["default"]:
                    self.options[name] = ca["default"]
                additional_attributes.append({"name": name, "mode": ca["type"]})

        if len(additional_attributes) > 0:
            html.append(
                '    <tr class="row-odd dox-trace-attribute dox-trace-hide-if-empty"><td><p>\n'
            )

            for attr in additional_attributes:
                name = attr["name"]
                mode = attr["mode"]
                if name in self.option_spec and not self.iface_back_comp:
                    pretty_name = name.replace("_", " ").title()
                    if (
                        name in self.options
                        and self.options[name]
                        and self.options[name] == ":raw-html:``"
                    ):
                        self.options[name] = ""

                    if name in self.options and self.options[name]:
                        val = self.options[name]
                        html.append(f"        <strong>{pretty_name}:</strong> ")
                        if mode == "enum":
                            html.append(", ".join(val))
                            html.append("<br>\n")
                        elif mode == "refs":
                            for r in val:
                                raw_nodes.append(nodes.raw("", "".join(html), format="html"))
                                explicit = bool(re.match(r"^(SMD|SWA)_[^_\n<> ]+_([^\n<> ]+)", r))
                                ref_node = addnodes.pending_xref(
                                    "",
                                    refdomain="std",
                                    refexplicit=explicit,
                                    reftarget=r.lower(),
                                    reftype="ref",
                                    refwarn=True,
                                )
                                ref_node += nodes.Text(r)
                                inline_node = nodes.inline()
                                inline_node += ref_node
                                raw_nodes.append(inline_node)
                                html = [", "]
                            html = ["<br>\n"]
                        else:  # text
                            if (
                                self.role in ["requirement", "information"]
                                and len(val) > 11
                                and val.startswith(":raw-html:`")
                                and val.endswith("`")
                            ):
                                html.append(val[11:-1])
                                html.append("<br>\n")
                            else:
                                raw_nodes.append(nodes.raw("", "".join(html), format="html"))
                                # in options of directives no empty lines are allowed, therefore
                                # preserve line breaks expect if line ends with backlash
                                val = re.sub(r"( )*\\( )*(\n|$)", " ", val, re.M).strip()
                                self.options[name] = val
                                val = val.replace("\n", "\n\n").split("\n")

                                if len(val) > 1:
                                    # Sphinx does not render paragraphs like bullet points correctly
                                    # here if not prepended by whitespaces
                                    val = [" " + v for v in val]
                                    html = []
                                else:
                                    html = ["<br>\n"]
                                text_nodes = DimViewList.string_to_nodes(
                                    val, self.content_offset, self
                                )
                                # The ViewList from docutils always generates a paragraph wrapper
                                # node, here text_nodes[0]. This will be replaced by an inline node
                                # to avoid newlines in the HTML output.
                                additional_attributes_node = nodes.inline()
                                additional_attributes_node += text_nodes[0].children
                                raw_nodes.append(additional_attributes_node)
                                self.options[name + "_nodes"] = text_nodes[0].children
                    elif name == "verification_criteria":
                        if self.isSRS and "tool" not in tags and not self.strike:
                            html.append(
                                '        <span class="dox-trace-attribute-missing"><strong>Verification Criteria:</strong> [missing]<br></span>\n'
                            )
                        else:
                            html.append(
                                '        <span class="dox-trace-attribute-empty"><strong>Verification Criteria:</strong> -<br></span>\n'
                            )
                        self.options[name] = ""
                    else:
                        html.append(
                            f'        <span class="dox-trace-attribute-empty"><strong>{pretty_name}:</strong> -<br></span>\n'
                        )
                        self.options[name] = ""
                elif name == "derived":
                    name = mode
                    pretty_name = name.replace("_", " ").title()
                    attr_formatted = f"<strong>Derived {pretty_name}:</strong> "
                    html.append("        ")
                    raw_nodes.append(nodes.raw("", "".join(html), format="html"))
                    n = nodes.comment()
                    n.attributes["backward_ref_id"] = ref_id
                    n.attributes["backward_attr"] = f"parent_{name}"
                    n.attributes["backward_attr_formatted"] = attr_formatted
                    inline_node = nodes.inline()
                    inline_node += n
                    raw_nodes.append(inline_node)
                    html = ["\n"]

            html.append('    </p></td></tr>\n    <tr class="row-even" hidden/>\n')

            if self.iface_back_comp:
                self.options.pop("verification_criteria", None)
            elif (
                "verification_criteria" in self.options
                and self.options["verification_criteria"] != ""
            ):
                self.options["verification_criteria"] = "See Sphinx documentation."

        html.append('    <tr class="row-odd dox-trace-attribute dox-trace-hide-if-empty"><td><p>\n')
        html.append("        ")
        attr_formatted = "<strong>Upstream References:</strong> "
        raw_nodes.append(nodes.raw("", "".join(html), format="html"))
        n = nodes.comment()
        n.attributes["backward_ref_id"] = ref_id
        n.attributes["backward_attr"] = "upstream"
        n.attributes["backward_attr_formatted"] = attr_formatted
        inline_node = nodes.inline()
        inline_node += n
        raw_nodes.append(inline_node)
        html = ["\n"]
        if self.role != "mod":
            html.append("        ")
            attr_formatted = "<strong>Downstream References:</strong> "
            raw_nodes.append(nodes.raw("", "".join(html), format="html"))
            n = nodes.comment()
            n.attributes["backward_ref_id"] = ref_id
            n.attributes["backward_attr"] = "downstream"
            n.attributes["backward_attr_formatted"] = attr_formatted
            inline_node = nodes.inline()
            inline_node += n
            raw_nodes.append(inline_node)
            html = []
            if "sources" in self.option_spec:
                if self.role == "unit" or self.iface_back_comp or "sources" in self.options:
                    html = ["\n"]
                    if "sources" not in self.options:
                        if self.strike or "covered" in tags:
                            html.append(
                                '        <span class="dox-trace-attribute-empty"><strong>Sources:</strong> -</span>\n'
                            )
                        else:
                            html.append(
                                '        <span class="dox-trace-attribute-missing"><strong>Sources:</strong> [missing]</span>\n'
                            )
                        self.options["sources"] = []
                    else:
                        sources = self.calc_sources(document, line_number)
                        html.append(f"        <strong>Sources:</strong> {sources}\n")
                else:
                    self.options["sources"] = []

        else:  # a mod specification
            if "location" in self.options:
                html.append("        <strong>Location:</strong> ")
                file = os.path.join(
                    self.env.app.srcdir, self.options["location"], "doc/index"
                ).replace("\\", "/")
                file_with_ending = file + ".rst"
                if not os.path.isfile(file_with_ending):
                    if self.strike:
                        html.append(self.options["location"])
                    else:
                        html.append(self.red + self.options["location"] + self.colEnd)
                else:
                    rst_file = os.path.join(self.env.app.srcdir, docname).replace("\\", "/")
                    rst_dir = os.path.dirname(rst_file)
                    doc_link = os.path.relpath(file, rst_dir).replace("\\", "/")

                    raw_nodes.append(nodes.raw("", "".join(html), format="html"))
                    ref_node = addnodes.pending_xref(
                        "",
                        refdomain="std",
                        refexplicit=True,
                        reftarget=doc_link,
                        reftype="doc",
                        refwarn=True,
                    )
                    ref_node += nodes.Text(self.options["location"])
                    inline_node = nodes.inline()
                    inline_node += ref_node
                    raw_nodes.append(inline_node)
                    html = []
                    self.options["tags"] = ["covered"]
                html.append("\n")
            else:
                if self.strike:
                    html.append(
                        '        <span class="dox-trace-attribute-empty"><strong>Location:</strong> -</span>\n'
                    )
                else:
                    html.append(
                        '        <span class="dox-trace-attribute-missing"><strong>Location:</strong> [missing]</span>\n'
                    )

        html.append("    </p></td></tr>\n    </tbody>\n</table>\n")
        if self.strike:
            html.append(
                '<div class="dox-trace-initially-hidden dox-trace-strikethrough-table"></div>\n</div>\n'
            )

        raw_nodes.append(nodes.raw("", "".join(html), format="html"))

        std["spec_options"][ref_id] = self.options
        std["spec_options"][ref_id]["role"] = self.role

        return raw_nodes


class UnitDirective(DoxTraceDirective):
    role = "unit"
    option_spec = DoxTraceDirective.create_option_spec(role)


class SpecDirective(DoxTraceDirective):
    role = "spec"
    option_spec = DoxTraceDirective.create_option_spec(role)


class InterfaceDirective(DoxTraceDirective):
    role = "interface"
    option_spec = DoxTraceDirective.create_option_spec(role)


class RequirementDirective(DoxTraceDirective):
    role = "requirement"
    option_spec = DoxTraceDirective.create_option_spec(role)


class InformationDirective(DoxTraceDirective):
    role = "information"
    option_spec = DoxTraceDirective.create_option_spec(role)


class ModDirective(DoxTraceDirective):
    role = "mod"
    option_spec = DoxTraceDirective.create_option_spec(role)


class SrsDirective(DoxTraceDirective):
    role = "srs"
    option_spec = DoxTraceDirective.create_option_spec(role)
