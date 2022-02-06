var helper = require('./helpers.js')
const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];



const undirectedPath = (edges, nodeA, nodeB) => {

};



helper.print(helper.convertEdgesToAdjencyList(edges));

undirectedPath(edges, 'j', 'm'); // -> true