# 278. First Bad Version 

The main bottle neck here is that we should limit the number of calls to the API `isBadVersion()`. This means that 
the binary lifting technique is not the most efficient solution. 

## Binary Lifting 
Let k be the index at which we change versions from "Good" to "Bad". 

In binary lifting we are iteratively building up to the index k using powers of 2 (n/2, n/4 n/8 etc.). This means that in order to get the "perfect" increment up to k we might have to try many powers of 2 before getting the right one. This means that we would call `isBadVersion` many times before actually getting the correct index. 


![diagram](./image/firstBadVersion.png)

## Binary Searching

In binary searching we are always halving the sample size down each time ensuring that we would limit the number of `isBadVersion` calls. This makes the binary search implementation more efficient that the Binary lifting solution.
