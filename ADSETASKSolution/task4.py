# Run file on system bash input file is 'task_four_input' and output is 'output.tsv'
# Command to run: 'python3 task4.py'
"""
Approach:

1) Cut is used to fetch the first column out of the input file using -f1 option and then that is piped.
2) Grep to find all the starting item names with Xerox -n oprtion to return line number in the input file.
3) Awk to order the columns as per the question line number should be added to last column
4) Sort command sorts  the output of last command on first field (column) as the key and -k ooption for that and 'r' to reverse the sort as ascending order.
5) Write the result in the output.tsv file.

"""
import os

taskFourcmd = 'cut -f1 task_four_input.tsv | grep -n \'^Xerox\' | awk -F: \'{print $2 \"\t\" $1}\' | sort -t\'|\' -k1r > output.tsv'

os.system(taskFourcmd)