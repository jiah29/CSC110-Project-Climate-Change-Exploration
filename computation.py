"""CSC110 Fall 2020 Project Phase 2

Instructions (READ THIS FIRST!)
===============================

This module contains functions that filter countries according to
their income classification, and also functions that calculate
the averages of emission data and value data.

Do not edit any function in this module.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of TAs and
instructors of  CSC110 at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2020 Jia Hao Choo and Komal Saini.
"""
from typing import Dict, List, Tuple
import statistics
from init_dataclass import Country, Emissions, Revenue


################################################################################
# Part 1 - Filter country according to income classifications
################################################################################
def filter_country(countries_list: Dict[str, Country], classification: str) \
        -> Dict[str, Country]:
    """Return a mapping of all Country object that has the
    classification.

    Preconditions:
        - classification in ['High income', 'Upper middle income',
                               Lower middle income', 'Low income']

    >>> countries_lst = {'CO1': Country('CO1', 'High income', 'Country 1', None, None),\
                    'CO2': Country('CO2', 'High income', 'Country 2', None, None),\
                    'CO3': Country('CO3', 'Low income', 'Country 3', None, None),\
                    'CO4': Country('CO4', 'Upper middle income', 'Country 4', None, None)}
    >>> valid_countries = filter_country(countries_lst, 'High income')
    >>> valid_countries == {'CO1': Country(country_code='CO1', income_group='High income',\
                                   name='Country 1', sector_emissions=None, \
                                   sector_revenues=None),\
                            'CO2': Country(country_code='CO2', income_group='High income', \
                                   name='Country 2', sector_emissions=None, sector_revenues=None)}
    True
    """
    filtered_countries = dict()

    for country in countries_list:
        if countries_list[country].income_group == classification:
            filtered_countries[country] = countries_list[country]

    return filtered_countries


################################################################################
# Part 2 - Finding the emission averages
################################################################################
def find_emission_average(countries_list: Dict[str, Country]) -> Dict[str, List[float]]:
    """Return the mapping of each sector to a list of averages of emission data every year
    from 1990 to 2016.


    Preconditions:
        - sector in ['Agriculture', 'Manufacturing', 'Industry']

    >>> emissions = Emissions(country_code='CO1',\
                              industry_emissions=[0.05, 0.05, 0.06, 0.06,\
                              0.07, 0.07, 0.08, 0.1, 0.11, 0.12, 0.11, 0.12,\
                              0.12, 0.14, 0.14, 0.14, 0.16, 0.18, 0.2, 0.22,\
                              0.25, 0.31, 0.38, 0.45, 0.53, 0.59, 0.74], \
                              manufacture_emissions=[2.1, 1.4, 0.8, 0.5, 0.5, \
                              0.5, 0.5, 0.2, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, \
                              0.4, 0.7, 0.6, 0.5, 0.8, 1.0, 1.1, 0.6, 0.6, 0.9, \
                              0.7, 0.6], \
                              agriculture_emissions=[8.09, 8.41, 8.42, 8.5, \
                              8.54, 8.97, 9.98, 10.95, 11.75, 12.79, 10.99, \
                              9.28, 11.57, 12.05, 11.79, 12.08, 12.05, 12.12, \
                              13.45, 13.86, 15.85, 15.91, 15.78, 15.73, 16.22, \
                              15.15, 15.35])

    >>> countries_lst = {'CO1': Country('CO1', 'High income', 'Country 1', emissions, None),\
                    'CO2': Country('CO2', 'High income', 'Country 2', emissions, None),\
                    'CO3': Country('CO3', 'Low income', 'Country 3', emissions, None),}

    >>> find_emission_average(countries_lst) == {'Agriculture': [8.09, 8.41, 8.42, 8.5, \
                                                8.54, 8.97, 9.98, 10.95, 11.75, 12.79, 10.99, \
                                                9.28, 11.57, 12.05, 11.79, 12.08, 12.05, 12.12, \
                                                13.45, 13.86, 15.85, 15.91, 15.78, 15.73, 16.22, \
                                                15.15, 15.35], \
                                                'Manufacturing': [2.1, 1.4, 0.8, 0.5, 0.5, \
                                                0.5, 0.5, 0.2, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, \
                                                0.4, 0.7, 0.6, 0.5, 0.8, 1.0, 1.1, 0.6, 0.6, 0.9, \
                                                0.7, 0.6], \
                                                'Industry': [0.05, 0.05, 0.06, 0.06,\
                                                0.07, 0.07, 0.08, 0.1, 0.11, 0.12, 0.11, 0.12,\
                                                0.12, 0.14, 0.14, 0.14, 0.16, 0.18, 0.2, 0.22,\
                                                0.25, 0.31, 0.38, 0.45, 0.53, 0.59, 0.74]}
    True
    """
    mapping_accumulator = {'Agriculture': [], 'Manufacturing': [], 'Industry': []}

    for i in range(27):

        tuple_values = find_emission_year_average(countries_list, i)

        mapping_accumulator['Agriculture'].append(tuple_values[0])
        mapping_accumulator['Manufacturing'].append(tuple_values[1])
        mapping_accumulator['Industry'].append(tuple_values[2])

    return mapping_accumulator


def find_emission_year_average(countries_list: Dict[str, Country], index: int) -> \
        Tuple[float, float, float]:
    """Find the emission average for a particular year, represented by the index.
    Return a tuple of three float, with  each float representing the average
    of each sector.

    Helper function for find_emission_average.

    Preconditions:
        - 0 <= index <= 26

    >>> emissions = Emissions(country_code='CO1',\
                              industry_emissions=[0.05, 0.05, 0.06, 0.06,\
                              0.07, 0.07, 0.08, 0.1, 0.11, 0.12, 0.11, 0.12,\
                              0.12, 0.14, 0.14, 0.14, 0.16, 0.18, 0.2, 0.22,\
                              0.25, 0.31, 0.38, 0.45, 0.53, 0.59, 0.74], \
                              manufacture_emissions=[2.1, 1.4, 0.8, 0.5, 0.5, \
                              0.5, 0.5, 0.2, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, \
                              0.4, 0.7, 0.6, 0.5, 0.8, 1.0, 1.1, 0.6, 0.6, 0.9, \
                              0.7, 0.6], \
                              agriculture_emissions=[8.09, 8.41, 8.42, 8.5, \
                              8.54, 8.97, 9.98, 10.95, 11.75, 12.79, 10.99, \
                              9.28, 11.57, 12.05, 11.79, 12.08, 12.05, 12.12, \
                              13.45, 13.86, 15.85, 15.91, 15.78, 15.73, 16.22, \
                              15.15, 15.35])

    >>> emissions2 = Emissions(country_code='CO1',\
                              industry_emissions=[2.1, 1.4, 0.8, 0.5, 0.5, \
                              0.5, 0.5, 0.2, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, \
                              0.4, 0.7, 0.6, 0.5, 0.8, 1.0, 1.1, 0.6, 0.6, 0.9, \
                              0.7, 0.6], \
                              manufacture_emissions=[0.05, 0.05, 0.06, 0.06,\
                              0.07, 0.07, 0.08, 0.1, 0.11, 0.12, 0.11, 0.12,\
                              0.12, 0.14, 0.14, 0.14, 0.16, 0.18, 0.2, 0.22,\
                              0.25, 0.31, 0.38, 0.45, 0.53, 0.59, 0.74], \
                              agriculture_emissions=[8.09, 8.41, 8.42, 8.5, \
                              8.54, 8.97, 9.98, 10.95, 11.75, 12.79, 10.99, \
                              9.28, 11.57, 12.05, 11.79, 12.08, 12.05, 12.12, \
                              13.45, 13.86, 15.85, 15.91, 15.78, 15.73, 16.22, \
                              15.15, 15.35])

    >>> countries_lst = {'CO1': Country('CO1', 'High income', 'Country 1', emissions, None),\
                    'CO2': Country('CO2', 'High income', 'Country 2', emissions2, None),\
                    'CO3': Country('CO3', 'Low income', 'Country 3', emissions2, None),}

    >>> find_emission_year_average(countries_lst, 0)
    (8.09, 0.7333333333333334, 1.4166666666666667)
    """
    industry_year_data = []
    manufacture_year_data = []
    agriculture_year_data = []

    for country in countries_list:

        emission_values = get_emission_value(countries_list, country, index)

        if 'Industry' in emission_values:
            industry_year_data.append(emission_values['Industry'])

        if 'Manufacture' in emission_values:
            manufacture_year_data.append(emission_values['Manufacture'])

        if 'Agriculture' in emission_values:
            agriculture_year_data.append(emission_values['Agriculture'])

    industry_average = float(statistics.mean(industry_year_data))
    manufacture_average = float(statistics.mean(manufacture_year_data))
    agriculture_average = float(statistics.mean(agriculture_year_data))

    return (agriculture_average, manufacture_average, industry_average)


def get_emission_value(countries_list: Dict[str, Country], country: str, index: int) -> \
        Dict[str, float]:
    """Return a tuple of three floats, with each float representing the
    value of emission of each sector.

    Helper function for find_emission_year_average.

    Preconditions:
        - 0 <= index <= 26
        - country in countries_list

    >>> co1_emissions = Emissions(country_code='CO1',\
                                  industry_emissions=[0.05, 0.05, 0.06, 0.06,\
                                  0.07, 0.07, 0.08, 0.1, 0.11, 0.12, 0.11, 0.12,\
                                  0.12, 0.14, 0.14, 0.14, 0.16, 0.18, 0.2, 0.22,\
                                  0.25, 0.31, 0.38, 0.45, 0.53, 0.59, 0.74], \
                                  manufacture_emissions=None, \
                                  agriculture_emissions=[8.09, 8.41, 8.42, 8.5, \
                                  8.54, 8.97, 9.98, 10.95, 11.75, 12.79, 10.99, \
                                  9.28, 11.57, 12.05, 11.79, 12.08, 12.05, 12.12, \
                                  13.45, 13.86, 15.85, 15.91, 15.78, 15.73, 16.22, \
                                  15.15, 15.35])

    >>> countries_lst = {'CO1': Country('CO1', 'High income', 'Country 1', co1_emissions, None),\
                    'CO2': Country('CO2', 'High income', 'Country 2', None, None),\
                    'CO3': Country('CO3', 'Low income', 'Country 3', None, None),}

    >>> get_emission_value(countries_lst, 'CO1', 0)
    {'Industry': 0.05, 'Agriculture': 8.09}

    """
    emission_values = {}

    if countries_list[country].sector_emissions is not None:
        if countries_list[country].sector_emissions.industry_emissions is not None:
            industry_emission = \
                countries_list[country].sector_emissions.industry_emissions[index]
            if industry_emission != '':
                emission_values['Industry'] = industry_emission

        if countries_list[country].sector_emissions.manufacture_emissions is not None:
            manufacture_emission = \
                countries_list[country].sector_emissions.manufacture_emissions[index]
            if manufacture_emission != '':
                emission_values['Manufacture'] = manufacture_emission

        if countries_list[country].sector_emissions.agriculture_emissions is not None:
            agriculture_emission = \
                countries_list[country].sector_emissions.agriculture_emissions[index]
            if agriculture_emission != '':
                emission_values['Agriculture'] = agriculture_emission

    return emission_values


################################################################################
# Part 3 - Finding the revenue averages
################################################################################

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['typing', 'init_dataclass', 'python_ta.contracts', 'statistics'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
