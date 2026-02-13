class Calculator:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        """
        Multiply two intigers.
        
        Args:
            a (int): The first integer.
            b (int): the second integer.

        Returns:
            int: The product of a and b.
        """
        return a * b
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """
        Calculate sum of the given list of numbers

        Args:
            x (list): List of floating numbers

        Returns:
            float: The sum of numbers in the list x
        
        """

        return sum(x)
    
    @staticmethod
    def calculate_daily_expense(total: float, days: int) -> float:
        """
        Calculate daily expense.

        Args:
            total (float): Total cost.
            days (int): Total number of days.

        Returns:
            float: Single day expense. 
        """
        return total/days if days>0 else 0