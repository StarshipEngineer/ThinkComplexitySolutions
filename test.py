# import Graph
# import GraphWorld
#
# # n = int(10)
# # labels = string.ascii_lowercase + string.ascii_uppercase
# # vs = [Vertex(c) for c in labels[:n]]
# vs = [Graph.Vertex('a')]
#
# g = Graph.Graph(vs)
# g.add_all_edges()
# layout = GraphWorld.CircleLayout(g)
#
# gw = GraphWorld.GraphWorld()
# gw.show_graph(g, layout)
# gw.mainloop()
#

# d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
# target = 'a'
# first_index = 0
# last_index = len(d) - 1
# in_list = True
# while first_index != last_index and in_list:
#     middle_index = int((first_index + last_index) / 2)
#     if target == d[middle_index]:
#         print 'This is immediate find'
#         break
#     elif target < d[middle_index]:
#         last_index = middle_index
#         print 'last index = %s' % (last_index)
#     elif target > d[middle_index]:
#         first_index = middle_index
#         print 'first index = %s' % (first_index)
# if d[middle_index] == target:
#     index = middle_index
# else:
#     index = None
# print index


# for i in range(20):
#     d.append('%s') % i

d = [e for e in range(10)]
print d
