function solution(A) {
    // Create a Set for O(1) lookup
    const numSet = new Set(A);
    
    // Start from 1 and find the first missing positive integer
    let smallest = 1;
    
    while (numSet.has(smallest)) {
        smallest++;
    }
    
    return smallest;
}

console.log(solution([-1, -3]))