from pdfrw import PdfReader, PdfWriter

def mergeFiles(inputFile1, inputFile2, outputFile):
    pdf1 = PdfReader(inputFile1)
    pdf2 = PdfReader(inputFile2)

    writer = PdfWriter()

    writer.addpages(pdf1.pages)
    
    writer.addpages(pdf2.pages)

    writer.write(outputFile)

    print(f"PDF {inputFile1} and {inputFile2} are merged now in {outputFile}")
