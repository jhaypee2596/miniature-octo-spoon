import subprocess

list_files = subprocess.run(["pdf2pptx", "THE ROMANS ROAD TO SALVATION.pdf","-o THE ROMANS ROAD TO SALVATION.pptx"])
print("The files are converted successfully")