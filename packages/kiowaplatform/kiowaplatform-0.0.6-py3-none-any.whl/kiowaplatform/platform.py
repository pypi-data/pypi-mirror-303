# platform.py

def calculate_imei_check_digit(imei_14_digits: str) -> int:
    """
    Calculate IMEI check digit for a 14-digit IMEI to make it 15 digits.
    
    Args:
        imei_14_digits (str): The first 14 digits of the IMEI.

    Returns:
        int: The calculated check digit (15th digit).

    Raises:
        ValueError: If the input is not a 14-digit string composed only of digits.
    """
    if not isinstance(imei_14_digits, str):
        raise ValueError("IMEI must be a string.")

    if len(imei_14_digits) != 14:
        raise ValueError("IMEI must be exactly 14 digits long.")

    if not imei_14_digits.isdigit():
        raise ValueError("IMEI must contain only digits.")

    # Convert the IMEI string into a list of integers
    imei_digits = [int(digit) for digit in imei_14_digits]

    # Double every second digit from the right (even-indexed in reverse order)
    for i in range(len(imei_digits) - 1, -1, -2):
        imei_digits[i] *= 2
        # If doubling results in a number greater than 9, subtract 9
        if imei_digits[i] > 9:
            imei_digits[i] -= 9

    # Sum all the digits
    total_sum = sum(imei_digits)

    # Calculate the check digit
    check_digit = (10 - (total_sum % 10)) % 10

    return check_digit
