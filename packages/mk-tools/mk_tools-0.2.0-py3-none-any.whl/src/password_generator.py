#!/usr/bin/env python3

import secrets
import string


class PasswordGenerator(object):

    @classmethod
    def __exclude(cls) -> str:
        exclude_this = ["[", "]", "{", "}", "/", "\\", "<", ">", "=", "&"]
        specials = string.punctuation

        return "".join(s2 for s2 in [s for s in specials if s not in exclude_this])

    @classmethod
    def __get_alphabet(cls, exclude_some: bool = False) -> str:
        if exclude_some:
            return string.ascii_letters + string.digits + cls.__exclude()
        return string.ascii_letters + string.digits + string.punctuation

    @classmethod
    def generate_pwd(cls, pwd_length: int = 16, exclude_some: bool = False) -> str:
        if pwd_length < 1:
            raise ValueError("pwd_length must be greater than or equal to 1")
        pwd = ""
        alphabet = cls.__get_alphabet(exclude_some=exclude_some)
        for i in range(pwd_length):
            pwd += "".join(secrets.choice(alphabet))

        return pwd
