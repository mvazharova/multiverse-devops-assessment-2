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
    actual_data = []

    # Act
    produced_data = remove_duplicates(actual_data)

    # Assert
    assert produced_data == actual_data

# Test 2 - Test case for removing duplicates from a list with no duplicates
def test_deduplication_no_duplication_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]

    # Act
    produced_data = remove_duplicates(actual_data)

    # Assert
    assert produced_data == actual_data

# # Test 3 - Test case for removing duplicates from a list with one duplicates
def test_deduplication_one_duplication_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana'],
        ['3', 'Cuba', 'Havana']
    ]

    expected_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    # Act
    produced_data = remove_duplicates(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 4 - Test case for removing duplicates from a list with multiple duplicates
def test_deduplication_multiple_duplications_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    expected_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    # Act
    produced_data = remove_duplicates(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 5 - Test case for removing duplicates from a list with one nested value duplicates
def test_deduplication_nested_duplication_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', ['Havana']],
        ['3', 'Cuba', ['Havana']]
    ]

    expected_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', ['Havana']]
    ]

    # Act
    produced_data = remove_duplicates(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 6 - Test case for removing duplicates from a list with multiple nested values duplicates
def test_deduplication_multiple_nested_duplication_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', ['Cuba', 'Havana']],
        ['3', ['Cuba', 'Havana']]
    ]

    expected_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['3', ['Cuba', 'Havana']]
    ]

    # Act
    produced_data = remove_duplicates(actual_data)

    # Assert
    assert produced_data == expected_data

########################################
############### Ticket 3 ###############
########################################

# Test 1 - Test case for ignoring empty lines from an empty list
def test_ignore_empty_lines_empty_list():
    # Arrange
    actual_data = []

    # Act
    produced_data = ignore_empty_lines(actual_data)

    # Assert
    assert produced_data == actual_data

# Test 2 - Test case for ignoring empty lines in list with no empty lines
def test_ignore_empty_lines_no_empty_lines_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]


    # Act
    produced_data = ignore_empty_lines(actual_data)

    # Assert
    assert produced_data == actual_data

# Test 3 - Test case for ignoring empty lines in list with one empty lines
def test_ignore_empty_lines_one_empty_line_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['','','']
    ]

    expected_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]

    # Act
    produced_data = ignore_empty_lines(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 4 - Test case for ignoring empty lines in list with multiple variations of empty lines
def test_ignore_empty_lines_multiple_empty_lines_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo'],
        ['','',''],
        [' ',' ',' '],
        ['\n','\n','\n']
    ]

    expected_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','Japan','Tokyo']
    ]

    # Act
    produced_data = ignore_empty_lines(actual_data)

    # Assert
    assert produced_data == expected_data

########################################
############### Ticket 4 ###############
########################################

# Test 1 - Test case for capitalising names from an empty list
def test_capitalisation_empty_list():
    # Arrange
    actual_data = []

    # Act
    produced_data = capitalise_name_fields(actual_data)

    # Assert
    assert produced_data == actual_data

# Test 2 - Test case for capitalising names when input is lowercase
def test_capitalisation_multiple_lowercase_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','Belgium','brussels'],
        ['2','japan','Tokyo'],
        ['3', 'cuba', 'havana']
    ]

    expected_data = [
        ['ID','Country','Capital'], 
        ['1','Belgium','Brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    # Act
    produced_data = capitalise_name_fields(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 3 - Test case for capitalising names when input is uppercase
def test_capitalisation_multiple_uppercase_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','BELGIUM','BRUSSELS'],
        ['2','JAPAN','TOKYO'],
        ['3', 'CUBA', 'havana']
    ]

    expected_data = [
        ['ID','Country','Capital'], 
        ['1','Belgium','Brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    # Act
    produced_data = capitalise_name_fields(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 4 - Test case for capitalising names when input is mix-case
def test_capitalisation_multiple_mixcase_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','BeLgIuM','bRuSsElS'],
        ['2','japAN','TOKyo'],
        ['3', 'cUBA', 'havana']
    ]

    expected_data = [
        ['ID','Country','Capital'], 
        ['1','Belgium','Brussels'],
        ['2','Japan','Tokyo'],
        ['3', 'Cuba', 'Havana']
    ]

    # Act
    produced_data = capitalise_name_fields(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 5 - Test case for capitalising names when input has special and non-alphabetic characters
def test_capitalisation_multiple_special_characters_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital'],
        ['1','BeLgIuM','Bru$$els'],
        ['2','japAN1','T0KY0'],
        ['3', 'cuba!', 'havana2']
    ]

    expected_data = [
        ['ID','Country','Capital'], 
        ['1','Belgium','Bru$$els'],
        ['2','Japan1','T0ky0'],
        ['3', 'Cuba!', 'Havana2']
    ]

    # Act
    produced_data = capitalise_name_fields(actual_data)

    # Assert
    assert produced_data == expected_data

########################################
############### Ticket 5 ###############
########################################

# Test 1 - Test case for validating numerical column from an empty list
def test_validate_ans3_empty_list():
    # Arrange
    actual_data = []

    # Act
    produced_data = validate_ans3(actual_data)

    # Assert
    assert produced_data == actual_data

# Test 2 - Test case for validating numerical column with empty value
def test_validate_ans3_no_input_value_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital', 'Elevation', 'Humidity','Score'], 
        ['1','Belgium','Brussels', '13', '77', ''],
        ['2','Japan','Tokyo', '40', '98', '1'],
        ['3', 'Cuba', 'Havana', '59', '76', '7']
    ]

    expected_data = [
        ['2','Japan','Tokyo', '40', '98', '1'],
        ['3', 'Cuba', 'Havana', '59', '76', '7']
    ]

    # Act
    produced_data = validate_ans3(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 3 - Test case for validating numerical column with zero as a value
def test_validate_ans3_value_zero_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital', 'Elevation', 'Humidity','Score'], 
        ['1','Belgium','Brussels', '13', '77', '10'],
        ['2','Japan','Tokyo', '40', '98', '1'],
        ['3', 'Cuba', 'Havana', '59', '76', '0']
    ]

    expected_data = [
        ['1','Belgium','Brussels', '13', '77', '10'],
        ['2','Japan','Tokyo', '40', '98', '1']
    ]

    # Act
    produced_data = validate_ans3(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 4 - Test case for validating numerical column with negative and above 10 value
def test_validate_ans3_invalid_values_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital', 'Elevation', 'Humidity','Score'], 
        ['1','Belgium','Brussels', '13', '77', '10'],
        ['2','Japan','Tokyo', '40', '98', '-11'],
        ['3', 'Cuba', 'Havana', '59', '76', '20']
    ]

    expected_data = [
        ['1','Belgium','Brussels', '13', '77', '10']
    ]

    # Act
    produced_data = validate_ans3(actual_data)

    # Assert
    assert produced_data == expected_data

# Test 5 - Test case for validating numerical column with string value
def test_validate_ans3_string_values_list():
    # Arrange
    actual_data = [
        ['ID','Country','Capital', 'Elevation', 'Humidity','Score'], 
        ['1','Belgium','Brussels', '13', '77', 'two'],
        ['2','Japan','Tokyo', '40', '98', '5'],
        ['3', 'Cuba', 'Havana', '59', '76', 'none']
    ]

    expected_data = [
        ['2','Japan','Tokyo', '40', '98', '5']
    ]

    # Act
    produced_data = validate_ans3(actual_data)

    # Assert
    assert produced_data == expected_data