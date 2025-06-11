#!/usr/bin/env python3
"""
Comprehensive test script for matrix operations.
Follows the error handling and testing guidelines.
"""
from alumathpeergroup10 import Matrix, multiply, add, subtract, transpose

def test_matrix_creation():
    """Test matrix creation with various inputs."""
    print("\n=== Testing Matrix Creation ===")
    
    # Test 1: Valid matrix
    try:
        m = Matrix([[1, 2], [3, 4]])
        print("✓ Valid 2x2 matrix created successfully")
    except Exception as e:
        print(f"✗ Failed to create valid matrix: {e}")
        return False
    
    # Test 2: Empty matrix
    try:
        m = Matrix([])
        print("✗ Should not create empty matrix")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected empty matrix: {e}")
    
    # Test 3: Non-rectangular matrix
    try:
        m = Matrix([[1, 2], [3]])
        print("✗ Should not create non-rectangular matrix")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected non-rectangular matrix: {e}")
    
    # Test 4: Invalid data type
    try:
        m = Matrix([[1, 2], [3, 'a']])
        print("✗ Should not create matrix with non-numeric data")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected invalid data type: {e}")
    
    # Test 5: None input
    try:
        m = Matrix(None)
        print("✗ Should not create matrix from None")
        return False
    except TypeError as e:
        print(f"✓ Correctly rejected None input: {e}")
    
    return True

def test_matrix_addition():
    """Test matrix addition with various inputs."""
    print("\n=== Testing Matrix Addition ===")
    
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    
    # Test 1: Valid addition
    try:
        result = add(a, b)
        print("✓ Valid addition successful")
        print(f"  {a} +\n{b} =\n{result}")
    except Exception as e:
        print(f"✗ Valid addition failed: {e}")
        return False
    
    # Test 2: Different dimensions
    c = Matrix([[1, 2, 3]])
    try:
        result = add(a, c)
        print("✗ Should not add matrices of different sizes")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected addition with different sizes: {e}")
    
    # Test 3: None input
    try:
        result = add(a, None)
        print("✗ Should not add with None")
        return False
    except TypeError as e:
        print(f"✓ Correctly rejected None input: {e}")
    
    return True

def test_matrix_subtraction():
    """Test matrix subtraction with various inputs."""
    print("\n=== Testing Matrix Subtraction ===")
    
    a = Matrix([[5, 6], [7, 8]])
    b = Matrix([[1, 2], [3, 4]])
    
    # Test 1: Valid subtraction
    try:
        result = subtract(a, b)
        print("✓ Valid subtraction successful")
        print(f"  {a} -\n{b} =\n{result}")
    except Exception as e:
        print(f"✗ Valid subtraction failed: {e}")
        return False
    
    # Test 2: Different dimensions
    c = Matrix([[1, 2, 3]])
    try:
        result = subtract(a, c)
        print("✗ Should not subtract matrices of different sizes")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected subtraction with different sizes: {e}")
    
    return True

def test_matrix_multiplication():
    """Test matrix multiplication with various inputs."""
    print("\n=== Testing Matrix Multiplication ===")
    
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    
    # Test 1: Valid multiplication (2x2 * 2x2)
    try:
        result = multiply(a, b)
        print("✓ Valid 2x2 multiplication successful")
        print(f"  {a} *\n{b} =\n{result}")
    except Exception as e:
        print(f"✗ Valid 2x2 multiplication failed: {e}")
        return False
    
    # Test 2: Valid multiplication (2x3 * 3x2)
    c = Matrix([[1, 2, 3], [4, 5, 6]])
    d = Matrix([[7, 8], [9, 10], [11, 12]])
    try:
        result = multiply(c, d)
        print("✓ Valid 2x3 * 3x2 multiplication successful")
        print(f"  {c} *\n{d} =\n{result}")
    except Exception as e:
        print(f"✗ Valid 2x3 * 3x2 multiplication failed: {e}")
        return False
    
    # Test 3: Invalid dimensions (2x2 * 3x2)
    e = Matrix([[1, 2], [3, 4], [5, 6]])
    try:
        result = multiply(a, e)  # 2x2 * 3x2 - should fail
        print("✗ Should not multiply incompatible matrices")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected invalid dimensions: {e}")
    
    # Test 4: None input
    try:
        result = multiply(a, None)
        print("✗ Should not multiply with None")
        return False
    except TypeError as e:
        print(f"✓ Correctly rejected None input: {e}")
    
    return True

def test_matrix_transpose():
    """Test matrix transposition."""
    print("\n=== Testing Matrix Transpose ===")
    
    # Test 1: 2x3 matrix
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    try:
        result = transpose(a)
        print("✓ Transpose successful")
        print(f"  Original (2x3):\n{a}")
        print(f"  Transposed (3x2):\n{result}")
    except Exception as e:
        print(f"✗ Transpose failed: {e}")
        return False
    
    # Test 2: None input
    try:
        result = transpose(None)
        print("✗ Should not transpose None")
        return False
    except TypeError as e:
        print(f"✓ Correctly rejected None input: {e}")
    
    return True

def main():
    """Run all tests."""
    tests = [
        ("Matrix Creation", test_matrix_creation),
        ("Matrix Addition", test_matrix_addition),
        ("Matrix Subtraction", test_matrix_subtraction),
        ("Matrix Multiplication", test_matrix_multiplication),
        ("Matrix Transpose", test_matrix_transpose)
    ]
    
    all_passed = True
    for name, test_func in tests:
        print(f"\n{' Starting: ' + name + ' ':=^80}")
        try:
            if not test_func():
                print(f"\n✗ {name} FAILED")
                all_passed = False
                continue
            print(f"\n✓ {name} PASSED")
        except Exception as e:
            print(f"\n✗ {name} CRASHED: {e}")
            all_passed = False
    
    print("\n" + "="*80)
    if all_passed:
        print(" ALL TESTS PASSED ".center(80, "="))
    else:
        print(" SOME TESTS FAILED ".center(80, "!"))
    print("="*80)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit(main())
