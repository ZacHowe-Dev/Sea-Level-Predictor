import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(
        'epa-sea-level.csv',
        index_col=0
    )
    x = df.index
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    # Create first line of best fit
    result = linregress(x, y)
    slope = result.slope
    intercept = result.intercept
    line_x = pd.Series([i for i in range(1880,2051)])
    line_y = slope * line_x + intercept
    plt.plot(line_x, line_y, color="red", label="Line of Best Fit")

    # Create second line of best fit
    df_2000 = df.copy()
    df_2000 = df_2000[(df_2000.index >= 2000)]
    x2 = df_2000.index
    y2 = df_2000['CSIRO Adjusted Sea Level']
    result2 = linregress(x2, y2)
    slope2 = result2.slope
    intercept2 = result2.intercept
    line_x2 = pd.Series([i for i in range(2000,2051)])
    line_y2 = slope2 * line_x2 + intercept2
    plt.plot(line_x2, line_y2, color="blue", label="Line of Best Fit2")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
