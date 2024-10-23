import re
import copy

from sphinx.util import logging

logger = logging.getLogger(__name__)


def prepare_env(app, _env, _docnames):
    std = app.env.domaindata["std"]

    # docname => ref_ids
    if "local" not in std:
        std["local"] = {}
    if "local_ordered" not in std:
        std["local_ordered"] = {}

    # ref_id => node
    if "spec_node" not in std:
        std["spec_node"] = {}

    # ref_id => spec_id
    if "spec_id" not in std:
        std["spec_id"] = {}

    # ref_id => spec_id
    if "spec_options" not in std:
        std["spec_options"] = {}

    std["last_dox_trace_version"] = app.extensions["dox_trace"].version


def add_node_to_env(document, spec_id, node):
    ref_id = spec_id.lower()
    env = document.settings.env
    std = env.domaindata["std"]

    if ref_id in std["spec_id"]:
        logger.error(f"specification {spec_id} found twice")

    docname = env.docname
    if docname not in env.domaindata["std"]["local"]:
        std["local"][docname] = {ref_id}
        std["local_ordered"][docname] = [ref_id]
    else:
        std["local"][docname].add(ref_id)
        std["local_ordered"][docname].append(ref_id)

    text = spec_id
    m = re.match(r"^(SMD|SWA)_[^_\n<> ]+_([^\n<> ]+)", spec_id)
    if m:
        text = m.group(2).strip()

    std["anonlabels"][ref_id] = env.docname, ref_id
    std["labels"][ref_id] = env.docname, ref_id, text
    std["spec_node"][ref_id] = node
    std["spec_id"][ref_id] = spec_id


def purge_doc_from_env(_app, env, docname):
    std = env.domaindata["std"]
    doc_attr = ["spec_options", "anonlabels", "labels", "spec_node", "spec_id"]
    if docname in env.domaindata["std"]["local"]:
        for ref_id in std["local"][docname]:
            for attr in doc_attr:
                assert attr in std
                std[attr].pop(ref_id, None)
    std["local"].pop(docname, None)
    std["local_ordered"].pop(docname, None)


def merge_env_parallel_build(_app, env, _docnames, other):
    std = env.domaindata["std"]
    std_other = other.domaindata["std"]

    doc_attr = [
        "local",
        "local_ordered",
        "spec_node",
        "spec_id",
        "spec_options",
        "anonlabels",
        "labels",
    ]
    for attr in doc_attr:
        std[attr].update(std_other[attr])


# for unit testing only
def merge_env_parallel_build_non_posix(app, _doctree, _docname):
    other = copy.deepcopy(app.env)
    std = app.env.domaindata["std"]
    doc_attr = [
        "local",
        "local_ordered",
        "spec_node",
        "spec_id",
        "spec_options",
        "anonlabels",
        "labels",
    ]
    for attr in doc_attr:
        std[attr].clear()
    merge_env_parallel_build(app, app.env, None, other)

    ext = app.extensions["dox_trace"]
    read_allowed = getattr(ext, "parallel_read_safe", None)
    write_allowed = getattr(ext, "parallel_write_safe", None)
    tester_dummy = "Parallel = " + str(read_allowed and write_allowed)
    std["spec_options"]["swa_spec_main"]["tester"] = tester_dummy
