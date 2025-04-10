def factorial(n):
    product = 1
    print(f"at the start product is {product}")
    while n > 0:
        n -= 1
        print(f"we multiply {product} by {n}")
        product *= n
        print(f"we get {product}")

    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")