def is_even(number):
    return number % 2 == 0

def is_range_version1(x):

    if 0 <= x < 10:
        return True
    else:
        return False


# Unit Tests for is_even

# Test Case 1: Even number
assert is_even(4) == True

# Test Case 2: Odd number
assert is_even(7) == False

# Test Case 3: Zero (an even number)
assert is_even(0) == True

# Unit Tests for is_range_version1

# Test Case 1: Number within the range
assert is_range_version1(5) == True

# Test Case 2: Number outside the range (too low)
assert is_range_version1(-1) == False

# Test Case 3: Number outside the range (too high)
assert is_range_version1(10) == False

# Test Case 4: Edge case at lower boundary
assert is_range_version1(0) == True

# Test Case 5: Edge case at upper boundary
assert is_range_version1(9) == True

# Test Case 6: Number exactly at the exclusion limit
assert is_range_version1(10) == False

print("All test cases passed!")
