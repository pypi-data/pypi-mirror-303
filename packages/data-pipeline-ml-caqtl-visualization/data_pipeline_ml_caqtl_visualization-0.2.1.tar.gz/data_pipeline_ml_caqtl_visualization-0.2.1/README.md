## Data Pipeline

Processes inference models predictions and observed data, exploratory data analysis, data vizualization.

## Configuration

Before running the pipelines, you need to configure them. Configuration files are located in the `/config/` directory. For custom configurations:

    This will create the following files that the user needs to fill out:

    - `pipelines/data_pipeline/configs/direct_input_config.json`
    - `pipelines/data_pipeline/configs/personal_config.json`

2. **Edit Config Files**: Modify the configuration files to match your data and setup. These files contain the necessary parameters and paths required to run the pipelines successfully. Ensure that all paths, model checkpoints, and settings are correctly specified to match your environment.



### Option 1: Default Repository Structure

Use this option if you're following the default setup as structured in the repository:

```bash
python generate_config.py --config_file configs/default_config.json
```

### Option 2: Custom Configuration

Use this option if you need to specify custom paths and settings:

```bash
python generate_config.py --direct_input --config_file configs/direct_input_config.json
```

3. **Usage**: Once the configuration is complete, you can run the pipeline.

## Running the pipeline

### Data Frame Generation

### Exploratory Data Analysis(EDA)

### Data Visualization


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details

