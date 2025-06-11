#!/usr/bin/env python3
"""
Step-by-step testing for alumathpeergroup10 package.
Follows the order of operations with clear error handling.
"""

def print_step(step_num, title):
    """Print a formatted step header."""
    print(f"\n{'='*80}")
    print(f"STEP {step_num}: {title}".center(80))
    print(f"{'='*80}")

def test_matrix_creation():
    """Step 1: Test matrix creation with various inputs."""
    from alumathpeergroup10 import Matrix
    
    print_step(1, "Testing Matrix Creation")
    
    # Test 1.1: Valid matrix
    try:
        print("Test 1.1: Valid 2x2 matrix")
        m = Matrix([[1, 2], [3, 4]])
        print(f"✓ Created matrix: {m}")
    except Exception as e:
        print(f"✗ Failed to create valid matrix: {e}")
        return False
    
    # Test 1.2: Empty matrix
    print("\nTest 1.2: Empty matrix")
    try:
        m = Matrix([])
        print(f"✗ Should not create empty matrix: {m}")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected empty matrix: {e}")
    
    # Test 1.3: Non-rectangular matrix
    print("\nTest 1.3: Non-rectangular matrix")
    try:
        m = Matrix([[1, 2], [3]])
        print(f"✗ Should not create non-rectangular matrix: {m}")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected non-rectangular matrix: {e}")
    
    # Test 1.4: Invalid data type
    print("\nTest 1.4: Invalid data type")
    try:
        m = Matrix([[1, 2], [3, 'a']])
        print(f"✗ Should not create matrix with non-numeric data: {m}")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected invalid data type: {e}")
    
    return True

def test_matrix_operations():
    """Step 2: Test basic matrix operations."""
    from alumathpeergroup10 import Matrix, add, subtract, transpose
    
    print_step(2, "Testing Basic Matrix Operations")
    
    # Setup test matrices
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    
    # Test 2.1: Matrix addition
    try:
        print("Test 2.1: Matrix addition")
        result = add(a, b)
        print(f"✓ Addition successful: {result}")
    except Exception as e:
        print(f"✗ Addition failed: {e}")
        return False
    
    # Test 2.2: Matrix subtraction
    try:
        print("\nTest 2.2: Matrix subtraction")
        result = subtract(a, b)
        print(f"✓ Subtraction successful: {result}")
    except Exception as e:
        print(f"✗ Subtraction failed: {e}")
        return False
    
    # Test 2.3: Matrix transpose
    try:
        print("\nTest 2.3: Matrix transpose")
        result = transpose(a)
        print(f"✓ Transpose successful: {result}")
    except Exception as e:
        print(f"✗ Transpose failed: {e}")
        return False
    
    # Test 2.4: Dimension mismatch in addition
    print("\nTest 2.4: Addition with dimension mismatch")
    try:
        c = Matrix([[1, 2, 3]])
        result = add(a, c)
        print(f"✗ Should not add matrices of different sizes: {result}")
        return False
    except ValueError as e:
        print(f"✓ Correctly rejected addition with different sizes: {e}")
    
    return True

def test_matrix_multiplication():
    """Step 3: Test matrix multiplication."""
    from alumathpeergroup10 import Matrix, multiply
    
    print_step(3, "Testing Matrix Multiplication")
    
    # Test 3.1: Valid multiplication (2x2 × 2x2)
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    
    try:
        print("Test 3.1: Valid 2x2 multiplication")
        result = multiply(a, b)
        print(f"✓ Multiplication successful: {result}")
    except Exception as e:
        print(f"✗ Multiplication failed: {e}")
        return False
    
    # Test 3.2: Valid multiplication (2x3 × 3x2)
    c = Matrix([[1, 2, 3], [4, 5, 6]])
    d = Matrix([[7, 8], [9, 10], [11, 12]])
    
    try:
        print("\nTest 3.2: Valid 2x3 × 3x2 multiplication")
        result = multiply(c, d)
        print(f"✓ Multiplication successful: {result}")
    except Exception as e:
        print(f"✗ Multiplication failed: {e}")
        return False
    
    # Test 3.3: Invalid dimensions (2x2 × 2x3)
    print("\nTest 3.3: Invalid dimensions (2x2 × 2x3)")
    e = Matrix([[1, 2, 3], [4, 5, 6]])  # 2x3 matrix
    try:
        result = multiply(a, e)  # a is 2x2, e is 2x3 - should fail
        print(f"✗ Should not multiply incompatible matrices: {result}")
        return False
    except ValueError as e:
        expected_msg = "columns of first matrix (2) must equal rows of second matrix (2)"
        if expected_msg in str(e):
            print(f"✓ Correctly rejected invalid dimensions: {e}")
        else:
            print(f"✗ Wrong error message for dimension mismatch: {e}")
            return False
    
    return True

def test_edge_cases():
    """Step 4: Test edge cases and error handling."""
    from alumathpeergroup10 import Matrix, multiply, add, subtract
    
    print_step(4, "Testing Edge Cases")
    
    # Test 4.1: None input
    print("Test 4.1: None input")
    try:
        m = Matrix(None)
        print(f"✗ Should not create matrix from None: {m}")
        return False
    except TypeError as e:
        print(f"✓ Correctly rejected None input: {e}")
    
    # Test 4.2: Single element matrix
    try:
        print("\nTest 4.2: Single element matrix")
        m = Matrix([[42]])
        print(f"✓ Created single-element matrix: {m}")
    except Exception as e:
        print(f"✗ Failed to create single-element matrix: {e}")
        return False
    
    # Test 4.3: Large matrix
    try:
        print("\nTest 4.3: Large matrix (100x100)")
        size = 100
        large = Matrix([[i + j for j in range(size)] for i in range(size)])
        print(f"✓ Created {size}x{size} matrix")
    except Exception as e:
        print(f"✗ Failed to create large matrix: {e}")
        return False
    
    return True

def main():
    """Run all test steps in order."""
    print("="*80)
    print(" MATRIX OPERATIONS TEST SUITE ".center(80, "="))
    print("="*80)
    
    steps = [
        ("Matrix Creation", test_matrix_creation),
        ("Basic Operations", test_matrix_operations),
        ("Matrix Multiplication", test_matrix_multiplication),
        ("Edge Cases", test_edge_cases)
    ]
    
    all_passed = True
    for name, test_func in steps:
        print(f"\n{' STARTING: ' + name + ' ':-^80}")
        try:
            if not test_func():
                print(f"\n✗ {name} FAILED")
                all_passed = False
                break
            print(f"\n✓ {name} PASSED")
        except Exception as e:
            print(f"\n✗ {name} CRASHED: {e}")
            all_passed = False
            break
    
    print("\n" + "="*80)
    if all_passed:
        print(" ALL TESTS PASSED ".center(80, "="))
    else:
        print(" TEST FAILED ".center(80, "!"))
    print("="*80)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit(main())
