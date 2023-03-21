import sys
from csvhelper import *


def main():
    # Ticket 1
    data_array = read_a_csv_file('results.csv')
    # Ticket 2
    data_deduplication = remove_duplicates(data_array)
    # Ticket 3
    data_without_empty_lines = ignore_empty_lines(data_deduplication)

if __name__ == '__main__':
    sys.exit(main())