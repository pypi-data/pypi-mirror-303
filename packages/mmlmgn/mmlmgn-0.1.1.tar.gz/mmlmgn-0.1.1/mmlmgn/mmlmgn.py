"""MMLMGN runner."""
from .DataProcess import PrepareBinData
from torch import optim
from .Module import MMLMGN
from .DataSet import Dataset_MDA
import warnings
from .trainer import train_epoch_MDA, train_epoch_MDA_ST, train_epoch_MDA_TP
from dataclasses import dataclass

warnings.filterwarnings("ignore")

@dataclass
class InputPaths:
    Bin_data_path: str
    SimWalk_RNA_path: str
    SimWalk_Dis_path: str
    SimST_RNA_path: str
    SimST_Dis_path: str
    """ Paths to the input data.
    Parameters:
        Bin_data_path (str): Path to the RNA and disease association data.
        SimWalk_RNA_path (str): Path to the RNA Walker data.
        SimWalk_Dis_path (str): Path to the disease Walker data.
        SimST_RNA_path (str): Path to the RNA ST data.
        SimST_Dis_path (str): Path to the disease ST data.
    """
@dataclass
class OutputPaths:
    Save_RNA_BinFeature_path: str
    Save_DIS_BinFeature_path: str
    Save_RNAWalkerFeature_path: str
    Save_DISWalkerFeature_path: str
    Save_RNA_STFeature_path: str
    Save_DIS_STFeature_path: str
    
    """ Paths to the output data.
        Save_RNA_BinFeature_path (str): Path where RNA binary features are saved.
        Save_DIS_BinFeature_path (str): Path where disease binary features are saved.
        Save_RNAWalkerFeature_path (str): Path where RNA Walker features are saved.
        Save_DISWalkerFeature_path (str): Path where disease Walker features are saved.
        Save_RNA_STFeature_path (str): Path where RNA ST features are saved.
        Save_DIS_STFeature_path (str): Path where disease ST features are saved.
    """
    
def run(input_paths: InputPaths, output_paths: OutputPaths, mi_num=467, dis_num=72, 
        hidden_list=[256, 256], proj_hidden=64, validation=5, epochs=5, lr=0.01):
    """
    Executes the MMLMGN model training and saves the embedding results.

    Parameters:
        input_paths (InputPaths): Container for all input data file paths.
        output_paths (OutputPaths): Container for all output file paths.
        mi_num (int): Number of RNAs. Default is 467.
        dis_num (int): Number of diseases. Default is 72.
        hidden_list (list of int): List of sizes for hidden layers. Default is [256, 256].
        proj_hidden (int): Size of the projection hidden layer. Default is 64.
        validation (int): Number of validations. Default is 5.
        epochs (int): Number of training epochs. Default is 5.
        lr (float): Learning rate for the optimizer. Default is 0.01.
    Returns:
        None
    """
    # Example of how you might use the paths in your function
    dataset = PrepareBinData(
        input_paths.Bin_data_path,
        input_paths.SimWalk_RNA_path,
        input_paths.SimWalk_Dis_path,
        input_paths.SimST_RNA_path,
        input_paths.SimST_Dis_path
    )
    
    model_MDA = MMLMGN(mi_num, dis_num, hidden_list, proj_hidden)
    optimizer = optim.Adam(model_MDA.parameters(), lr=lr)
    train_data_MDA = Dataset_MDA(validation, dataset)

    # Example training function calls using the paths from output_paths
    train_epoch_MDA(model_MDA, train_data_MDA[0], optimizer, epochs, output_paths.Save_RNA_BinFeature_path, output_paths.Save_DIS_BinFeature_path)
    train_epoch_MDA_ST(model_MDA, train_data_MDA[0], optimizer, epochs, output_paths.Save_RNAWalkerFeature_path, output_paths.Save_DISWalkerFeature_path)
    train_epoch_MDA_TP(model_MDA, train_data_MDA[0], optimizer, epochs, output_paths.Save_RNA_STFeature_path, output_paths.Save_DIS_STFeature_path)
    print("Finish")

if __name__ == "__main__":

    run()
