const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];

const convertEdgesToAdjencyList = (edges) => {

  const graph = {};

  for (let edge of edges) {
    const [x, y] = edges;

    if(!(x in graph)) graph[x] = []
    if(!(y in graph)) graph[y] = []
    


  }

}

const undirectedPath = (edges, nodeA, nodeB) => {

};

undirectedPath(edges, 'j', 'm'); // -> true