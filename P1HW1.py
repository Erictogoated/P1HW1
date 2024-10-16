# Eric Corbett
# 9/26/2024
# P1HW1
# coding a math equation 
def calculate_exponent(base, exponent):
    return base ** exponent


def calculate_sum_and_subtract(a, b, c):
    return (a + b) - c


base = int(input("Enter the base value (integer): "))
exponent = int(input("Enter the exponent value (integer): "))

result = calculate_exponent(base, exponent)

print(f"{base} raised to the power of {exponent} is {result}!!!")


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

final_result = calculate_sum_and_subtract(num1, num2, num3)


print(f"The result of adding {num1} and {num2}, then subtracting {num3} is {final_result}!!!")
