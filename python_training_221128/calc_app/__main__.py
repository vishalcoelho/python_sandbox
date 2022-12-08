# Exercise #4
# ===========
# Requirement 1. Break the project up into multiple modules such as one class
# per module or some related set of functions into a module.
#
# Requirement 2. Utilize three classes within the Calc App. The key part to
# this exercise is not the class syntax, but the applying of classes to
# existing code. Do the best you can with this. There is no "right" answer, and
# an extensive demo will follow with the instructor's suggested solution.

""" Module docstring"""

from calc_app.history import (
    History, Entry
)


def calc_app() -> None:
    """ calc_app function
    See google doc strings or sphinx"""
    _history = History()

    while True:
        valid_arithmetic_command = False
        recalc_result = False
        command = input("Enter a command: ")
        if ((command == "add") or (command == "subtract") or
            (command == "multiply") or (command == "divide") or
                (command == "exponent")):
            operand = float(input("Please enter an operand: "))

        match command:
            case 'add' | 'subtract' | 'multiply' | 'divide' | 'exponent':
                valid_arithmetic_command = True
                recalc_result = True
            case "clear":
                recalc_result = True
                _history.clear()
            case "history":
                _history.print()
            case "exit":
                break
            case "remove":
                entry_id = int(input("Entry ID? > "))
                _history.del_entry(entry_id)
                recalc_result = True
            case "load":
                file_name = input("Enter history file name >")
                _history.load(file_name)
                recalc_result = True
            case "save":
                file_name = input("Enter history file name >")
                _history.save(file_name)
            case _:
                print("Invalid Command")
        if valid_arithmetic_command:
            entry = Entry(command, operand)
            _history.add_entry(entry)
        if recalc_result:
            try:
                print(_history.calc_result())
            except Exception as e:
                print(e)


# __name__ will  have the name of the file (__main__) when directly invoked,
# but wont have the same name when imported as a module.
if __name__ == "__main__":
    calc_app()
