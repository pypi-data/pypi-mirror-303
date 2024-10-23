# prevents "no", "yes" etc. to be interpreted as bool

from yaml.constructor import SafeConstructor
from yaml.reader import *
from yaml.scanner import *
from yaml.parser import *
from yaml.composer import *
from yaml.resolver import *


class SafeCstrWithoutBoolean(SafeConstructor):
    def add_bool(self, node):
        return self.construct_scalar(node)


SafeCstrWithoutBoolean.add_constructor("tag:yaml.org,2002:bool", SafeCstrWithoutBoolean.add_bool)


class SafeLoaderWithoutBoolean(Reader, Scanner, Parser, Composer, SafeCstrWithoutBoolean, Resolver):
    def __init__(self, stream):
        Reader.__init__(self, stream)
        Scanner.__init__(self)
        Parser.__init__(self)
        Composer.__init__(self)
        SafeCstrWithoutBoolean.__init__(self)
        Resolver.__init__(self)
