def generate_html_table(data):
    html = "<div style='overflow-x:auto;'>"
    html += "<table style='border-collapse: collapse; border: 1px solid black;'>"
    # Add table headers
    html += "<tr>"
    for header in data[0]:
        html += "<th style='border: 1px solid black;'>{}</th>".format(header)
    html += "</tr>"
    # Add table rows
    for row in data[1:]:
        html += "<tr>"
        for cell in row:
            html += "<td style='border: 1px solid black;'>{}</td>".format(cell)
        html += "</tr>"
    html += "</table>"
    html += "</div>"
    return html

# Example data
data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"]
]

# Generate HTML table
html_table = generate_html_table(data)

# Print or save the generated HTML code
print(html_table)