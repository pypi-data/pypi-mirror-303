from typing import Dict


class MGobject:
    def __init__(self, attributes=None):
        if attributes is None:
            attributes = {}
        self.attributes = attributes
