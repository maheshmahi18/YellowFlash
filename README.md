---

````markdown
# 🌩️ Yellow Flash

**Yellow Flash** is a powerful and recursive file system scanner built in Python. It traverses all folders and subfolders from a given path, logs traversal steps, detects **hidden files**, and handles **access-restricted directories**. The logs are categorized and saved after the scan into organized text files.

---

## 📚 Table of Contents

- [Features](#features)  
- [Installation and Setup](#installation-and-setup)  
- [Usage](#usage)  
- [Output File Structure](#output-file-structure)  
- [Customization](#customization)  
- [Credits](#credits)  
- [Contributing](#contributing)  
- [License](#license)

---

## 🚀 Features

- Recursively traverses all folders and subfolders in the specified path.
- Identifies and logs **hidden files** based on selected file type category (e.g., videos, images, audio, text).
- Categorizes and logs **restricted paths**, **hidden files**, and **all traversed paths**.
- Outputs logs to a `Test` folder with proper file size management (splitting if needed).
- Live display of folder traversal in the terminal.

---

## 🛠️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/maheshmahi18/yellow-flash.git
cd yellow-flash
````

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note**: No external dependencies are required as the code primarily uses the standard Python library.

---

## ⚙️ Usage

### Run the Script

```bash
python yellow_flash.py
```

### Follow the Prompts

1. Choose the category of files to search (Video, Image, Audio, or Text).
2. Enter the full path to scan (e.g., `C:\`).

The program will:

* Display traversal logs in the terminal.
* After scanning, save logs to the `Test` folder in the current directory.

---

## 📁 Output File Structure

The logs will be saved under the `Test/` folder:

| File Name                                    | Description                                  |
| -------------------------------------------- | -------------------------------------------- |
| `PTest.txt`, `PTest1.txt`, `PTest2.txt`, ... | Traversed folder and file paths              |
| `ETest.txt`                                  | Paths where access was denied or failed      |
| `STest.txt`                                  | Hidden files matching the selected extension |

---

## 🧩 Customization

You can modify the following constants in `yellow_flash.py`:

* `MAX_PTEST_SIZE`: Maximum size of each `PTest` file before splitting (default: 512KB).
* `TEST_FOLDER`: Folder name where logs will be saved (`Test` by default).
* Extension categories can be extended in `get_extensions_by_category()`.

---

## 👤 Credits

* **Project Owner**: [Mahesh](mailto:gorlamahii@gmail.com)
* **Tool Inspiration**: System cleanup and file audit utilities

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit and push.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for more details.

```

---

