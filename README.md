# Archive NCNA Pages as PDF

This script archives all the current NCNA pages in their respective subfolders as PDF files.

## Preliminary Step: Check Python 3 Installation

Before running the script, ensure that Python 3 is installed on your system. Open a terminal and execute the following command:

```bash
python3 --version
```
## Additional Requirements

Before running the script, make sure to install the following Python libraries:

1. **Requests** - For checking the validity of URLs.
   ```bash
   pip3 install requests
   ```

2. **PyPDF2** - For handling PDF operations.
   ```bash
   pip3 install PyPDF2
   ```
2. **Validators** - For handling PDF operations.
   ```bash
   pip3 install Validators
   ```


If Python 3 is installed, you will see the version number. If not, you will need to install Python 3. You can download Python 3 from the [official Python website](https://www.python.org/downloads/).

## Running the Script

After confirming that Python 3 is installed, run the following command(s) in this directory:

If you wish to Archieve the pdf by entering the link at the command line:

```bash
python3 ArchieveWithInput.py
```

If you wish to Archieve the pdf by entering a text file:

```bash
python3 ArchieveWithTxtFile.py
```

