from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Create a PDF document
pdf = SimpleDocTemplate("table_example.pdf", pagesize=letter)

# Sample data for table
data = [
    ['Header 1', 'Header 2', 'Header 3'],
    ['Row 1, Cell 1', 'Row 1, Cell 2', 'Row 1, Cell 3'],
    ['Row 2, Cell 1', 'Row 2, Cell 2', 'Row 2, Cell 3'],
    ['Row 3, Cell 1', 'Row 3, Cell 2', 'Row 3, Cell 3']
]

# Create a table instance
table = Table(data)

# Add table style
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

table.setStyle(style)

# Add table to PDF document
elems = []
elems.append(table)
pdf.build(elems)
