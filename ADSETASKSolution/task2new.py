"""
Python Script to read data from csv and write output the top 3 deparrtment and their names based on avgerage montly salary
'./datafiles/departments.csv' - Departments.csv -> CSV for department and their names data
'./datafiles/employees.csv' - Employees.csv  -> CSV for employees  and their deparment data
'./datafiles/salaries.csv'- Salaries.csv  -> CSV for salaries per month of each employee data
'./datafiles/joined_data.csv'- joined_data.csv  -> CSV for Joined data with department and salary amount and month
'./datafiles/top_departments.csv'- top_departments.csv  -> CSV for retruning the top 3 department with their names.
"""

"""
Approach 

1) Define data as Dictionaries for all three tables.
2) Combine the data file to getdepartment id, salary amount and month data and save into new file.
3) From the new file read the data and group and find the average of each department.
4) Return result of top three and write into output file.
"""

import csv
from collections import defaultdict

# Create dictionaries to store data from CSV files
departments_data = {}
employees_data = {}
salaries_data = {}

# Read data from departments.csv
with open('./datafiles/departments.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        departments_data[row['dept_id']] = row['dept_name']

# Read data from employees.csv
with open('./datafiles/employees.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees_data[row['emp_id']] = {'dept_id': row['dept_id']}

# Read data from salaries.csv
with open('./datafiles/salaries.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        emp_id = row['emp_id']
        salary_amt = float(row['salary_amt'])
        salary_month = row['salary_month']

        if emp_id not in salaries_data:
            salaries_data[emp_id] = {'salaries': []}

        salaries_data[emp_id]['salaries'].append({'amt': salary_amt, 'month': salary_month})

# Create a list to store the joined data
joined_data = []

# Perform the join of all three tables
for emp_id, emp_data in employees_data.items():
    dept_id = emp_data['dept_id']
    if emp_id in salaries_data:
        salaries = salaries_data[emp_id]['salaries']
        for salary in salaries:
            joined_data.append({'dept_id': dept_id, 'salarymonth': salary['month'], 'salary amount': salary['amt']})

# Define the output CSV file path
output_file = './datafiles/joined_data.csv'

# Write the joined data to the new CSV file
with open(output_file, mode='w', newline='') as file:
    fieldnames = ['dept_id', 'salarymonth', 'salary amount']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in joined_data:
        writer.writerow(row)

print(f'Joined data has been written to {output_file}')

#==============================================================================

# Create a dictionary to store salaries and months by department
department_salaries = defaultdict(list)

# Read data from joined_data.csv
with open('./datafiles/joined_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dept_id = row['dept_id']
        salary_amt = float(row['salary amount'])
        salary_month = row['salarymonth']
        
        department_salaries[dept_id].append((salary_amt, salary_month))

# Calculate the average monthly salary for each department
average_monthly_salaries = {}
for dept_id, salaries in department_salaries.items():
    total_salary = 0
    unique_months = set()
    for salary, month in salaries:
        total_salary += salary
        unique_months.add(month)
    
    average_salary = total_salary / len(unique_months)
    average_monthly_salaries[dept_id] = average_salary

# Get the top 3 departments by average monthly salary
top_3_departments = sorted(average_monthly_salaries.items(), key=lambda x: x[1], reverse=True)[:3]

# Read department names from departments.csv
department_names = {}
with open('./datafiles/departments.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        department_names[row['dept_id']] = row['dept_name']

# Create and write the results to the output CSV file using DictWriter
output_file = './datafiles/top_departments.csv'
fieldnames = ['DEPT_NAME', 'AVG_MONTHLY_SALARY (USD)']

with open(output_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for dept_id, avg_salary in top_3_departments:
        dept_name = department_names.get(dept_id)
        writer.writerow({'DEPT_NAME': dept_name, 'AVG_MONTHLY_SALARY (USD)': f'{avg_salary:.2f}'})

print(f'Top 3 Departments by Average Monthly Salary written to {output_file}')
