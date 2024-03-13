<<<<<<< HEAD
# pylint: disable=missing-module-docstring
import os
import re
# import matplotlib.pyplot as plt

def image_pathimg():
    # Define the base path
        base_path = "runs/detect/"

        # Check if the base path exists
        if not os.path.exists(base_path):
            print(f"Error: Base path '{base_path}' does not exist.")
            exit()

        # Get all subdirectories (folders) within the base path
        subdirs = os.listdir(base_path)

        # Filter out non-directory entries
        subdirs = [d for d in subdirs if os.path.isdir(os.path.join(base_path, d))]

        # Check if any subdirectories exist
        if not subdirs:
            print("No subdirectories found in the base path.")
            exit()

        # Extract numerical parts using regular expression
        numbers = [int(re.findall(r"\d+", d)[0]) if re.findall(r"\d+", d) else 0 for d in subdirs]

        # Find directories with 'predict' prefix and their indices
        predict_indices = [i for i, d in enumerate(subdirs) if d.startswith("predict")]

        # Safely access the index within predict_indices
        if predict_indices:
            max_predict_index = max(predict_indices, key=lambda i: numbers[i])
            predict_path = os.path.join(base_path, subdirs[max_predict_index])
        else:
            print("No 'predict' directory found. Using the directory with the highest numerical value:")
            highest_index = numbers.index(max(numbers))
            predict_path = os.path.join(base_path, subdirs[highest_index])

        # Check if the chosen directory is empty
        if not os.listdir(predict_path):
            print(f"The chosen directory '{predict_path}' is empty.")
            exit()

        # Get the first file path within the selected directory (modify for multiple files)
        img_path = os.path.join(predict_path, os.listdir(predict_path)[0])

        print(f"Image displayed from: {img_path}")
        return img_path


image_pathimg()
image_pathimg()
=======
# pylint: disable=missing-module-docstring
import os
import re

def image_pathimg():
    # Define the base path
        base_path = "runs/detect/"

        # Check if the base path exists
        if not os.path.exists(base_path):
            print(f"Error: Base path '{base_path}' does not exist.")
            exit()

        # Get all subdirectories (folders) within the base path
        subdirs = os.listdir(base_path)

        # Filter out non-directory entries
        subdirs = [d for d in subdirs if os.path.isdir(os.path.join(base_path, d))]

        # Check if any subdirectories exist
        if not subdirs:
            print("No subdirectories found in the base path.")
            exit()

        # Extract numerical parts using regular expression
        numbers = [int(re.findall(r"\d+", d)[0]) if re.findall(r"\d+", d) else 0 for d in subdirs]

        # Find directories with 'predict' prefix and their indices
        predict_indices = [i for i, d in enumerate(subdirs) if d.startswith("predict")]

        # Safely access the index within predict_indices
        if predict_indices:
            max_predict_index = max(predict_indices, key=lambda i: numbers[i])
            predict_path = os.path.join(base_path, subdirs[max_predict_index])
        else:
            print("No 'predict' directory found. Using the directory with the highest numerical value:")
            highest_index = numbers.index(max(numbers))
            predict_path = os.path.join(base_path, subdirs[highest_index])

        # Check if the chosen directory is empty
        if not os.listdir(predict_path):
            print(f"The chosen directory '{predict_path}' is empty.")
            exit()

        # Get the first file path within the selected directory (modify for multiple files)
        img_path = os.path.join(predict_path, os.listdir(predict_path)[0])

        print(f"Image displayed from: {img_path}")
        return img_path

