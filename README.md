# Knowledge Graphs and LLMs in Action — Course Template

This repository provides a clean, best-practices template for teaching with Jupyter notebooks, inspired by [github.com/alenegro81/knowledge-graphs-and-llms-in-action/tree/main/chapters/ch03](https://github.com/alenegro81/knowledge-graphs-and-llms-in-action/tree/main/chapters/ch03).

## Structure

- `notebooks/` — Jupyter notebooks for lessons, with clear explanations and code comments.
- `data/` — Datasets used in the course (small, shareable, or scripts to download/generate data).
- `environment.yml` — Conda environment file for reproducibility (or `requirements.txt` for pip).
- `README.md` — This file, with setup and usage instructions.

## Setup

1. Clone this repository.
2. Create the environment:
   - With conda: `conda env create -f environment.yml && conda activate kg-llm-course`
   - Or with pip: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
3. Start JupyterLab: `jupyter lab`

## Teaching Best Practices
- Each notebook starts with learning objectives and ends with exercises.
- Code is well-commented and modular.
- Data is small and shareable, or scripts are provided to download/generate it.
- Environment is fully reproducible.

## Next Steps
- Add your first notebook to `notebooks/`.
- Place or link your data in `data/`.
- Update `environment.yml` or `requirements.txt` as needed.

