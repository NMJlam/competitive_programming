# Mistakes

1) Didn't find the minimum by using the `x-1` condition. 
By definition of `x-1` not being in the set, we know that `x` is the minimum element of some sequence.

2) Didn't iterate through the set. The list might have duplicates therefore wasting iterations that we could have saved.

## Why is this linear time complexity?

![diagram]('./image/image.png')

In the worst case this is `O(k+k) = O(k)`

This is because we would only iterate for potential `ml` candidate at `x`.
This means that the outer loop only runs in `k` time.

The worst case of the inner loop would be running in `k` time, but by definition of `x` being the min we would not iterate for any other subsequences.
