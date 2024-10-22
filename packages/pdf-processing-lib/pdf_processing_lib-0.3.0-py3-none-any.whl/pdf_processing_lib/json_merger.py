import os
import json
import hashlib
import random

class JSONMerger:
    def __init__(self, root_directory):
        self.root_directory = root_directory

    def generate_hash(self):
        # Generate a random string and hash it
        random_string = str(random.randint(0, 1000000))
        return hashlib.md5(random_string.encode()).hexdigest()[:16]

    def process_json_files(self):
        combined_data = []

        for root, _, files in os.walk(self.root_directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        try:
                            data = json.load(f)
                            if isinstance(data, list):
                                for item in data:
                                    if isinstance(item, dict):
                                        item['hash'] = self.generate_hash()
                                combined_data.extend(data)
                            elif isinstance(data, dict):
                                data['hash'] = self.generate_hash()
                                combined_data.append(data)
                        except json.JSONDecodeError:
                            print(f"Error decoding JSON in file: {file_path}")

        return combined_data

    def merge_and_hash(self, output_file):
        combined_data = self.process_json_files()

        with open(output_file, 'w') as f:
            json.dump(combined_data, f, indent=2, ensure_ascii=False)

        print(f"Combined JSON with added hash keys has been written to {output_file}")
        return output_file, len(combined_data)

    def run(self, output_file):
        if not os.path.isdir(self.root_directory):
            print("The specified directory does not exist.")
            return None, 0

        return self.merge_and_hash(output_file)