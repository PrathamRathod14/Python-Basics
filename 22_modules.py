# modules_demo.py

import math
import random
import datetime
import os
import sys
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

# 1. Math Module Example
def math_module_example():
    print("=== Math Module Example ===")
    print("Square root of 16:", math.sqrt(16))
    print("Ceiling of 4.2:", math.ceil(4.2))
    print("Value of Pi:", math.pi)


# 2. Random Module Example
def random_module_example():
    print("\n=== Random Module Example ===")
    print("Random integer between 1 and 10:", random.randint(1, 10))
    print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))
    print("Random float between 0 and 1:", random.random())


# 3. Datetime Module Example
def datetime_module_example():
    print("\n=== Datetime Module Example ===")
    now = datetime.datetime.now()
    print("Current date and time:", now)
    print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))


# 4. OS Module Example
def os_module_example():
    print("\n=== OS Module Example ===")
    print("Current working directory:", os.getcwd())
    print("List of files in current directory:", os.listdir())


# 5. Sys Module Example
def sys_module_example():
    print("\n=== Sys Module Example ===")
    print("Python version:", sys.version)
    print("Command line arguments:", sys.argv)


# 6. Logging Module Example
def logging_module_example():
    print("\n=== Logging Module Example ===")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")


if __name__ == "__main__":
    math_module_example()
    random_module_example()
    datetime_module_example()
    os_module_example()
    sys_module_example()
    logging_module_example()
