from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


min_length = 4
valid_domains = (".com", ".bg", ".net", ".org")

name_pattern = r'\w+'
domain_pattern = r'\.[a-z]+'

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")
    if len(email.split("@")[0]) < min_length:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if findall(name_pattern, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name can contain only letters, digits and underscores!")
    if findall(domain_pattern, email)[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
