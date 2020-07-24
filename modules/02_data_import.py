# 02 - import data and check dataset

# nytimes dataset
# source: https://github.com/nytimes/covid-19-data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"

# load data from url
df_total = pd.read_csv(url)

# subset data by state
# https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
df_california = df_total[df_total['state'] == 'California']

# show tabel info
df_california.info()

# show summary statistics
df_california['cases'].describe()
