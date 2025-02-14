"""CSC110 Fall 2020 Project Phase 2

Instructions (READ THIS FIRST!)
===============================

The module contains only functions that transform all data in
csv files used in this project into usable Python data types
for further computations in init_dataclass.py.

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
        - index 1 represents its income group
        - index 2 is the full name of the country

    Note: If any data is unavailable, it will be represented
    with an empty string.

    >>> country = read_country_data()
    >>> country[0]
    ['AFG', 'Low income', 'Afghanistan']
    >>> non_country_example = country[98] # These will be filtered out during computations
    >>> non_country_example == ['HPC', '', 'Heavily indebted poor countries (HIPC)']
    True
    """
    with open('datasets/country_metadata.csv', encoding='ISO-8859-1') as country_file:
        reader = csv.reader(country_file)

        next(reader)

        country_data_lst = []

        for row in reader:
            row.pop(1)
            country_data_lst.append(row)

    return country_data_lst


def read_revenue_data(filename: str) -> Dict[str, List]:
    """Return a mapping with the country codes as the keys mapped to
    the corresponding list of revenue data of a specific sector
    from 1990 to 2016.

    This function will be used to read Agriculture value,
    Industry value and Manufacturing value, specified by the filename input.

    Note: If the data for a particular year is unavailable, it is
    represented with an empty string.

    Preconditions:
        - filename.startswith('datasets/')
        - filename.endswith('.csv')

    >>> agriculture = read_revenue_data('datasets/agriculture.csv')
    >>> agriculture['ABW'] == ['', '', '', '', '', 6681564.246, \
    6703910.615, 6586592.179, 6793296.089, 6603351.955, 7681564.246, \
    7779329.609, 7808379.888, 8112849.162, 8727932.961, 9012290.503, \
    9546927.374, 10597206.7, 10451955.31, 11005027.93, '', '', '', '', \
    '', '', '']
    True
    """
    with open(filename, encoding='ISO-8859-1') as value_file:
        reader = csv.reader(value_file)

        next(reader)

        value_data_mapping = {}

        for row in reader:

            country_code = str(row[1])
            value_each_year = row[3:30]

            convert_str_to_int = []
            for value in value_each_year:
                if value != '':
                    convert_str_to_int.append(float(value))
                else:
                    convert_str_to_int.append(value)

            value_data_mapping[country_code] = convert_str_to_int

    return value_data_mapping


def read_emissions_data(sector: str) -> Dict[str, List]:
    """Return a mapping with the country codes as the keys mapped to
    the corresponding list of emissions data of a specific sector
    from 1990 to 2016.

    This function reads 'emissions.csv', but the output will
    differ according to the input sector name. For example, if the
    argument is "Agriculture", this function will produce a list of mapping
    containing country codes mapped to a list of agricultural emissions values.

    Note: If the data for a particular year is unavailable, it is
    represented with an empty string in the list.

    Preconditions:
        - sector in ['Agriculture', 'Manufacturing', 'Industry']

    >>> manufacturing = read_emissions_data('Manufacturing')
    >>> manufacturing['ALB'] == [2.1, 1.4, 0.8, 0.5, 0.5, \
    0.5, 0.5, 0.2, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, 0.4, 0.7, \
    0.6, 0.5, 0.8, 1.0, 1.1, 0.6, 0.6, 0.9, 0.7, 0.6]
    True
    >>> special_case = manufacturing['KHM']
    >>> special_case == ['', '', '', '', '', 0.0, 0.0, 0.0, 0.1, \
                        0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, \
                        0.1, 0.2, 0.2, 0.2, 0.2, 0.3, 0.2, 0.2, 0.7]
    True
    """
    with open('datasets/emissions.csv', encoding='ISO-8859-1') as emission_file:
        reader = csv.reader(emission_file)

        next(reader)

        emission_data_mapping = {}

        sector_specified = sector
        if sector_specified == 'Manufacturing':
            sector_specified = 'Manufacturing/Construction'
        elif sector_specified == 'Industry':
            sector_specified = 'Industrial Processes'
        else:
            pass

        valid_rows = [r for r in reader if r[2] == sector_specified]

        for row in valid_rows:

            # The list is reversed as the columns in csv goes from 2016 to 1990.
            country_code = str(row[1])
            emission_each_year = reversed(row[4:31])

            convert_str_to_int = []
            for emission in emission_each_year:
                if emission != 'N/A':
                    convert_str_to_int.append(float(emission))
                else:
                    convert_str_to_int.append('')

            emission_data_mapping[country_code] = convert_str_to_int

        return emission_data_mapping


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'allowed-io': ['read_country_data', 'read_value_data', 'read_emissions_data',
                       'read_revenue_data'],
        'extra-imports': ['csv', 'python_ta.contracts'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
