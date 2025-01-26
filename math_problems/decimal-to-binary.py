def decimal_to_binary(decimal_num):
    """Converts a decimal number to binary."""
    if decimal_num == 0:
        return "0"

    binary_result = ""
    while decimal_num > 0:
        binary_result = str(decimal_num % 2) + binary_result
        decimal_num //= 2
        print(binary_result)

    return binary_result 



if __name__ == '__main__':
    decimal_number = 25
    binary_number = decimal_to_binary(decimal_number)
    print(f"The binary of {decimal_number} = {binary_number}")
