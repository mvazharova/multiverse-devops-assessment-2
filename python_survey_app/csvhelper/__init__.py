import csv

def get_input(filename):
    data = []
    # f =  open(filename) # risky as we need to close it
    with open(filename) as f: # open(filename, 'r') r stands for read, w stands for write, a for append and could do a combination
        for line in f.readlines():
            # clean_line = line.strip()
            # line_list = clean_line.split(',')
            # data.append(line_list)
            data.append(line.strip().split(','))

# Ticket 1
def read_a_csv_file(filename):
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        return data
    
# Ticket 2
def remove_duplicates(data_array):
    unique_data = []
    seen = set()
    for row in data_array:
        if row[0] not in seen:
            unique_data.append(row)
            seen.add(row[0])
    return unique_data


# Ticket 3
def ignore_empty_lines(data_deduplication):
    new_list = []
    for line in data_deduplication:
        if line:
            is_empty = True
            for char in line:
                if char not in [' ','', '\t', '\n', '\r']:
                    is_empty = False
                    break
            if not is_empty:
                new_list.append(line)

    return new_list

#Ticket 4
def capitalise_name_fields(data_without_empty_lines):
    capitalized_data = [[row[0], row[1].capitalize(), row[2].capitalize()] + row[3:] for row in data_without_empty_lines]
    return capitalized_data

# Ticket 5
def validate_ans3(data_capitalisation):
    new_list = []

    for row in data_capitalisation:
        # check if the value in the 5th index column is a valid integer string
        if row[5].isdigit() and 1 <= int(row[5]) <= 10:
            new_list.append(row)

    return new_list