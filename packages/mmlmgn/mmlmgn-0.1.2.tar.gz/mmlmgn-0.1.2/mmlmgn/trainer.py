import torch
import numpy as np
from . import ConstructHW
import warnings
from .utils import get_L2reg, Myloss
import pandas as pd
warnings.filterwarnings("ignore")
device = torch.device("cpu")


def test(
    model,
    data,
    concat_mi_tensor,
    concat_dis_tensor,
    G_mi_Kn,
    G_mi_Km,
    G_dis_Kn,
    G_dis_Km,
):
    model.eval()
    score, _, _, _, _ = model(
        concat_mi_tensor, concat_dis_tensor, G_mi_Kn, G_mi_Km, G_dis_Kn, G_dis_Km
    )
    test_one_index = data[3][0]
    test_zero_index = data[3][1]
    true_one = data[5][test_one_index]
    true_zero = data[5][test_zero_index]

    pre_one = score[test_one_index]
    pre_zero = score[test_zero_index]

    return true_one, true_zero, pre_one, pre_zero


def train_epoch_MDA(model, train_data, optim, epochs, Save_RNA_BinFeature_path, Save_DIS_BinFeature_path):

    model.train()
    regression_crit = Myloss()

    one_index = train_data[2][0]
    zero_index = train_data[2][1]


    dis_sim_integrate_tensor = train_data[0].to(device)
    mi_sim_integrate_tensor = train_data[1].to(device)


    concat_miRNA = np.hstack(
        [train_data[4].numpy(), mi_sim_integrate_tensor.detach().cpu().numpy()]
    )
    concat_mi_tensor = torch.FloatTensor(concat_miRNA)
    concat_mi_tensor = concat_mi_tensor.to(device)

    G_mi_Kn = ConstructHW.constructHW_knn(
        concat_mi_tensor.detach().cpu().numpy(), K_neigs=[13], is_probH=False
    )
    G_mi_Km = ConstructHW.constructHW_kmean(
        concat_mi_tensor.detach().cpu().numpy(), clusters=[9]
    )
    G_mi_Kn = G_mi_Kn.to(device)
    G_mi_Km = G_mi_Km.to(device)

    concat_dis = np.hstack(
        [train_data[4].numpy().T, dis_sim_integrate_tensor.detach().cpu().numpy()]
    )
    concat_dis_tensor = torch.FloatTensor(concat_dis)
    concat_dis_tensor = concat_dis_tensor.to(device)

    G_dis_Kn = ConstructHW.constructHW_knn(
        concat_dis_tensor.detach().cpu().numpy(), K_neigs=[13], is_probH=False
    )
    G_dis_Km = ConstructHW.constructHW_kmean(
        concat_dis_tensor.detach().cpu().numpy(), clusters=[9]
    )
    G_dis_Kn = G_dis_Kn.to(device)
    G_dis_Km = G_dis_Km.to(device)

    X1 = []
    Y1 = []

    for epoch in range(1, epochs + 1):

        score, mi_cl_loss, dis_cl_loss, X1, Y1 = model(
            concat_mi_tensor,
            concat_dis_tensor,
            G_mi_Kn,
            G_mi_Km,
            G_dis_Kn,
            G_dis_Km,
        )

        recover_loss = regression_crit(
            one_index, zero_index, train_data[4].to(device), score
        )
        reg_loss = get_L2reg(model.parameters())

        tol_loss = recover_loss + mi_cl_loss + dis_cl_loss + 0.00001 * reg_loss
        optim.zero_grad()
        tol_loss.backward()
        optim.step()

    true_value_one, true_value_zero, pre_value_one, pre_value_zero = test(
        model,
        train_data,
        concat_mi_tensor,
        concat_dis_tensor,
        G_mi_Kn,
        G_mi_Km,
        G_dis_Kn,
        G_dis_Km,
    )

    X1 = X1.detach().numpy()
    Y1 = Y1.detach().numpy()
    X = pd.DataFrame(X1)
    Y = pd.DataFrame(Y1)

    X.to_csv(Save_RNA_BinFeature_path, index=True)
    Y.to_csv(Save_DIS_BinFeature_path, index=True)

    return 0


def train_epoch_MDA_ST(model, train_data, optim, epochs, Save_RNAWalkerFeature_path, Save_DISWalkerFeature_path):

    model.train()
    regression_crit = Myloss()

    one_index = train_data[2][0]
    zero_index = train_data[2][1]


    dis_Walker_integrate_tensor = train_data[14].to(device)
    mi_Walker_integrate_tensor = train_data[15].to(device)

    dis_Walker_OD_tensor = train_data[12].to(device)
    mi_Walker_OD_tensor = train_data[13].to(device)

    mi_Walker_integrate_tensor1 = np.hstack(
        [train_data[4].numpy(), mi_Walker_integrate_tensor.detach().cpu().numpy()]
    )
    Walker_mi_tensor = torch.FloatTensor(mi_Walker_integrate_tensor1)
    Walker_mi_tensor = Walker_mi_tensor.to(device)

    G_Walker_mi_Kn = ConstructHW.constructHW_knn(
        Walker_mi_tensor.detach().cpu().numpy(), K_neigs=[13], is_probH=False
    )
    G_Walker_mi_Km = ConstructHW.constructHW_kmean(
        Walker_mi_tensor.detach().cpu().numpy(), clusters=[9]
    )
    G_Walker_mi_Kn = G_Walker_mi_Kn.to(device)
    G_Walker_mi_Km = G_Walker_mi_Km.to(device)

    dis_Walker_integrate_tensor1 = np.hstack(
        [train_data[4].numpy().T, dis_Walker_integrate_tensor.detach().cpu().numpy()]
    )
    Walker_dis_tensor = torch.FloatTensor(dis_Walker_integrate_tensor1)
    Walker_dis_tensor = Walker_dis_tensor.to(device)

    G_Walker_dis_Kn = ConstructHW.constructHW_knn(
        Walker_dis_tensor.detach().cpu().numpy(), K_neigs=[13], is_probH=False
    )
    G_Walker_dis_Km = ConstructHW.constructHW_kmean(
        Walker_dis_tensor.detach().cpu().numpy(), clusters=[9]
    )
    G_Walker_dis_Kn = G_Walker_dis_Kn.to(device)
    G_Walker_dis_Km = G_Walker_dis_Km.to(device)

    mi_Walker_OD_tensor1 = np.hstack(
        [train_data[4].numpy(), mi_Walker_OD_tensor.detach().cpu().numpy()]
    )
    Walker_mi_OD_tensor = torch.FloatTensor(mi_Walker_OD_tensor1)
    Walker_mi_OD_tensor = Walker_mi_OD_tensor.to(device)

    dis_Walker_OD_tensor1 = np.hstack(
        [train_data[4].numpy().T, dis_Walker_OD_tensor.detach().cpu().numpy()]
    )
    Walker_dis_OD_tensor = torch.FloatTensor(dis_Walker_OD_tensor1)
    Walker_dis_OD_tensor = Walker_dis_OD_tensor.to(device)

    X1 = []
    Y1 = []

    for epoch in range(1, epochs + 1):

        score_TP, mi_TP_loss, dis_TP_loss, X1, Y1 = model(
            Walker_mi_OD_tensor,
            Walker_dis_OD_tensor,
            G_Walker_mi_Kn,
            G_Walker_mi_Km,
            G_Walker_dis_Kn,
            G_Walker_dis_Km,
        )

        recover_loss_TP = regression_crit(
            one_index, zero_index, train_data[4].to(device), score_TP
        )
        reg_loss_TP = get_L2reg(model.parameters())

        tol_loss_TP = recover_loss_TP + mi_TP_loss + dis_TP_loss + 0.00001 * reg_loss_TP
        optim.zero_grad()
        tol_loss_TP.backward()
        optim.step()

    true_value_one_TP, true_value_zero_TP, pre_value_one_TP, pre_value_zero_TP = test(
        model,
        train_data,
        Walker_mi_OD_tensor,
        Walker_dis_OD_tensor,
        G_Walker_mi_Kn,
        G_Walker_mi_Km,
        G_Walker_dis_Kn,
        G_Walker_dis_Km,
    )

    X1 = X1.detach().numpy()
    Y1 = Y1.detach().numpy()
    X = pd.DataFrame(X1)
    Y = pd.DataFrame(Y1)

    X.to_csv(Save_RNAWalkerFeature_path, index=True)
    Y.to_csv(Save_DISWalkerFeature_path, index=True)

    return 0


def train_epoch_MDA_TP(model, train_data, optim, epochs, Save_RNA_STFeature_path, Save_DIS_STFeature_path):

    model.train()
    regression_crit = Myloss()

    one_index = train_data[2][0]
    zero_index = train_data[2][1]

    dis_Walker_integrate_tensor = train_data[10].to(device)
    mi_Walker_integrate_tensor = train_data[11].to(device)

    dis_Walker_OD_tensor = train_data[8].to(device)
    mi_Walker_OD_tensor = train_data[9].to(device)

    mi_Walker_integrate_tensor1 = np.hstack(
        [train_data[4].numpy(), mi_Walker_integrate_tensor.detach().cpu().numpy()]
    )
    Walker_mi_tensor = torch.FloatTensor(mi_Walker_integrate_tensor1)
    Walker_mi_tensor = Walker_mi_tensor.to(device)

    G_Walker_mi_Kn = ConstructHW.constructHW_knn(
        Walker_mi_tensor.detach().cpu().numpy(), K_neigs=[13], is_probH=False
    )
    G_Walker_mi_Km = ConstructHW.constructHW_kmean(
        Walker_mi_tensor.detach().cpu().numpy(), clusters=[9]
    )
    G_Walker_mi_Kn = G_Walker_mi_Kn.to(device)
    G_Walker_mi_Km = G_Walker_mi_Km.to(device)


    dis_Walker_integrate_tensor1 = np.hstack(
        [train_data[4].numpy().T, dis_Walker_integrate_tensor.detach().cpu().numpy()]
    )
    Walker_dis_tensor = torch.FloatTensor(dis_Walker_integrate_tensor1)
    Walker_dis_tensor = Walker_dis_tensor.to(device)

    G_Walker_dis_Kn = ConstructHW.constructHW_knn(
        Walker_dis_tensor.detach().cpu().numpy(), K_neigs=[13], is_probH=False
    )
    G_Walker_dis_Km = ConstructHW.constructHW_kmean(
        Walker_dis_tensor.detach().cpu().numpy(), clusters=[9]
    )
    G_Walker_dis_Kn = G_Walker_dis_Kn.to(device)
    G_Walker_dis_Km = G_Walker_dis_Km.to(device)


    mi_Walker_OD_tensor1 = np.hstack(
        [train_data[4].numpy(), mi_Walker_OD_tensor.detach().cpu().numpy()]
    )
    Walker_mi_OD_tensor = torch.FloatTensor(mi_Walker_OD_tensor1)
    Walker_mi_OD_tensor = Walker_mi_OD_tensor.to(device)

    dis_Walker_OD_tensor1 = np.hstack(
        [train_data[4].numpy().T, dis_Walker_OD_tensor.detach().cpu().numpy()]
    )
    Walker_dis_OD_tensor = torch.FloatTensor(dis_Walker_OD_tensor1)
    Walker_dis_OD_tensor = Walker_dis_OD_tensor.to(device)

    X1 = []
    Y1 = []

    for epoch in range(1, epochs + 1):

        score_TP, mi_TP_loss, dis_TP_loss, X1, Y1 = model(
            Walker_mi_OD_tensor,
            Walker_dis_OD_tensor,
            G_Walker_mi_Kn,
            G_Walker_mi_Km,
            G_Walker_dis_Kn,
            G_Walker_dis_Km,
        )

        recover_loss_TP = regression_crit(
            one_index, zero_index, train_data[4].to(device), score_TP
        )
        reg_loss_TP = get_L2reg(model.parameters())

        tol_loss_TP = recover_loss_TP + mi_TP_loss + dis_TP_loss + 0.00001 * reg_loss_TP
        optim.zero_grad()
        tol_loss_TP.backward()
        optim.step()

    true_value_one_TP, true_value_zero_TP, pre_value_one_TP, pre_value_zero_TP = test(
        model,
        train_data,
        Walker_mi_OD_tensor,
        Walker_dis_OD_tensor,
        G_Walker_mi_Kn,
        G_Walker_mi_Km,
        G_Walker_dis_Kn,
        G_Walker_dis_Km,
    )

    X1 = X1.detach().numpy()
    Y1 = Y1.detach().numpy()
    X = pd.DataFrame(X1)
    Y = pd.DataFrame(Y1)

    X.to_csv(Save_RNA_STFeature_path, index=True)
    Y.to_csv(Save_DIS_STFeature_path, index=True)

    return 0
