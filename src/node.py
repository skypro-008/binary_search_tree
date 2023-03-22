class Node:
    """Класс для представления узла с данными."""

    def __init__(self, data: dict) -> None:
        self.data = data
        self.left = None
        self.right = None
