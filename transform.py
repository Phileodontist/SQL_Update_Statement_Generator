import sys

# Converts each file into its own array
temp_arr = []
for arg in sys.argv[1:]:
    with open(arg, 'r') as f:
        temp_arr.append([line.replace('\n', '') for line in f.readlines()])

# Transforms every array into a single string
for index, value in enumerate(temp_arr):
    final_str = "; ".join(temp_arr[index])
    # Removes tailing semi-colon
    print(final_str[0:len(final_str)])
