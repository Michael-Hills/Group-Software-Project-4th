from datetime import date
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from .models import like_choices, dislike_choices


def CalculateAgeStr(dob):
    """ Function to calculate age from DOB which is a string"""

    # Retrieve current date
    today = date.today()

    #Calculate age
    age = today.year - int(dob[:4])

    return age

def calculateStep(max_y):
    """Function to calculate step size based on maximum y value"""

    # Define number of ticks on y axis
    num_ticks = 5

    # Calculate minimum step size to have max_ticks
    step = max_y / (num_ticks - 1)
        
    return step


def getConcernLevelChart(df, paramX):
        
    # Pivot table to get counts of concern level for each age group
    pivot_table = df.pivot_table(index= paramX + "_group", columns='concern_level', aggfunc='size', fill_value=0)

    # Sort concern level from low to high
    pivot_table = pivot_table[["Low","Medium","High"]]

    # Get maximum y value
    max_y = int(pivot_table.max().max())
    
    # Calculate step based on maximum y value 
    step = calculateStep(max_y)

    # Plot chart
    pivot_table.plot(kind='bar', stacked=False,  color=["#008000","#ffff00","#ff0000"])

    # Set labels of x axis
    plt.xlabel(paramX.capitalize())
    plt.ylabel("Number of persons")
    plt.xticks(rotation=0)

    # Set legend of chart
    plt.legend(loc="upper right")

    # Set title of chart
    plt.title("Concern level by " + paramX)

    # Set y axis size and step
    y_ticks = np.ceil(np.arange(0, max_y + 1, step=step)).astype(int)
    plt.yticks(y_ticks)

    plt.savefig('base\static\images\chart.png', transparent=True)

    return 1

def getLikesDislikesChart(df, paramX, paramY, age_labels):
    """ Function to create a chart based on likes and dislikes"""

    # Get tuple of choices depending on parameter y
    if paramY == "likes":
        choices = like_choices
    elif paramY == "dislikes":
        choices = dislike_choices

        # Change length of based on paramX
    if paramX == "age":
        # Index 0 will be index 0 of age_labels
        size_counts = len(age_labels)
    elif paramX == "gender":
        # Index 0 will be Male, 1 Female and 2 Other
        size_counts = 3
        
    # Create dictionary for each like to hold the count value of each gender or age group
    counts = {key[0]: [0] * size_counts for key in like_choices}

    # Iterate through each profile in the df
    for i, row in df.iterrows():
        # Get index based on gender
        if paramX == "gender":
            match row["gender"]:
                case "M":
                    idx = 0
                case "F":
                    idx = 1
                case "O":
                    idx = 2
        # Or get index based on age group
        elif paramX == "age":
            if row["age"] == 0:
                idx = 0
            if row["age"] < int(age_labels[1][-2:]):
                idx = 1
            elif row["age"] < int(age_labels[2][-2:]):
                idx = 2
            elif row["age"] < int(age_labels[3][-2:]):
                idx = 3
            elif row["age"] < int(age_labels[4][-2:]):
                idx = 4
                
        # Iterate through likes for a profile and add count to like/dislike and gender of that profile
        for item in row[paramY]:
            counts[item][idx] +=1

    # Plot grouped bar chart with labels
    x = np.arange(size_counts)
    bar_width = 0.25
    multiplier = 0

    # Set colormap for each like
    cmap = plt.get_cmap("prism")

    fig,ax = plt.subplots(layout="constrained")

    # Plot each grouped bar
    for item, count in counts.items():
        offset = bar_width * multiplier
        rects = ax.bar(x + offset, count, bar_width, label = item, color=cmap(multiplier / len(choices)))
        ax.bar_label(rects, padding=size_counts)
        multiplier += 1
    
    # Set labels and title
    ax.set_ylabel("Number of persons")
    ax.set_xlabel(paramX.capitalize())
    ax.set_title(paramY.capitalize() + " by " + paramX.capitalize())
    
    # Set label for each group of bars based on x parameter
    if paramX == "age":
        ax.set_xticks(x + bar_width, tuple(age_labels))
    elif paramX == "gender":
        ax.set_xticks(x + bar_width, ("M", "F", "O"))

    ax.legend(loc="upper right", ncols = size_counts)
    plt.show()

    plt.savefig('base\static\images\chart.png', transparent=True)
    
    return 1

def getBooleanChart(df, paramX, paramY, age_labels):
    """ Function to create a chart for the boolean fields """

    # Format title based on parameters x and y
    title = "How many take/are " + (paramY.split("_")[1]).capitalize()

    # Get amount of the selected y parameter
    pivot_table = df.pivot_table(index= paramX + "_group", columns=paramY, aggfunc='size', fill_value=0)
    
    # Reord pivot_table so True comes before False
    pivot_table = pivot_table.reindex(columns=[True, False])

    # Get maximum y value
    max_y = int(pivot_table.max().max())

    # Calculate step based on maximum y value 
    step = calculateStep(max_y)

    pivot_table.plot(kind='bar', stacked=False, color=["#ff0000","#008000"])

    # Set labels of x axis
    plt.xlabel(paramX.capitalize())
    plt.ylabel("Number of persons")
    plt.xticks(rotation=0)
    
    # Set legend of chart
    plt.legend(labels=["Yes", "No"])
    
    # Set title of chart
    plt.title(title)

    # Set y axis of size and step
    y_ticks = np.ceil(np.arange(0, max_y + 1, step=step)).astype(int)
    plt.yticks(y_ticks)
    
    plt.show()
    plt.savefig('base\static\images\chart.png', transparent=True)

    return 1

def getChart(df, paramY, paramX, chart_type):
    """ Function to create the chart for the data analysis page """
    
    # Get current year so age is always 0 into the future
    current_year = str(date.today().year)

    # Turn DOB None into the 1st of January of the current year so age is 0
    df["dob"] = df["dob"].fillna(current_year + "-01-01")

    # Calculate age based on DOB
    df["age"] = df["dob"].apply(CalculateAgeStr)

    age_labels = []

    # Create column grouped by parameter
    if paramX == "age":

        # Define age groups
        age_bins = [-1, 16, 30, 46, 65, 100]

        # Create age group labels
        age_labels = ['0', '16-29', '30-45', '46-65','65-99']

        # Bin ages into age groups
        df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)
    else:
        # For gender parameter there is no need to bin genders into gender groups
        df["gender_group"] = df["gender"]

    if paramY == "concern_level":
        return getConcernLevelChart(df, paramX)
    elif paramY == "likes" or paramY == "dislikes":
        return getLikesDislikesChart(df, paramX, paramY, age_labels)
    elif paramY == "is_homeless" or paramY == "is_alcoholic" or paramY == "using_drugs" or paramY == "taking_medication":
        return getBooleanChart(df, paramX, paramY, age_labels)

    return 0