<div align="center">

# TemplateMath: Template-based Data Generation (TDG)

[![ICLRW](https://img.shields.io/badge/ICLRW-Published-blue)]()
[![arXiv](https://img.shields.io/badge/arXiv-2411.18104-green.svg)](https://arxiv.org/abs/2411.18104)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Website](https://img.shields.io/badge/Project-Website-green)]([https://templatemath.github.io](https://templatemath.github.io))
[![TemplateGSM](https://img.shields.io/badge/Huggingface-Datasets-blue)](https://huggingface.co/datasets/math-ai/TemplateGSM)

</div>

This is the official repository for the paper **"Training and Evaluating Language Models with Template-based Data Generation"**, published at the ICLR 2025 DATA-FM Workshop.

Our work introduces **Template-based Data Generation (TDG)**, a scalable paradigm to address the critical data bottleneck in training LLMs for complex reasoning tasks. We use TDG to create **TemplateGSM**, a massive dataset designed to unlock the next level of mathematical reasoning in AI.

## 🚀 What is TemplateGSM?

**TemplateGSM** is a foundational dataset containing **over 7.4 million** grade school math problems. Each problem is synthetically generated and comes with both a natural language explanation and a programmatically verifiable code solution.

Unlike existing resources, TemplateGSM is built on a framework of **programmatic verification**, ensuring every single problem-solution pair is correct. This provides an unprecedented level of quality at a massive scale, making it ideal for both supervised fine-tuning (SFT) and emerging alignment techniques like **Reinforcement Learning with Verifiable Rewards (RLVR)**.

At **\>500x the size** of the widely-used MATH benchmark, TemplateGSM provides the community with a powerful new resource to train and evaluate more capable and reliable models.

## ✅ Key Features

  * **Massive Scale**: Over **7.4 million** problem-solution pairs, with the potential to generate a virtually infinite amount more using our open-source code.
  * **Programmatic Verification**: Every solution is accompanied by executable Python code that has been run to verify its correctness. This guarantees data quality and eliminates the noise found in web-scraped datasets.
  * **Rich Diversity**: Generated from **7,473** unique meta-templates (authored by GPT-4), the dataset covers a wide range of mathematical structures and linguistic styles.
  * **Enables Verifiable Rewards**: The dataset's structure provides a direct, binary reward signal (correct/incorrect) for training models with reinforcement learning, a concept we term **Reinforcement Learning with Verifiable Rewards (RLVR)**.

## 💡 How to Use

You can easily access and use TemplateGSM directly from the Hugging Face Hub.

```python
from datasets import load_dataset

# Load the full dataset (7.47M problems)
dataset = load_dataset("math-ai/TemplateGSM", "templategsm-7473-1k")

# Or, load a smaller configuration
# dataset = load_dataset("math-ai/TemplateGSM", "templategsm-1000-1k") # 1M problems

print(dataset['train'][0])
```

### Dataset Structure

  * `problem`: `string` - The mathematical word problem.
  * `solution_code`: `string` - A commented Python solution that programmatically solves the problem.
  * `result`: `string` - The final numerical answer.
  * `solution_wocode`: `string` - A step-by-step solution explained in natural language.
  * `template_id`: `int` - The ID of the meta-template used for generation.
  * `problem_id`: `int` - A unique index for the problem within its template.
  * `source`: `string` - The original data source used to inspire the template.

\<details\>
\<summary\>\<b\>View All Configurations\</b\>\</summary\>

The dataset is organized into several configurations based on the number of templates used:

  - **`templategsm-1000-1k`**: 1,000,000 problems from the first 1,000 templates.
  - **`templategsm-2000-1k`**: 2,000,000 problems from the first 2,000 templates.
  - **`templategsm-4000-1k`**: 4,000,000 problems from the first 4,000 templates.
  - **`templategsm-7473-1k`**: 7,473,000 problems from all 7,473 templates (the full dataset).

\</details\>

## 🙏 Citation

If you use the TemplateGSM dataset, the Template-based Data Generation (TDG) paradigm, or the concept of RLVR in your research, please cite our paper. Your citation allows us to continue building and sharing impactful resources with the community\!

### Citing the Dataset or Methodology:

```bibtex
@article{zhang2024training,
    title={Training and Evaluating Language Models with Template-based Data Generation},
    author={Zhang, Yifan and Luo, Yifan and Yuan, Yang and Yao, Andrew Chi-Chih},
    journal={arXiv preprint arXiv:2411.18104},
    year={2024},
    eprint={2411.18104},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
