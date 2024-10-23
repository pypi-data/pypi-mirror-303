import sys
import yaml
import os

from .dim_write import dim_write
from .backward_refs import calc_backward, inject_backward_references
from .env import (
    prepare_env,
    purge_doc_from_env,
    merge_env_parallel_build,
    merge_env_parallel_build_non_posix,
)
from .report import DoxTraceTraceabilityDirective, inject_report
from .undefined_refs import (
    UndefinedRefsDirective,
    calc_unresolved_references,
    inject_undefined_references,
)
from .checks import check_unintended_comments, check_consistency
from .properties import prop_role, PropDirective
from .enclosed import EnclosedDirective
from .config import config_inited, DoxTraceConfigDirective
from .coverage import coverage_end
from .roles import spec_role
from .directives import (
    ModDirective,
    UnitDirective,
    SpecDirective,
    InterfaceDirective,
    SrsDirective,
    RequirementDirective,
    InformationDirective,
    DoxTraceDirective,
)
from sphinx import version_info as sphinx_version
from sphinx.util import logging
from .yaml import SafeLoaderWithoutBoolean
from .version import __version__

if sys.version_info < (3, 8):
    try:
        raise RuntimeError("The dox_trace extension requires Python 3.8+")
    finally:
        coverage_end()

if sphinx_version < (6, 2, 0):
    try:
        raise RuntimeError("The dox_trace extension requires Sphinx 6.2+")
    finally:
        coverage_end()

logger = logging.getLogger(__name__)


# needed to collect coverage correctly in unit test
def config_inited_wrapper(app, config):
    exception_raised = False
    try:
        if config.dox_trace_properties_file:
            if not os.path.isfile(config.dox_trace_properties_file):
                raise ValueError("%s does not exist" % config.dox_trace_properties_file)
            with open(config.dox_trace_properties_file, "r") as stream:
                config["properties"] = yaml.load(stream, SafeLoaderWithoutBoolean)

        DoxTraceDirective.attribute_mappings["valid_in_dim"].append(
            "security" if config.dox_trace_security_backward else "cal"
        )
        DoxTraceDirective.attribute_mappings["valid_in_dim"].append(
            "test_setups" if config.dox_trace_test_setups_backward else "verification_methods"
        )

        return config_inited(app, config)
    except Exception as e:
        exception_raised = True
        raise e
    finally:
        if exception_raised:
            coverage_end()


def build_finished(app, exception):
    try:
        if exception:
            raise exception

        if app.config.dox_trace_dim_root:
            logger.info("writing Dim files... ", nonl=True)
            dim_write(app)
            logger.info("done")

    except Exception as e:
        # use this to debug bugs in this extension
        # import traceback
        # traceback.print_exc()
        raise e
    finally:
        coverage_end()


def version_changed(app, env, _added, _changed, _removed):
    std = env.domaindata["std"]
    version = app.extensions["dox_trace"].version
    if "last_dox_trace_version" not in std or std["last_dox_trace_version"] != version:
        return app.env.found_docs
    return []


def setup(app):
    ###########################
    # EXTENSION CONFIGURATION #
    ###########################

    app.add_config_value("dox_trace_dim_root", None, "html", [str])
    app.add_config_value("dox_trace_tolerant_naming_convention", False, "html", [bool])
    app.add_config_value("dox_trace_allow_deprecated", False, "html", [bool])
    app.add_config_value("dox_trace_allow_undefined_refs", False, "html", [bool])
    app.add_config_value("dox_trace_security_backward", {}, "html", [bool])
    app.add_config_value("dox_trace_test_setups_backward", {}, "html", [bool])
    app.add_config_value("dox_trace_custom_attributes", {}, "html", [dict])
    app.add_config_value("dox_trace_properties_file", None, "html", [str])

    ################
    # OFFICIAL API #
    ################

    # directives used by developers writing documentation
    app.add_directive("mod", ModDirective)
    app.add_directive("spec", SpecDirective)
    app.add_directive("unit", UnitDirective)
    app.add_directive("interface", InterfaceDirective)
    app.add_directive("srs", SrsDirective)

    # directives used by Dim tool
    app.add_directive("requirement", RequirementDirective)
    app.add_directive("information", InformationDirective)

    # special commands for configuration / displaying information
    app.add_directive("dox_trace_config", DoxTraceConfigDirective)
    app.add_directive("undefined_refs", UndefinedRefsDirective)
    app.add_directive("traceability_report", DoxTraceTraceabilityDirective)

    # properties
    app.add_role("prop", prop_role)
    app.add_directive("prop", PropDirective)

    # enclosed
    app.add_directive("enclosed", EnclosedDirective)

    ###############################
    # INTERNAL API, NO PUBLIC USE #
    ###############################

    app.add_role("mod_generated", spec_role)
    app.add_role("spec_generated", spec_role)
    app.add_role("unit_generated", spec_role)
    app.add_role("interface_generated", spec_role)
    app.add_role("requirement_generated", spec_role)
    app.add_role("information_generated", spec_role)
    app.add_role("srs_generated", spec_role)

    ####################
    # SPHINX CALLBACKS #
    ####################

    app.connect("config-inited", config_inited_wrapper)
    app.connect("env-get-outdated", version_changed)
    app.connect("env-before-read-docs", prepare_env)
    app.connect("env-purge-doc", purge_doc_from_env)
    app.connect("env-merge-info", merge_env_parallel_build)
    app.connect("doctree-read", check_unintended_comments)
    app.connect("env-updated", calc_backward)
    app.connect("env-updated", calc_unresolved_references)
    app.connect("env-check-consistency", check_consistency)
    app.connect("doctree-resolved", inject_backward_references)
    app.connect("doctree-resolved", inject_undefined_references)
    app.connect("doctree-resolved", inject_report)
    app.connect("build-finished", build_finished)

    ####################
    # FOR UNIT TESTING #
    ####################

    version = __version__
    if os.environ.get("MANIPULATE_DOXTRACE_VERSION"):
        version = "manipulated_version"

    if os.environ.get("MANIPULATE_DOXTRACE_PARALLEL"):
        app.connect("doctree-resolved", merge_env_parallel_build_non_posix)

    return {
        "version": version,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
