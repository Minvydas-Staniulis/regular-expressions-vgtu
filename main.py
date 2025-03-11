import re
#regular expression 1
phone_pattern = r"\+3706\d{7}"
test_input = "+37060079911"
if re.fullmatch(phone_pattern, test_input):
    print("Teisingas numeris")
else:
    print("Neteisingas numeris")

#regular expression 2
license_plate_pattern = r"^[A-Z]{3}\d{3}$"
test_input = "AAA111"
if re.fullmatch(license_plate_pattern, test_input.upper()):
    print("Teisingi VN")
else:
    print("Neteisingi VN")
#regular expression 3
person_code_pattern = r"^[1-6]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}\d$"
test_codes = [
    "39805231234",  # (1998-05-23)
    "50211251234",  # (2002-11-25)
    "69002251234",  # nera menesio 00
    "31230121234",  # nera vasario 31
    "79912311234",  # (1999-12-31)
    "12345678901",
]

for code in test_codes:
    if re.fullmatch(person_code_pattern, code):
        print(f"Teisingas: {code}")
    else:
        print(f"Neteisingas: {code}")