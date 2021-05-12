import os
import shutil
import csv

# https://www.kaggle.com/c/aptos2019-blindness-detection/data

csv_file = './dr_dataset/train.csv'
existing_path_prefix = './dr_dataset/train_images/'
new_path_prefix = "./dr_dataset/"

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            pass    # Skip header row
        else:
            filename, filepath = row
            old_filename = os.path.join(existing_path_prefix, filename + '.png')
            new_filename = os.path.join(new_path_prefix, filepath + '/' + filename + '.png')

            shutil.move(old_filename, new_filename)