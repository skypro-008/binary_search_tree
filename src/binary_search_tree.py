from src.node import Node


class BinarySearchTree:
    """Класс для хранения структуры бинарного дерева поиска."""

    def __init__(self) -> None:
        """BST инициализируется пустым деревом."""
        self.root = None

    def insert(self, data: dict) -> None:
        """Добавляем данные в BST."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node: Node, data: dict) -> None:
        """Рекурсивно ищем место куда добавить новый узел."""
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left, data)

        if data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)

    def search(self, data_id: int) -> dict | None:
        """Ищем данные по data_id и возвращаем словарь."""
        if self.root is None:
            return None
        else:
            return self._search_recursively(self.root, data_id)

    def _search_recursively(self, node: Node, data_id: int) -> dict | None:
        """Ищем рекурсивно данные и возвращаем, если наши, иначе None."""
        if data_id == node.data['id']:
            return node.data
        if data_id < node.data['id']:
            if node.left is None:
                return None
            else:
                return self._search_recursively(node.left, data_id)
        if data_id > node.data['id']:
            if node.right is None:
                return None
            else:
                return self._search_recursively(node.right, data_id)
