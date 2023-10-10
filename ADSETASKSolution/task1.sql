/*
===================================================================
*********** Please note : Run on MySQL version 8 **********************
===================================================================  
Fetch top 3 departments along with their name and average monthly salary. Below is the format of the report.
DEPT_NAME | AVG_MONTHLY_SALARY (USD)

Schema name for the database is 'onlinesalesaidb'. Please replace the same during execution 
with your database name.
There are three tables please replace the names accordingly. 
Departments -> dept_id(PK), dept_name
Employees -> emp_id (PK), emp_name, dept_id(FK)
Salaries -> emp_id(FK),salary_month,salary_amt

*/
---------------------------- Query -----------------------:


SELECT 
    d.dept_name AS DEPT_NAME,
    /* The sum is divided by the count of distinct months 
    to calculate the average per month for each department*/
    sum(s.salary_amt)/count(distinct(s.SALARY_MONTH)) AS `AVG_MONTHLY_SALARY (USD)`
FROM 
    onlinesalesaidb.departments d
/* Join the three tables to get the data respectively
*/
JOIN 
    onlinesalesaidb.employees e ON d.dept_id = e.dept_id
JOIN 
    onlinesalesaidb.salaries s ON e.emp_id = s.emp_id
/*
Grouping the the data based on dept_name
*/
GROUP BY 
    d.dept_name
/*
To filter as per the request of fetching top 3 data
*/
ORDER BY 
    `AVG_MONTHLY_SALARY (USD)` DESC
LIMIT 3;
