const testGraph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
};


const hasPath = (graph, source, destination) => {

    // if source and destination are same there is a path
    if (source === destination) return true;

    // go to each neighbor 
    for (let n of graph[source]) {
        if (hasPath(graph, n, destination) == true) {
            return true;
        }
    }

    // we ran through all the nodes and neighbor 
    return false;

}

const result = hasPath(testGraph, 'f', 'j'); // true
console.log(result);
