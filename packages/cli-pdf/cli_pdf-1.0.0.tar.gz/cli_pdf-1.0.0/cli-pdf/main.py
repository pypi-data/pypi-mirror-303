import argparse
from mymodule.lib import fileCommon, readFieldnames, rename, merge, split, password


def main():
    parser = argparse.ArgumentParser(description="A PDF CLI Tool")

    parser.add_argument('-i', '--input', type=str, required=True, help='input File')
    parser.add_argument('-o', '--output', type=str, help='output')
    parser.add_argument('-rf', '--readfieldnames', action='store_true', help='read fieldnames')
    parser.add_argument('-rn', '--renamefieldnames', type=str, help='rename fieldnames')
    parser.add_argument('-m', '--merge', type=str, help='merge two pdfs in one')
    parser.add_argument('-s', '--split', type=int, help='split a Pdf')
    parser.add_argument('-dc', '--decrypt', action='store_true', help='decrypt a Pdf')
    parser.add_argument('-ec', '--encrypt', action='store_true', help='encrypt a Pdf')
    parser.add_argument('-p', '--password', type=str, help='password')
    parser.add_argument('-if', '--info', action='store_true', help='Info of the PDF')

    args = parser.parse_args()

    if args.input:
        fileCommon.check_exits_file(args.input)
        fileCommon.is_pdf(args.input)
        

    if args.readfieldnames: 
        if args.output:
            fields = readFieldnames.readFieldnames(args.input)
            readFieldnames.saveFieldnames(fields, args.output)
        else: 
            readFieldnames.readFieldnames(args.input)

    if args.renamefieldnames:
        if not args.output:
            print(f"Required Output pdf File")
            exit()
        fileCommon.is_json(args.renamefieldnames)
        rename.renameFields(args.input, args.renamefieldnames, args.output)

    if args.merge:
        if not args.output:
            print(f"Required Output pdf File")
            exit()
        fileCommon.check_exits_file(args.merge)
        merge.mergeFiles(args.input, args.merge, args.output)

    if args.split: 
        fileCommon.check_exits_file(args.input)   
        split.split(args.input, args.split)

    if args.decrypt: 
        if not args.password:
            print(f"No Password found")
            exit()
        if not args.output:
            print(f"Required Output pdf File")
            exit()
        password.decrypt_file_with_password(args.input, args.output, args.password)

    if args.encrypt:
        if not args.password:
            print(f"No Password found")
            exit()
        if not args.output:
            print(f"Required Output pdf File")
            exit()
        fileCommon.check_exits_file(args.input)
        password.encrypt_file_with_password(args.input, args.output, args.password)

    if args.info:
        fileCommon.info_pdf(args)
if __name__ == "__main__":
    main()
