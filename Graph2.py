""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""


class Vertex(object):

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__


class Edge(tuple):

    def __new__(cls, *vs):
        if len(vs) != 2:
            raise(ValueError, 'Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        self[v] = {}

    def add_edge(self, e):
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        try:
            return self[v1][v2]
        except KeyError:
            return None

    def vertices(self):
        vs = []
        for v in self.keys():
            vs.append(v.__repr__())
        return vs

    # def edges(self):
    #     es = []
    #     for e in self[].items:
    #         pass


def main(script, *args):
    v = Vertex('v')
    print(v)
    w = Vertex('w')
    print(w)
    e = Edge(v, w)
    print(e)
    g = Graph([v, w], [e])
    x = Vertex('x')
    g.add_vertex(x)
    print('This is the vertices method:')
    print(g.vertices())


if __name__ == '__main__':
    import sys
    main(*sys.argv)