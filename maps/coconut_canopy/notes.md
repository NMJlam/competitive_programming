# Reflection 

We cannot use a scaled array of 2 because:

```
arr = [1,2]
```

If the algorithm expects that we would throw to:

```
1 => (0, 2)
2 => (1, 3)
res = 1
```

However, with the 2x scaling logic we are thowing:

```
1 => 2 * 1 => (1, 3)
2 => 2 * 2 => (3, 5)
res = 2
```
