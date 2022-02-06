const { help } = require('optimist');
var helper = require('./helpers.js')
const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];



const undirectedPath = (edges, nodeA, nodeB) => {

  // convert edges into a graph adjency list
  const graph = helper.convertEdgesToAdjencyList(edges);

  return hasPath(graph, nodeA, nodeB, new Set());

};

const hasPath = (graph, src, dst, visited) => {

  if (src === dst) return true;

  if(visited.has(src)) return false;

  visited.add(src);

  for (const n of graph[src]) {
    if (hasPath(graph, n, dst, visited) === true) {
      return true;
    }
  }

  return false;

}



helper.print(helper.convertEdgesToAdjencyList(edges));

helper.print(undirectedPath(edges, 'j', 'm')); // -> true