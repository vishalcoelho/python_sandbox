"""
docstring
"""
import re
from typing import Generator
from calc_app import arithmetic

import os
import re

# Notes
# 1. use _ for private data members, OR
# 2. use __ for private data members to mangle the names of private data, class
# methods can use the unmangled name but every thing outside needs the
# mangled name
# 3. def get_private_data(self):
#        ret private_data <-------this is not a copy of the private data but a
#                                 reference to your internal data
#    use ret private_data.copy() or,
#        ret [entry for entry in private_data] list comprehension
#
#  4. copy is a shallow copy, it returns the list of references, so someone can
#  manipulate the underlying data, you can use deepcopy() for a full and proper
#  copy.
#
# 5. for multiple inheritance, use className.__mro__ to find the method
# resolution order
#
# 6. class Worker(Person):
#       def __init__(self):
#             super().__init__() --> can be problematic for multi-inheritance
#             Person.__init__(self)  --> this is better
#
# 7. Class methods: not bound to an instance of the class
# akin to a static method for other languages
# class Person:
#     def __init__(self):
#         ...
#
#     @classmethod
#     def create(cls, full_name: str) -> Person: ---->  from __future__ import annotations will let you use the type hint
#         name_parts = full_name.split(" ")          >  without complaining about an unknown type
#         return Person(name_parts[0], name_parts[1])
#
# person = Person.create("Bob Smith")
# Allows me to call a class method without a class instance
#
# 8. static method for a class requires a class instance, but cant access the
#    innards of a class
# class Person:
#     @staticmethod
#         def print():
#         print(f"hello")
# static methods are available to the class as well
# Person.print() or person = Person() then person.print()


def gen_unique_id() -> Generator[int, None, None]:
    """ Generator for unique id"""
    unique_id = 0
    while True:
        unique_id += 1
        yield unique_id


unique_id_gen = gen_unique_id()


class Entry:
    """A history entry"""

    def __init__(self, op_name: str, op_operand: float) -> None:
        global unique_id_gen
        self.op_name = op_name
        self.op_operand = op_operand
        self.id = next(unique_id_gen)

    @classmethod
    def parse(cls, line: str) -> {int, str, float}:
        entry_match = re.search(
            r"\('id: (\.*?)', 'Operation: (.*?)', 'Operand: (.*?)'\)", line)
        op_id = int(entry_match.group(1))
        op_name = entry_match.group(2)
        op_operand = float(entry_match.group(1))

        return {'id': op_id, 'Operation': op_name, 'Operand': op_operand}

    def __str__(self) -> str:
        return f"('id: {self.id}', 'Operation: {self.op_name}', 'Operand: {self.op_operand}')"

    def print(self) -> None:
        """print"""
        print((
            f"id: {self.id}",
            f"Operation: {self.op_name}",
            f"Operand: {self.op_operand}",
        ))


class History:
    """
    Implements the history module with the ability to add and delete entries,
    clear and print out the entire history.
    """

    def __init__(self) -> None:
        self.history: list[Entry] = []
        self.arithmetic = arithmetic.Arithmetic()

    @staticmethod
    def get_abs_path(file_name: str) -> str:
        """ Get absolute file path """
        return os.path.join(os.path.dirname(__file__), file_name)

    def add_entry(self, entry: Entry) -> None:
        """Add an entry to the history"""
        self.history.append(entry)

    def del_entry(self, entry_id: int) -> None:
        """Delete an entry from the history"""
        for entry in self.history:
            if entry.id == entry_id:
                self.history.remove(entry)
                break

    def print(self) -> None:
        if len(self.history) == 0:
            print("[]")
        else:
            for entry in self.history:
                entry.print()

    def clear(self) -> None:
        """ Clears the history"""
        self.history = []

    def calc_result(self) -> float:
        """ Calculate result from history"""
        self.arithmetic.clear()
        for entry in self.history:
            self.arithmetic.calculate(entry.op_name, entry.op_operand)
        return self.arithmetic.result

    def load(self, file_name: str) -> None:
        """ Load history from a file"""
        file_path = self.get_abs_path(file_name)
        try:
            with open(file_path, "r", encoding="UTF-8") as history_file:
                for line in history_file:
                    self.history.append(Entry.parse(line))
                self.history = [entry for entry in history_file]
        except IOError as exc:
            print(exc)
            self.history = []

    def save(self, file_name: str) -> None:
        """Save history to a file"""
        file_path = self.get_abs_path(file_name)
        print(f"saving to {file_path}")
        with open(file_path, "w", encoding="UTF-8") as history_file:
            for entry in self.history:
                history_file.write(entry.__str__() + "\n")
