# User se 2 numbers lo aur unka LCM aur HCF calculate karo.

def find_lcm(x, y):
    """
    Calculates the Least Common Multiple (LCM) of two numbers without using the math module.
    """
    # Determine the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

# Example usage:
num1 = int(input("enter a: "))
num2 = int(input("enter b: "))
print(f"The LCM of {num1} and {num2} is: {find_lcm(num1, num2)}")


def find_hcf(a, b):
    """
    Calculates the HCF (GCD) of two numbers using the Euclidean algorithm.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The HCF of a and b.
    """
    # Ensure numbers are positive, as HCF is typically defined for positive integers.
    a = abs(a)
    b = abs(b)

    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = int(input("enter a: "))
num2 = int(input("enter b: "))
hcf_result = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf_result}")
