# pass-functions-to-c
Experiment with how to best pass an arbitrary number of functions to C

## Usage

To test, do for instance,
```
import passfuncc
passfuncc.evaluate_and_add(2.,lambda r: r+1,lambda x: x**2.)
```
or
```
import passfuncc; passfuncc.evaluate_and_add(2.,lambda r: r+1,lambda x: x**2.,lambda y: y**3)
```

