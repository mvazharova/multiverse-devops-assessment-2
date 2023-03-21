import sys
from csvhelper import *


def main():
    # Ticket 1
    data_array = read_a_csv_file('results.csv')
    # Ticket 2
    data_deduplication = remove_duplicates(data_array)

if __name__ == '__main__':
    sys.exit(main())