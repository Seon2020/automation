from automation.automation import find_phone_numbers, find_emails

test_string = 'This is a test that has emails like taco@taconation.com and crazycatlady@gmail.com! It also has phone numbers like 1234567891 and (425)234-7890 and 3459867 and 234-5832'

def test_phone_numbers():
    actual = find_phone_numbers(test_string)
    expected = ['123-456-7891', '206-234-5832', '206-345-9867', '425-234-7890']
    assert actual == expected

def test_emails():
    actual = find_emails(test_string)
    expected = ['crazycatlady@gmail.com', 'taco@taconation.com']
    assert actual == expected