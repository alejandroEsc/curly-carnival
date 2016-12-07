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
