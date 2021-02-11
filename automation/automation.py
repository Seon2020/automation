import re 

number_val = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
email_val = re.compile(r'[\w\.-]+@[\w\.-]+')

def read_file(file_path: str):
    with open(file_path, 'r') as f:
        content = f.read()
        return content

def find_phone_numbers(text):
    output = re.findall(number_val, text)
    full_list = []
    for i in output:
        if len(i) == 7 or len(i) == 8: i = '206' + i
        numbers_only = filter(str.isdigit, i)
        numbers_string = ''.join(numbers_only)
        proper_format = numbers_string[0:3] + '-' + numbers_string[3:6] + '-' + numbers_string[6:]
        if proper_format not in full_list: full_list.append(proper_format) 
    full_list.sort()
    return full_list

def find_emails(text):
    output = re.findall(email_val, text)
    full_list = [] 
    for i in output:
        if i not in full_list: full_list.append(i) 
    full_list.sort()
    return full_list

def write_content_to_file(arr: list, file_path: str):
    with open(file_path, 'w') as f:
        for i in arr:
            f.write(i + '\n')
        
if __name__ == '__main__':
    contents = read_file('../potential-contacts.txt')
    emails = find_emails(contents)
    numbers = find_phone_numbers(contents)
    # Below code verifies that my write content to file function works. 
    write_content_to_file(numbers, '../phone_numbers.txt')
    write_content_to_file(emails, '../emails.txt')