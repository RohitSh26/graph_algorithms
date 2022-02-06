// define a graph

const depthFirstprint = (graph, source) => {
    const stack = [source];

    // while the stack is not empty
    while (stack.length > 0) {

        // get the current node
        let current = stack.pop();
        
        console.log(current);

        // for each neighbor of current node push them into the stack
        for (let neighbor of graph[current]) {
            stack.push(neighbor);
        }
        
    }
}

const depthFirstRecursivePrint = (graph, root) => {
    
     console.log(root);

    for(let neighbor of graph[root]){
        depthFirstRecursivePrint(graph, neighbor);
    }   
}

const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
}


depthFirstprint(graph, 'a');

depthFirstRecursivePrint(graph, 'a');