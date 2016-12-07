import pytest
from src.controller import Controller


class TestController:

    def test_add_node(self):
        name = 'node_a'
        weight = 5

        c = Controller()
        assert c.add(name) is True
        node = c.fetch(name)
        assert node.name == name
        assert isinstance(node.weight, int)

        c = Controller()
        assert c.add(name, weight) is True
        assert c.add(name, weight) is False
        node = c.fetch(name)
        assert node.name == name
        assert node.weight == weight

    def test_dump(self):
        res = [
            {'name': 'node_a', 'weight': 3},
            {'name': 'node_c', 'weight': 5},
            {'name': 'node_b', 'weight': 7},
            ]
        c = Controller()
        # Adding these nodes out of order ensure ordered return
        c.add('node_a', 3)
        c.add('node_b', 7)
        c.add('node_c', 5)

        assert c.dump() == res

    def test_print_ordered_names(self):
        res = 'node_a node_c node_b'

        c = Controller()
        # Adding these nodes out of order ensure ordered return
        c.add('node_a', 3)
        c.add('node_b', 7)
        c.add('node_c', 5)

        assert c.print_ordered_names(False) == res
