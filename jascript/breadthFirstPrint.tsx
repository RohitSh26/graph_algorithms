// Breath First Search
const breadthFirstPrint = (aGraph, root) => {

    // create a queue, and add first node as root
    const queue = [root];

    // while there are node on queue
    while (queue.length > 0) {

        // get the first in node from the queue and call it current
        const current = queue.shift()

        console.log(current);

        // go to each neighbor of the current node and push them at the end
        for (let n of aGraph[current]) {
            queue.push(n);
        }
    }
}

// Input Graph
const aGraph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
}

// Call breath first print
breadthFirstPrint(aGraph, 'a');