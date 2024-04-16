import tabula
from tabula import read_pdf

def extract_tables_from_pdf(pdf_path):
    # Read PDF file
    # 'pages' argument can be set to 'all' or specific numbers like '1,2,3' or ranges like '1-3'
    # 'multiple_tables' is set to True to extract all tables found on a page
    tables = read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Save each table as a CSV file
    for index, table in enumerate(tables):
        table.to_csv(f"table_{index + 1}.csv", index=False)

    return tables

# Specify the path to your PDF
pdf_path = 'path_to_your_pdf.pdf'
tables = extract_tables_from_pdf(pdf_path)

# Print the first table to see an example (assuming there is at least one table)
if tables:
    print("First extracted table:")
    print(tables[0])
else:
    print("No tables found.")
