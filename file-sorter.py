import os
import shutil
import time

file_mapping = {
    "Documents":[".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Apps":[".exe", ".msi"],
    "Audios":[".mp3", ".wav", ".flac"],
    "Pictures":[".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos":[".mp4", ".avi", ".mkv", ".mov", ".flv"]
}
folder_paths = []


def move_files(source):
    docCount = 0
    appCount = 0
    audioCount = 0
    picCount = 0
    vidCount = 0
    for _, dirs, files in os.walk(source):
        for file in files:
            if get_extension(file) in file_mapping["Documents"]:
                file_path = os.path.join(source, file)
                shutil.move(file_path, folder_paths[0])
                docCount = docCount + 1
            elif get_extension(file) in file_mapping["Apps"]:
                file_path = os.path.join(source, file)
                shutil.move(file_path, folder_paths[1])
                appCount = appCount + 1
            elif get_extension(file) in file_mapping["Audios"]:
                file_path = os.path.join(source, file)
                shutil.move(file_path, folder_paths[2])
                audioCount = audioCount + 1
            elif get_extension(file) in file_mapping["Pictures"]:
                file_path = os.path.join(source, file)
                shutil.move(file_path, folder_paths[3])
                picCount = picCount + 1
            elif get_extension(file) in file_mapping["Videos"]:
                file_path = os.path.join(source, file)
                shutil.move(file_path, folder_paths[4])
                vidCount = vidCount + 1
            else:
                print(f"{file} could not be moved.")
        break
    print(f"{docCount} document(s) moved, {appCount} application(s) moved, {audioCount} audio(s) moved, "
          f"{picCount} picture(s) moved, {vidCount} video(s) moved")


def make_dirs(source):
    for folder in file_mapping:
        folder_path = os.path.join(source, folder)
        os.makedirs(folder_path, exist_ok=True)
        folder_paths.append(folder_path)

def get_extension(file_name):
    extension = os.path.splitext(file_name)[1]
    return extension

def main():
    source = os.path.expanduser('~/Downloads')
    destination = os.path.join(source, "Sorted")
    make_dirs(destination)
    move_files(source)

if __name__ == "__main__":

    while True:
        main()
        wait_time = 12
        print(f"Application will run again in {wait_time} minutes...")
        time.sleep(wait_time * 60)
