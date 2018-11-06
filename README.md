# SQL_Update_Statement_Generator
## Introduction
With the generate_update_statements script, one is able to generate SQL update statements in bulk. One only needs to provide a list of columns, list of values for each column, and a list of ids (for the where statement).

**Note:** 
* This script was tailored for the use of creating update statements for the 'Antibody Registry' mysql database. 
* This wasn't generalized for all-purpose use. 
* (There are better methods of doing bulk updating, but for now creating update statements in bulk fits the current needs)

## Preprocessing

