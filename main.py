"""CSC110 Fall 2020 Project Phase 2

Instructions (READ THIS FIRST!)
===============================

Run this module in python console to generate outputs.

Do not edit any function statements in this module, except
commenting and uncommenting the plot_graph functions.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of TAs and
instructors of  CSC110 at the University of Toronto St. George campus.
All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2020 Jia Hao Choo and Komal Saini.
"""
from init_dataclass import init_countries
from computation import filter_country, find_emission_average, find_average_revenue
from display_graph import create_dataframe, plot_graph

if __name__ == '__main__':

    #  Read data from csv and create dataclass objects for use in computations:
    #  This function uses other functions from init_dataclass and read_csv
    #  to automatically read data from csv files and create dataclass objects.
    countries = init_countries()

    #  Filter the countries list into four different mappings according to
    #  their income classifications.
    high = filter_country(countries, 'High income')
    upper_middle = filter_country(countries, 'Upper middle income')
    lower_middle = filter_country(countries, 'Lower middle income')
    low = filter_country(countries, 'Low income')

    #  Find the average emission value of each sector for each income classification.
    high_average_emission = find_emission_average(high)
    upper_middle_average_emission = find_emission_average(upper_middle)
    lower_middle_average_emission = find_emission_average(lower_middle)
    low_average_emission = find_emission_average(low)

    #  Find the average revenue of each sector for each income classification.
    high_average_revenue = find_average_revenue(high)
    upper_middle_average_revenue = find_average_revenue(upper_middle)
    lower_middle_average_revenue = find_average_revenue(lower_middle)
    low_average_revenue = find_average_revenue(low)

    #  Combine averages into one dict
    high_income = {}
    high_income.update(high_average_emission)
    high_income.update(high_average_revenue)

    upper_middle_income = {}
    upper_middle_income.update(upper_middle_average_emission)
    upper_middle_income.update(upper_middle_average_revenue)

    lower_middle_income = {}
    lower_middle_income.update(lower_middle_average_emission)
    lower_middle_income.update(lower_middle_average_revenue)

    low_income = {}
    low_income.update(low_average_emission)
    low_income.update(low_average_revenue)

    #  Creating dataframe objects
    high_income_df = create_dataframe(high_income)
    upper_middle_income_df = create_dataframe(upper_middle_income)
    lower_middle_income_df = create_dataframe(lower_middle_income)
    low_income_df = create_dataframe(low_income)

    #  Plotting - default graph is for High Income countries
    plot_graph(high_income_df, 'High Income')

    #   If you want to see the graph for upper middle income countries,
    #   uncomment the code below, and comment out other plot_graph functions.
    # plot_graph(upper_middle_income_df, 'Upper Middle Income')

    #   If you want to see the graph for lower middle income countries,
    #   uncomment the code below, and comment out other plot_graph functions.
    # plot_graph(lower_middle_income_df, 'Lower Middle Income')

    #   If you want to see the graph for low income countries,
    #   uncomment the code below, and comment out other plot_graph functions.
    # plot_graph(low_income_df, 'Low Income')
