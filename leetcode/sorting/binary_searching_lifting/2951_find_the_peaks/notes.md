# Sometimes implementing the naive solution is better. 

In this case, we cannot use binary search or binary lifting, this is because we need to find multiple peaks. 
Binary lifting is only able to find 1 single maximum, as it performs jumps based on a monotonic property of the array.
In this question there is no monotonic property as there are multiple maximums.
Therefore, the optimal solution is to iterate through the entire array to find the randomly scattered peaks.
