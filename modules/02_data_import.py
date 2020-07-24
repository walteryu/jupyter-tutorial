# nytimes dataset
# source: https://github.com/nytimes/covid-19-data

# load data via url
# https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url/41880513#41880513
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
df_total = pd.read_csv(url)

# nytimes dataset: filter by state
# https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
df_california = df_total[df_total['state'] == 'California']

# show columns and datatypes
df_california.info()
