#!/usr/bin/env python3
"""
Verify that the alumathpeergroup10 package works correctly.
"""

def test_imports():
    """Test that all required imports work."""
    try:
        from alumathpeergroup10 import Matrix, multiply, add, subtract, transpose
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_multiplication():
    """Test matrix multiplication with valid and invalid inputs."""
    from alumathpeergroup10 import Matrix, multiply
    
    print("\nTesting valid multiplication (2x2 × 2x2):")
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    
    print("Matrix A:")
    print(a)
    print("\nMatrix B:")
    print(b)
    
    try:
        result = multiply(a, b)
        print("\nResult of A × B:")
        print(result)
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False
    
    print("\nTesting invalid multiplication (1x2 × 3x2):")
    c = Matrix([[1, 2]])
    d = Matrix([[1, 2], [3, 4], [5, 6]])
    
    print("\nMatrix C:")
    print(c)
    print("\nMatrix D:")
    print(d)
    
    try:
        result2 = multiply(c, d)
        print("✗ Expected error but got result:", result2)
        return False
    except ValueError as e:
        print("\n✓ Caught expected error:")
        print(f"   {e}")
        
        # Verify the error message format
        if "Peer Group 10 says:" in str(e):
            print("✓ Error message includes required prefix")
        else:
            print("✗ Error message is missing required prefix")
            return False
    
    return True

def main():
    """Run all tests."""
    print("=== Testing alumathpeergroup10 Package ===\n")
    
    # Test 1: Verify imports
    print("1. Testing imports...")
    if not test_imports():
        return 1
    
    # Test 2: Verify multiplication
    print("\n2. Testing matrix multiplication...")
    if not test_multiplication():
        return 1
    
    print("\n=== All tests passed successfully! ===")
    return 0

if __name__ == "__main__":
    exit(main())
