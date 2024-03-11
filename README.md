# Training Language Models with Syntactic Data Generation 

## TemplateGSM Dataset

The TemplateGSM dataset is a novel and extensive collection containing over **7 million grade school math problems** with code solutions and natural language solutions designed for advancing the study and application of mathematical reasoning within the realm of language modeling and AI. This dataset is crafted to challenge and evaluate the capabilities of language models in understanding and generating solutions to mathematical problems derived from a set of **7473** predefined **problem templates** using examples from the GSM8K dataset as prototypes. Each template encapsulates a unique mathematical problem structure, offering a diverse array of challenges that span various domains of mathematics.

Huggingface dataset: https://huggingface.co/datasets/math-ai/TemplateGSM

## Objective

TemplateGSM aims to serve as a benchmark for:
- Assessing language models' proficiency in mathematical reasoning and symbolic computation.
- Training and fine-tuning language models to improve their performance in generating accurate and logically sound mathematical solutions.
- Encouraging the development of models capable of understanding and solving complex mathematical problems, thereby bridging the gap between natural language processing and mathematical reasoning.

## Dataset Structure

TemplateGSM is organized into configurations based on the volume of problems generated from each template:

### Configurations

- **templategsm-1000-1k**: Contains 1000 * 1k problems generated from each of the 1000 templates (template 0000-0999), totaling over 1 million individual problems.
- **templategsm-2000-1k**: Contains 2000 * 1k problems generated from each of the 2000 templates (template 0000-1999), culminating in a dataset with 2 million problems.
- **templategsm-4000-1k**: Contains 4000 * 1k problems generated from each of the 4000 templates (template 0000-3999), culminating in a dataset with 4 million problems.
- **templategsm-7473-1k**: Contains 7473 * 1k problems generated from each of the 7473 templates (template 0000-7472), culminating in a dataset with over 7.47 million problems.

### Data Fields

Each problem in the dataset includes the following fields:
- `problem`: The problem statement.
- `solution_code`: A commented solution code that solves the problem in Python.
- `result`: The final answer to the problem.
- `solution_wocode`: The solution in natural language without the use of code.
- `source`: This field indicates the template is constructed from which data source and which seed is used in problem generation, e.g., `gsm8k-train-round2-seed42`.
- `template_id`: This field indicates the template from which the problem was generated, e.g.,  `0`.
- `problem_id`: An index unique to each problem within its template.

## How to Use

```XML
configs:
- config_name: templategsm-4000-1k
  data_files:
      - split: train
        path:
          - data/1k/0000-0999/*.jsonl
          - data/1k/1000-1999/*.jsonl
          - data/1k/2000-3999/*.jsonl
  default: true
- config_name: templategsm-2000-1k
  data_files:
      - split: train
        path:
          - data/1k/0000-0999/*.jsonl
          - data/1k/1000-1999/*.jsonl
- config_name: templategsm-1000-1k
  data_files:
      - split: train
        path:
          - data/1k/0000-0999/*.jsonl
- config_name: templategsm-7473-1k
  data_files:
      - split: train
        path:
          - data/1k/0000-0999/*.jsonl
          - data/1k/1000-1999/*.jsonl
          - data/1k/2000-3999/*.jsonl
          - data/1k/4000-7472/*.jsonl
```

To access the TemplateGSM dataset, you can use the Huggingface `datasets` library:

```python
from datasets import load_dataset

# Load a specific configuration
dataset = load_dataset("math-ai/TemplateGSM", "templategsm-4000-1k") # or any valid config_name
```

## License

This dataset is made available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Citation

If you utilize TemplateMath or the TemplateGSM dataset in your research or application, please consider citing it:

```bibtex
@misc{zhang2024training,
    title={TemplateMath: Training Language Models with Syntactic Data Generation},
    author={Zhang, Yifan and Luo, Yifan and Yuan, Yang and Yao, Andrew Chi-Chih},
    year={2024},
}
