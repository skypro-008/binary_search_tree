import pytest
from src.binary_search_tree import BinarySearchTree


@pytest.fixture
def bst_root():
    """BST с единственным узлом в вершине."""
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    return bst


def test_bst_empty():
    """BST при инициализации должен быть пустым."""
    bst = BinarySearchTree()
    assert bst.root is None


def test_bst_insert_root(bst_root):
    """Проверяем добавление узла в вершину дерева."""
    assert bst_root.root.data['id'] == 40


def test_bst_insert_left(bst_root):
    """Проверяем добавление влево от вершины BST."""
    bst_root.insert({'id': 30})
    assert bst_root.root.left.data['id'] == 30


def test_bst_insert_right(bst_root):
    """Проверяем добавление вправо от вершины BST."""
    bst_root.insert({'id': 50})
    assert bst_root.root.right.data['id'] == 50
