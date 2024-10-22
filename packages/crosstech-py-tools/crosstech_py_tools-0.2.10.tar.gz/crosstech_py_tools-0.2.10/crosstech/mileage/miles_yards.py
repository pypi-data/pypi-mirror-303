import math


YDS_TO_CHN = 0.0454545
YDS_TO_MIL = 0.000568182


class MilesYards:
    """
    A class to represent distance in miles, yards, and chains, from `miles.yards`.
    
    ------------------------------------------------------------------------------------------------
    
    Note:
    -----
    It takes yards to 4 decimal places. Hence, for example, input of `3.88` is `3` miles and `8800` yards.
    
    ------------------------------------------------------------------------------------------------

    Attributes
    ----------
    miles : int
        The integer part of the miles.
    chains : float
        The equivalent distance in chains.
    yards : float
        The fractional part of the miles converted to yards.
    miles_decimal : float
        The total distance in miles as a floating-point number.
    """

    def __str__(self):
        return f"Miles (float): {self.miles_decimal}, Miles (int): {self.miles}, Yards: {self.yards}, Chains: {self.chains}"

    def __init__(self, miles_yards: float):
        self.miles = 0
        self.chains = 0
        self.yards = 0
        self.miles_decimal = 0

        self._define_from_miles_yards(miles_yards)

    def _define_from_miles_yards(self, miles_yards: float) -> None:
        """
        Defines the attributes based on the given distance in miles and yards.

        Parameters
        ----------
        miles_yards : float
            The distance in miles.yards.

        Notes
        -----
        - The integer part of miles_yards is assigned to miles.
        - The fractional part of miles_yards is converted to yards.
        - The equivalent distance (of the yards part) is calculated in chain.
        - The total distance in miles as a floating-point number is computed.
        """
        if miles_yards < 0:
            self.miles = math.ceil(miles_yards)
        else:
            self.miles = math.floor(miles_yards)

        self.yards = (miles_yards - self.miles) * 10000
        self.chains = YDS_TO_CHN * self.yards
        self.miles_decimal = self.miles + self.yards * YDS_TO_MIL
