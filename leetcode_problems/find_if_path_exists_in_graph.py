class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = self.convert_edges_into_adjency_list(edges)
        
        return self.has_path(graph, source, destination, set())
    
    def has_path(self, graph, src, dst, visited_nodes):

        if src == dst: return True

        if src in visited_nodes: return

        visited_nodes.add(src)

        for n in graph[src]:
            if self.has_path(graph, n, dst, visited_nodes): return True

        return False

    def convert_edges_into_adjency_list(self, edges):
        graph = {}
        
        for x, y in edges:
            if(x not in graph): graph[x] = []
            if(y not in graph): graph[y] = []
                
            graph[x].append(y)
            graph[y].append(x)

        return graph