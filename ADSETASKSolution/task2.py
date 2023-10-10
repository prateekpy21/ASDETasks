"""
Python Script to read data from csv and write output the top 3 deparrtment and their names based on avgerage montly salary
'./ASDE Assignment' - Departments.csv -> CSV for department and their names data
'./ASDE Assignment' - Employees.csv  -> CSV for employees  and their deparment data
'./ASDE Assignment'- Salaries.csv  -> CSV for salaries per month of each employee data
"""
import csv # To perform csv operations
from collections import defaultdict

# To store data from each CSV defining dictionaries
departments_data = {}
employees_data   = {}
salaries_data = defaultdict(list)

# Read the departments file into a dictionary where keys are ids and values are names:
with open('./datafiles/departments.csv','r') as deptCsvFile:
    deptReader=csv.DictReader(deptCsvFile)
    for row in deptReader:
        departments_data[row['dept_id']] = row['dept_name']

#Read the employees file into a dictionary where keys are emp ids and values are dept ids:
with open("./datafiles/employees.csv", 'r')as empCsvFile:
    empReader=csv.DictReader(empCsvFile)
    for row in empReader:
        employees_data[row['emp_id']] = row['dept_id']

#Read the salaries file into a dictionary where keys are (emp id,month),values are salary amount:
with open('./datafiles/salaries.csv','r') as salaryCsvFile:
    salaryReader=csv.DictReader(salaryCsvFile)
    for row in salaryReader:
        emp_id = row['emp_id']
        salary_month = row['salary_month']
        salary_amt = float(row['amt'])

        # Find the employees based on emp_ids department and store in the dept_id
        if emp_id in employees_data:
            dept_id = employees_data[emp_id]
            # Find the department names for dept_id coming from above
            if dept_id in departments_data:
                dept_name = departments_data[dept_id]
                # Store slary data by department and month
                salaries_data[(dept_name, salary_month)].append(salary_amt)

# Calculate the average monthly salary and department rank
monthly_avg_salaries = defaultdict(list)
for (dept_name,salary_month) , salaries in salaries_data.items():
    avg_salary = sum(salaries) / len(salaries)
    monthly_avg_salaries[salary_month].append((dept_name,avg_salary))

# Stores the final result 
salary_per_dept_data = []
salary_per_dept_data_csv=[]
for salary_month,department_avg_salaries in monthly_avg_salaries.items():
    department_avg_salaries.sort(key=lambda x:x[1],reverse=True)
    for rank,(dept_name,avg_salary) in enumerate(department_avg_salaries,start=1):
        salary_per_dept_data.append((dept_name,avg_salary,rank))
        #salary_per_dept_data_csv.append({'DEPT_NAME': dept_name, 'AVG_MONTHLY_SALARY (USD)': avg_salary,'Rank': rank})
    for dept_name,avg_salary in department_avg_salaries[:3]:
        salary_per_dept_data_csv.append({'DEPT_NAME': dept_name, 'AVG_MONTHLY_SALARY (USD)': avg_salary})
        

# Filter the data based on condition as top 3 are only required per month 
top_three_dept_data = [(dept_name,avg_salary) for dept_name,avg_salary,rank in salary_per_dept_data if rank <=3]

#top_three_dept_data_csv = [row for row in salary_per_dept_data_csv if row['Rank'] <=3]

# Print the result
for dept_name,avg_salary in top_three_dept_data:
    print(f'DEPT_NAME: {dept_name}, AVG_MONTHLY_SALARY (USD): {avg_salary:.2f}')

# Defination for filename for writing the result in the output file
output_csv_file = './datafiles/task2_csv_file.csv'

# Write to resulted data to the output csv file
with open(output_csv_file,'w',newline='') as outputFile:
    fieldNames = ['DEPT_NAME','AVG_MONTHLY_SALARY (USD)']
    writerObj = csv.DictWriter(outputFile,fieldnames=fieldNames)

    #Write headers first
    writerObj.writeheader()

    # Write the data
    writerObj.writerows(salary_per_dept_data_csv)









