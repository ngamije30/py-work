#!/usr/bin/env python3
"""
Demo script for alumathpeergroup10 matrix operations.
Shows usage of matrix operations with different dimensions and error handling.
"""

def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f" {title} ".center(60, "="))
    print("=" * 60)

def demo_matrix_creation():
    """Demonstrate creating matrices of different sizes."""
    from alumathpeergroup10 import Matrix
    
    print_header("1. Creating Matrices")
    
    # 2x2 matrix
    a = Matrix([[1, 2], [3, 4]])
    print("Matrix A (2x2):")
    print(a)
    
    # 2x3 matrix
    b = Matrix([[1, 2, 3], [4, 5, 6]])
    print("\nMatrix B (2x3):")
    print(b)
    
    # 3x2 matrix
    c = Matrix([[1, 2], [3, 4], [5, 6]])
    print("\nMatrix C (3x2):")
    print(c)
    
    return a, b, c

def demo_multiplication():
    """Demonstrate matrix multiplication."""
    from alumathpeergroup10 import Matrix, multiply
    
    print_header("2. Matrix Multiplication (Valid)")
    
    # 2x3 × 3x2 = 2x2
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[7, 8], [9, 10], [11, 12]])
    
    print("Matrix A (2x3):")
    print(a)
    print("\nMatrix B (3x2):")
    print(b)
    
    result = multiply(a, b)
    print("\nA × B (2x2):")
    print(result)

def demo_multiplication_errors():
    """Demonstrate error handling in matrix multiplication."""
    from alumathpeergroup10 import Matrix, multiply
    
    print_header("3. Matrix Multiplication (Errors)")
    
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print("Matrix A (2x2):")
    print(a)
    print("\nMatrix B (3x3):")
    print(b)
    
    print("\nAttempting A × B (Invalid dimensions):")
    try:
        result = multiply(a, b)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

def demo_add_subtract():
    """Demonstrate matrix addition and subtraction."""
    from alumathpeergroup10 import Matrix, add, subtract
    
    print_header("4. Matrix Addition & Subtraction")
    
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[4, 3], [2, 1]])
    
    print("Matrix A:")
    print(a)
    print("\nMatrix B:")
    print(b)
    
    # Addition
    print("\nA + B:")
    print(add(a, b))
    
    # Subtraction
    print("\nA - B:")
    print(subtract(a, b))

def demo_transpose():
    """Demonstrate matrix transposition."""
    from alumathpeergroup10 import Matrix, transpose
    
    print_header("5. Matrix Transpose")
    
    # Original matrix
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    print("Original Matrix (2x3):")
    print(a)
    
    # Transposed
    print("\nTransposed (3x2):")
    print(transpose(a))

def main():
    """Run all demos."""
    # Create sample matrices
    a, b, c = demo_matrix_creation()
    
    # Demo operations
    demo_multiplication()
    demo_multiplication_errors()
    demo_add_subtract()
    demo_transpose()
    
    print("\n" + "=" * 60)
    print(" Demo Completed Successfully ".center(60, "="))
    print("=" * 60)

if __name__ == "__main__":
    main()
