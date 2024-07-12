import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

# Set the PDF file name and path
filename = "payment_receipt.pdf"
filepath = os.path.join(os.getcwd(), filename)

# Create a new PDF document
pdf = canvas.Canvas(filepath, pagesize=A4)

# Set the font and font size
pdf.setFont("Helvetica", 12)

# Add the company logo (optional)
# logo_path = "path/to/logo.png"
# pdf.drawImage(logo_path, 1*inch, 10*inch, width=2*inch, height=1*inch)

# Add the receipt header
pdf.drawString(1*inch, 9*inch, "Payment Receipt")
pdf.drawString(1*inch, 8.5*inch, "Date: 2023-02-20")
pdf.drawString(1*inch, 8*inch, "Receipt No: #001")

# Add the payment details
pdf.drawString(1*inch, 7*inch, "Payment Method: Credit Card")
pdf.drawString(1*inch, 6.5*inch, "Amount: ₹10,000.00")
pdf.drawString(1*inch, 6*inch, "Transaction ID: 1234567890")

# Add the customer information
pdf.drawString(1*inch, 5*inch, "Customer Name: John Doe")
pdf.drawString(1*inch, 4.5*inch, "Address: 123 Main St, Anytown, India")

# Save the PDF
pdf.save()

print(f"Payment receipt generated: {filepath}")
