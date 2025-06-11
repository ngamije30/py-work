#!/usr/bin/env python3
"""
Test script for matrix multiplication in alumathpeergroup10 package.
"""
from alumathpeergroup10 import Matrix, multiply

def test_multiplication():
    """Test matrix multiplication with various cases."""
    # Test 1: 2x2 * 2x2
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    result = multiply(a, b)
    print("Test 1 (2x2 * 2x2):")
    print(f"{a} *\n{b} =\n{result}\n")
    
    # Test 2: 2x3 * 3x2
    c = Matrix([[1, 2, 3], [4, 5, 6]])
    d = Matrix([[7, 8], [9, 10], [11, 12]])
    result = multiply(c, d)
    print("Test 2 (2x3 * 3x2):")
    print(f"{c} *\n{d} =\n{result}\n")
    
    # Test 3: Invalid dimensions (2x2 * 3x2)
    print("Test 3 (2x2 * 3x2):")
    try:
        # Create a 3x2 matrix (3 rows, 2 columns)
        e = Matrix([[1, 2], [3, 4], [5, 6]])
        result = multiply(a, e)  # a is 2x2, e is 3x2 - should fail due to dimension mismatch
        print("✗ Test failed: Should not multiply 2x2 and 3x2 matrices")
        print(f"Got result: {result}")
    except ValueError as e:
        expected_msg = "columns of first matrix (2) must equal rows of second matrix (3)"
        if expected_msg in str(e):
            print(f"✓ Correctly caught error: {e}")
        else:
            print(f"✗ Wrong error message. Expected '{expected_msg}', got: {e}")

if __name__ == "__main__":
    test_multiplication()
