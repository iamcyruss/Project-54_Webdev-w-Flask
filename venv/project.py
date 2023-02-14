def logging_decoration(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned {result}")
    return wrapper


@logging_decoration
def a_function(num1, num2, num3):
    return num1 * num2 * num3


a_function(1, 2 , 3)
