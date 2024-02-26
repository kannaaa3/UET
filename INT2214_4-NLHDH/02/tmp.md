**3.12**. Call `res[i]` is the number of total created process the loop length `i`. Hence `res[0] = 1`, `res[1] = 2`.

As we can see, `res[i] = 2 * res[i-1]` since after the first `fork()`, there are exactly two equivalent process that run the loop length `i-1`.

Hence, the answer is `2^4 = 16` created process.

**3.14**. Both processes continued to run on the same next piece of code. The only different is the value of `pid` variable: the parent's `pid` is equal to its child created by `fork()`, but the child's `pid` is `0`. 

The output of parent should be:
```
parent: pid = 2603     // C: child pid returned from fork()
parent: pid1 = 2600    // D: actual pid return from getpid()
```
The output of the child:
```
child: pid = 0         // A: pid since fork()
child: pid1 = 2603     // B: actual pid return from getpid()
```

