

from jinja2 import Template

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"My name is {self.name}, age is {self.age}"


person1 = Person(123, 222)
person2 = Person("RRR", 14)

print(person1.name)
print(person2.name)

greeting1 = person1.greet()
print(greeting1)

greeting2 = person2.greet()
print(greeting2)


# decorators
def template_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@template_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# template 

# 定义模板
template = Template("Hello, {{ name }}!")

# 渲染模板
result = template.render(name="Bob")
print(result)  # 输出: Hello, Bob!


