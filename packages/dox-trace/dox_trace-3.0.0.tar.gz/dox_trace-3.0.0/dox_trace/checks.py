import re

from sphinx.util import logging
from docutils import nodes

logger = logging.getLogger(__name__)


def check_invalid_refs(app):
    std = app.env.domaindata["std"]
    spec_options = app.env.domaindata["std"]["spec_options"]
    for ref_id, options in spec_options.items():
        for target_spec_id in spec_options[ref_id]["refs"]:
            target_spec_id_lower = target_spec_id.lower()
            if target_spec_id_lower not in spec_options and target_spec_id_lower in std["labels"]:
                logger.warning(
                    f"Found invalid reference from {std['spec_id'][ref_id]} to {target_spec_id}"
                )


def check_cyclic_recursive(app, spec_options, ref_id, cyclic_stack, already_checked):
    if ref_id in cyclic_stack:
        current_stack = [app.env.domaindata["std"]["spec_id"][c] for c in cyclic_stack + [ref_id]]
        ref_stack = " -> ".join(current_stack)
        logger.error(f"Found cyclic reference: {ref_stack}")
    else:
        cyclic_stack.append(ref_id)
        ref_opt = spec_options[ref_id]
        for target_spec_id in ref_opt["downstream_refs"]:
            target_ref_id = target_spec_id.lower()
            if (
                target_ref_id not in already_checked
                and target_ref_id in spec_options
                and ref_opt["category"] == spec_options[target_ref_id]["category"]
            ):
                check_cyclic_recursive(
                    app, spec_options, target_ref_id, cyclic_stack, already_checked
                )
        cyclic_stack.pop()
        already_checked.add(ref_id)


def check_cyclic(app):
    spec_options = app.env.domaindata["std"]["spec_options"]
    cyclic_stack = []
    already_checked = set()
    for ref_id, options in spec_options.items():
        if ref_id not in already_checked:
            check_cyclic_recursive(app, spec_options, ref_id, cyclic_stack, already_checked)


def check_case(app):
    std = app.env.domaindata["std"]
    spec_options = std["spec_options"]
    for ref_id, options in spec_options.items():
        for target_spec_id in spec_options[ref_id]["refs"]:
            target_spec_id_real = std["spec_id"][target_spec_id.lower()]
            if target_spec_id != target_spec_id_real:
                logger.error(
                    f"Incorrect case in refs of {std['spec_id'][ref_id]}: {target_spec_id} instead of {target_spec_id_real}"
                )


def check_unintended_comments(_app, doctree):
    for node in doctree.traverse(nodes.comment):
        if len(node.rawsource) > 0:
            first_line = node.rawsource.partition("\n")[0]
            for name in ["spec", "mod", "interface", "unit", "srs"]:
                if re.match(rf"^\W*{name}\W*$", first_line) is not None:
                    logger.error(
                        f'{node.source}:{node.line}: first line of comment looks like a typo: "{first_line}"'
                    )


def check_consistency(app, _env):
    check_invalid_refs(app)
    check_cyclic(app)
    check_case(app)
