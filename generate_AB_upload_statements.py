import sys

def trailing_error(values, columns):
    # Throw Error if semi-colon is found in values; 
    # Probably not needed anymore with the transform.py script
    trailing_error = 0
    for index in range(len(values)):
        if (';' in values[index][len(values[len(values)-1])-1]):
            print("ERROR: Remove tailing ';' in the last value of the '{}' column in the values file".format(columns[index]))
            print('\t --> ' +  values[index][len(values[len(values)-1])-1])
            trailing_error = 1
    
    # Exits if Invalid values
    if (trailing_error == 1):
        exit()


def main():

    if (len(sys.argv) < 3):
        print('(Error: Insufficient arguments) Ex: python generate_AB_upload_statements.py columns.txt values.txt ids.txt')
        exit()

    # Columns, Values, Where statement
    column_list = sys.argv[1]
    value_list = sys.argv[2]
    id_list = sys.argv[3]

    with open(column_list, "r") as file1:
        columns = [line.replace('\n', '') for line in file1.readlines()]

    with open(value_list, "r") as file2:
        values = [line.replace('\n', '').split('; ') for line in file2.readlines()]

    with open(id_list) as file3:
        id_values = [line.replace('\n', '').split('; ') for line in file3.readlines()]

    # Check Values
    trailing_error(values, columns)

    update_statement_base = "update antibody_table set "

    # Generates set statements
    column_str_arr = []
    for column, column_value_arr in zip(columns, values):
        string_list = []
        if (column == 'comments'):
            for value in column_value_arr:
                set_string = "{}=concat(comments, '; ', '{}')".format(column,value)
                string_list.append(set_string)
        else:
            for value in column_value_arr:
                set_string = "{}='{}'".format(column,value)
                string_list.append(set_string)
        column_str_arr.append(string_list)

    update_statement_list = []
    # Set update statement with first column
    for index, set_block in enumerate(column_str_arr[0]):
        if (len(columns) == 1):
            update_statement_final = update_statement_base + set_block \
            + " where id='{}';".format(id_values[0][index])
            update_statement_list.append(update_statement_final)
        else:
            update_statement_final = update_statement_base + set_block
            update_statement_list.append(update_statement_final)

    update_statement_list_final = []
    # Appends the rest of the columns & id statement
    for count, str_arr in enumerate(column_str_arr):
        if (count == 0):
            continue
        if (count < len(columns) - 1):
            for index, set_block in enumerate(str_arr):
                update_statement_list[index] = update_statement_list[index] \
                + ', ' + set_block
        else:
            for index, set_block in enumerate(str_arr):
                update_statement_list_final.append(update_statement_list[index] \
                + ', ' + set_block + " where id='{}';".format(id_values[0][index]))

    # Prints the final version of the update statements
    for statement in update_statement_list_final:
        print(statement.replace('^M', ''))

if __name__ == "__main__":
    main()
