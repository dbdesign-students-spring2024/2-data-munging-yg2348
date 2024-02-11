import csv

def calculate_decade_average(data, start_year, end_year):
    decade_data = [row for row in data if start_year <= int(row[0]) <= end_year]
    
    if not decade_data:
        return None  # No data for the specified decade

    anomalies = [float(anomaly) for anomaly in decade_data[0][1:]]
    
    for row in decade_data[1:]:
        anomalies = [anomaly + float(val) for anomaly, val in zip(anomalies, row[1:])]

    avg_anomalies = [anomaly / len(decade_data) for anomaly in anomalies]
    return avg_anomalies

def main():
    # Specify the cleaned data filename
    cleaned_data_filename = 'data/clean_data.csv'

    # Read the cleaned data file using the csv module
    with open(cleaned_data_filename, 'r') as cleaned_file:
        reader = csv.reader(cleaned_file, delimiter='|')
        data = [row for row in reader if row and row[0].strip().isdigit()]  # Skip non-numeric or empty rows

    if not data:
        print("No valid data found.")
        return

    # Output the data for debugging
    print("Data:")
    for row in data:
        print(row)

    # Output average temperature anomaly for each decade
    start_year = 1880
    end_year = 1889

    while end_year <= int(data[-1][0]):
        avg_anomalies = calculate_decade_average(data, start_year, end_year)

        if avg_anomalies is not None:
            print(f'{start_year} to {end_year}: {avg_anomalies[0]:.2f} F')
        
        start_year += 10
        end_year += 10

if __name__ == "__main__":
    main()
