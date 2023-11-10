def write_file(file_name, file_content):
    with open(f"{file_name}.txt","w") as outfile:
        outfile.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as infile:
        infile.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as infile:
        return infile.read()
