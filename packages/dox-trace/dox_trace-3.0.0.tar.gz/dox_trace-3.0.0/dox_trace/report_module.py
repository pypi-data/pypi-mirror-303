from .report_generic import calc_table_type


def calc_table_module_type(app, category, fromdocname, modules, developer):
    if app.env.config.dox_trace_allow_deprecated:
        types = ["spec", "interface", "unit"]
    else:
        types = ["spec", "unit"]
    return calc_table_type(app, category, fromdocname, modules, developer, types)
