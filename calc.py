def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    # TODO: implement subtraction
    if operator == "-"
        return num1-num2
    # TODO: implement multiplication
    if operator == "*"
        return num1*num2
    # TODO: implement division
    if operator == "/"
        return num1/num2
    else:
        return None


if __name__ == "__main__":
    # ask user for input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # ask user for operator
    operator = input("Enter operator (+, -, *, /): ")

    # calculate result
    result = calculate(num1, operator, num2)

    if result is None:
        print("Invalid operator")
    else:
        # print result
        print(num1, operator, num2, "=", result)
