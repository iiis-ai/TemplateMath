import json
import os
from tqdm import tqdm
from time import sleep

# Define the source and target directories
source_dir = "/root/documents/template-gen/generated-problems/round2"
target_dir = "/root/documents/template-gen/generated-problems/round2-reformatted"

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Error log file path
error_log_path = "./error.txt"

# Function to process and reformat a single file
def process_file(file_index, error_log_file):
    source_file_path = f"{source_dir}/gsm8k-train-round2-problems-{file_index}.jsonl"
    target_file_path = f"{target_dir}/templategsm-train-problems-{file_index}.jsonl"

    # Initialize a counter for the lines
    line_count = 0

    with open(source_file_path, 'r') as source_file, open(target_file_path, 'w') as target_file:
        for line in tqdm(source_file, desc=f"Processing file {file_index}"):
            # Parse the original JSON object
            original_data = json.loads(line)

            # Reformat the JSON object
            reformatted_data = {
                "problem": original_data["problem"],
                "solution_code": original_data["solution_code"],
                "result": original_data["result"],
                "solution_wocode": original_data["solution_wocode"],
                "source": original_data["source"],
                "template_id": original_data["template_id"],
                "problem_id": original_data["problem_id"],
            }

            # Write the reformatted JSON object to the new file
            target_file.write(json.dumps(reformatted_data) + '\n')

            # Increment the line count
            line_count += 1

    # After processing, check if the line count is less than 1000
    if line_count < 1000:
        print("### WARNING ###\n" * 5)
        print(f"File contains less than 1000 examples: {source_file_path}")
        sleep(60)
        # Write the source file path to the error log
        error_log_file.write(f"{source_file_path}\n")

# Open the error log file in append mode
with open(error_log_path, 'a') as error_log_file:
    # Process all files with tqdm for a progress bar
    for i in tqdm(range(0, 7473), desc="Overall Progress"):
        process_file(i, error_log_file)

print("Processing complete.")
