mergepdfs shows a basic use of pypdf2 to merge pdf files

*How it works:

** First make sure package pypdf2 is installed:

$ sudo pip install -U pip
$ pip install pypdf2

**On a terminal prompt, type this:

$ ./mergepdfs.py file1.pdf file2.pdf fileN.pdf
(replace file1, file2, ..., fileN by actual files names)

**To make the script executable you can run this prior to execution

$ chmod u+x mergepdfs.py

**After execution, you'll obtail a file named "output.pdf"
that actually contains each page of the provided pdf files.
