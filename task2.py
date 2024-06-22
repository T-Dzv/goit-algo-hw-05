from typing import Callable, Generator
import re

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"\d+\.\d+|\d+"  # Match floating-point numbers and integers
    profits = re.findall(pattern, text) # receiving the list of numbers from the text
    for profit in profits:
        yield float(profit)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total_income = 0
    for profit in func(text): # Use the provided generator function to get numbers from the text and sum them to total_income
        total_income += profit
    return total_income

# test case to check if generator_numbers function works as supposed. Uncomment to check
# text = text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# number_generator = generator_numbers(text)  # Create a single generator instance
# print(next(number_generator))  # Prints: 1000.01
# print(next(number_generator))  # Prints: 27.45
# print(next(number_generator))  # Prints: 324.00

# test case to check if sum_profit function works as supposed. Uncomment to check
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}") # Prints 1351.46




