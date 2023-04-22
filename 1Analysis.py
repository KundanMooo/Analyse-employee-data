import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbrn
df=pd.read_csv('D:\DS\Internshala\employee_promotionnnn.csv')
# Glancing data
df.head()
df.info()
df.isna().sum()
# What is the average salary of employees by department?
plt.figure(figsize=(15,2))
df1=df.groupby('department')['salary'].mean().reset_index().sort_values('salary',ascending=False)
print(df1)
plt.plot('department', 'salary', data=df1)
plt.xlabel('department')
plt.ylabel('salary')
plt.title('Average Salary by Department')
plt.show()
# What is the average salary of employees by department?
plt.figure(figsize=(15,2))
df1=df.groupby('department')['salary'].sum().reset_index().sort_values('salary',ascending=False)
print(df1)
plt.plot('department', 'salary', data=df1)
plt.xlabel('department')
plt.ylabel('salary')
plt.title('Average Salary by Department')
plt.show()
# Which department has the highest number of employees?
plt.figure(figsize=(10,5))
df2=df.groupby('department')['employee_id'].count().reset_index().sort_values('employee_id',ascending=False)
print(df2)
plt.plot('department', 'employee_id', data=df2)
plt.xlabel('department')
plt.ylabel('Number of employee')
plt.title('Number of employee by Department')
plt.show()
# # What is the distribution of gender in the company?
plt.figure(figsize=(5,2.5))
df3=df.groupby('gender')['employee_id'].count().reset_index()
plt.pie(df3.employee_id, labels=df3.gender, autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.show()
# Is there a correlation between years of experience and salary?
plt.figure(figsize=(5,2.5))

df2=df.groupby('Years of Experience')['salary'].mean().reset_index()
plt.plot('Years of Experience', 'salary', data=df2)
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary by experience')
plt.show()
plt.figure(figsize=(5,2.5))

df2=df.groupby('Years of Experience')['salary'].count().reset_index()
plt.plot('Years of Experience', 'salary', data=df2)
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary by experience')
plt.show()