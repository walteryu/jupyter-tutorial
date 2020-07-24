# 03 - data plot example and please add you own too!

# set plot size and title
plt.figure(figsize=(8, 12))
plt.title('Count Plot: Total Case Count in CA by County')

# create countplot and sort categories by value
# https://stackoverflow.com/questions/46623583/seaborn-countplot-order-categories-by-count
sns.countplot(
    y="county",
    data=df_california,
    order = df_california['county'].value_counts().index
)
