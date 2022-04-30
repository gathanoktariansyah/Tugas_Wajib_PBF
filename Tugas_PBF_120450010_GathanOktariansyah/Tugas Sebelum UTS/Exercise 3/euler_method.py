from solver import *

def cauchy_euler(params,Func):
    t0 = params['t0']
    t_end = params['t_end']
    h = params['h']
    y0 = params['y0']
    dy0 = params['dy0']
    
    res_euler = []
    t = []
    step = int((t_end - t0) / h)
    
    for i in range(step):
        tm = (i + 1) * h
        (y_next, dy_next) = euler(tm, h, y0, dy0, Func)
        res_euler.append(y_next)
        t.append(tm)
        y0 = y_next
        dy0 = dy_next
    return (t, res_euler)

def cauchy_eulercromer(params, Func):
    t0 = params['t0']
    t_end = params['t_end']
    h = params['h']
    y0 = params['y0']
    dy0 = params['dy0']
    
    res_eulercromer = []
    t = []
    step = int((t_end - t0) / h)
    
    for i in range(step):
        tm = (i + 1) * h
        (y_next, dy_next) = eulercromer(tm, h, y0, dy0, Func)
        res_eulercromer.append(y_next)
        t.append(tm)
        y0 = y_next
        dy0 = dy_next
    return (t, res_eulercromer)