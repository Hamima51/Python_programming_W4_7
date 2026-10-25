print("Program starting.")

print("\nCheck multiplicative persistence.")
number = abs(int(input("Insert an integer: ")))

steps = 0

while number >= 10:
    digits = [int(digit) for digit in str(number)]
    product = 1
    for digit in digits:
        product *= digit
    print(" * ".join(str(digit) for digit in digits) + f" = {product}")
    number = product
    steps += 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")

print("\nProgram ending.")