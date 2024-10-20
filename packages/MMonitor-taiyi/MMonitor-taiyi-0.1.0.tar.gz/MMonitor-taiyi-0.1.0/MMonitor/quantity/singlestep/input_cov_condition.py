import math

from MMonitor.quantity.singlestep.base_class import SingleStepQuantity
from MMonitor.extensions import ForwardInputEigOfCovExtension
import torch
import numpy as np
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

class InputCovCondition(SingleStepQuantity):
    def _compute(self, global_step):
        eig_values, step = getattr(self._module, 'eig_values', (None, None))
        if eig_values is None or step is None or step != global_step:
            data = self._module.input_eig_data
            cov = cal_cov_matrix(data) 
            eig_values = cal_eig(cov) 
            eig_values, _ = torch.sort(eig_values, descending=True)
            setattr(self._module, 'eig_values', (eig_values, global_step)) 
        eps = 1e-7
        condition = eig_values[0] / (torch.abs(eig_values[-1]) + eps)
        return condition

    def forward_extensions(self):
        extensions = [ForwardInputEigOfCovExtension()]
        return extensions