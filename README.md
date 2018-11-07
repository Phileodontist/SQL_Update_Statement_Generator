# SQL_Update_Statement_Generator
## Introduction
With the generate_update_statements script, one is able to generate SQL update statements in bulk. One only needs to provide a list of columns, list of values for each column, and a list of ids.

**Note:** 
* This script was tailored for the use of creating update statements for the 'Antibody Registry' mysql database. 
* This wasn't generalized for all-purpose use. 
* (There are better methods of doing bulk updating, but for now creating update statements in bulk fits the current needs)

## Input
The generate_update_statements script requires three files as input when being executed in the command line, the first file being the list of columns, the second being a list of values for each column, and lastly a list of ids (for the where statement).
 
### Preprocessing
In order to run the script, one needs to preform some preprocessing to get the input into a particular format. Below presents the format that is required and how one can get their data in that format.

**Formating:** [columns.txt](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/columns.txt), [values.txt](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/values.txt), [ids.txt](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/ids.txt)

**Transform: 
<br/> (Using the transform.py script to convert a file such as [this](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/ids.txt) into the format shown in the values.txt & ids.txt files)** 

1. To transform one's data into the format as seen in the values.txt file, one has to create a separate file for each column for their values. **Ex:** [val1.txt](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/val1.txt), [val2.txt](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/val2.txt), [val2.txt](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/val3.txt)
2. By running the following command, one is able to convert these files into one file to use as the 'values file' for the generate_update_statements script: `python transform.py val1.txt val2.txt val3.txt > example_output.txt`

</br>**Note:** The same thing can be done for the ids.txt file. `python transform.py ids_list.txt > ids.txt`

### Executing the Script
After performing the preprocessing step, one is now able to execute the generate_update_statements script by running the following command: `python generate_update_statements columns.txt values.txt ids.txt > example_output.txt` 
<br/>[The end result](https://github.com/Phileodontist/SQL_Update_Statement_Generator/blob/master/example_output.txt)

<br/>**Note:** This script is currently written to hand only one statement in the 'where' clause.
