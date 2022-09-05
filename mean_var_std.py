import numpy as np

def calculate(list):

  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  
  calculations={}
  a = np.array(list).reshape(3,3)
  calculations.setdefault('mean',[a.mean(axis=0).tolist(),a.mean(axis=1).tolist(),a.mean()])
  calculations.setdefault('variance',[a.var(axis=0).tolist(),a.var(axis=1).tolist(),a.var()])
  calculations.setdefault('standard deviation',[a.std(axis=0).tolist(),a.std(axis=1).tolist(),a.std()])
  calculations.setdefault('max',[a.max(axis=0).tolist(),a.max(axis=1).tolist(),a.max()])
  calculations.setdefault('min',[a.min(axis=0).tolist(),a.min(axis=1).tolist(),a.min()])
  calculations.setdefault('sum',[a.sum(axis=0).tolist(),a.sum(axis=1).tolist(),a.sum()])
  return calculations
