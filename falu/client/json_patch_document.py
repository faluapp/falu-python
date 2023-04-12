class JsonPatchDocument(object):

    def __init__(self):
        self.operations = []

    def add(self, path: str, value):
        self.operations.append(AddOperation(path=path, value=value).__dict__)
        return self

    def remove(self, path):
        self.operations.append(RemoveOperation(path=path).__dict__)
        return self

    def test(self, path: str, value):
        self.operations.append(TestOperation(path=path, value=value).__dict__)
        return self

    def replace(self, path: str, value):
        self.operations.append(ReplaceOperation(path=path, value=value).__dict__)
        return self

    def move(self, path: str, _from):
        self.operations.append(MoveOperation(path=path, _from=_from).__dict__)
        return self

    def copy(self, path: str, _from):
        self.operations.append(CopyOperation(path=path, _from=_from).__dict__)
        return self

    def get_operations(self):
        return self.operations


class PathOperation(object):

    def __init__(self, op):
        self.op = op


class AddOperation(PathOperation):
    def __init__(self, path: str, value):
        super().__init__("add")
        self.path = path
        self.value = value


class CopyOperation(PathOperation):
    def __init__(self, path: str, _from):
        super().__init__("copy")
        self.path = path
        self._from = _from


class MoveOperation(PathOperation):
    def __init__(self, path: str, _from):
        super().__init__("move")
        self.path = path
        self._from = _from


class RemoveOperation(PathOperation):
    def __init__(self, path: str):
        super().__init__("remove")
        self.path = path


class ReplaceOperation(PathOperation):
    def __init__(self, path: str, value):
        super().__init__("replace")
        self.path = path
        self.value = value


class TestOperation(PathOperation):
    def __init__(self, path: str, value):
        super().__init__("test")
        self.path = path
        self.value = value
