# ComfyUI Workflow Reconstructor with Custom Metadata Extraction and Batch Support
import json
import re
import sys
import os
from PIL import Image

def extract_metadata_custom(image_file):
    try:
        with Image.open(image_file) as img:
            metadata = img.info
            return metadata
    except Exception as e:
        print(f"Error extracting metadata from {image_file}: {e}")
        return None


def extract_workflow_from_metadata(metadata, output_file):
    try:
        workflow_data = metadata.get('workflow') or metadata.get('prompt')
        if not workflow_data:
            print("Error: Workflow data not found in metadata.")
            return None

        try:
            workflow_json = json.loads(workflow_data)
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from extracted workflow data.")
            return None

        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(workflow_json, outfile, indent=4)

        print(f"Workflow successfully saved to {output_file}.")
        return output_file

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def process_files(file_list):
    for image_file in file_list:
        output_file = f"{os.path.splitext(image_file)[0]}.json"
        metadata = extract_metadata_custom(image_file)
        if metadata:
            extract_workflow_from_metadata(metadata, output_file)


def main():
    if len(sys.argv) != 2:
        print("Usage: python comfyui_workflow_reconstructor.py <image_file_or_pattern>")
        sys.exit(1)

    pattern = sys.argv[1]

    if '*' in pattern:
        file_list = [f for f in os.listdir('.') if re.match(pattern.replace('*', '.*'), f)]
    else:
        file_list = [pattern] if os.path.isfile(pattern) else []

    if not file_list:
        print("Error: No matching files found.")
        sys.exit(1)

    process_files(file_list)


if __name__ == "__main__":
    main()
