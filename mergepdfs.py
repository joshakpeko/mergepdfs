# mergepdfs leverages PyPDF2 package to concatenate various pdf files
# into one. Files names may be provided on command line as arguments
import os, sys

import PyPDF2


def main():
    files = sys.argv[1:]
    if len(files) < 2:
        print("Provide at least 2 pdf files to merge")
        sys.exit(0)
    mergeFiles(*files)
    return

def mergeFiles(*files):
    pdfMerger = PyPDF2.PdfFileMerger()
    for f in files:
        try:
            pdfMerger.append(f)
        except Exception as ex:
            print(ex.with_traceback(None))
            continue

    pdfMerger.write("output.pdf")
    pdfMerger.close()
    return


if __name__ == "__main__":
    main()
