import subprocess

list_files = subprocess.run(["pdf2pptx", "usad-lesson-10.pdf", "-o usad-lesson-10.pptx"])
print("The files are converted successfully")