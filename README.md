# UnclutterDesktop
Unclutter your desktop with a Click
Overview
This script scans the Desktop directory for files and organizes them into folders according to their file extensions. Each folder is named after the respective extension, and multiple files with the same extension are placed in the same folder.

Example
Before running the script:

```
Desktop/
|-- document1.txt
|-- image1.jpg
|-- document2.docx
|-- image2.png
|-- organize_desktop.py
After running the script:
```

```
Desktop/
|-- txt/
|   |-- document1.txt
|-- jpg/
|   |-- image1.jpg
|-- docx/
|   |-- document2.docx
|-- png/
|   |-- image2.png
|-- organize_desktop.py
```

Notes
The script assumes a case-sensitive file extension.
Make sure to backup important files before running the script.
The script excludes itself from being moved into a folder.
