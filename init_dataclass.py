"""CSC110 Fall 2020 Project Phase 2

Instructions (READ THIS FIRST!)
===============================
This module contains data class information, and functions
that initialize and produce data class objects for use in
init_dataclass.py.

Do not edit any function or data class in this module.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of TAs and
instructors of  CSC110 at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.
This file is Copyright (c) 2020 Jia Hao Choo and Komal Saini.
"""

from dataclasses import dataclass
from typing import Dict, Optional

from read_csv import read_emissions_data, read_value_data, read_country_data


@dataclass
class Emissions:
    """A data class that represents the emissions generated
    by each industry in a country. If any emission data is
    missing, the attribute will be None.

    Instance Attributes:
        - country_code: A string representing the country code.
        - industry_emissions: A list of industrial emissions from year 1990 to 2016.
        - manufacture_emissions: A list of manufacturing emissions from year 1990 to 2016.
        - agriculture_emissions: A list of agricultural emissions from year 1990 to 2016.

    Representation Invariants:
        - len(self.country_code) == 3
        - len(self.industry_emissions) == 27 or self.industry_emissions is None
        - len(self.manufacture_emissions) == 27 or self.manufacture_emissions is None
        - len(self.agriculture_emissions) == 27 or self.agriculture_emissions is None

    >>> afghanistan_emissions = Emissions(country_code='AFG',\
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
    """
    country_code: str
    industry_emissions: Optional[list] = None
    manufacture_emissions: Optional[list] = None
    agriculture_emissions: Optional[list] = None


@dataclass
class Revenue:
    """A data class that represents the revenue generated by each industry in a country.

     Instance Attributes:
         - country_code: A string representing the country code.
         - industry_value: A list of the revenue of industrial sector from 1990 to 2016.
         - manufacture_value: A list of the revenue of manufacturing sector from 1990 to 2016.
         - agriculture_value: A list of the revenue of agricultural sector from 1990 to 2016.

     Representation Invariants:
         - len(self.country_code) == 3
         - len(self.industry_value) == 27
         - len(self.manufacture_value) == 27
         - len(self.agriculture_value) == 27

     >>> aruba_revenue = Revenue(country_code='ABW', \
                                 industry_value=['', '', '', '', '', 203335195.5, \
                                 206810055.9, 262463687.2, 291620111.7, 267882681.6, \
                                 296480446.9, 305515642.5, 296703352.0, 339418994.4, \
                                 392163687.2, 431287150.8, 474557541.9, 496345810.1, \
                                 495007262.6, 404204469.3, '', '', '', '', '', '', ''], \
                                 manufacture_value=['', '', '', '', '', 33251396.65, \
                                 34636871.51, 37944134.08, 46530726.26, 62011173.18, \
                                 73480446.93, 74039106.15, 74597765.36, 75156424.58, \
                                 75715083.8, 76273743.02, 76832402.23, 77391061.45, \
                                 77949720.67, 78508379.89, '', '', '', '', '', '', ''], \
                                 agriculture_value=['', '', '', '', '', 6681564.246, \
                                 6703910.615, 6586592.179, 6793296.089, 6603351.955, \
                                 7681564.246, 7779329.609, 7808379.888, 8112849.162,\
                                  8727932.961, 9012290.503, 9546927.374, 10597206.7, \
                                  10451955.31, 11005027.93, '', '', '', '', '', '', ''])
     """
    country_code: str
    industry_value: list
    manufacture_value: list
    agriculture_value: list


@dataclass
class Country:
    """A data class that represents a country.

    If a country does not have the corresponding revenues or emissions data,
    its instance attributes sector_emissions or sector_values will be None

    Instance Attributes:
        - country_code: A string representing the country code.
        - region: A string representing the country's region.
        - income_group: A string representing the country's income group.
        - name: A string representing the full name of the country.
        - sector_emissions: Emissions data class object containing
                            emission data of each sector for the country.
        - sector_values: Values data class object containing revenue data
                         of each sector for the country.

    Representation Invariants:
        - len(self.country_code) == 3
        - self.region != ''
        - self.income_group in ['High income', 'Upper middle income',
                               Lower middle income', 'Low income']
        - self.name != ''

    >>> sample_country = Country('SAM', 'Asia', 'Lower middle income', 'Sample', None, None)
    """
    country_code: str
    region: str
    income_group: str
    name: str
    sector_emissions: Optional[Emissions] = None
    sector_revenues: Optional[Revenue] = None


def init_emissions() -> Dict[str, Emissions]:
    """Returns a dictionary of Emissions objects keyed by the country code.

    >>> sample = init_emissions()
    >>> sample['AFG'] == Emissions(country_code='AFG',\
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
    True
    """

    emissions = dict()

    agriculture_data = read_emissions_data('Agriculture')
    industry_data = read_emissions_data('Industry')
    manufacture_data = read_emissions_data('Manufacturing')

    for code in agriculture_data:
        emissions[code] = Emissions(country_code=code)
        emissions[code].agriculture_emissions = agriculture_data[code]

    for code in industry_data:
        if code in emissions:
            emissions[code].industry_emissions = industry_data[code]
        else:
            emissions[code] = Emissions(country_code=code)
            emissions[code].industry_emissions = industry_data[code]

    for code in manufacture_data:
        if code in emissions:
            emissions[code].manufacture_emissions = manufacture_data[code]
        else:
            emissions[code] = Emissions(country_code=code)
            emissions[code].manufacture_emissions = manufacture_data[code]

    return emissions


def init_revenue() -> Dict[str, Revenue]:
    """Returns a dictionary of Revenues objects keyed by the country code.

    >>> sample = init_revenue()
    >>> sample['ABW'] == Revenue(country_code='ABW', \
                                 industry_value=['', '', '', '', '', 203335195.5, \
                                 206810055.9, 262463687.2, 291620111.7, 267882681.6, \
                                 296480446.9, 305515642.5, 296703352.0, 339418994.4, \
                                 392163687.2, 431287150.8, 474557541.9, 496345810.1, \
                                 495007262.6, 404204469.3, '', '', '', '', '', '', ''], \
                                 manufacture_value=['', '', '', '', '', 33251396.65, \
                                 34636871.51, 37944134.08, 46530726.26, 62011173.18, \
                                 73480446.93, 74039106.15, 74597765.36, 75156424.58, \
                                 75715083.8, 76273743.02, 76832402.23, 77391061.45, \
                                 77949720.67, 78508379.89, '', '', '', '', '', '', ''], \
                                 agriculture_value=['', '', '', '', '', 6681564.246, \
                                 6703910.615, 6586592.179, 6793296.089, 6603351.955, \
                                 7681564.246, 7779329.609, 7808379.888, 8112849.162,\
                                  8727932.961, 9012290.503, 9546927.374, 10597206.7, \
                                  10451955.31, 11005027.93, '', '', '', '', '', '', ''])
    True
    """
    revenues = dict()

    agriculture_data = read_value_data('datasets/agriculture.csv')
    industry_data = read_value_data('datasets/industry.csv')
    manufacture_data = read_value_data('datasets/manufacturing.csv')

    for code in agriculture_data:
        revenues[code] = Revenue(country_code=code,
                                 agriculture_value=agriculture_data[code],
                                 industry_value=industry_data[code],
                                 manufacture_value=manufacture_data[code])

    return revenues


def init_countries() -> Dict[str, Country]:
    """Returns a dictionary of Country objects keyed by the country code.

    >>> sample = init_countries()
    >>> sample['AFG'].country_code
    'AFG'
    >>> sample['AFG'].income_group
    'Low income'
    >>> emissions = init_emissions()
    >>> sample['AFG'].sector_emissions == emissions['AFG']
    True
    >>> revenues = init_revenue()
    >>> sample['AFG'].sector_revenues == revenues['AFG']
    True
    """
    countries = dict()

    countries_data = read_country_data()
    emissions_objects = init_emissions()
    revenues_objects = init_revenue()

    for country_data in countries_data:
        if country_data[2] != '':
            [code, region, income_group, name] = country_data
            countries[code] = Country(country_code=code,
                                      region=region,
                                      income_group=income_group,
                                      name=name)

    for country in countries:
        if countries[country].country_code in emissions_objects:
            countries[country].sector_emissions = \
                emissions_objects[countries[country].country_code]

    for country in countries:
        if countries[country].country_code in revenues_objects:
            countries[country].sector_revenues = \
                revenues_objects[countries[country].country_code]

    return countries


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['typing', 'dataclasses', 'read_csv', 'python_ta.contracts'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
