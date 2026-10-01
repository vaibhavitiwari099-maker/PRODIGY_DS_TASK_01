# Prodigy InfoTech — Data Science Internship

## Task 01: Population Data Visualization

### Project Overview

This project analyzes population data using Python and visualizes the 10 most populous countries in 2024 through a bar chart.

### Objective

To practice data loading, data cleaning, filtering, sorting, and visualization using Python libraries.

### Dataset

The dataset contains country and regional population estimates from 1960 to 2024.

**Source:** [Prodigy InfoTech Data Science Datasets](https://github.com/Prodigy-InfoTech/data-science-datasets/tree/main/Task%201)

### Technologies Used

* Python
* Pandas
* Matplotlib
* PyCountry
* Git and GitHub
* Visual Studio Code

### Project Workflow

1. Loaded the CSV dataset using Pandas.
2. Identified actual countries using ISO-3 country codes.
3. Selected population data for 2024.
4. Removed missing population values.
5. Sorted countries by population in descending order.
6. Selected the top 10 countries.
7. Created a bar chart using Matplotlib.
8. Exported the chart as a PNG image.

### Project Structure

```text
PRODIGY_DS_TASK_01/
├── dataset/
│   └── API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv
├── output/
│   └── top_10_population_2024.png
├── src/
│   └── analysis.py
├── .gitignore
├── README.md
└── requirements.txt
```

### How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/vaibhavitiwari099-maker/PRODIGY_DS_TASK_01.git
cd PRODIGY_DS_TASK_01
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the virtual environment on Windows**

```powershell
.\.venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the analysis**

```bash
python .\src\analysis.py
```

The generated chart is saved at `output/top_10_population_2024.png`.

### Output

The bar chart compares the 2024 population of the 10 most populous countries in the dataset.

### Key Learning Outcomes

* Reading CSV files with Pandas
* Cleaning and filtering datasets
* Working with country codes
* Sorting and selecting records
* Creating data visualizations
* Managing a project using Git and GitHub

### Conclusion

This project demonstrates a basic data analysis workflow, from loading and processing a real-world dataset to generating and saving a visualization.
