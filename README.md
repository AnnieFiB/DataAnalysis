# Data Analytics Portfolio

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter)](https://jupyter.org)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C8CBF?logo=seaborn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/SQL-336791?logo=postgresql&logoColor=white)


## Repository Structure

```
/
├── DataAnalysis/
│   ├── notebooks/              # Jupyter notebooks
│   │   ├── archives/           # Archived notebooks
│   │   ├── model/              # Trained models or model notebooks
│   │   ├── datasets/           # Raw or processed data used in notebooks
│   │   ├── report_html/        # Data profiling or HTML reports
│   │   └── exploratoryEDA/     # Exploratory data analysis notebooks
│   ├── scripts/                # Python analysis scripts
│   ├── assets/                 # Images, charts, or supporting files
│   ├── .gitignore
│   ├── cleanup.bat
│   ├── requirements.txt
│   └── README.md

```

## Key Components

### 1. Data Analysis

| Feature                | Description |
|------------------------|-------------|
| **Machine Learning**   | Scikit-learn pipelines & model evaluation |
| **Machine Learning Lifecycle**  | Model training, evaluation, and deployment |
| **Visualization**      | Plotly/Matplotlib/Seaborn dashboards |
| **EDA**               | Automated Pandas Profiling reports |
| **SQL Integration**    | Querying structured data |


```python
import pandas as pd
from pandasql import sqldf

df = pd.read_csv("data.csv")
sqldf("SELECT * FROM df WHERE age > 30")
```
## Installation

```bash
# Clone with large file support
git clone https://github.com/yourusername/DataPortfolio.git --config core.longpaths=true

# Install analysis dependencies
pip install -r requirements.txt \
  scikit-learn \
  plotly \
  pandasql \
  jupyterlab
```

## Notebook Setup

```bash
# Start Jupyter Lab
jupyter lab --ip=0.0.0.0 --port=8888
```

Typical notebook structure:

```
# % Title
## 1. Business Objective
## 2. Data Loading
## 3. Exploratory Analysis
## 4. Feature Engineering
## 5. Model Development
## 6. Insights & Recommendations
```

## Workflow Example

```bash
# 1. Explore data
jupyter lab DataAnalysis/notebooks/exploratory/data_profiling.ipynb

```

## Maintenance

```bash
# Run cleanup script (Windows)
cleanup.bat
cleanup.sh

```

