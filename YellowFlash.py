import os
import ctypes

MAX_PTEST_SIZE = 512 * 1024  # 512 KB split size (can be increased)
TEST_FOLDER = "Test"

def is_hidden(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(str(filepath))
        return attrs != -1 and (attrs & 2)  # FILE_ATTRIBUTE_HIDDEN
    except Exception:
        return False

def get_extensions_by_category(choice):
    file_types = {
        '1': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm'],
        '2': ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'],
        '3': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
        '4': ['.txt', '.md', '.csv', '.log', '.xml', '.json', '.ini']
    }
    return file_types.get(choice, [])

def search_hidden_files(path, extensions, logs):
    try:
        with os.scandir(path) as entries:
            log_line = f"📁 Scanning: {path}"
            print(log_line)
            logs["PTest"].append(log_line)

            for entry in entries:
                full_path = os.path.join(path, entry.name)

                if entry.is_dir(follow_symlinks=False):
                    if is_hidden(full_path):
                        logs["PTest"].append(f"     📂 Hidden Folder: {full_path}")
                    search_hidden_files(full_path, extensions, logs)

                elif entry.is_file(follow_symlinks=False):
                    logs["PTest"].append(f"  └── 📄 File: {full_path}")
                    if any(entry.name.lower().endswith(ext) for ext in extensions):
                        if is_hidden(full_path):
                            logs["STest"].append(f"🔒 Hidden File: {full_path}")

    except PermissionError:
        logs["ETest"].append(f"⛔ Permission denied: {path}")
    except FileNotFoundError:
        logs["ETest"].append(f"❌ Path not found: {path}")
    except Exception as e:
        logs["ETest"].append(f"⚠️ Error accessing {path}: {e}")

def write_logs_to_files(logs):
    os.makedirs(TEST_FOLDER, exist_ok=True)

    # Write PTest logs in split files
    ptest_index = 1
    ptest_lines = []
    current_size = 0

    for line in logs["PTest"]:
        encoded = (line + '\n').encode('utf-8')
        if current_size + len(encoded) > MAX_PTEST_SIZE:
            with open(os.path.join(TEST_FOLDER, f"PTest{ptest_index}.txt"), 'w', encoding='utf-8') as f:
                f.writelines(ptest_lines)
            ptest_lines = []
            current_size = 0
            ptest_index += 1
        ptest_lines.append(line + '\n')
        current_size += len(encoded)

    if ptest_lines:
        with open(os.path.join(TEST_FOLDER, f"PTest{ptest_index}.txt"), 'w', encoding='utf-8') as f:
            f.writelines(ptest_lines)

    # ETest log
    with open(os.path.join(TEST_FOLDER, "ETest.txt"), 'w', encoding='utf-8') as f:
        f.write('\n'.join(logs["ETest"]))

    # STest log
    with open(os.path.join(TEST_FOLDER, "STest.txt"), 'w', encoding='utf-8') as f:
        f.write('\n'.join(logs["STest"]))

def main():
    print("Choose file category to search for hidden files:")
    print("1. Video Files")
    print("2. Image Files")
    print("3. Audio Files")
    print("4. Text Files")
    choice = input("Enter your choice (1-4): ").strip()

    extensions = get_extensions_by_category(choice)
    if not extensions:
        print("❌ Invalid choice. Please select a number from 1 to 4.")
        return

    search_path = input("Enter drive/folder path to search (e.g., C:\\, D:\\folder): ").strip()

    if len(search_path) == 2 and search_path.endswith(':'):
        search_path += '\\'

    if not os.path.exists(search_path):
        print(f"❌ Path does not exist: {search_path}")
        return

    print(f"\n🔍 Starting hidden file search in: {search_path}")
    print(f"🧩 Extensions: {extensions}\n")

    logs = {"PTest": [], "ETest": [], "STest": []}
    search_hidden_files(search_path, extensions, logs)

    print("\n📦 Saving log files to 'Test' folder...")
    write_logs_to_files(logs)
    print("✅ Done! Logs saved as PTest, ETest, and STest files.")

if __name__ == "__main__":
    main()
