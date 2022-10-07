import subprocess

list_files = subprocess.run(["pdf2pptx", "test.pdf","-o test.pptx"])
print("The files are converted successfully")