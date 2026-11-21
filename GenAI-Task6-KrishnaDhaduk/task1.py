
try:
    numerator = int(input("Enter Numeretor Value"))
    denominator = int(input("Enter Denominator Value."))
    result = numerator / denominator
except ValueError as ve:
    print("Input value not numeric.")
except ZeroDivisionError as zde:
    print("0 is not value to divite with.")
else:
    print(f"Result value is {result}")
finally:
    print("Operation Complete")