import subprocess
import os

urlGlobal = [
    "https://na.icpc.global/",
    "c",
    "https://na.icpc.global/regionals/ncna-home/ncna-hall-of-champions/",
    "https://na.icpc.global/regionals/ncna-home/ncna-information-for-coaches/",
    "https://na.icpc.global/regionals/ncna-home/ncna-information-for-coaches-contestants/",
    "https://na.icpc.global/regionals/ncna-home/ncna-information-for-site-directors/",
    "https://na.icpc.global/regionals/ncna-home/ncna-organizers/",
    "https://na.icpc.global/regionals/ncna-home/",
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna-note-to-teams-2022-23/",
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna-problem-archive-2022-23/",

]

urlSitePages = [
    "https://na.icpc.global/regionals/ncna-home/regionals2023-24/ncna-sites-2023-2024/ncna-sites-csbsju/",
    "https://na.icpc.global/regionals/ncna-home/regionals2023-24/ncna-sites-2023-2024/ncna-sites-university-of-minnesota/",
    "https://na.icpc.global/regionals/ncna-home/regionals2023-24/ncna-sites-2023-2024/ncna-sites-macalester/"
]

url202324 = [
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna-future-contestants-2022-23/",
    "https://na.icpc.global/regionals/ncna-home/regionals2023-24/",
    "https://na.icpc.global/regionals/ncna-home/regionals2023-24/ncna-sites-2023-2024/"
]
url202223 = [
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna22-contest-photos/",
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna-coach-recognition-2022-23/",
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna-future-contestants-2022-23/",
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna-regionals-2022-2023/",
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/ncna-sites-2022-23/",
    "https://na.icpc.global/2022-23/regionals/ncna-2022-23/"
]

url202122 = [
    "https://na.icpc.global/2021-22/regionals/ncna-regionals-2021-2022/"
]

# Create the main folder "NCNA" on the desktop
output_base_directory = os.path.join(os.path.expanduser("~"), "Desktop", "NCNA")

if not os.path.exists(output_base_directory):
    os.makedirs(output_base_directory)
    
# Define a dictionary to associate URLs with their respective lists
url_lists = {
    "Global": urlGlobal,
    "SitePages": urlSitePages,
    "2023-24": url202324,
    "2022-23": url202223,
    "2021-22": url202122
}

# Loop through each URL list and create subfolders for them
for list_name, urls in url_lists.items():
    subfolder_path = os.path.join(output_base_directory, list_name)
    
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    # Loop through the URLs in the current list and save PDFs with names based on the rightmost portion of the URL
    for index, url in enumerate(urls):
        # Extract the rightmost portion of the URL
        url_parts = url.split("/")
        pdf_name = url_parts[-2] if url_parts[-1] == "" else url_parts[-1]
        output_pdf_path = os.path.join(subfolder_path, f"{pdf_name}.pdf")

        command = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "--headless",
            "--disable-gpu",
            "--print-to-pdf=" + output_pdf_path,
            url
        ]

        subprocess.call(command)

print("PDFs have been created in their respective subfolders.")