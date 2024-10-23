from abc import ABC, abstractmethod


class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass


class MyMeta(type):
    def __subclasshook__(cls, subclass):
        if cls is MyInterface:
            attributes = getattr(subclass, '__dict__', {})
            if 'my_method' in attributes:
                return True
        return NotImplemented


class MyClass(metaclass=MyMeta):
    def my_method(self):
        print("Hello, world!")


# MyClass 并没有直接从 MyInterface 继承，但是由于 __subclasshook__ 的实现，
# MyClass 被视为实现了 MyInterface 接口。
isinstance(MyClass(), MyInterface)  # 输出: True

