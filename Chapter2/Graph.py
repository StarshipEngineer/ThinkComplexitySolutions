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
    # For vertices a and b, graph[a][b] maps
    # to the edge that connects a->b, if it exists.

    def __init__(self, vs=[], es=[]):
        # Creates a new graph.
        # vs: list of vertices;
        # es: list of edges.
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

    def remove_edge(self, v, w):
        del self[v][w]

    def vertices(self):
        return [v for v in self.keys()]

    def edges(self):
        es = []
        for i in self.keys():
            for e in self[i].keys():
                es.append(self[i][e])
        return es

    def out_vertices(self, v):
        return [i for i in self[v].keys()]

    def out_edges(self, v):
        return [self[v][i] for i in self[v].keys()]

    def add_all_edges(self):
        for l in self:
            for m in self:
                if l != m:
                    self[l][m] = l, m
                    self[m][l] = l, m

    def add_regular_edges(self, degree):
        for l in self:
            for m in self:
                if l != m:
                    self[l][m] = l, m
                    self[m][l] = l, m


def main(script, *args):
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    vs = [v, w, x]
    e = Edge(v, w)
    es = [e]
    g = Graph(vs, es)
    print g.out_vertices(x)

if __name__ == '__main__':
    import sys
    main(*sys.argv)