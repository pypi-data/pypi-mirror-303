from pdfrw import PdfReader, PdfWriter

def split(inputfile, split_on_page: int):
    pdf = PdfReader(inputfile)
    
    total_pages = len(pdf.pages)
    if split_on_page < 1 or split_on_page >= total_pages:
        print(f"Invalid split page: {split_on_page}. The file has {total_pages} pages.")
        return

    writer_part1 = PdfWriter()
    writer_part1.addpages(pdf.pages[:split_on_page])

    writer_part2 = PdfWriter()
    writer_part2.addpages(pdf.pages[split_on_page:])

    output_part1 = inputfile.replace(".pdf", f"_part1.pdf")
    output_part2 = inputfile.replace(".pdf", f"_part2.pdf")

    writer_part1.write(output_part1)
    writer_part2.write(output_part2)

    print(f"The file has been successfully split into {output_part1} and {output_part2}.")
