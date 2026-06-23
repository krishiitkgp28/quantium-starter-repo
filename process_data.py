import csv
import glob
import os

# Define input and output paths
data_folder = "data/"
output_file = "formatted_output.csv"

# Use glob to find all .csv files in the data folder
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

# Open output file for writing
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    # Write header
    writer.writerow(["Sales", "Date", "Region"])

    # Process each CSV file
    for file_path in csv_files:
        with open(file_path, mode='r') as infile:
            reader = csv.reader(infile)
            header = next(reader)   # skip header row

            for row in reader:
                # row structure: product, price, quantity, date, region
                product = row[0]
                # Only keep pink morsels
                if product == "pink morsel":
                    # Clean price: remove '$' and convert to float
                    price_str = row[1].replace('$', '')
                    price = float(price_str)
                    quantity = int(row[2])
                    sales = price * quantity
                    date = row[3]
                    region = row[4]

                    # Write the processed row
                    writer.writerow([sales, date, region])

print(f"Processing complete. Output written to {output_file}")