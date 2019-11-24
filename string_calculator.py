import re
import logging
import time
"""
Copyright: @2019
Author: Zweli Mthethwa
"""
# create and configure logger
logging.basicConfig(filename = "logs/string_calculator.log", level=logging.DEBUG, format="%(asctime)s %(message)s")
logger = logging.getLogger()

class StringCalculator():
    """This class has functions that do basic mathematics operations on numbers"""
    # constructor for the string calculator object
    def __init__(self):
        pass
    def add(self, numbers):
        """
        Calculates the sum of all the numbers in string 'numbers'. Numbers bigger than 1000 are ignored
        when calculating the sum. Throws an exception if any of the numbers in string 'numbers' is negative.

        Parameters:
        numbers (str): the string with numbers separated by commas or any delimiter

        Returns:
        int: the sum of all numbers in string 'numbers'
        """

        if len(numbers) == 0:
            return 0
        else:
            string_values = re.findall(r"\d+|-\d+", numbers)
            print(string_values)
            total = 0
            negatives = []
            for i in range(len(string_values)):
                if int(string_values[i]) < 0:
                    logger.info("A negative number: " + string_values[i] + " was found")
                    negatives.append(string_values[i])
                    continue
                if int(string_values[i]) <= 1000:
                    total += int(string_values[i])
            if len(negatives) == 0:
                return total
            else:
                negative_values_string = ""
                for i in range(len(negatives)):
                    if i != len(negatives)-1:
                        negative_values_string += negatives[i]+","
                    else:
                        negative_values_string += negatives[i]
                raise Exception("negatives not allowed "+negative_values_string)


def main():
    calculator = StringCalculator()
    print(calculator.add("//;\n-31;-2"))
if __name__ == '__main__':
    main()
