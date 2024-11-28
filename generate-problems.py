import random
import json
import jsonlines
import os
import math
from tqdm import tqdm
import sympy
import multiprocessing

SEED = 42
random.seed(SEED)  # Consistent random generation

first_names = []
with jsonlines.open('./data/top_first_names.jsonl') as reader:
    for line in reader:
        first_names.append(line['first_name'])

last_names = []
with jsonlines.open('./data/top_last_names.jsonl') as reader:
    for line in reader:
        last_names.append(line['last_name'])

items = []
with jsonlines.open('./data/items-llm.jsonl') as reader:
    for line in reader:
        items.append(line)

places = []
with jsonlines.open('./data/places-llm.jsonl') as reader:
    for line in reader:
        places.append(line)

us_counties = []
with jsonlines.open('./data/us_counties.jsonl') as reader:
    for line in reader:
        us_counties.append(line)

# Load template samples
template_samples = []
with open(os.path.join("output", "gsm8k-train-round2-4000_7472.jsonl"), "r") as f:
    template_samples = [json.loads(line) for line in f.readlines()]

def run_with_timeout(sample, timeout):
    try:
        local_scope = {'random': random, 'first_names': first_names, 'last_names': last_names, 'items': items,
                       'places': places, 'us_counties': us_counties, 'sample': sample, 'json': json, 'os': os, 'math': math}
        exec(sample['template'], local_scope, local_scope)
        problem, solution_code, result, solution_wocode = local_scope['generate_problem_and_solution_code']()
        sample['problem'] = problem
        sample['solution_code'] = solution_code
        sample['result'] = str(result)
        sample['solution_wocode'] = solution_wocode
        sample['error'] = None
    except Exception as e:
        sample['error'] = str(e)
    return sample

def process_sample(sample, timeout=10):
    with multiprocessing.Pool(1) as pool:
        result = pool.apply_async(run_with_timeout, (sample, timeout))
        try:
            return result.get(timeout=timeout)
        except multiprocessing.TimeoutError:
            sample['error'] = 'Timeout'
            sample['timeout'] = True
            print(f"Timeout for sample idx: {sample.get('idx', 'N/A')}")
            return sample

def generate_and_save_problems(processed_samples_wo_error):
    for sample in tqdm(processed_samples_wo_error, desc="Generating problems"):
        problems = []
        for problem_id in range(1000):
            try:
                local_scope = {'random': random, 'first_names': first_names, 'last_names': last_names, 
                               'items': items, 'places': places, 'us_counties': us_counties, 
                               'sample': sample, 'json': json, 'os': os, 'math': math, 'sympy': sympy}
                exec(sample['template'], local_scope, local_scope)
                problem, solution_code, result, solution_wocode = local_scope['generate_problem_and_solution_code']()
                problems.append({
                    "source": f"gsm8k-train-round2-seed{SEED}",
                    "template_id": sample['idx'],
                    "problem_id": problem_id,
                    "problem": problem,
                    "solution_code": solution_code,
                    "result": str(result),
                    "solution_wocode": solution_wocode,
                })
            except Exception as e:
                print(f"Error generating problem for template idx: {sample['idx']} - {e}")
                continue

        # Use the `idx` field from the sample for the filename
        os.makedirs('./generated-problems', exist_ok=True)
        os.makedirs('./generated-problems/round2', exist_ok=True)
        filename = f'./generated-problems/round2/gsm8k-train-round2-problems-{sample["idx"]}.jsonl'
        with jsonlines.open(filename, mode='w') as writer:
            writer.write_all(problems)

def main():
    processed_samples = []
    for sample in tqdm(template_samples[:], desc="Processing samples"):
        if (sample['idx'] not in [5431]):
            continue
        for i in range(50):
            processed_sample = process_sample(sample, timeout=10)
            if processed_sample.get('error') is not None:
                break

        processed_samples.append(processed_sample)
    
    with jsonlines.open(os.path.join("output", 'gsm8k-train-round2-0_999-processed.jsonl'), mode='w') as writer:
        writer.write_all(processed_samples)

    processed_samples_wo_error = [sample for sample in processed_samples if sample.get('error') is None]

    generate_and_save_problems(processed_samples_wo_error)

    print(f"Processing complete. Problems generated for {len(processed_samples_wo_error)} templates.")

if __name__ == "__main__":
    main()
