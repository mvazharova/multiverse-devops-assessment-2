from csvhelper import * 
from pathlib import Path
import os
import pytest

filename = "results.csv"

########################################
############### Ticket 1 ###############
########################################

# Test 1 - Test case to check the file exists 
def test_file_exists():
    file_exists = Path(filename).is_file()
    assert file_exists == True

# Test 2 - Test case for FileNotFoundError when a file that doesn't exist is provided
def test_read_a_csv_file_nonexistent_file():
    # Arrange
    filename_nonexisting = 'nonexistent_file.csv'
    if os.path.exists(filename_nonexisting):
        os.remove(filename_nonexisting)

    # Act and Assert
    with pytest.raises(FileNotFoundError):
        result = read_a_csv_file(filename_nonexisting)

# Test 3 - Test case for producing empty list when an empty file is passed to the function
def test_read_a_csv_file_empty_file():
    # Arrange
    filename_empty = 'empty_file.csv'
    with open(filename_empty, 'w') as csvfile:
        pass

    expected_output = []

    # Act
    actual_output = read_a_csv_file(filename_empty)

    # Assert
    assert actual_output == expected_output

    # Clean up
    os.remove(filename_empty)

# Test 4 - Test case for raising ValueError when providing a non CSV file
def test_read_a_csv_file_non_csv_file():
    # Arrange
    filename_non_csv = 'non_csv_file.txt'
    with open(filename_non_csv, 'w') as f:
        pass

    # Act and Assert
    with pytest.raises(ValueError):
        result = read_a_csv_file(filename_non_csv)

    # Clean up
    os.remove(filename_non_csv)

########################################
############### Ticket 2 ###############
########################################

# Test 1 - Test case for removing duplicates from an empty list
def test_deduplication_empty_list():
    # Arrange
    data_array = []

    # Act
    produced_array = remove_duplicates(data_array)

    # Assert
    assert produced_array == data_array

# Test 2 - Test case for removing duplicates from a list with no duplicates
def test_deduplication_no_duplication_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]

    # Act
    produced_array = remove_duplicates(data_array)

    # Assert
    assert produced_array == data_array

# # Test 3 - Test case for removing duplicates from a list with one duplicates
def test_deduplication_one_duplication_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana'],
        ['3', 'Cuba', 'Havana']
    ]

    expected_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    # Act
    produced_array = remove_duplicates(data_array)

    # Assert
    assert produced_array == expected_array

# Test 4 - Test case for removing duplicates from a list with multiple duplicates
def test_deduplication_multiple_duplications_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    expected_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    # Act
    produced_array = remove_duplicates(data_array)

    # Assert
    assert produced_array == expected_array

# Test 5 - Test case for removing duplicates from a list with one nested value duplicates
def test_deduplication_nested_duplication_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', ['Havana']],
        ['3', 'Cuba', ['Havana']]
    ]

    expected_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', ['Havana']]
    ]

    # Act
    produced_array = remove_duplicates(data_array)

    # Assert
    assert produced_array == expected_array

# Test 6 - Test case for removing duplicates from a list with multiple nested values duplicates
def test_deduplication_multiple_nested_duplication_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', ['Cuba', 'Havana']],
        ['3', ['Cuba', 'Havana']]
    ]

    expected_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', ['Cuba', 'Havana']]
    ]

    # Act
    produced_array = remove_duplicates(data_array)

    # Assert
    assert produced_array == expected_array

########################################
############### Ticket 3 ###############
########################################

# Test 1 - Test case for ignoring empty lines in an empty list
def test_ignore_empty_lines_empty_list():
    # Arrange
    data_array = []

    # Act
    produced_array = ignore_empty_lines(data_array)

    # Assert
    assert produced_array == data_array

# Test 2 - Test case for ignoring empty lines in list with no empty lines
def test_ignore_empty_lines_no_empty_lines_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]


    # Act
    produced_array = ignore_empty_lines(data_array)

    # Assert
    assert produced_array == data_array

# Test 3 - Test case for ignoring empty lines in list with one empty lines
def test_ignore_empty_lines_one_empty_line_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['','','']
    ]

    expected_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]

    # Act
    produced_array = ignore_empty_lines(data_array)

    # Assert
    assert produced_array == expected_array

# Test 4 - Test case for ignoring empty lines in list with multiple variations of empty lines
def test_ignore_empty_lines_multiple_empty_lines_list():
    # Arrange
    data_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['','',''],
        [' ',' ',' '],
        ['\n','\n','\n']
    ]

    expected_array = [
        ['ID','Country','Capital City'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]

    # Act
    produced_array = ignore_empty_lines(data_array)

    # Assert
    assert produced_array == expected_array

