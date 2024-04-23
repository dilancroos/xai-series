# %% Imports
import matplotlib.pyplot as plt
from utils import DataLoader

# %% Load data
data_loader = DataLoader()
data_loader.load_dataset()
data = data_loader.data

# %% Show head
print(data.shape)
data.head()

# %% Show general statistics
data.info()

# %% Show histogram for all columns
columns = data.columns
for col in columns:
    print("col: ", col)
    data[col].hist()
    plt.show()

# %% Show preprocessed dataframe
data_loader.preprocess_data()

# %% Show head
data_loader.data.head()

# %% Show info
data_loader.data.info()

# %% Change False to 0 and True to 1 in all columns
# data_loader.data = data_loader.data.astype(int)

# %% Show head
# data_loader.data.head()

# %% Show info
# data_loader.data.info()

# %%
