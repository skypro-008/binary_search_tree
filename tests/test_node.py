from src.node import Node


def test_node_init():
    """Тестируем инициализацию узла."""
    data = {'id': 1}
    node = Node(data)
    assert node.data == data
    assert node.left is None
    assert node.right is None
