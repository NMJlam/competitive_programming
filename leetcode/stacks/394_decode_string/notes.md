## Mistakes

What I needed to identify was that we need to iterate to the smallest bracket level. 
For example in `3[a3[ac]]` the smallest bracket level is `[ac]`, this means that we need to iterate from the front the back of the array.

Second of all, what I should have done was save the strings and the mulitplication operations within a stack instead of treating the entire list of letters as a stack

