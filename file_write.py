def write_to_file(file_name, data):
    with open(file_name, 'w') as f:
        for line in data:
            f.write(line)

while True:
    latest_input = 1
    lines = []
    name = input("Enter file name: ")
    while latest_input:
        latest_input = input("Enter line, if none, write: ")
        if not latest_input == "":
            lines.append(latest_input)
        else:
            write_to_file(name, lines)
            print("File written.")
            break
