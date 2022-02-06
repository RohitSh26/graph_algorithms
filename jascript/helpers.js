
module.exports = {

    print,
    convertEdgesToAdjencyList
}

// print message to log
function print(message) {console.log(message)}

// convert edges to adjencyList
function convertEdgesToAdjencyList(edges) {

    const graph = {};
  
    for (let edge of edges) {
  
      const [x, y] = edge;
  
      if(!(x in graph)) graph[x] = [];
      if(!(y in graph)) graph[y] = [];
      
      graph[x].push(y);
      graph[y].push(x);
  
    }
  
    return graph;
  
  }