class Cluster(object):
    CORE_NODE = 0
    BORDER_NODE = 1

    def __init__(self, name):
        self.name = name
        self.internal_names = set()
        self.cores = set()
        self.borders = set()

    def add(self, node, state):
        if state == self.CORE_NODE:
            self.borders.discard(node)
            self.cores.add(node)
        elif state == self.BORDER_NODE:
            self.borders.add(node)
            # TODO: we also need to support downgrading a node in incremental mode
        else:
            raise ValueError(
                "invalid state %r, expected %r (%s.CORE_NODE) or %r (%s.BORDER_NODE)" % (
                    state, self.CORE_NODE, self.__class__.__name__,
                    self.BORDER_NODE, self.__class__.__name__
                )
            )

    def __iadd__(self, other):
        if isinstance(self, other.__class__):
            self.cores.update(other.cores)
            self.borders.update(other.borders)
            # ensure that none of the core nodes are in list of border nodes
            self.borders = self.borders - self.cores
            self.internal_names.union(other.internal_names)
            self.internal_names.add(other.name)
            return self
        return NotImplemented

    def __repr__(self):
        return "%s(name=%s, names=%s, core_nodes=%s, border_nodes=%s)" % (
            self.__class__.__name__,
            self.name,
            self.internal_names,
            self.cores,
            self.borders
        )
