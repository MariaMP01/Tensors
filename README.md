# Tensors
In this assignment Your target will be to code a module that is able to perform the following operations with Pytorch 2-dimensional Tensors
# Repository
In the first place it is needed to create a repository in GitHub which I have called 'Tensors' and in it I added all the files needed
# Calculator
Now in python is time to create the functions needed for the tensor calculator.
Inside a class called 'TensorCalculator' we create all this functions.
download or clone the assignment repository, any initial setup or configuration required, and any dependencies that need to be installed.

For all the functions I used a '@staticmethod' as the function does not call any item from the class
1. Returns an all-Ones Tensor
```python
    @staticmethod
    def tensor_ones(dim_x, dim_y, dim_z):
        ones = torch.ones([dim_x, dim_y, dim_z])
        return ones
```
2. Returns an all-Zeros Tensor
```python
    @staticmethod
    def tensor_zeros(dim_x, dim_y, dim_z):
        zeros = torch.zeros([dim_x, dim_y, dim_z])
        return zeros
```
3. Returns a Tensor with random values
```python
    @staticmethod
    def tensor_random(dim_x, dim_y, dim_z):
        randomt = torch.rand([dim_x, dim_y, dim_z])
        return randomt
```
4. Returns the sum of two tensor
```python
    @staticmethod
    def tensor_sum(tensor1, tensor2):
        tsum = tensor1 + tensor2
        return tsum
```
5. Returns the multiplication of two tensors
```python
    @staticmethod
    def tensor_mult(tensor1, tensor2):
        tmult = tensor1 * tensor2
        return tmult
```

# Additional functions 
I have created two additional functions to operate with tensors. 
1. The first one is a function that adds 1 to each element of the tensor
```python
    @staticmethod
    def tensor_plusone(tensor1):
        tdim = tensor1.size()
        tones = torch.ones(tdim)
        tplusone = tensor1 + tones
        return tplusone
```
2. The second one is a functions that multiplies by a given number a given tensor
```python
    @staticmethod
    def tensor_multN(tensor1, n):
        tmult = torch.mul(tensor1, n)
        return tmult
```

# GitHub
I commit the python file with the changes to the GitHub repository created before. 
And finally copy the link ready to be passed.
