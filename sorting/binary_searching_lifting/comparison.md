# What is binary search and binary lifting used for?
Binary search and binary lifting are useful when there is a sorted/monotonic property. At some point k:

`Arr[k] <= Arr[k+1]`

`Arr[k] >= Arr[k-1]`

This allows us to find the minimum/maximum of functions that are monotonic.
