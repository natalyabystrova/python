import re
# email_address = """geek-brains@mail.ru"""
email = re.compile(r"""(?P<name>\-{0,}?\+{0,}?\'{0,}?\.{0,}?\w+?\+{0,}?\-
{0,}?\.{0,}?\'{0,}?\w+?)@
(?P<domain>\w+\.{0,}?\-{0,}?\w+)""", re.VERBOSE)                             #domain
def email_parse(email_address):
        rez = email.search(email_address)
        if not rez:
            raise ValueError("wrong email: 'email_address'")
        print(rez.groupdict())
        return rez.groupdict()
email_parse("geek.bra.ins@mail.ru")
    # print(rez.groupdict())rez.groupdict