"""CSC110 Fall 2020 Project Phase 2

Instructions (READ THIS FIRST!)
===============================

The module contains only functions that transform all data in
csv files used in this project into usable Python data types
for further computations in computation.py.

Do not edit any function in the module.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of TAs and
instructors of  CSC110 at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2020 Jia Hao Choo and Komal Saini.
"""
import csv
from typing import List, Dict


def read_country_data() -> List[List[str]]:
    """Return a list containing the metadata of all countries in the
    'country_metadata.csv'.

    Each inner list represents the data for a particular country.
        - index 0 is the country code
        - index 1 represents the region of the country
        - index 2 represents its income group
        - index 3 is the full name of the country

    >>> country = read_country_data()
    >>> country[0]
    ['AFG', 'South Asia', 'Low income', 'Afghanistan']
    """
    with open('datasets/country_metadata.csv', encoding='ISO-8859-1') as country_file:
        reader = csv.reader(country_file)

        # Skip header row
        next(reader)

        country_data_lst = []

        for row in reader:
            country_data_lst.append(row)

    return country_data_lst


def read_value_data(filename: str) -> List[Dict[str, List]]:
    """Return a list of mapping containing the country code mapped to
    a list of revenue data of a specific sector from 1990 to 2016.
    This function will be used to read Agriculture value,
    Industry value and Manufacturing value, specified by the filename input.

    Preconditions:
        - filename.startswith('datasets/')
        - filename.endswith('.csv')

    >>> agriculture = read_value_data('datasets/agriculture.csv')
    >>> agriculture[0] == {'ABW': ['', '', '', '', '', 6681564.246, \
    6703910.615, 6586592.179, 6793296.089, 6603351.955, 7681564.246, \
    7779329.609, 7808379.888, 8112849.162, 8727932.961, 9012290.503, \
    9546927.374, 10597206.7, 10451955.31, 11005027.93, '', '', '', '', \
    '', '', '']}
    True
    """
    with open(filename, encoding='ISO-8859-1') as value_file:
        reader = csv.reader(value_file)

        # Skip header row
        next(reader)

        value_data_lst = []

        for row in reader:
            country_data = {}

            # Collect the country code
            # Collect the list of values for the country
            country_code = str(row[1])
            value_each_year = row[3:30]

            # Convert each value in the list value_each_year from str to int
            # If value == '', keep the original str format
            convert_str_to_int = []
            for value in value_each_year:
                if value != '':
                    convert_str_to_int.append(float(value))
                else:
                    convert_str_to_int.append(value)

            # Put the country_code as key in the mapping, and the converted lst
            # as its value
            country_data[country_code] = convert_str_to_int

            # Append the mapping back to the main value data list
            value_data_lst.append(country_data)

    return value_data_lst


def read_emissions_data(sector: str) -> List[Dict[str, List]]:
    """Return a list of mapping containing the country code mapped to
    a list of emissions data of a specific sector from 1990 to 2016.
    This function reads 'emissions.csv', but the output will
    differ according to the input sector name. For example, if the
    argument is "Agriculture", this function will produce a list of mapping
    containing country codes mapped to a list of agricultural emissions values.

    Preconditions:
        - sector in ['Agriculture', 'Manufacturing', 'Industry']

    >>> manufacturing = read_emissions_data('Manufacturing')
    >>> manufacturing[0] == {'ALB': [2.1, 1.4, 0.8, 0.5, 0.5, \
    0.5, 0.5, 0.2, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, 0.4, 0.7, \
    0.6, 0.5, 0.8, 1.0, 1.1, 0.6, 0.6, 0.9, 0.7, 0.6]}
    True
    """
    with open('datasets/emissions.csv', encoding='ISO-8859-1') as emission_file:
        reader = csv.reader(emission_file)

        # Skip header row
        next(reader)

        emission_data_lst = []

        sector_specified = sector
        if sector_specified == 'Manufacturing':
            sector_specified = 'Manufacturing/Construction'
        elif sector_specified == 'Industry':
            sector_specified = 'Industrial Processes'
        else:
            pass

        # Filter only the rows with the specified sector
        valid_rows = [r for r in reader if r[2] == sector_specified]

        for row in valid_rows:
            country_data = {}

            # Collect the country code
            # Collect the list of values for the country. This list
            # is reversed as the columns in csv goes from 2016 to 1990.
            country_code = str(row[1])
            emission_each_year = reversed(row[4:31])

            # Convert each value in the list value_each_year from str to int
            # If value == '', keep the original str format
            convert_str_to_int = []
            for emission in emission_each_year:
                if emission != 'N/A':
                    convert_str_to_int.append(float(emission))
                else:
                    convert_str_to_int.append(emission)

            # Put the country_code as key in the mapping, and the converted lst
            # as its value
            country_data[country_code] = convert_str_to_int

            # Append the mapping back to the main value data list
            emission_data_lst.append(country_data)

        return emission_data_lst


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'allowed-io': ['read_country_data', 'read_value_data', 'read_emissions_data'],
        'extra-imports': ['csv', 'python_ta.contracts'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
