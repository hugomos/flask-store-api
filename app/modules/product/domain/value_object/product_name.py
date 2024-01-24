class ProductName:
    def __init__(self, value: str):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @staticmethod
    def create(value: str):
        if type(value) != str:
            raise Exception('name must be a string')

        if value.strip() == '':
            raise Exception('name cannot be empty')

        if len(value) < 3:
            raise Exception('name must be at least 3 characters long')

        if len(value) > 80:
            raise Exception('name must be at most 80 characters long')

        return ProductName(value)

    @staticmethod
    def build(value: str):
        return ProductName(value)
