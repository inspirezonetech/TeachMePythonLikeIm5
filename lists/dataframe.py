# ------------------------------------------------------------------------------------
# Tutorial: creating a dataframe from lists
# ------------------------------------------------------------------------------------
# Think of a dataframe as an excel spreadsheet. All it is is a two-dimensional structure consisting of rows and columns.
# Here I'll show you how to create a datframe with three columns using a list of lists.
# Remember a list is created using square brackets []. So list of lists is different lists all wraped in a square bracket i.e. [['Sophie'], ['Jade']]
# PS: anywhere you see a step, remove the hashtag before the code and remove everything in the bracket (). This does not include step 2!
# e.g. in your practice, copy only "import pandas as pd" not "# import pandas as pd (step 2)"

# Firstly, pip install pandas then import pandas as pd
# pip install pandas (step 1)
# import pandas as pd (step 2)
# Creating a list of lists with two strings and an integer each
list = [['Purple Hibiscus', 'Chimamanda', 2001], ['Things Fall Apart', 'Chinua', 1980]]  # Step 3

# Storing the transformation from list to dataframe in a variable
# df means dataframe but you can call your variable anything
# df = pd.DataFrame(list, columns=['BookTitle', 'AuthorFirstName', 'YearPublished']) (Step 4)
# df (step 5)

# There are different ways to create a dataframe from lists. This was just one of them!

# ------------------------------------------------------------------------------------
# Challenge: get the right answer !
#  1. Make your own list of lists
#  2. Store it in another variable that is not called df
#  3. Create a dataframe from it
# ------------------------------------------------------------------------------------
