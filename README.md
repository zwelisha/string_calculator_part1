This is an implementation of the String Calculator taking into consideration the following instructions:

1. Create a simple String caclulator with a method signature
int Add(string numbers), however since this is python I opted for add(numbers)

The method can take up to two numbers, separated by commas, and will return their sum.
for an example "" or "1" or "1,2" as inputs.

for an empty string it will return 0

- Start with the simplest test case of an empty string and move to one and two numbers
simple as possible so that you force yourself to write tests you did not think about.

- Remember to refector after each passing test

2. Allow the method to handle an unknown amount of numbers

3. Allow the Add method to handle new lines between numbers (instead of commas)
        1. the following input is ok:
        "1\n2,3" (will equal 6)
        2. the following input is NOT ok:
        "1,\n"

4. Support different delimiters
        1. to change a delimiter, the beginning of the string will contain separate line that looks like this:
        “//[delimiter]\n[numbers...]” for example “//;\n1;2” should return three where the default delimiter is ';'.
        2. the first line is optional. All existing scenarios should still be supported.

5. Calling Add with a negative number will throw an exception "negatives not allowed" - and the negative that was passed.
  If there are multiple negatives show all of them in the exception message.
  STOP HERE if you are a beginner. Continue if you can finish the steps so far in less than 30 minutes.

6. Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2

7. Delimiters can be of any length with the following format:
“//[delimiter]\n” for example: "//[***]\n1***2***3" should return 6


8. Allow multiple delimeters like this:
    "//[delim1][delim2]\n" for example:
    "//[*][%]\n1*2%3" should return 6

9. Make sure you can also handle multiple delimiters with length longer than one character
