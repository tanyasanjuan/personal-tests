# Data correlations
# Finding Relationships, 
# The corr() method calculates the relationship between each column in the data set.
# The corr() method ignores "not numeric" columns.

import pandas as pd
df = pd.read_csv('datacorrelation.csv')
print(df.corr())

# The Result of the corr() method is a table with a lot of numbers 
# that represents how well the relationship is between two columns.
# The number varies from -1 to 1.
    # 1 means that there is a 1 to 1 relationship (a perfect correlation), 
    # and for this data set, each time a value went up in the first column, the other one went up as well.
    # 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
    # -0.9 would be just as good relationship as 0.9, but if you increase one value, 
    # the other will probably go down.
    # 0.2 means NOT a good relationship, 
    # meaning that if one value goes up does not mean that the other will.

#In this dataset:   
# Perfect correlation: "Duration" and "Duration" got the number 1.000000, 
# which makes sense, each column always has a perfect relationship with itself.

# Good Correlation: "Duration" and "Calories" got a 0.922721 correlation, 
# which is a very good correlation, and we can predict that the longer you work out, the more calories you burn,
# and the other way around: 
# if you burned a lot of calories, you probably had a long work out.

# Bad correlation: "Duration" and "Maxpulse" got a 0.009403 correlation, 
# which is a very bad correlation, meaning that we can not predict the max pulse 
# by just looking at the duration of the work out, and vice versa.

# Plotting
# Pandas use the plot() method to create diagrams.
# we can use pyplot, a submodule of the Matplotlib library, to show the diagrams.
import matplotlib.pyplot as plt
df.plot()
plt.show()
# The plot() method will create a line for each column in the DataFrame.
# The plt.show() method will display the diagram.

# Kind argument
# The plot() method can take an argument called 'kind' to specify the kind of diagram.
# If we want a scatter plot, we need to specify an X and Y axis.

# Here we will create a scatter plot, with "Duration" on the X axis, and "Calories" on the Y axis:
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()
# The result will be a scatter plot diagram, with dots representing the values from the two columns