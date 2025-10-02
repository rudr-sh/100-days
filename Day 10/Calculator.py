restart = ""
while restart != "exit":
    if restart == "n" or restart == "":
        f_num = float(input("What is the first number: "))
    else:
        f_num = answer
    operation = input(f"+\n-\n*\n/\nWhat operation do you want to use: ")
    n_num = float(input("What is the next number: "))
    def addition(n1,n2):
        return n1 + n2
    def subtraction(n1,n2):
        return n1 - n2
    def multiplication(n1,n2):
        return n1 * n2
    def division(n1,n2):
        return n1 / n2

    operators = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division,
    }
    answer = (operators[operation](f_num,n_num))
    print(f"{f_num} {operation} {n_num} = {answer}")
    restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'exit' to exit calculator.").lower()
