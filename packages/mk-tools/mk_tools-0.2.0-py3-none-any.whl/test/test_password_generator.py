#!/usr/bin/env python3

import unittest
from mk_tools.src.password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    excluded = ["[", "]", "{", "}", "/", "\\", "<", ">", "=", "&"]

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_generate_pwd_length(self) -> None:
        pwd = PasswordGenerator.generate_pwd()
        self.assertEqual(len(pwd), 16)

        pwd_length = 10
        pwd = PasswordGenerator.generate_pwd(pwd_length=pwd_length)
        self.assertEqual(len(pwd), pwd_length)

        pwd_length = 1
        pwd = PasswordGenerator.generate_pwd(pwd_length=pwd_length)
        self.assertEqual(len(pwd), pwd_length)

        pwd_length = 100
        pwd = PasswordGenerator.generate_pwd(pwd_length=pwd_length)
        self.assertEqual(len(pwd), pwd_length)

    def test_generate_pwd_value_error(self) -> None:
        pwd_length = -1
        with self.assertRaises(ValueError):
            _ = PasswordGenerator.generate_pwd(pwd_length=pwd_length)

        pwd_length = 0
        with self.assertRaises(ValueError):
            _ = PasswordGenerator.generate_pwd(pwd_length=pwd_length)

    def test_generate_pwd_excluded_symbols(self) -> None:
        pwd = PasswordGenerator.generate_pwd()


if __name__ == "__main__":
    unittest.main()
