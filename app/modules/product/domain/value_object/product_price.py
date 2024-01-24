class ProductPrice:
    def __init__(self, value: float):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @staticmethod
    def create(value: float):
        if type(value) == int:
            value = round(float(value), 2)

        if value < 1:
            raise Exception('price must be greater than 0')

        return ProductPrice(value)

    @staticmethod
    def build(value: float):
        return ProductPrice(value)
