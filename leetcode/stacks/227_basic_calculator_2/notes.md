# Reflection

Was able to get the main idea here.

I think the main issue was implementing the solution:

1) What I failed to notice was that '+' and '-' are just inverses of each other, so we can just store all of the values on a stack and return the sum.

2) Another thing, is that I wasn't able to understand how to parse the values. 
What I tried to do was to parse the first number and then parse the (operation, number) pairs.
To parse the values what I should have done was to store the operation and then parse the number, using the previous operation to decide the conditonal I would go down.

## Optimal solution

Given that solution is the sum of the stack we can actually keep a running sum of the solution. Seen in the optimal solution.


