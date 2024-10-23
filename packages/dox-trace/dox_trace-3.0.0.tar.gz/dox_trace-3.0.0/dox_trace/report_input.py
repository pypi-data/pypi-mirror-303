import re
from .report_generic import (
    create_table,
    create_row_heading,
    create_row_values,
    init_row_values,
    sum_up_row_values,
)


def calc_table_input_developer(app, category, fromdocname, modules, developer):
    std = app.env.domaindata["std"]
    dev_regex = re.compile("\\A" + developer.replace(" ", "[ _]*") + "\\Z", re.IGNORECASE)

    table, thead, tbody = create_table(5)
    value_names = ["all", developer, "other", "not set"]
    thead += create_row_heading(value_names)

    values_total = init_row_values(value_names)
    rows = []
    for modules_name, ref_ids in modules.items():
        values_module = init_row_values(value_names)
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            spec_id = std["spec_id"][ref_id]
            if "developer" not in options or options["developer"] in ["", "[missing]"]:
                values_module["not set"].append(spec_id)
            else:
                dev_split = options["developer_split"]
                if any(re.match(dev_regex, dev) for dev in dev_split):
                    values_module[developer].append(spec_id)
                    if len(dev_split) > 1:
                        # more than just one developer
                        values_module["other"].append(spec_id)
                else:
                    values_module["other"].append(spec_id)
            values_module["all"].append(spec_id)

        # no "continue" above, at least one value is > 0
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

    # no "continue" above, at least one row exists
    tbody += create_row_values(
        app, fromdocname, category, value_names, "TOTAL", values_total.values(), calc_sum=False
    )
    tbody += rows
    return table


def calc_table_input_review_status(app, category, fromdocname, modules, developer):
    std = app.env.domaindata["std"]
    dev_regex = re.compile("\\A" + developer.replace(" ", "[ _]*") + "\\Z", re.IGNORECASE)

    table, thead, tbody = create_table(7)
    value_names = ["all", "accepted", "unclear", "rejected", "not_relevant", "not_reviewed"]
    thead += create_row_heading(value_names)

    values_total = init_row_values(value_names)
    rows = []
    for modules_name, ref_ids in modules.items():
        values_module = init_row_values(value_names)
        for ref_id in ref_ids:
            options = std["spec_options"][ref_id]
            if options["status"] != "valid":
                continue
            dev_split = options["developer_split"]
            if not any(re.match(dev_regex, dev) for dev in dev_split):
                continue
            if options["review_status"] in value_names:
                spec_id = std["spec_id"][ref_id]
                values_module[options["review_status"]].append(spec_id)

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
