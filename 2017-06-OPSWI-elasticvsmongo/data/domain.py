class Class:

    def __init__(self, name):
        self.name = name
        self.methods = []

    def add_method(self, method):
        self.methods.append(method)


class Package:

    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.classes = []

    def add_class(self, clazz):
        self.classes.append(clazz)
