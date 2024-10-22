<h1 align='center'>
    <strong> Synthetic Data Generator </strong>
</h1>

<p align='center'>
    Designed to generate synthetic data on the fly so you can stress test your pipelines with ease.
</p>

<div align="center">

  <a href="code coverage">![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)</a>
  <a href="tests">![tests](https://img.shields.io/badge/tests-35%20passed%2C%200%20failed-brightgreen)</a>
  <a href="python version">![sbt_version](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)</a>

</div>

### **1. Intro**

The Synthetic Data Generator is a powerful tool designed to help developers and data engineers stress test their data pipelines with ease. By generating realistic, customizable synthetic data on the fly, this project enables thorough testing of data processing systems under various conditions and loads.

Key features of the Synthetic Data Generator include:

- **On-demand data generation**: Create large volumes of synthetic data as needed;
- **Scalability**: Suitable for testing small to large-scale data pipelines;
- **Integration-friendly**: Designed to work seamlessly with various data processing frameworks.

Whether you're developing a new data pipeline, optimizing an existing one, or conducting performance testing, the Synthetic Data Generator provides the flexible, controllable data source you need to ensure your systems are robust and reliable under real-world conditions.

### **2. How to Use - _high level_**

- if you want to generate samples to all the file type handled by the project:
````python
from neso_utils import SyntheticDataGenerator

from neso_utils.synthetic_data_generator import FileType
from neso_utils.synthetic_data_generator import ValuesType

generator = SyntheticDataGenerator(
    target_size_mb=10,
    num_columns=10,
    sample_rows_num=1000,
)

generator.generate_all_file_types("test_data", "test_folder")
````

- if you want to generate samples to a specific file type:

````python
from neso_utils import SyntheticDataGenerator

from neso_utils.synthetic_data_generator import FileType
from neso_utils.synthetic_data_generator import ValuesType

generator = SyntheticDataGenerator(target_size_mb=100)

generator.generate_file(
    values_type=ValuesType.STRING,
    file_name="test_data_100mb",
    file_type=FileType.CSV,
    landing_path="test_folder"
)
````

### **A1. Future Work**

There are still some points that we should tackle:

- It's hard to scale the size of the generated data for the ttl files up to the target size, since it's not proportional to the records number - *something that needs to be explored*;
