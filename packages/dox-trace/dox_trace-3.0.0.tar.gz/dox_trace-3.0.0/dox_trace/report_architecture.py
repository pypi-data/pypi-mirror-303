from .report_generic import calc_table_type


def calc_table_architecture_type(app, category, fromdocname, modules, developer):
    types = ["spec", "interface", "mod"]
    return calc_table_type(app, category, fromdocname, modules, developer, types)
