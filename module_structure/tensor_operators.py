import torch


__all__ = ['TensorCalculator']


class TensorCalculator():

    def __init__(self):
        return None


    @staticmethod
    def tensor_ones(dim_x, dim_y, dim_z):
        ones = torch.ones([dim_x, dim_y, dim_z])
        return ones

    @staticmethod
    def tensor_zeros(dim_x, dim_y, dim_z):
        zeros = torch.zeros([dim_x, dim_y, dim_z])
        return zeros

    @staticmethod
    def tensor_random(dim_x, dim_y, dim_z):
        randomt = torch.rand([dim_x, dim_y, dim_z])
        return randomt

    @staticmethod
    def tensor_sum(tensor1, tensor2):
        tsum = tensor1 + tensor2
        return tsum

    @staticmethod
    def tensor_mult(tensor1, tensor2):
        tmult = tensor1 * tensor2
        return tmult

    @staticmethod
    def tensor_plusone(tensor1):
        tdim = tensor1.size()
        tones = torch.ones(tdim)
        tplusone = tensor1 + tones
        return tplusone

