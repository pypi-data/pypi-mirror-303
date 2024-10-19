import argparse


def parameter_parser():

    parser = argparse.ArgumentParser(description="Run MGNN.")

    parser.add_argument(
        "--Bin_data_path",
        type=str,
        default="../data/NodeGraph.csv",
        help="Path to the association of RNA and disease",
    )

    parser.add_argument(
        "--SimWalk_RNA_path",
        type=str,
        default="../data/Node_A_Walker.csv",
        help="Path to the walker of RNA",
    )

    parser.add_argument(
        "--SimWalk_Dis_path",
        type=str,
        default="../data/Node_B_Walker.csv",
        help="Path to the walker of disease",
    )

    parser.add_argument(
        "--SimST_RNA_path",
        type=str,
        default="../data/Node_A_St.csv",
        help="Path to the ST of RNA",
    )

    parser.add_argument(
        "--SimST_Dis_path",
        type=str,
        default="../data/Node_B_St.csv",
        help="Path to the ST of disease",
    )

    parser.add_argument(
        "--validation", type=int, default=2, help="the number of validation"
    )
    parser.add_argument("--epoch", type=int, default=5, help="the number of epoch.")
    parser.add_argument("--mi_num", type=int, default=467, help="the number of RNA")
    parser.add_argument(
        "--dis_num", type=int, default=72, help="the number of diseases"
    )
    parser.add_argument("--alpha", type=int, default=0.11, help="the size of alpha")
    parser.add_argument(
        "--dropout", type=float, default=0.1, help="Dropout rate (1 - keep probability)"
    )
    parser.add_argument(
        "--proj_hidden", type=int, default=64, help="the number of proj_hidden"
    )

    parser.add_argument(
        "--hidden_list", nargs="+", type=int, help="the number of hidden_list"
    )
    parser.set_defaults(hidden_list=[256, 256])

    parser.add_argument(
        "--Save_RNA_BinFeature_path",
        type=str,
        default="../output/NodeAGraphEmb.csv",
        help="Path to save the node A Graph processed file",
    )

    parser.add_argument(
        "--Save_DIS_BinFeature_path",
        type=str,
        default="../output/NodeBGraphEmb.csv",
        help="Path to save the node B Graph processed file",
    )

    parser.add_argument(
        "--Save_RNAWalkerFeature_path",
        type=str,
        default="../output/NodeAWalkerEmb.csv",
        help="Path to save the node A Walker processed file",
    )

    parser.add_argument(
        "--Save_DISWalkerFeature_path",
        type=str,
        default="../output/NodeBWalkerEmb.csv",
        help="Path to save the node B Walker processed file",
    )

    parser.add_argument(
        "--Save_RNA_STFeature_path",
        type=str,
        default="../output/NodeAStEmb.csv",
        help="Path to save the node A ST processed file",
    )

    parser.add_argument(
        "--Save_DIS_STFeature_path",
        type=str,
        default="../output/NodeBStEmb.csv",
        help="Path to save the node B ST processed file",
    )

    return parser.parse_args()
