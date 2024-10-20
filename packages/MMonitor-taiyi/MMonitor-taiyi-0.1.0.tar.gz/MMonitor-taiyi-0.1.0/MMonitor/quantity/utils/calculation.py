import torch
import torch.linalg as linalg


def cal_cov_matrix(input):
    if input.dim() == 2:
        return torch.cov(input.T) 

    if input.dim() == 3:
        input = input.transpose(0, 2).contiguous().view(input.shape[2], -1)

        return torch.cov(input)


def cal_eig(input):

    try:
        _, eigvals, _ = linalg.svd(input.float())
    except Exception as e:
        lens = min(input.shape)
        eigvals = torch.tensor([1.1 for i in range(lens)])
        eigvals[lens-1] = 111
    return eigvals

def cal_eig_not_sym(input):
    try:
        _, eigvals, _ = linalg.svd(input.float())
    except Exception as e:
        lens = min(input.shape)
        eigvals = torch.tensor([1.1 for i in range(lens)])
        eigvals[lens-1] = 111
    return eigvals
