import numpy as np

# function that takes as input a list of numbers, and returns the list of values given by the softmax function.
def softmax(L):
    den = np.sum(np.exp(L))
    rt_list = []
    for i in L:
        rt_list.append(np.exp(i)/den)
    return rt_list
