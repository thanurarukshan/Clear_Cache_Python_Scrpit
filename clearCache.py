import os
import shutil
import tempfile

def clear_windows_cache():
    try:
        # Get the path to the temporary files directory
        temp_dir = tempfile.gettempdir()
        temp_dir2 = "C:\Windows\Temp"

        # Iterate over the files in the temporary directory and delete them
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    #print(file_path)
                    pass
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        for root, dirs, files in os.walk(temp_dir2):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    #print(file_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

        print("Windows cache cleared - done.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clear_windows_cache()
