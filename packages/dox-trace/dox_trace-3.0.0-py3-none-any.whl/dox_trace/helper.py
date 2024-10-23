from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

cat_name2level = {"module": 1, "architecture": 2, "software": 3, "system": 4, "input": 5}


def create_ref_node(app, ref_id, fromdocname):
    std = app.env.domaindata["std"]
    spec_id = std["spec_id"][ref_id]
    docname, r = std["anonlabels"][ref_id]
    refuri = app.builder.get_relative_uri(fromdocname, docname) + "#" + r
    return nodes.reference(
        spec_id,
        spec_id,
        internal=True,
        refdocname=docname,
        refuri=refuri,
        refid=r,
    )


class DimViewList(ViewList):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    def puts(self, string):
        self.append(string, self.filename)

    @staticmethod
    def string_to_nodes(string, offset, directive):
        filename = directive.get_source_info()[0]
        line_number = directive.get_source_info()[1]

        rst = DimViewList(filename)
        for s in string:
            rst.puts(s)

        node = nodes.section()
        node.document = directive.state.document
        nested_parse_with_titles(directive.state, rst, node, offset)

        titles = []
        for generated_node in node.traverse():
            if isinstance(generated_node, nodes.title):
                titles.append(generated_node)
            generated_node.line = line_number

        # within a spec-box, there is sometimes no newline rendered by RTD before a heading
        previous_parent = None
        for t in titles:
            p = t.parent
            assert p is not None  # in most cases p is a section node
            pp = p.parent
            assert pp is not None  # in most cases pp is a section node

            # in the following case, Sphinx renders a newline already
            if (pp.parent is not None or previous_parent is None) and pp.parent != previous_parent:
                previous_parent = pp.parent
                continue
            previous_parent = pp.parent

            # if spec is starting with a heading, no newline is needed
            idx = pp.index(p)
            if idx == 0:
                continue
            # also no newline is needed if the heading has an anchor, e.g. .. _xyz:
            if isinstance(pp.children[idx - 1], nodes.target):
                continue
            # or previous element is a block
            if isinstance(pp.children[idx - 1], nodes.literal_block):
                continue
            # or previous element ended with a block
            pp_grandchildren = pp.children[idx - 1].children
            if len(pp_grandchildren) > 0 and isinstance(pp_grandchildren[-1], nodes.literal_block):
                continue

            # the newline is enforced by an invisible space instead of <br>, because in some
            # situations the <br> would be packed into a container/span/paragraph, which makes the
            # vertical gap before the heading larger than intended
            newline = nodes.raw("", "&nbsp;", format="html")

            if len(pp_grandchildren) > 0 and isinstance(pp_grandchildren[-1], nodes.target):
                # if previous section ended with an anchor, place the newline here
                pp_grandchildren.insert(len(pp_grandchildren) - 1, newline)
            else:
                # otherwise in front of the heading
                pp.children.insert(idx, newline)

        return node.children
