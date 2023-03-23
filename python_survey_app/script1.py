import sys
from csvhelper import *


def main():
    # Ticket 1
    data_array = read_a_csv_file('results.csv')
    # Ticket 2
    data_deduplication = remove_duplicates(data_array)
    # Ticket 3
    data_without_empty_lines = ignore_empty_lines(data_deduplication)
    # Ticket 4
    data_capitalisation = capitalise_name_fields(data_without_empty_lines)
    # Ticket 5
    data_validate_ans3 = validate_ans3(data_capitalisation)
    # Ticket 6
    write_clean_data(data_validate_ans3, 'clean_results.csv')

if __name__ == '__main__':
    sys.exit(main())