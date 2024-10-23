import os

enable_coverage = os.environ.get("SPHINX_COVERAGE")

if enable_coverage:
    import coverage

    dox_trace_root = os.path.dirname(__file__)
    source = [dox_trace_root]
    omit = [os.path.join(dox_trace_root, "__init__.py"), __file__]
    cov = coverage.Coverage(branch=True, source=source, omit=omit)


def coverage_start():
    if enable_coverage:
        cov.start()


def coverage_end():
    if enable_coverage:
        cov.stop()
        cov.save()
