
# MMLMGN

## Introduction

`MMLMGN` is a Python library designed to implement feature engineering based on **multi-similarity modality hypergraph contrastive learning**. It serves as the core implementation for the paper:  

**A Multi-Channel Graph Neural Network based on Multi-Similarity Modality Hypergraph Contrastive Learning for Predicting Unknown Types of Cancer Biomarkers**. 

The library offers a high-level API that simplifies tasks related to **graph representation learning**.

## Installation

Install `MMLMGN` via `pip`:

```bash
pip install MMLMGN
```

## Usage Example

Below is a sample usage demonstrating how to set input and output paths and run the model:

```python
import os
from mmlmgn.mmlmgn import InputPaths, OutputPaths, run

data_dir = 'data'
output_dir = 'output'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define input paths or use default InputPaths and OutputPaths
input_paths = InputPaths(
    Bin_data_path=f"{data_dir}/NodeGraph.csv",
    SimWalk_RNA_path=f"{data_dir}/NodeAWalker.csv",
    SimWalk_Dis_path=f"{data_dir}/NodeBWalker.csv",
    SimST_RNA_path=f"{data_dir}/NodeASt.csv",
    SimST_Dis_path=f"{data_dir}/NodeBSt.csv"
)

output_paths = OutputPaths(
    Save_RNA_BinFeature_path=f"{output_dir}/NodeAGraphEmb.csv",
    Save_DIS_BinFeature_path=f"{output_dir}/NodeBGraphEmb.csv",
    Save_RNAWalkerFeature_path=f"{output_dir}/NodeAWalkerEmb.csv",
    Save_DISWalkerFeature_path=f"{output_dir}/NodeBWalkerEmb.csv",
    Save_RNA_STFeature_path=f"{output_dir}/NodeAStEmb.csv",
    Save_DIS_STFeature_path=f"{output_dir}/NodeBStEmb.csv"
)

# Execute the graph representation learning process
run(input_paths, output_paths, 
    mi_num=467, dis_num=72,
    hidden_list=[256, 256], 
    proj_hidden=64,
    validation=1,
    epochs=2,
    lr=0.00001)
```
This example demonstrates how to configure input and output paths and run the learning process using the provided `run` function.


## Parameter Description

### Input

- File `NodeGraph.csv` is the graph input, used to construct the kernel similarity modal hyperedge of the node


- Files `NodeAWalker.csv` and `NodeBWalker.csv` are the feature inputs of two nodes, with a size of N*M, n is the number of nodes, and M is the feature dimension, used to construct the nearest neighbor modal hyperedge


- Files `NodeASt.csv` and `NodeBSt.csv` are the feature inputs of two nodes, with a size of N*M, n is the number of nodes, and M is the feature dimension, used to construct the structural topology modal hyperedge

Users can refer to https://github.com/1axin/MML-MGNN/tree/main/data to customize input to use MMLMGN


### Output


- NodeAGraphEmb.csv, NodeBGraphEmb.csv are the kernel similarity modal embeddings of nodes A and B respectively.


- NodeAWalkerEmb.csv, NodeBWalkerEmb.csv are the nearest neighbor similarity modal embeddings of nodes A and B respectively.


- NodeAStEmb.csv, NodeBStEmb.csv are the structural topology similarity modal embeddings of nodes A and B respectively.

### Parameters of run

- `input_paths`: An `InputPaths` object containing paths to the input data files. These files typically include network data or similarity data and serve as the primary input for the model.

- `output_paths`: An `OutputPaths` object that specifies where the feature extraction results and model outputs will be saved.

- `mi_num`: Indicates the number of Node A in the input data. 

- `dis_num`: Represents the number of Node B in the input data.

- `hidden_list`: A list that defines the number of neurons in each hidden layer of the model. 

- `proj_hidden`: Refers to the hidden layer size used during the projection process. This is typically used to adjust the intermediate representation of the data for optimal downstream feature usage.

- `epochs`: Number of training iterations. This defines how many times the model will go through the entire training dataset to converge towards a set of optimal parameters.

- `lr`: Learning rate, which controls the step size during the parameter updates in the training process. A smaller learning rate often leads to more stable convergence but might require longer training time.

These parameters are primarily used to configure the structure of the model and the training process, and they can be adjusted according to the specific task and characteristics of the data to optimize model performance.


## Features

- **Multi-similarity modality hypergraph contrastive learning**: Supports feature extraction across multiple similarity-based modalities.
- **Easy-to-use API**: Simple and flexible API for configuring input and output paths.
- **Customizable**: Users can easily adjust parameters such as hidden layers, projection dimensions, learning rate, and epochs.

## Documentation

For more detailed examples of input and output data, please visit https://github.com/1axin/MML-MGNN

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

For more details, refer to the [contributing guide](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it.

---

Thank you for using `MMLMGN`! If you encounter any issues or have suggestions, please open an issue on the repository.