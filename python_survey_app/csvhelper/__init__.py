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