# N-Queens Problem
### How to use

Install dependencies
```bash
$ pip install -r requierments
```
```python
from main import QueensMatrix
q = QueensMatrix(8)
q.solve(verbose=False)
q.draw()
```


### How to run tests
```bash
$ python -m pytest test.py -vvvv
```