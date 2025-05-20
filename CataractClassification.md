In the YAML file, you'll find the necessary details you need to include:

**$schema**: The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including $schema at the top of your file enables you to invoke schema and resource completions.

The code refers to the local folder, which stores the scripts you want to run. The command key specifies that the main.py script in the src folder should be executed, using the value of inputs.diabetes for the diabetes-csv parameter.
Version 1 of the registered data asset diabetes-data in the Azure Machine Learning workspace is mounted to the compute to be used as input for the script.
The compute instance aml-instance will be used to run the scripts.
The latest version of the registered custom basic-env-scikit environment will be installed on the compute instance before running the script.
To test the YAML definition of the job, you can trigger it using the CLI v2.
