# Handling exceptions

import logging

# Setup logging configuration
logging.basicConfig(filename='errors.log', level=logging.ERROR)


def division_example():
    try:
        x = 10 / 0  # This will raise an error
    except ZeroDivisionError:
        print("Cannot divide by zero!")


def multiple_exceptions_example():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Invalid input! Please enter a number.")
    else:
        print(f"The result is {result}")
    finally:
        print("Execution completed.")


def custom_exception_example():
    class NegativeNumberError(Exception):
        pass

    try:
        num = int(input("Enter a positive number: "))
        if num < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")
    except NegativeNumberError as e:
        print(e)


def nested_try_example():
    try:
        file = open("sample.txt", "r")
        try:
            content = file.read()
            print(content)
        except Exception as e:
            print("Error reading the file:", e)
        finally:
            file.close()
    except FileNotFoundError:
        print("File not found!")


def specific_exception_example():
    try:
        lst = [1, 2, 3]
        print(lst[5])  # IndexError
    except IndexError as e:
        print(f"Index error occurred: {e}")


def logging_example():
    try:
        a = 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"Exception occurred: {e}")
        print("An error occurred, and it has been logged.")


# Run all examples
if __name__ == "__main__":
    print("=== Division Example ===")
    division_example()

    print("\n=== Multiple Exceptions Example ===")
    multiple_exceptions_example()

    print("\n=== Custom Exception Example ===")
    custom_exception_example()

    print("\n=== Nested Try Example ===")
    nested_try_example()

    print("\n=== Specific Exception Example ===")
    specific_exception_example()

    print("\n=== Logging Example ===")
    logging_example()
