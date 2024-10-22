import PyPDF2
import json

def readFieldnames(inputfile):
    with open(inputfile, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        fields = reader.get_form_text_fields()
        
        if fields:
            print("---------------Fieldnames---------------")
            for field_name, value in fields.items():
                value_display = value if value is not None else 'noValue'
                print(f"Fieldname: {field_name} \nValue: {value_display}\n")
            return fields
        else:
            print("No Fieldnames found")
            exit


def saveFieldnames(fields, output):
    with open(output, 'w') as outfile:
        json.dump(fields, outfile, indent=4)


