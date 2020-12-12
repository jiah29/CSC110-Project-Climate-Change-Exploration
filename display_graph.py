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
import plotly.graph_objects as go
from plotly.subplots import make_subplots


################################################################################
# Part 1 - Create pandas dataframe objects
################################################################################
def create_dataframe(average: Dict[str, List[float]]) -> pandas.DataFrame:
    """Return a dataframe object that stores average revenue and average
    emission data from the dict.

    There are 7 columns: the first column is the year column,
    the second to fourth columns are the Emission value of each sector,
    the fifth to last columns represent the Revenue of each sector.

    There are 26 rows (representing year 1990 to 2016, with each row
    representing the data specified by each column title.

    >>> from computation import find_emission_average, find_average_revenue
    >>> from init_dataclass import init_countries
    >>> countries = init_countries()
    >>> average_emissions = find_emission_average(countries)
    >>> average_revenues = find_average_revenue(countries)
    >>> average = {}
    >>> average.update(average_emissions)
    >>> average.update(average_revenues)
    >>> sample_df = create_dataframe(average)
    >>> sample_df.loc[0, "Agriculture Revenue"]
    6025401740.822624
    >>> sample_df.loc[0, "Agriculture Emission"]
    26.694414893617022
    """
    df = pandas.DataFrame.from_dict(average, orient='columns')

    years = [str(year) for year in range(1990, 2017)]

    df.insert(0, 'Year', years)

    return df


################################################################################
# Part 2 - Plotting
################################################################################
def plot_graph(dataframe: pandas.DataFrame, group: str) -> None:
    """Plot interactive bar graph. Default graph is Agriculture Sector.
    Use the button to switch between different sectors.

    Preconditions:
        - group in ['High Income', 'Upper Middle Income', 'Lower Middle Income', 'Low Income']

    >>> from computation import find_emission_average, find_average_revenue, filter_country
    >>> from init_dataclass import init_countries
    >>> countries = init_countries()
    >>> high = filter_country(countries, 'High income')
    >>> average_emissions = find_emission_average(high)
    >>> average_revenues = find_average_revenue(high)
    >>> high_income = {}
    >>> high_income.update(average_emissions)
    >>> high_income.update(average_revenues)
    >>> sample_df = create_dataframe(high_income)
    >>> plot_graph(sample_df, 'High Income')
    """
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.update_layout(barmode='group')

    fig.add_trace(go.Bar(x=dataframe['Year'], y=dataframe['Agriculture Emission'],
                         offsetgroup=0, name='Emission'),
                  secondary_y=False)

    fig.add_trace(go.Bar(x=dataframe['Year'], y=dataframe['Agriculture Revenue'],
                         offsetgroup=1, name='Revenue'),
                  secondary_y=True)

    fig.add_trace(go.Bar(x=dataframe['Year'], y=dataframe['Manufacturing Emission'],
                         offsetgroup=0, name='Emission', visible=False),
                  secondary_y=False)

    fig.add_trace(go.Bar(x=dataframe['Year'], y=dataframe['Manufacturing Revenue'],
                         offsetgroup=1, name='Revenue', visible=False),
                  secondary_y=True)

    fig.add_trace(go.Bar(x=dataframe['Year'], y=dataframe['Industry Emission'],
                         offsetgroup=0, name='Emission', visible=False),
                  secondary_y=False)

    fig.add_trace(go.Bar(x=dataframe['Year'], y=dataframe['Industry Revenue'],
                         offsetgroup=1, name='Revenue', visible=False),
                  secondary_y=True)

    fig.update_layout(
        title_text=f"{group} Countries: Agriculture")

    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Emission Value (MTCO2e)", secondary_y=False)
    fig.update_yaxes(title_text="Revenue (US$)", secondary_y=True)

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="down",
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Agriculture", method="update",
                            args=[{"visible": [True, True, False, False, False, False]},
                                  {"title": f"{group} Countries: Agriculture"}]
                        ),
                        dict(
                            label="Manufacturing", method="update",
                            args=[{"visible": [False, False, True, True, False, False]},
                                  {"title": f"{group} Countries: Manufacturing"}]
                        ),
                        dict(
                            label="Industry", method="update",
                            args=[{"visible": [False, False, False, False, True, True]},
                                  {"title": f"{group} Countries: Industry"}]
                        )
                    ]
                )
            )
        ]
    )

    fig.show()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'allowed-io': [],
        'extra-imports': ['pandas', 'plotly.subplots', 'plotly.graph_objects',
                          'typing', 'python_ta.contracts'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)
