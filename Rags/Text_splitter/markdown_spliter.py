from langchain_text_splitters import RecursiveCharacterTextSplitter,Language


text= """# Project Overview

This project is designed to streamline the process of data cleaning and feature engineering, providing analysts and data scientists with a consistent, reusable framework for processing structured datasets before moving into machine learning pipelines or visualization dashboards.

The system supports multiple data sources including CSV, JSON, and SQL-based tables, while also allowing for easy extension through a modular architecture. Users can configure each data pipeline by editing a simple YAML file, reducing the amount of boilerplate code and encouraging best practices across different teams.

## Why Use This?

Modern data workflows often become tangled and error-prone due to inconsistent handling of missing values, poor naming standards, and untracked transformations. By introducing this framework, your team will benefit from a transparent, version-controlled, and collaborative process that makes sure your data transformations are not only correct but also easy to explain and reproduce over time.

Moreover, our framework integrates seamlessly with standard tools like Jupyter notebooks, Airflow, and container orchestration solutions, making it ideal for both small research projects and production-grade data pipelines.


### Getting Started

Before you begin, make sure you have Python 3.10 or higher installed, along with pip and a supported virtual environment tool. Once your environment is ready, you can install the required packages by running `pip install -r requirements.txt` from the root directory of the repository.

After installation, simply configure your data sources inside the `config.yaml` file, and you can immediately launch the pipeline with the included CLI. The CLI supports logging options, dry runs, and step-by-step debugging to help you catch errors early before running the entire pipeline end-to-end.

"""


spliter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=500,
    chunk_overlap=0
    
)

result=spliter.split_text(text)

print(len(result)
      )
print(result)