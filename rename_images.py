import os
import shutil
import csv

source_folder = "/Users/zeinab/Downloads/0-1836"  # Specify the path to the folder containing the subfolders
destination_folder = "/Users/zeinab/Downloads/all_images"  # Specify the path to the destination folder
csv_file = "/Users/zeinab/Downloads/0.csv"  # Specify the path to the CSV file

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Folder", "Image Names"])

    for folder_num in range(1837):
        folder_path = os.path.join(source_folder, str(folder_num))
        if not os.path.isdir(folder_path):
            continue  # Skip if the folder doesn't exist

        image_files = os.listdir(folder_path)
        new_image_names = []

        for i, image_file in enumerate(image_files):
            old_path = os.path.join(folder_path, image_file)
            new_filename = "{}_{}.jpg".format(folder_num, i+1)
            new_image_names.append(new_filename)
            new_path = os.path.join(destination_folder, new_filename)
            shutil.copy2(old_path, new_path)

        new_image_names_str = ",".join(new_image_names)
        writer.writerow([folder_num, new_image_names_str])

print("Image renaming and moving completed!")



