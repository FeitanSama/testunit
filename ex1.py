# Adds :
# - self in parameters of all functions
# - check if x or x and y are instance of numbers
# - error message if x or x and y are not instance of numbers
# - add documenation
# - delete 'tests' function in the end of script

class Calculator:

    """ A class used to Calculate

    Parameters
    __________

    None

    Methods
    __________

    add(x,y)
        add 2 numbers

    subtract(x, y)
        subtract 2 numbers
    
    multiply(x, y)
        multiply 2 numbers

    divide(x, y)
        divide 2 numbers
    
    power(x, y)
        power x by y

    square_root(x)
        return square root of x
    
    """

    def add(self,x, y):

        """ Function for add 2 numbers (int or/and float)
        
        Parameters 
        __________

        x : int / float 
            first number
        y : int / float
            second number

        Returns
        __________

        x + y : int / float
            addition of x and y

        Raises
        __________

        Invalid input: both arguments must be numbers.
            if x or y are not instance of numbers (int or float)

        Invalid input: two arguments are required.
            if x or y are missing
        """

        try:
            if len([x, y]) != 2:
                raise TypeError("Invalid input: two arguments are required.")

            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Invalid input: both arguments must be numbers.")

            return x + y

        except TypeError as error:

            return str(error)

    def subtract(self,x, y):

        """ Function for subtract 2 numbers (int or/and float)
        
        Parameters 
        __________

        x : int / float 
            first number
        y : int / float
            second number

        Returns
        __________

        x - y : int / float
            subtract of x and y

        Raises
        __________

        Invalid input: both arguments must be numbers.
            if x or y are not instance of numbers (int or float)

        Invalid input: two arguments are required.
            if x or y are missing
        """
        try:
            if len([x, y]) != 2:
                raise TypeError("Invalid input: two arguments are required.")

            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Invalid input: both arguments must be numbers.")

            return x - y

        except TypeError as error:

            return str(error)
    
    def multiply(self,x, y):

        """ Function for multiply 2 numbers (int or/and float)
        
        Parameters 
        __________

        x : int / float 
            first number
        y : int / float
            second number

        Returns
        __________

        x * y : int / float
            multiplication of x and y

        Raises
        __________

        Invalid input: both arguments must be numbers.
            if x or y are not instance of numbers (int or float)

        Invalid input: two arguments are required.
            if x or y are missing
        """

        try:
            if len([x, y]) != 2:
                raise TypeError("Invalid input: two arguments are required.")

            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Invalid input: both arguments must be numbers.")

            return x * y

        except TypeError as error:

            return str(error)
    
    def divide(self,x, y):

        """ Function for divide 2 numbers (int or/and float)
        
        Parameters 
        __________

        x : int / float 
            first number
        y : int / float
            second number

        Returns
        __________

        x / y : int / float
            division of x by y

        Raises
        __________

        TypeError - Invalid input: both arguments must be numbers.
            if x or y are not instance of numbers (int or float)

        TypeError - Invalid input: two arguments are required.
            if x or y are missing

        ZeroDivisionError - Invalid input: division by zero.
            Impossible to divide a number by zero

        """
        try:
            
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Invalid input: both arguments must be numbers.")

            if len([x, y]) != 2:
                raise TypeError("Invalid input: two arguments are required.")

            if y == 0:
                raise ZeroDivisionError("Invalid input: division by zero.")

            return x / y

        except (ZeroDivisionError, TypeError) as error:

            return str(error)
    
    def power(self,x, y):

        """ Function for power 2 numbers (int or/and float)
        
        Parameters 
        __________

        x : int / float 
            first number
        y : int / float
            second number

        Returns
        __________

        result = x ** y : int / float
            power of x by y

        Raises
        __________

        Invalid input: both arguments must be numbers.
            if x or y are not instance of numbers (int or float)

        Invalid input: two arguments are required.
            if x or y are missing
        """
        try:
            if len([x, y]) != 2:
                raise TypeError("Invalid input: two arguments are required.")

            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Invalid input: both arguments must be numbers.")
                
            return x**y

        except TypeError as error:
            return str(error)
        

    def square_root(self,x,y=None):
        """ Function for square_root a number (int or float)
        
        Parameters 
        __________

        x : int / float 
            number to square_root

        Returns
        __________

        val = sqrt(x) : int / float
            power of x by y

        Raises
        __________

        Invalid input: both arguments must be numbers.
            if x is not instance of numbers (int or float)

        Invalid input: one arguments are required.
            if x is missing

        ZeroDivisionError - Invalid input: division by zero.
            Impossible to divide a number by zero
        """
        try:

            if len([x]) != 1:
                raise TypeError("Invalid input: two arguments are required.")

            if not isinstance(x, (int, float)):
                raise TypeError("Invalid input: both arguments must be numbers.")
                
            try:
                if x == 0 or x == 1:
                    return x
                val = x
                precision = 0.0000001
                while abs(val - x / val) > precision:
                    val = (val + x / val) / 2
                return val
            except:
                raise ZeroDivisionError("Invalid input: division by zero.")

        except (ZeroDivisionError,TypeError) as error:
            return str(error)
