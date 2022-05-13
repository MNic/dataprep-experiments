# Example, intended to be run line-by-line interactively.
import pandas as pd
from model.data.lib.iris import dataset

# Convert list of dataclasses into dataframe
df = pd.DataFrame(dataset.data)
df.head()

# Render information about the dataset from the imported dataset wrapper object
dataset.size
dataset.fields
dataset.sample()
dataset.asjson()[0:2]