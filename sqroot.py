def sqrt(x):
    if x == 0:
        return 0
    
    guess = x
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    
    return guess

# Example usage
print(sqrt(4))  # Output: 2
print(sqrt(8))  # Output: 2
