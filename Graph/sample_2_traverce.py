class Graph:
    def __init__(self):
        self.dic = {}

    def add_vertex(self, data):
        self.dic[data] = []


    def insert(self, vertex, edge, is_bidirectional):
        if vertex not in self.dic:
            self.add_vertex(vertex)
        if edge not in self.dic:
            self.add_vertex(edge)
        self.dic[vertex].append(edge)
        if is_bidirectional:
            self.dic[edge].append(vertex)

    def display(self):
        for x in self.dic:
            print(f"{x}: {' '.join(map(str, self.dic[x]))}")

    def DFS(self, node):
        visited = set()
        if node not in self.dic:
            print("The node not in graph")
            return
        stack = []
        stack.append(node)
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current, "-->", end=" ")
                visited.add(current)
                for i in self.dic[current]:
                    stack.append(i)

    def BFS(self, node):
        visited = set()
        if node not in self.dic:
            print("The node not in graph")
            return
        queue = []
        queue.append(node)
        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current, "-->", end=" ")
                visited.add(current)
                for i in self.dic[current]:
                    queue.append(i)

graph = Graph()
graph.insert(3, 5, True)
graph.insert(3, 4, True)
graph.insert(5, 6, False)
graph.display()
print("DFS:")
graph.DFS(3)

print("\nBFS:")
graph.BFS(3)