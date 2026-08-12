class Punto:
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    def get_x(self):
        return self.__X

    def set_x(self, x):
        self.__X = x

    def get_y(self):
        return self.__Y

    def set_y(self, y):
        self.__Y = y

    def __str__(self):
        return f"Punto(X={self.__X}, Y={self.__Y})"
    
