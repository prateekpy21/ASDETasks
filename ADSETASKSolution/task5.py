# Run file on system bash
# Command to run: 'python3 task5.py'

"""
Approach:

1) find command to find the all files using '.' since we are only looking for sub folder we use maxdepth as 1 i.e. one level only.
2) -type options to define the type since we arelooking for files. 
3) stat command to have %U %G for user and group information and run on each level and group them as one. 
4) cut the output to display as only the groups.
5) Sort for sorting the result. 
"""

import os
taskcmd = 'find . -maxdepth 1 -type f -exec stat -c "%U %G" {} + | cut -d\' \' -f2 | sort -u'
os.system(taskcmd)