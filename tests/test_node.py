import pytest
from src.node import Node


class TestNode:

    def test_create_node(self):
        name = 'node_a'
        weight = 5
        a = Node(name, weight)
        assert a.name == name
        assert a.weight == weight

    def test_insert_after(self):
        # Test wrong order insertion
        a = Node('node_a', 3)
        b = Node('node_b', 5)
        with pytest.raises(AssertionError):
            a.insert_after(b)

        # Test duplicate name inertion
        a = Node('node_a', 3)
        b = Node('node_a', 5)
        with pytest.raises(AssertionError):
            b.insert_after(a)

        # Test correct order insertion
        a = Node('node_a', 3)
        b = Node('node_b', 5)
        assert b.insert_after(a) is True

    def test_insert_before(self):
        # Test wrong order insertion
        a = Node('node_a', 3)
        b = Node('node_b', 5)
        with pytest.raises(AssertionError):
            b.insert_before(a)

        # Test correct order insertion
        a = Node('node_a', 3)
        b = Node('node_b', 5)
        assert a.insert_before(b) is True
