import seaborn as sns
tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')
titanic

import matplotlib.pyplot as plt

sns.histplot(titanic['age'].dropna(), kde=True)
plt.title('Distribution of Age')
plt.show()


sns.countplot(x='class', hue='survived', data=titanic)
plt.title('Survival Count by Class')
plt.show()

sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

sns.scatterplot(x='age', y='fare', data=titanic, hue='survived', palette='coolwarm')
plt.title('Age vs Fare by Survival')
plt.show()

survival_rate_by_class = titanic.groupby('pclass')['survived'].mean()
survival_rate_by_class.plot(kind='bar', color='skyblue')
plt.title('Survival Rate by Pclass')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.xticks(rotation=0)
plt.show()

sns.heatmap(titanic.isnull(), cbar=False, cmap='viridis')
plt.title('Missing dataaa')
plt.show()

sns.boxplot(x='survived', y='fare', data=titanic)
plt.title('Fare dstrbute')
plt.show()

