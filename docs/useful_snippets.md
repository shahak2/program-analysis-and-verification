
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