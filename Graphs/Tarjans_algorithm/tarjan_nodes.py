from Graphs.nodes import Node


# add two attributes on top of Node class
class TarjanNode(Node):
    def __init__(self, key: int = None, data: str = None):
        super().__init__(key=key, data=data)
        self.low_link = self.key
        self.on_stack = False
