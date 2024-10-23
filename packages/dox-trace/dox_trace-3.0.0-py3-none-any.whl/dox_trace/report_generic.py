import re
from .report_table import create_table, create_row_heading, create_row_values, create_row_refs
from .backward_refs import downstream_missing_trace, upstream_missing_trace
from .helper import cat_name2level


def create_developer_regex(developer):
    return re.compile("\\A" + developer.replace(" ", "[ _]*") + "\\Z", re.IGNORECASE)


def init_row_values(value_names):
    values = {}
    for value_name in value_names:
        values[value_name] = []
    return values


def sum_up_row_values(value_names, values_module, values_total):
    for value_name in value_names:
        values_total[value_name] += values_module[value_name]


def calc_table_status(app, category, fromdocname, modules, developer):
    std = app.env.domaindata["std"]
    dev_regex = create_developer_regex(developer)

    table, thead, tbody = create_table(5)
    value_names = ["all", "valid", "draft", "invalid"]
    thead += create_row_heading(value_names)

    values_total = init_row_values(value_names)
    rows = []
    for modules_name, ref_ids in modules.items():
        values_module = init_row_values(value_names)
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            dev_split = options["developer_split"]
            if not any(re.match(dev_regex, dev) for dev in dev_split):
                continue
            if options["status"] in value_names:
                spec_id = std["spec_id"][ref_id]
                values_module[options["status"]].append(spec_id)
        if not all(len(value) == 0 for value in values_module.values()):
            rows.append(
                create_row_values(
                    app,
                    fromdocname,
                    category,
                    value_names,
                    modules_name,
                    values_module.values(),
                    calc_sum=True,
                )
            )
            sum_up_row_values(value_names, values_module, values_total)

    if len(rows) > 0:
        tbody += create_row_values(
            app, fromdocname, category, value_names, "TOTAL", values_total.values(), calc_sum=True
        )
        tbody += rows
        return table

    return None


def get_dev_spec_id(std, options, dev_regex, ref_id):
    dev_split = options["developer_split"]
    if not any(re.match(dev_regex, dev) for dev in dev_split):
        return None
    if options["status"] != "valid":
        return None
    if options["review_status"] not in ["accepted"]:
        return None
    return std["spec_id"][ref_id]


def calc_table_type(app, category, fromdocname, modules, developer, types):
    std = app.env.domaindata["std"]
    dev_regex = create_developer_regex(developer)

    table, thead, tbody = create_table(2 + len(types))
    value_names = ["all"] + types
    thead += create_row_heading(value_names)

    values_total = init_row_values(value_names)
    rows = []
    for modules_name, ref_ids in modules.items():
        values_module = init_row_values(value_names)
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            spec_id = get_dev_spec_id(std, options, dev_regex, ref_id)
            if not spec_id:
                continue
            values_module[options["role"]].append(spec_id)
        if not all(len(value) == 0 for value in values_module.values()):
            rows.append(
                create_row_values(
                    app,
                    fromdocname,
                    category,
                    value_names,
                    modules_name,
                    values_module.values(),
                    calc_sum=True,
                )
            )
            sum_up_row_values(value_names, values_module, values_total)

    if len(rows) > 0:
        tbody += create_row_values(
            app, fromdocname, category, value_names, "TOTAL", values_total.values(), calc_sum=True
        )
        tbody += rows
        return table

    return None


def calc_table_safety_cal(app, category, fromdocname, modules, developer, attr_name):
    std = app.env.domaindata["std"]
    dev_regex = create_developer_regex(developer)

    data = {}
    value_names = []

    for modules_name, ref_ids in modules.items():
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            spec_id = get_dev_spec_id(std, options, dev_regex, ref_id)
            if not spec_id:
                continue

            if modules_name not in data:
                data[modules_name] = {}
            if options[attr_name] not in data[modules_name]:
                data[modules_name][options[attr_name]] = []
                if options[attr_name] not in value_names:
                    value_names.append(options[attr_name])
            data[modules_name][options[attr_name]].append(spec_id)

    if len(data) > 0:
        if "not_set" in value_names:
            value_names.remove("not_set")
        value_names.sort()
        value_names.append("not_set")
        value_names.insert(0, "all")

        values_total = init_row_values(value_names)
        rows = []
        for modules_name, values_module_short in data.items():
            values_module = init_row_values(value_names)
            for value in values_module_short:
                values_module[value] = values_module_short[value]
            sum_up_row_values(value_names, values_module, values_total)
            rows.append(
                create_row_values(
                    app,
                    fromdocname,
                    category,
                    value_names,
                    modules_name,
                    values_module.values(),
                    calc_sum=True,
                )
            )

        table, thead, tbody = create_table(1 + len(value_names))
        thead += create_row_heading(value_names)
        tbody += create_row_values(
            app, fromdocname, category, value_names, "TOTAL", values_total.values(), calc_sum=True
        )
        tbody += rows
        return table

    return None


def calc_table_safety(app, category, fromdocname, modules, developer):
    return calc_table_safety_cal(app, category, fromdocname, modules, developer, "asil")


def calc_table_cal(app, category, fromdocname, modules, developer):
    return calc_table_safety_cal(app, category, fromdocname, modules, developer, "cal")


def calc_table_security(app, category, fromdocname, modules, developer):
    std = app.env.domaindata["std"]
    dev_regex = create_developer_regex(developer)

    table, thead, tbody = create_table(5)
    value_names = ["all", "yes", "no", "not_set"]
    thead += create_row_heading(value_names)

    values_total = init_row_values(value_names)
    rows = []
    for modules_name, ref_ids in modules.items():
        values_module = init_row_values(value_names)
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            spec_id = get_dev_spec_id(std, options, dev_regex, ref_id)
            if not spec_id:
                continue

            if options["security"] in ["yes", "no", "not_set"]:
                values_module[options["security"]].append(spec_id)
            else:  # pragma: no cover (robustness)
                pass
        if not all(len(value) == 0 for value in values_module.values()):
            rows.append(
                create_row_values(
                    app,
                    fromdocname,
                    category,
                    value_names,
                    modules_name,
                    values_module.values(),
                    calc_sum=True,
                )
            )
            sum_up_row_values(value_names, values_module, values_total)

    if len(rows) > 0:
        tbody += create_row_values(
            app, fromdocname, category, value_names, "TOTAL", values_total.values(), calc_sum=True
        )
        tbody += rows
        return table

    return None


def calc_table_stream(app, category, fromdocname, modules, developer):
    std = app.env.domaindata["std"]
    dev_regex = create_developer_regex(developer)

    if category == "input":
        value_names = ["all", "Downstream Sufficient", "Downstream Missing"]
    else:
        value_names = [
            "all",
            "Upstream Sufficient",
            "Upstream Missing",
            "Downstream Sufficient",
            "Downstream Missing",
        ]

    table, thead, tbody = create_table(len(value_names) + 1)
    thead += create_row_heading(value_names)

    values_total = init_row_values(value_names)
    rows = []
    for modules_name, ref_ids in modules.items():
        values_module = init_row_values(value_names)
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            spec_id = get_dev_spec_id(std, options, dev_regex, ref_id)
            if not spec_id:
                continue
            values_module["all"].append(spec_id)

            if (
                ("downstream_refs" in options and options["downstream_refs"])
                or ("location" in options and options["location"] != "")
                or ("sources" in options and options["sources"] != [])
                or (not downstream_missing_trace(options))
            ):
                values_module["Downstream Sufficient"].append(spec_id)
            else:
                values_module["Downstream Missing"].append(spec_id)

            if category != "input":
                sufficient = not upstream_missing_trace(options)
                if not sufficient and "upstream_refs" in options and options["upstream_refs"]:
                    above = 2 if category == "software" else 1
                    current_level = cat_name2level[category]
                    sufficient = any(
                        cat_name2level[std["spec_options"][r]["category"]] <= current_level + above
                        for r in options["upstream_refs"]
                    )
                if sufficient:
                    values_module["Upstream Sufficient"].append(spec_id)
                else:
                    values_module["Upstream Missing"].append(spec_id)

        if not all(len(value) == 0 for value in values_module.values()):
            rows.append(
                create_row_values(
                    app,
                    fromdocname,
                    category,
                    value_names,
                    modules_name,
                    values_module.values(),
                    calc_sum=False,
                )
            )
            sum_up_row_values(value_names, values_module, values_total)

    if len(rows) > 0:
        tbody += create_row_values(
            app, fromdocname, category, value_names, "TOTAL", values_total.values(), calc_sum=False
        )
        tbody += rows
        return table

    return None


def calc_table_list(app, category, fromdocname, modules, developer):
    std = app.env.domaindata["std"]
    dev_regex = create_developer_regex(developer)

    if category == "input":
        value_names = ["ID", "Downstream"]
    else:
        value_names = ["ID", "Upstream", "Downstream"]

    table, thead, tbody = create_table(len(value_names) + 1, small=True)
    thead += create_row_heading(value_names)

    rows = []
    for modules_name, ref_ids in modules.items():
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            if not get_dev_spec_id(std, options, dev_regex, ref_id):
                continue

            location = sources = None
            downstream_refs = sorted(options["downstream_refs"])
            if "location" in options:
                location = options["location"]
            elif "sources" in options:
                sources = sorted(options["sources"])
            if not downstream_refs and not location and not sources:
                downstream_refs = "[missing]" if downstream_missing_trace(options) else "-"

            if category != "input":
                upstream_refs = sorted(options["upstream_refs"])
                if len(upstream_refs) == 0:
                    upstream_refs = "[missing]" if upstream_missing_trace(options) else "-"
            else:
                upstream_refs = None

            rows.append(
                create_row_refs(
                    app,
                    fromdocname,
                    modules_name,
                    ref_id,
                    downstream_refs,
                    location,
                    sources,
                    upstream_refs,
                )
            )

    if len(rows) > 0:
        tbody += rows
        return table

    return None
