import re

# email_address = """geek-brains@mail.ru"""
email = re.compile(r"""(?P<name>\-{0,}?\+{0,}?\'{0,}?\.{0,}?\w+?\+{0,}?\-
{0,}?\.{0,}?\'{0,}?\w+?)@
(?P<domain>\w+\.{0,}?\-{0,}?\w+)""", re.VERBOSE)


def email_parse(email_address):
    res = email.search(email_address)
    if not res:
        raise ValueError("wrong email: 'email_address'")
    print(res.groupdict())
    return res.groupdict()


email_parse("geekbra.ins@mail.ru")
