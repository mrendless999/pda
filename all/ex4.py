# Function with positional arguments
def positional_args(a, b):
    print("Positional Arguments:")
    print("a =", a)
    print("b =", b)

# Function with default arguments
def default_args(a, b=10):
    print("\nDefault Arguments:")
    print("a =", a)
    print("b =", b)

# Function with keyword arguments
def keyword_args(a, b):
    print("\nKeyword Arguments:")
    print("a =", a)
    print("b =", b)

# Function with variable-length arguments
def variable_length_args(*args, **kwargs):
    print("\nVariable-length Arguments:")
    print("Positional (args):", args)
    print("Keyword (kwargs):", kwargs)

# Main program to call functions with different types of arguments
if __name__ == "__main__":
    print("Calling Positional Arguments Function:")
    positional_args(5, 15)

    print("\nCalling Default Arguments Function:")
    default_args(7)           # Uses default value for b
    default_args(7, 20)      # Overrides default value for b

    print("\nCalling Keyword Arguments Function:")
    keyword_args(a=25, b=35)
    keyword_args(b=50, a=40) # Order can be changed with keyword arguments

    print("\nCalling Variable-length Arguments Function:")
    variable_length_args(1, 2, 3, name="Alice", age=30)
