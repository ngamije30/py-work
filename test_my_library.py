#!/usr/bin/env python3
"""
Test script for alumathpeergroup10 library
"""

def test_basic_functionality():
    """Test basic matrix operations"""
    print("🧪 Testing alumathpeergroup10 library...")
    
    try:
        from alumathpeergroup10 import Matrix, multiply, add, subtract, transpose
        print("✓ Import successful")
        
        # Test 1: Basic matrix creation
        print("\n📋 Test 1: Matrix Creation")
        a = Matrix([[1, 2], [3, 4]])
        print(f"Matrix A shape: {a.shape}")
        print(f"Matrix A:\n{a}")
        
        # Test 2: Matrix multiplication (2x2 × 2x2)
        print("\n🔢 Test 2: Matrix Multiplication (2x2 × 2x2)")
        b = Matrix([[5, 6], [7, 8]])
        result = multiply(a, b)
        print(f"A × B result:\n{result}")
        print(f"Expected: [[19, 22], [43, 50]]")
        
        # Test 3: Different dimensions (1x3 × 3x1)
        print("\n🔢 Test 3: Different Dimensions (1x3 × 3x1)")
        c = Matrix([[1, 2, 3]])
        d = Matrix([[4], [5], [6]])
        result2 = multiply(c, d)
        print(f"C × D result:\n{result2}")
        print(f"Expected: [[32]]")
        
        # Test 4: Matrix addition
        print("\n➕ Test 4: Matrix Addition")
        e = Matrix([[1, 1], [1, 1]])
        f = Matrix([[2, 2], [2, 2]])
        result3 = add(e, f)
        print(f"E + F result:\n{result3}")
        print(f"Expected: [[3, 3], [3, 3]]")
        
        # Test 5: Matrix transpose
        print("\n🔄 Test 5: Matrix Transpose")
        g = Matrix([[1, 2, 3], [4, 5, 6]])
        result4 = transpose(g)
        print(f"G transpose:\n{result4}")
        print(f"Expected: [[1, 4], [2, 5], [3, 6]]")
        
        print("\n✅ All basic tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_error_handling():
    """Test error handling"""
    print("\n🚨 Testing Error Handling...")
    
    try:
        from alumathpeergroup10 import Matrix, multiply
        
        # Test invalid multiplication dimensions
        print("\n📐 Test: Invalid Multiplication Dimensions")
        try:
            a = Matrix([[1, 2]])  # 1x2
            b = Matrix([[1, 2], [3, 4], [5, 6]])  # 3x2
            result = multiply(a, b)  # Should fail
            print("❌ Error: This should have failed!")
        except ValueError as e:
            print(f"✓ Caught expected error: {e}")
        
        # Test invalid matrix creation
        print("\n📐 Test: Invalid Matrix Creation")
        try:
            invalid_matrix = Matrix([[1, 2], [3]])  # Irregular shape
            print("❌ Error: This should have failed!")
        except ValueError as e:
            print(f"✓ Caught expected error: {e}")
            
        print("\n✅ Error handling tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def performance_test():
    """Basic performance test"""
    print("\n⚡ Performance Test...")
    
    try:
        from alumathpeergroup10 import Matrix, multiply
        import time
        
        # Create larger matrices
        size = 50
        data_a = [[i + j for j in range(size)] for i in range(size)]
        data_b = [[i * j + 1 for j in range(size)] for i in range(size)]
        
        a = Matrix(data_a)
        b = Matrix(data_b)
        
        start_time = time.time()
        result = multiply(a, b)
        end_time = time.time()
        
        print(f"✓ Multiplied {size}x{size} matrices in {end_time - start_time:.4f} seconds")
        print(f"✓ Result shape: {result.shape}")
        
        return True
        
    except Exception as e:
        print(f"❌ Performance test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting alumathpeergroup10 Library Tests")
    print("=" * 50)
    
    # Run all tests
    tests_passed = 0
    total_tests = 3
    
    if test_basic_functionality():
        tests_passed += 1
    
    if test_error_handling():
        tests_passed += 1
        
    if performance_test():
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Your library is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
