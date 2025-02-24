# %%
import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/Lenovo/Downloads/insurance.csv')

# Display the first few rows
print(df.head())

# %%
# Check dataset info
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())

# %%
# Check unique values in categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    print(f"{col}: {df[col].unique()}")

# %%
// pip install seaborn # type: ignore


# %%
# Correlation matrix for numerical variables
import seaborn as sns
import matplotlib.pyplot as plt

# Select only numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])

corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# %%
# Pairplot for numerical variables
sns.pairplot(df)
plt.show()

# %%
# Group by a categorical variable (e.g., 'smoker') and analyze numerical variables
grouped = df.groupby('smoker')['charges'].mean()
print(grouped)
# Group by a categorical variable (e.g., 'smoker') and analyze numerical variables
grouped = df.groupby('sex')['charges'].mean()
print(grouped)
# Group by a categorical variable (e.g., 'smoker') and analyze numerical variables
grouped = df.groupby('region')['charges'].mean()
print(grouped)

# %%
# pip install scipy

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway, chi2_contingency



# Add a new column to categorize 'charges' into bins for Chi-Square test
df['charges_category'] = pd.cut(df['charges'], bins=[0, 10000, 30000, float('inf')], labels=['low', 'medium', 'high'])

# List of categorical and numerical variables
categorical_vars = ['sex', 'smoker', 'region']
numerical_vars = ['age', 'bmi', 'children']

# Perform ANOVA for categorical variables
print("ANOVA Results:")
for cat_var in categorical_vars:
    categories = df[cat_var].unique()
    groups = [df[df[cat_var] == category]['charges'] for category in categories]
    f_stat, p_value = f_oneway(*groups)
    print(f"{cat_var} vs charges - F-statistic: {f_stat:.2f}, P-value: {p_value:.4f}")

# Perform Chi-Square test for categorical variables vs charges_category
print("\nChi-Square Results:")
for cat_var in categorical_vars:
    contingency_table = pd.crosstab(df[cat_var], df['charges_category'])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    print(f"{cat_var} vs charges_category - Chi2: {chi2:.2f}, P-value: {p:.4f}")

# Perform Correlation for numerical variables
print("\nCorrelation Results:")
for num_var in numerical_vars:
    correlation = df[num_var].corr(df['charges'])
    print(f"{num_var} vs charges - Correlation: {correlation:.2f}")

# Visualizations
# Boxplots for categorical variables vs charges
plt.figure(figsize=(15, 5))
for i, cat_var in enumerate(categorical_vars, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(x=cat_var, y='charges', data=df)
    plt.title(f'{cat_var} vs Charges')
plt.tight_layout()
plt.show()

# Scatterplots for numerical variables vs charges
plt.figure(figsize=(15, 5))
for i, num_var in enumerate(numerical_vars, 1):
    plt.subplot(1, 3, i)
    sns.scatterplot(x=num_var, y='charges', data=df, hue='smoker')
    plt.title(f'{num_var} vs Charges')
plt.tight_layout()
plt.show()
# %%
