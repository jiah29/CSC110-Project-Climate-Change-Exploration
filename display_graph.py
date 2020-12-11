"""CSC110 Fall 2020 Project Phase 2

Instructions (READ THIS FIRST!)
===============================

This module contains functions that create dataframe objects
and produce an interactive bar graph.

Do not edit any function in this module.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of TAs and
instructors of  CSC110 at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2020 Jia Hao Choo and Komal Saini.
"""
from typing import Dict, List
import pandas
import plotly
import plotly.graph_objects as go


################################################################################
# Part 1 - Create pandas dataframe objects
################################################################################
def create_dataframe(average_revenue: Dict[str, List[float]],
                     average_emission: Dict[str, List[float]]) -> pandas.DataFrame:
    """Return a dataframe object that stores average revenue and average
    emission data in rows, with each column representing each year.

    >>> from computation import find_emission_average, find_average_revenue
    >>> from init_dataclass import init_countries
    >>> countries = init_countries()
    >>> average_emissions = find_emission_average(countries)
    >>> average_revenues = find_average_revenue(countries)
    >>> sample_df = create_dataframe(average_revenues, average_emissions)
    >>> sample_df.loc["Agriculture Revenue", "1990"]
    6025401740.822624
    >>> sample_df.loc["Agriculture Emission", "1990"]
    26.694414893617022
    """
    years = [str(year) for year in range(1990, 2017)]

    df = pandas.DataFrame.from_dict(average_revenue, orient='index', columns=years)

    df = df.append(pandas.DataFrame.from_dict(average_emission, orient='index', columns=years))

    return df


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'extra-imports': ['pandas', 'plotly', 'plotly.graph_objects',
                          'typing', 'python_ta.contracts'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
