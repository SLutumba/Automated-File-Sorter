# **Automated File Sorter**

## **Overview**
The **Automated File Sorter** is a Python-based automation tool that organizes files in your `Downloads` folder into categorized subfolders such as **Documents**, **Apps**, **Audios**, **Pictures**, and **Videos**. 

This project includes a pre-built executable for easy use, so no programming knowledge or Python installation is required.

---

## **How to Use**

### **Using the Pre-Built Executable**
1. **Download the Executable**
   - Clone this repository or download it as a ZIP from [here](https://github.com/SLutumba/Automated-File-Sorter).

2. **Locate the Executable**
   - Navigate to the `executable` folder inside the project and find the file:
     - **Windows**: `FileOrganiser.exe`
     - **macOS/Linux**: Ensure you have Python if running the script directly.

3. **Run the Executable**
   - Double-click `FileOrganiser.exe`, or open a terminal/command prompt in the `executable` folder and run:
     ```bash
     FileOrganiser.exe
     ```
   - The program will automatically organize files in your `Downloads` folder.

4. **File Organization**
   - The script will:
     - Create a `Sorted` folder inside `Downloads`.
     - Move files into subfolders like **Documents**, **Pictures**, etc., based on their type.

5. **Run Interval**
   - The program checks for new files in `Downloads` every 12 minutes. To stop the program, close the terminal or the executable.

---

### **Using the Python Script**
For advanced users or those who want to modify the script:
1. Install Python (3.6 or later).
2. Clone the repository:
   ```bash
   git clone https://github.com/SLutumba/Automated-File-Sorter.git
   ```
3. Navigate to the project directory and run the script:
   ```bash
   python file-sorter.py
   ```

---

## **Building the Executable**
To rebuild the executable yourself:
1. Ensure Python and `PyInstaller` are installed:
   ```bash
   pip install pyinstaller
   ```
2. In the project directory, run:
   ```bash
   pyinstaller --onefile --name "FileOrganiser" file-sorter.py
   ```
3. Find the new executable in the `dist` folder.

---

## **Customization**
You can customize the script by editing `file-sorter.py`:
- Modify the `file_mapping` dictionary to add or remove file extensions.
- Change the `source` path to organize a folder other than `Downloads`.

---

## **Repository**
Find the full project on GitHub: [Automated File Sorter](https://github.com/SLutumba/Automated-File-Sorter).

---

## **License**
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

Would you like help updating the GitHub repository to include this or anything else?
