from PyPDF2 import PdfReader, PdfWriter

# Ask user to input PDFs to merge
print("Enter PDF filenames to merge, separated by commas (e.g., file1.pdf,file2.pdf):")
pdf_input = input().strip()

# Split input into list
pdfs = [name.strip() for name in pdf_input.split(",") if name.strip()]

if not pdfs:
    print("No PDF files provided. Exiting.")
    exit()

# Output filename
output_filename = input("Enter output PDF filename (e.g., merged.pdf): ").strip()
if not output_filename.endswith(".pdf"):
    output_filename += ".pdf"

# Create PDF writer
writer = PdfWriter()

# Add pages from each PDF
for pdf_file in pdfs:
    try:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)
        print(f"Added {pdf_file}")
    except FileNotFoundError:
        print(f"File not found: {pdf_file}. Skipping.")
    except Exception as e:
        print(f"Error reading {pdf_file}: {e}. Skipping.")

# Write merged PDF
try:
    with open(output_filename, "wb") as f:
        writer.write(f)
    print(f"Merged PDF saved as {output_filename}")
except Exception as e:
    print(f"Error writing merged PDF: {e}")