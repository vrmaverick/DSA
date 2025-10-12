# Just rember dont start or do xor with 0
# It returns zero if we take the XOR of two the same numbers. helps to find missing duplicates


def find_missing_number_xor(arr, n):
    """
    Finds the single missing number in an array containing numbers
    from 1 to n (with one number missing) using the XOR method.

    Args:
        arr (list[int]): The input array of n-1 numbers.
        n (int): The upper bound of the sequence (the size the array should be).

    Returns:
        int: The missing number.
    """
    # 1. XOR all numbers from 1 to n (x1)
    # Initialize x1 with the sequence from 1 up to and including n.
    x1 = 0
    for i in range(1, n + 1):
        x1 ^= i

    # 2. XOR all numbers in the input array (x2)
    x2 = 0
    for num in arr:
        x2 ^= num

    # 3. The missing number is x1 XOR x2
    # All present numbers cancel out, leaving only the missing one.
    return x1 ^ x2

# --- Example Usage ---

# The complete sequence should be 1 to 8 (so n=8)
arr_a = [1, 5, 2, 4, 8, 7, 6]  # Missing 3
n_a = 8

missing_a = find_missing_number_xor(arr_a, n_a)
print(f"Input Array: {arr_a}")
print(f"Expected range: 1 to {n_a}")
print(f"The missing number is: {missing_a}")

# Another example: 1 to 5 (n=5)
arr_b = [5, 1, 3, 2]  # Missing 4
n_b = 5

missing_b = find_missing_number_xor(arr_b, n_b)
print(f"\nInput Array: {arr_b}")
print(f"Expected range: 1 to {n_b}")
print(f"The missing number is: {missing_b}")
