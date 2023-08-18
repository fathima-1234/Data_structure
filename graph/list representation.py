def add_node(v):
    if v in graph:
        print("nod eis present")
    else:
        graph[v] = []
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print("node is not present")
    elif v2 not in graph:
        print("node is not present") 

    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)





graph = {}
add_node(4)
add_node(5)
add_edge(4,5,10)
print(graph)