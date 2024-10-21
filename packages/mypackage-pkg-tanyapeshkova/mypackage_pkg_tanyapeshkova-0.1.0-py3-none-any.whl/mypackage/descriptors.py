class MyDescriptor:
    def __get__(self, instance, owner):
        print("Getting the value")
        return instance._value

    def __set__(self, instance, value):
        print("Setting the value")
        instance._value = value

class MyClass:
    value = MyDescriptor()

    def __init__(self, value):
        self._value = value

if __name__ == "__main__":
    obj = MyClass(10)
    print(obj.value)
    obj.value = 20
    print(obj.value)