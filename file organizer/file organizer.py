import os
import shutil


source_folder = "F:/Python Folder/Automation project of python" # এই ফাইল পথ থেকে তথ্য আসবে
destination_folder = "F:/Python Folder/Automation project of python" # এই ফাইলে যাবে
all_files = os.listdir(source_folder)

for file_name in all_files:
    full_file_path = os.path.join(source_folder, file_name)
    
    # যদি এটি একটি ফাইল হয়
    if os.path.isfile(full_file_path):
        file_type = file_name.split('.')[-1].lower()
        
        # নতুন ফোল্ডার তৈরি করুন যদি না থাকে
        new_folder_path = os.path.join(destination_folder, file_type)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        
        # ফাইল কপি করুন
        shutil.copy(full_file_path, os.path.join(new_folder_path, file_name))
print("File organization completed successfully!")