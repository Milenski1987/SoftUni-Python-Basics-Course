number_one = int(input())
number_two = int(input())
operator = input()

result = 0
even_odd = ""

if operator == "+":
    result = number_one + number_two
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operator == "-":
    result = number_one - number_two
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operator == "*":
    result = number_one * number_two
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operator == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
elif operator == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two

if operator == "+" or operator == "-" or operator == "*":
    print(f"{number_one} {operator} {number_two} = {result} - {even_odd}")
elif operator == "/" and number_two != 0:
    print(f"{number_one} / {number_two} = {result:.2f}")
elif operator == "%" and number_two != 0:
    print(f"{number_one} % {number_two} = {result}")


