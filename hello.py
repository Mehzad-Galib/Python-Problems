import matplotlib.pyplot as plt
import pandas as pd

# creating bar chart
data = {'CSE': {2017: 15, 2018: 20, 2019: 51, 2020: 36, 2021: 59},
        'EEE': {2017: 49, 2018: 33, 2019: 28, 2020: 71, 2021: 11}, 'ME': {2017: 69, 2018: 66, 2019: 37, 2020: 15, 2021: 47},
        'ChE': {2017: 87, 2018: 32, 2019: 24, 2020: 27, 2021: 75}, 'URP': {2017: 5, 2018: 3, 2019: 4, 2020: 8, 2021: 2}
        }

df = pd.DataFrame(data)
print(df)

fig = df.plot.bar()
plt.show()

# creating pie chart for dept wise students
data_dept = pd.DataFrame({
    'students': [156, 222, 234, 333, 50], 'dept': ['CSE', 'EEE', 'ME', 'CHE', 'URP']})

data_dept.groupby(['dept']).sum().plot(kind='pie', y='students',
                                       autopct='%1.0f%%', title='Dept wise Students went to study abroad')
plt.show()

# creating pie chart for year wise students
data_yearly = pd.DataFrame({
    'students': [221, 154, 131, 164, 252], 'year': ['2017', '2018', '2019', '2020', '2021']})

data_yearly.groupby(['year']).sum().plot(kind='pie', y='students',
                                         autopct='%1.0f%%', title='Year wise Students went to study abroad')

plt.show()
