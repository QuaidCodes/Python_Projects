
# Exception Handling

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
except ZeroDivisionError as e:      # e is the exception in the console, by convention called e
    print(e)
except ValueError as e:
    print(e)
except Exception as e:              # If no specific exceptions were triggered
    print(e)
else:                               # If none of the exception events were triggered
    print(numerator/denominator)
finally:                            # Will always execute, fail or pass the exception tests
    print("Always Executed")