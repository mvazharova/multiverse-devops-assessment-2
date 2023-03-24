from csvhelper import * 
from pathlib import Path
import os
import pytest

filename = "results.csv"

# Ticket 1

# Test 1 - Check the file exists 
def test_file_exists():
    file_exists = Path(filename).is_file()
    assert file_exists == True

# Test 2 - Verify that when a file that doesn't exist is provided, the method raises a FileNotFoundError.
def test_read_a_csv_file_nonexistent_file():
    # Arrange
    filename_nonexisting = 'nonexistent_file.csv'
    if os.path.exists(filename_nonexisting):
        os.remove(filename_nonexisting)

    # Act and Assert
    with pytest.raises(FileNotFoundError):
        result = read_a_csv_file(filename_nonexisting)

# Test 3 - Check that when an empty file is passed to the function, it produces an empty list.
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

# Test 4 - Verify that when a non CSV file is provided, the method raises a ValueError.
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


