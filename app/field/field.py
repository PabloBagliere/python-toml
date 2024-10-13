class Field:
    def __init__(self, name, field_type, primary=False, length=None, alias=None):
        self.name = name
        self.type = field_type
        self.primary = primary
        self.length = length
        self.alias = alias
