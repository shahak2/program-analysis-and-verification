
### Usage:

paav.py - A Python script for performing static analysis.

positional arguments:

  path              The path to the program code.
  {p,s,c}           Specify the domain (parity, summation, or combined).

options:

  -h, --help        show this help message and exit
  -w, --widen       Use widen.
  -n, --narrow      Use narrow.
  -t, --run_tests   Run tests - No need for path or domain.
  -p, --plot_graph  Plot graph.

```
    usage: paav.py [-h] [-w] [-n] [-t] [-p] [path] [{p,s,c}]
```

### Examples:

- Basic parity domain test:
```
    py .\paav.py .\programs\examples\language_example.txt p
```

- Basic summation(interval) domain test:
```
    py .\paav.py .\programs\summation_tests\class_test.txt s
```

- Summation(interval) domain test with widening:
```
    py .\paav.py .\programs\summation_tests\class_test.txt s -w
```

- Summation(interval) domain test with widening and narrowing:
```
    py .\paav.py .\programs\summation_tests\class_test.txt s -w -n
```

- Basic combined domain (parity x interval) test:
```
    py .\paav.py .\programs\combined_tests\class_test.txt c
```

- Basic combined domain (parity x interval) test with plotting iterations:
```
    py .\paav.py .\programs\general_tests\simple_test.txt c -p
```

### Running tests:

- You could add -p for each test to plot the graph.

**Parity:**

```
    py .\paav.py programs/parity_tests/infinite_loop_missed.txt p
    py .\paav.py programs/parity_tests/simple_test.txt p
    py .\paav.py programs/parity_tests/TOP_limitation.txt p
    py .\paav.py programs/parity_tests/assertion_fails_intentionally.txt p
    py .\paav.py programs/parity_tests/fast_double_loop.txt p
```

**Summation:**

```
    py .\paav.py programs/summation_tests/class_test.txt s
    py .\paav.py programs/summation_tests/class_test.txt s -w
    py .\paav.py programs/summation_tests/class_test.txt s -w -n



```