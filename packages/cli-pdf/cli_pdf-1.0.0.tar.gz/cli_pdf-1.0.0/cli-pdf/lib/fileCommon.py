import os
import PyPDF2


def check_exits_file(file):
    if not os.path.exists(file):
        print(f"File {file} not found.")
        exit()
        
def is_pdf(file):
    file_art = file.split(".")[-1:]
    if (file_art[0] != 'pdf'): 
        print(f"File is not an PDF")
        exit()
        
def is_json(file): 
    file_art = file.split(".")[-1:]
    if(file_art[0] != 'json'):
        print(f'File is not an JSON')
        exit()
        
def testing():
    print(f"testing")
        
        
def info_pdf(args):
    with open(args.input, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        filename = os.path.basename(args.input)
        file_size = os.path.getsize(args.input) / 1024  
        
        num_pages = len(reader.pages)
        
        fields = reader.get_fields() if reader.get_fields() else {}
        
        metadata = reader.metadata
        
        print(f"----------- PDF Info -----------")
        print(f"Filename: {filename}")
        print(f"File size: {file_size:.2f} KB")
        print(f"Number of pages: {num_pages}")
        print(f"Number of text fields: {len(fields)}")
        
        pdf_version = reader.pdf_header
        print(f"PDF Version: {pdf_version}")
        
        if reader.is_encrypted:
            print("Encryption: Yes (password required)")
        else:
            print("Encryption: No")
        
        if metadata:
            print(f"Title: {metadata.get('/Title', 'N/A')}")
            print(f"Author: {metadata.get('/Author', 'N/A')}")
            print(f"Subject: {metadata.get('/Subject', 'N/A')}")
            print(f"Producer: {metadata.get('/Producer', 'N/A')}")
            print(f"Creation Date: {metadata.get('/CreationDate', 'N/A')}")
            print(f"Modification Date: {metadata.get('/ModDate', 'N/A')}")
        else:
            print("No metadata available.")
        
        print("\nPage details:")
        for i, page in enumerate(reader.pages):
            layout = "Landscape" if page.mediabox.width > page.mediabox.height else "Portrait"
            width = page.mediabox.width
            height = page.mediabox.height
            print(f"  Page {i + 1}: {layout} - Width: {width} pt, Height: {height} pt")
        
        
        if fields:
            print("\nForm fields:")
            for i, field in enumerate(fields.keys()):
                if i < 10:  
                    print(f"  Field {i+1}: {field}")
            if len(fields) > 10:
                print(f"  ... and {len(fields) - 10} more fields.")
        else:
            print("No form fields found.")

