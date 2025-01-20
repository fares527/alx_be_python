def safe_divide(numerator, denominator):
    try:
        numerator=float(numerator)
        denominator=float(denominator)
        return numerator/denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."


    