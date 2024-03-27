import numpy as np

def calculate(list):
    calculations = {}

    if len(list) < 9 :
        raise ValueError("List must contain nine numbers.")
    
    data = np.array([list[0:3],list[3:6],list[6:9]])
    #I didnt use reshape because I didnt know if I would receive a numpy array or a regular one
    calculations['mean'] = [data.mean(axis=0), data.mean(axis=1), np.mean(list)]
    calculations['varience'] = [data.var(axis=0), data.var(axis=1), np.var(list)]
    calculations['standard deviation'] = [data.std(axis=0), data.std(axis=1), np.std(list)]
    calculations['max'] = [data.max(axis=0), data.max(axis=1), np.max(list)]
    calculations['min'] = [data.min(axis=0), data.min(axis=1), np.min(list)]
    calculations['sum'] = [data.sum(axis=0), data.sum(axis=1), np.sum(list)]

    return calculations