import os

def rename_files(directory: str, prefix: str = "file") -> None:
    """Rename all files in the given directory with a prefix and running number."""
    if not os.path.isdir(directory):
        print("❌ Directory not found.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()

    count = 0
    for i, name in enumerate(files, start=1):
        ext = os.path.splitext(name)[1]
        new_name = f"{prefix}_{i}{ext}"
        old_path = os.path.join(directory, name)
        new_path = os.path.join(directory, new_name)

        # If new file name already exists, append a number
        if os.path.exists(new_path):
            base, ext2 = os.path.splitext(new_name)
            k = 2
            while os.path.exists(os.path.join(directory, f"{base}_{k}{ext2}")):
                k += 1
            new_path = os.path.join(directory, f"{base}_{k}{ext2}")

        os.rename(old_path, new_path)
        count += 1

    print(f"✅ {count} files renamed successfully!")

if __name__ == "__main__":
    folder = input("Enter folder path: ").strip().strip('"')
    prefix = input("Enter file prefix (default: file): ").strip() or "file"
    rename_files(folder, prefix)
