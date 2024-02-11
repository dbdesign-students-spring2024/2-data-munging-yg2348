# munge.py

def convert_celsius_to_fahrenheit(celsius):
    # Formula to convert Celsius to Fahrenheit
    return (celsius / 100) * 9/5 + 32

def center_align_headings(headings_line, columns):
    # Calculate the column widths dynamically based on the maximum length of the column names
    widths = [max(len(col), len("NaaN")) + 2 for col in columns]

    # Format the headings with center alignment
    formatted_headings = ' |'.join(col.center(width-1) for col, width in zip(columns, widths))

    return formatted_headings

def center_align_year(year_line, columns):
    # Calculate the column widths dynamically based on the maximum length of the numbers in each column
    widths = [max(len(col), len("NaaN"), len("Year")) + 1 for col in columns]

    # Format the year line with center alignment
    formatted_year_line = '|'.join(str(val).center(width ) if val.isdigit() or val == 'Year' else val.center(width) for val, width in zip(year_line.split(), widths))

    return formatted_year_line

def clean_and_transform_data(raw_data_filename, cleaned_data_filename):
    # Read the raw data file
    with open(raw_data_filename, 'r') as raw_file:
        lines = raw_file.readlines()

    # Extract and keep the first line of column headings
    headings_line = next(line for line in lines if line.startswith('Year'))

    # Extract columns from headings
    columns = headings_line.split()
   

    # Remove duplicate lines of column headings
    cleaned_lines = [center_align_headings(headings_line, columns)]
    headings_found = False

    for line in lines:
        if line.startswith('Year') and not headings_found:
            headings_found = True
        elif line.startswith('Year'):
            continue
        elif line.startswith('L'):
            cleaned_lines.append(line)
        else:
            values = line.split()

            if len(values) == len(columns):
                year = values[0]
                anomalies = [float(val) if val.replace('.', '').replace('-', '').isdigit() else None for val in values[1:]]
     
                cleaned_lines.append(f'{center_align_year(year, columns)} | {" | ".join("NaaN" if val is None else format(convert_celsius_to_fahrenheit(val), ".1f") for val in anomalies)}')

    with open(cleaned_data_filename, 'w') as cleaned_file:
        cleaned_file.write('\n'.join(cleaned_lines))
# Rest of the code remains unchanged...

if __name__ == "__main__":
    # Specify the filenames
    raw_data_filename = 'data/raw_data.txt'
    cleaned_data_filename = 'data/clean_data.csv'

    # Call the clean_and_transform_data function
    clean_and_transform_data(raw_data_filename, cleaned_data_filename)
