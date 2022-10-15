import subprocess

list_files = subprocess.run(["pdf2pptx", "unlad-lesson-10.pdf","-o unlad-lesson-10.pptx"])
print("The files are converted successfully")