# curly-carnival

This module is used to create a weighted list of named nodes

## Classes

### Node

The Node class represents a single Node with a name and weight

usage:
```python
>>> from curly_carnival.node import Node
>>> a = Node('node_a', 3)
>>> b = Node('node_b', 5)
>>> b.insert_after(a)
True
```

### Controller

The Controller class manages a chain of Nodes

usage:
```python
>>> from curly_carnival.controller import Controller
>>> controller = Controller() 
>>> controller.add('node_a')
True
>>> controller.add('node_b', 5)
True
>>> controller.add('node_b', 7)
False
>>> controller.fetch('node_a').weight
1

```
## Installation
```bash
pip install git+https://github.com/joejulian/curly-carnival.git
```

## Testing
```bash
python setup.py test
```
