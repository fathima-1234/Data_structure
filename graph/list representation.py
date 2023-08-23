class Graph:
    def __init__(self):
        self.graph = {}
    def add_node(self,node):
        if node  not in self.graph:
            self.graph[node] = []
    def add_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    def remove_node(self,node):
        if node in self.graph:
            del self.graph[node]
        for vertices in self.graph.values():
            if node in vertices:
                vertices.remove(node)

    def remove_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            if node1 in node2:
                self.graph[node1].remove[node1]
                self.graph[node2].remove[node1]

    def bfs (self,start_node):
        visited = set()
        queue = [start_node]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                queue.extend(self.graph[node])
    def dfs(self,start_node,visited = None):
        if visited  is None:
            visited = set()

        visited.add(start_node)
        print(start_node)
        for neighbour in self.graph[start_node]:
            if neighbour not in visited:
                self.dfs(neighbour,visited)

    def get_neighbour(self,node):
        if node in self.graph:
            return self.graph[node]
        else:
            return []
    def is_connected(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            visited  = set()
            stack = [node1]
            while stack:
                node = stack.pop()
                
                if node == node2:
                    return True
                if node not in visited:
                    visited.add(node)
                    stack.extend(self.graph[node])
        return False

    def short_distance(self,node1,target):
        if node1 == target:
            return 0
        visited = set()
        queue = [(node1, 0)]
        first = 0
        while first < len(queue):
            node,distance = queue[first]
            first = first + 1
            if node == target:
                return distance

            if node not in visited:
                visited.add(node)
            for neighbour in self.graph[node]:
               
                queue.append((neighbour, distance + 1))
        return -1

graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.add_node("d")
graph.add_node("e")
graph.add_node("f")
graph.add_node("g")

graph.add_edge("a","b")
graph.add_edge("b","c")
graph.add_edge("c","d")
graph.add_edge("d","a")
graph.add_edge("b","e")
graph.add_edge("e","g")
graph.add_edge("a","f")
graph.remove_node("f")
graph.remove_edge("c","d")
print(graph.graph)
graph.bfs("a")
connected = graph.is_connected("a","c")
print("C and A are connected:", connected)
print(graph.is_connected("a","b"))
print(graph.is_connected("a","d"))

print("dfs traversal")
graph.dfs("a")
result = graph.get_neighbour("a")
print(result)
distance = graph.short_distance("a", "c")
if distance != -1:
    print("Shortest distance between A and C:", distance)
else:
    print("There is no path between A and C.")

