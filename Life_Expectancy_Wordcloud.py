from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
file_path = '/Users/kunzhang/Desktop/Life expectancy Data.csv'
data = pd.read_csv(file_path)

# Standardize column names by stripping extra spaces
data.columns = data.columns.str.strip()

# Select relevant columns
relevant_columns = [
    'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure',
    'Hepatitis B', 'Measles', 'BMI', 'under-five deaths', 'Polio',
    'Total expenditure', 'Diphtheria', 'HIV/AIDS', 'GDP', 'Population',
    'thinness  1-19 years', 'thinness 5-9 years',
    'Income composition of resources', 'Schooling'
]

# Compute correlations with Life Expectancy
correlation = data[relevant_columns + ['Life expectancy']].corr()['Life expectancy']

# Find columns with high correlation (absolute correlation >= 0.5)
threshold = 0.5
high_correlation = correlation[correlation.abs() >= threshold]

# Sort the results
high_correlation = high_correlation.sort_values(ascending=False)

# Display the results
print("Columns with a high correlation with Life Expectancy:")
print(high_correlation)

# Prepare data for the word cloud (absolute correlation as importance)
wordcloud_data = correlation.drop('Life expectancy').abs().to_dict()

# Generate the word cloud with a custom background color
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='lightpink',  # Set background color
).generate_from_frequencies(wordcloud_data)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Factors Influencing Life Expectancy", fontsize=16)
plt.show()

