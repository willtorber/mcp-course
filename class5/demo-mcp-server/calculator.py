import math

class Calculator:
    """Basic Calculator with various math operations"""

    def format_result(self, a: float, operator: str, b: float, result: float) -> str:
        """Format the result of a calculation"""
        return f"{a:.2f} {operator} {b:.2f} = {result:.2f}"

    def add(self, a: float, b: float) -> str:
        """Adds two numbers"""
        result = a + b
        return self.format_result(a, "+", b, result)

    def subtract(self, a: float, b: float) -> str:
        """Subtract the second number from the first number"""
        result = a - b
        return self.format_result(a, "-", b, result)

    def multiply(self, a: float, b: float) -> str:
        """Multiply two numbers together"""
        result = a * b
        return self.format_result(a, "*", b, result)

    def divide(self, a: float, b: float) -> str:
        """Divide the first number by the second number"""
        if b == 0:
            return "Error: Cannot divide by zero"
        result = a / b
        return self.format_result(a, "/", b, result)

    def power(self, base: float, exponent: float) -> str:
        """Calculate the power of a number (base raised to an exponent)"""
        result = math.pow(base, exponent)
        return self.format_result(base, "^", exponent, result)

    def square_root(self, number: float) -> str:
        """Calculate the square root of a number"""
        if number < 0:
            return "Error: Cannot calculate square root of a negative number"
        result = math.sqrt(number)
        return f"√{number:.2f} = {result:.2f}"

    def modulus(self, a: float, b: float) -> str:
        """Calculate the remainder when one number is divided by another"""
        if b == 0:
            return "Error: Cannot divide by zero"
        result = a % b
        return self.format_result(a, "%", b, result)

    def absolute(self, number: float) -> str:
        """Calculate the absolute value of a number"""
        result = abs(number)
        return f"|{number:.2f}| = {result:.2f}"

    def help(self) -> str:
        """Get help about available calculator operations"""
        return (
            "Basic Calculator MCP Service\n\n"
            "Available operations:\n"
            "1. add(a, b) - Adds two numbers\n"
            "2. subtract(a, b) - Subtracts the second number from the first\n"
            "3. multiply(a, b) - Multiplies two numbers\n"
            "4. divide(a, b) - Divides the first number by the second\n"
            "5. power(base, exponent) - Raises a number to a power\n"
            "6. square_root(number) - Calculates the square root\n"
            "7. modulus(a, b) - Calculates the remainder of division\n"
            "8. absolute(number) - Calculates the absolute value\n\n"
            "Example usage: add(5, 3) will return 5 + 3 = 8"
        )
