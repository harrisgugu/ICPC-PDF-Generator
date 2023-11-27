import os
import subprocess
import PyPDF2
import re
import requests

url_pattern = re.compile(r'^https?://\S+')

urls = []
while True:
    url = input("Enter a URL (or 'stop' to finish): ")
    if url.lower() == 'stop':
        break
    if url_pattern.match(url):
        urls.append(url)
    else:
        print("Invalid URL:", url)

output_pdf_directory = os.path.join(os.path.expanduser("~"), "Desktop", "ICPC_Archive")

if not os.path.exists(output_pdf_directory):
    os.makedirs(output_pdf_directory)

pdfs_to_merge = []

for index, url in enumerate(urls):
    output_pdf_path = os.path.join(output_pdf_directory, f"output{index + 1}.pdf")

    command = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_pdf_path}",
        url
    ]

    subprocess.call(command)
    pdfs_to_merge.append(output_pdf_path)

merged_pdf_path = os.path.join(output_pdf_directory, "merged_output.pdf")
merger = PyPDF2.PdfMerger()

for pdf in pdfs_to_merge:
    merger.append(pdf)

merger.write(merged_pdf_path)
merger.close()

print("PDFs have been created and merged into one large PDF at:", merged_pdf_path)
