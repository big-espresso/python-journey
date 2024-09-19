#!/usr/bin/env python


# args and kwargs
def args_example(*args):
    print(args)
    for arg in args:
        print(arg)


print


def kwargs_example(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


my_args = ("Once", "upon", "a", "time")
my_kwargs = {"Uno": 1, "Dos": 2, "Tres": 3}

args_example(*my_args)
args_example("Once", "upon", "a", "time")

kwargs_example(**my_kwargs)
kwargs_example(Uno=1, Dos=2, Tres=3)

# args
# When you use *my_args, you're unpacking a tuple into individual arguments.
# The *args parameter inside the function then packs those individual arguments back into a tuple for use within the function.

# kwargs
# When you use **my_kwargs, you're unpacking a dictionary into individual keyword arguments.
# The **kwargs parameter inside the function packs those keyword arguments back into a dictionary for use within the function.


import random

random_integer = random.randint(1, 10)

print(random_integer)
