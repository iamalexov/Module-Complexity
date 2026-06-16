class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")

        self.limit = limit
        self.cache = {}

        self.head = None
        self.tail = None

    def _remove_node(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

    def _add_to_head(self, node):
        node.previous = None
        node.next = self.head

        if self.head:
            self.head.previous = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def get(self, key):
        node = self.cache.get(key)

        if node is None:
            return None

        self._move_to_head(node)

        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return

        node = Node(key, value)

        if len(self.cache) >= self.limit:
            lru_key = self.tail.key

            self._remove_node(self.tail)

            del self.cache[lru_key]

        self._add_to_head(node)

        self.cache[key] = node