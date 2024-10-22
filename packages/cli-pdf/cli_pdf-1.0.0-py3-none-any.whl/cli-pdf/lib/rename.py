import json
from pdfrw import PdfReader, PdfWriter, PageMerge

def renameFields(inputFile, rename_json, outputFile=f"renamed.pdf"):
    pdf = PdfReader(inputFile)
    

    with open(rename_json, 'r') as json_file:
        rename_map = json.load(json_file)
    
    print("--------------- Rename Fields ----------------------")
    
    for page in pdf.pages:
        annotations = page['/Annots']
        if annotations:
            for annotation in annotations:
                field = annotation['/T']
                
                if field:
                    old_field_name = field.to_unicode()
                    
                    if old_field_name in rename_map:
                        new_field_name = rename_map[old_field_name]
                        annotation.update({"/T": new_field_name})
                        print(f"Renaming: {old_field_name} -> {new_field_name}")
                    else:
                        print(f"Keeping: {old_field_name}")
    
    PdfWriter(outputFile, trailer=pdf).write()


