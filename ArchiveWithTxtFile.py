import subprocess
import os
import re
import PyPDF2
import requests
import validators

from headers import HEADERS


textfilePath = input("Enter the path of your text file with the links(seperated by comma): ")
archiveLinks = open(textfilePath,'r')
urlRegex = r"(https://na\.icpc\.global/.*|http://acmgnyr\.org/year2020/.*|https://acm2022\.scusa\.lsu\.edu/.*|http://www\.acmicpc-pacnw\.org/.*|https://rocky\.icpc\.io/.*|http://socalcontest\.org/current/index\.shtml.*|http://seusa\.vanb\.org/.*)"

urls = set()
# Create the main folder "NCNA" on the desktop
currline = 1

session = requests.Session()
# Set common headers for all requests made through this session
session.headers.update(HEADERS)

def is_valid_url(url):
    validation = validators.url(url)
    if validation:
        print("URL is valid")
        return True
    else:
        print("URL is invalid")
    return False


def check_wayback_machine(url):
    """
    Checks if a URL is available in the Wayback Machine and returns the archived URL.
    """
    wayback_api_url = f"http://archive.org/wayback/available?url={url}"
    response = requests.get(wayback_api_url)
    if response.status_code == 200:
        data = response.json()
        if data.get("archived_snapshots") and data["archived_snapshots"].get("closest"):
            archived_url = data["archived_snapshots"]["closest"]["url"]
            return archived_url
    return None

while True:
    line = archiveLinks.readline()
    if not line:
        break
    line = line.strip()
    if re.match(urlRegex,line) is None:
        print(f"The link is correctly formatted(not part of ICPC) on line {currline}, please double check.\n")
        exit(1)
    if is_valid_url(line):
        urls.add(line)
    else:
        print(f"The URL on line {currline} is not valid: {line}")
        exit(1)
    currline+=1


output_pdf_directory = os.path.join(os.path.expanduser("~"), "Desktop", "ICPC_Archive")

if not os.path.exists(output_pdf_directory):
    os.makedirs(output_pdf_directory)

pdfs_to_merge = []

for url in urls:
    # Extract the rightmost portion of the URL
    archived_url = check_wayback_machine(url)
    if archived_url:
        print(f"Archived URL found: {archived_url}")
    else:
        print(f"No archived URL found for: {url}, creating PDF")
        url_parts = url.split("/")
        pdf_name = url_parts[-2] if url_parts[-1] == "" else url_parts[-1]
        output_pdf_path = os.path.join(output_pdf_directory, f"{pdf_name}.pdf")

        command = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--headless",
            "--disable-gpu",
            "--print-to-pdf=" + output_pdf_path,
            url
        ]
        subprocess.call(command)
        pdfs_to_merge.append(output_pdf_path)
    
if len(pdfs_to_merge)>1 :
    merged_pdf_path = os.path.join(output_pdf_directory, "merged_output.pdf")
    merger = PyPDF2.PdfMerger()

    for pdf in pdfs_to_merge:
        merger.append(pdf)

    merger.write(merged_pdf_path)
    merger.close()

    print("PDFs have been created and merged into one large PDF at:", merged_pdf_path)
