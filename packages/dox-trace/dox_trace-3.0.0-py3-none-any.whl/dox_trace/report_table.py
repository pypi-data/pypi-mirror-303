from docutils import nodes
import itertools
import os
import re

dox_trace_row_counter = 0


def create_table(num_rows, small=False):
    table = nodes.table()
    if small:
        table["classes"] += ["dox-trace-small-font-table"]
    tg = nodes.tgroup(cols=num_rows)
    for _ in range(num_rows):
        tg += nodes.colspec()
    table += tg
    thead = nodes.thead()
    tg += thead
    tbody = nodes.tbody()
    tg += tbody
    return table, thead, tbody


def word_break(word):
    if len(word) <= 30:
        return word
    word = word.replace("_", "_<wbr>").replace("/", "/<wbr>")
    str_split = word.split("<wbr>")
    if any(len(s) > 30 for s in str_split):
        long_str = []
        for s in str_split:
            if len(s) > 30:
                long_str.append(re.sub(r"(.)([A-Z])", r"\1<wbr>\2", s))
            else:
                long_str.append(s)
        return "<wbr>".join(long_str)
    return word


def create_row_values(app, fromdocname, category, headings, module_name, values, calc_sum):
    std = app.env.domaindata["std"]
    if module_name == "TOTAL":
        for v in values:
            v.sort()
    global dox_trace_row_counter
    dox_trace_row_counter += 1
    row_id = str(dox_trace_row_counter)
    row = nodes.row()

    mod_node = nodes.raw("", word_break(module_name), format="html")
    row += nodes.entry("", mod_node)
    for i, (h, v) in enumerate(zip(headings, values)):
        if calc_sum and i == 0:
            v = sorted(list(itertools.chain.from_iterable(values)))
        if len(v) > 0:
            html = []
            postfix = category + "_" + row_id + "_" + h + "_" + module_name
            html.append(f'<a id="traceabilityReportButton_{postfix}">{len(v)}</a>\n')
            html.append(f'<div id="traceabilityReportModal_{postfix}" class="dox-trace-modal">\n')
            html.append(f'<div class="dox-trace-modal-content">\n')
            html.append(
                f'<span id="traceabilityReportClose_{postfix}" class="dox-trace-close">&times;</span>\n'
            )
            refs = []
            for spec_id in v:
                ref_id = spec_id.lower()
                if ref_id in std["anonlabels"]:
                    source_docname, r = std["anonlabels"][ref_id]
                    refuri = app.builder.get_relative_uri(fromdocname, source_docname) + "#" + r
                    refs.append(f'<a href="{refuri}">{spec_id}</a>')
                else:  # pragma: no cover (robustness)
                    pass
            joined_refs = "<br>\n".join(refs)
            html.append(f"<br><br><p>\n{joined_refs}</p>\n")
            html.append(f"</div></div>\n")
            row += nodes.entry("", nodes.raw("", "".join(html), format="html"))
        else:
            row += nodes.entry("", nodes.raw("", "0", format="html"))
    return row


def create_row_heading(entries):
    row = nodes.row()
    cell = nodes.entry()
    cell.set_class("dox-trace-strikethrough-cell")
    row += cell
    for e in entries:
        row += nodes.entry("", nodes.paragraph(text=e))
    return row


def create_ref_node(app, fromdocname, ref_id):
    std = app.env.domaindata["std"]

    inline = nodes.inline()
    if ref_id in std["spec_id"] and ref_id in std["anonlabels"]:
        source_docname, r = std["anonlabels"][ref_id]
        refuri = app.builder.get_relative_uri(fromdocname, source_docname) + "#" + r
        ref_node = nodes.reference(
            "",
            "",
            internal=True,
            refdocname=source_docname,
            refuri=refuri,
            refid=r,
        )
        spec_id = std["spec_id"][ref_id]
        spec_node = nodes.raw("", word_break(spec_id), format="html")
        ref_node += spec_node
        inline += ref_node
    else:
        spec_node = nodes.raw("", word_break(ref_id), format="html")
        inline.set_class("dox-trace-red")
        inline += spec_node
    return inline


def create_location_node(app, fromdocname, location):
    inline = nodes.inline()
    file = os.path.join(location, "doc/index").replace("\\", "/")
    loc_node = nodes.raw("", word_break(location), format="html")
    if os.path.isfile(os.path.join(app.srcdir, file + ".rst")):
        refuri = app.builder.get_relative_uri(fromdocname, file)
        ref_node = nodes.reference(
            "",
            "",
            internal=True,
            refdocname=file,
            refuri=refuri,
            refid=None,
        )
        ref_node += loc_node
        inline += ref_node
    else:
        inline.set_class("dox-trace-red")
        inline += loc_node
    return inline


def create_refs_entry(app, fromdocname, refs, location=None, sources=None):
    entry = nodes.entry("")
    if refs:
        for idx, ref_id in enumerate(refs):
            ref_node = create_ref_node(app, fromdocname, ref_id)
            if idx > 0:
                entry += nodes.raw("", ",<br>", format="html")
            entry += ref_node
    if location:
        entry += create_location_node(app, fromdocname, location)
    if sources:
        if refs and len(refs) > 0:
            entry += nodes.raw("", ",<br>", format="html")
        sources_with_word_break = [word_break(s) for s in sources]
        entry += nodes.raw("", ",<br>".join(sources_with_word_break), format="html")
    return entry


def create_row_refs(app, fromdocname, module_name, ref_id, downstream, location, sources, upstream):
    row = nodes.row()
    row += nodes.entry("", nodes.raw("", word_break(module_name), format="html"))
    row += nodes.entry("", create_ref_node(app, fromdocname, ref_id))

    if not upstream is None:
        if isinstance(upstream, str):
            row += nodes.entry("", nodes.raw("", word_break(upstream), format="html"))
        else:
            row += create_refs_entry(app, fromdocname, upstream)

    if isinstance(downstream, str) and not location and not sources:
        row += nodes.entry("", nodes.raw("", word_break(downstream), format="html"))
    else:
        row += create_refs_entry(app, fromdocname, downstream, location, sources)

    return row
