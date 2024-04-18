def generate_html_table(data):
    html = "<table>"
    # Add table headers
    html += "<tr>"
    for header in data[0]:
        html += "<th>{}</th>".format(header)
    html += "</tr>"
    # Add table rows
    for row in data[1:]:
        html += "<tr>"
        for cell in row:
            html += "<td>{}</td>".format(cell)
        html += "</tr>"
    html += "</table>"
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
