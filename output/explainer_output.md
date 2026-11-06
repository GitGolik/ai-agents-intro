## Topic: Python Decorators

## Simple Explanation
Decorators in Python are a powerful tool for extending the functionality of functions and methods. They are essentially functions that take another function and modify its behavior without changing its source code. Decorators are often used to add logging, authentication, caching, or other behaviors to functions.

## Key Concepts
- **Function Decorators**: Decorators are functions that take a function as an argument and return a new function.
- **Syntax**: A decorator is defined using the `@` symbol followed by the name of the decorator function.
- **Usage**: Decorators can be used to add functionality to existing functions.
- **Common Decorators**: Common decorators include `@staticmethod`, `@classmethod`, and `@property`.
- **Example**: Here's a simple example of a decorator that logs the execution time of a function:

```python
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@log_time
def example_function(n):
    for i in range(n):
        pass
```

## Example
Below is the code for the `log_time` decorator and an example usage of it:

```python
import time

# Function decorator
def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

# Example usage
@log_time
def example_function(n):
    for i in range(n):
        pass

example_function(1000000)
```

## Practice Exercise
Create a decorator that counts the number of times a function is called. Here's an example:

```python
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@count_calls
def my_function(x):
    return x * x

print(my_function(5))  # Output: 25
print(my_function(5))  # Output: 25
print(count_calls.my_function.count)  # Output: 2
```

## Common Mistakes
1. **Incorrect Syntax**: Ensure that the `@` symbol is placed correctly before the decorator function.
2. **Not Returning the Wrapper**: Ensure that the decorator returns the wrapper function.
3. **Not Using the Decorator**: Ensure that the decorator is applied to the function using the `@` symbol.

## Review Comments
- Decorators are a powerful tool for adding functionality to functions.
- They allow you to extend the behavior of functions without modifying their source code.
- Decorators can be used to add logging, authentication, caching, or other behaviors to functions.

## Final Summary
Decorators in Python are a powerful tool for extending the functionality of functions and methods. They are essentially functions that take a function and return a new function. Decorators can be used to add logging, authentication, caching, or other behaviors to functions. They are often used to add functionality to existing functions and can be used to create reusable and flexible code.