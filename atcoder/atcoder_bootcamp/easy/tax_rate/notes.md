# Reflection:

# Why the decimal rounding approach does not work
The reason that is this wrong is because of floating point precision.
The coding languages represent numbers in binary - this is to errors in floating number precision.
For instance, 1.08 might be represented with 1.079999999.
This means that as floats are being divided, it would lead to potentially inaccurate especially when rounding.

In competitive programming, we should try to avoid floating point division due to the above reasons.

# More efficient approaches
We can use binary searching or lifting here to solve for x.
This because in the range `1...n` there exists some x that can be found.
These techniques help to narrow down the searching window instead of 'brute-forcing' a search
