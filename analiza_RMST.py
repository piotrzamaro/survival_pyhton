
def analiza_rmst(ipd):
    import pandas as pd
    import rpy2.robjects as robjects
    import rpy2.robjects.packages
    import numpy as np
    from numpy import ndarray
    from rpy2.robjects import IntVector
    from rpy2.robjects import Formula

    # instalacja pakietów R
    stats = rpy2.robjects.packages.importr('stats')
    base = rpy2.robjects.packages.importr('base')
    utils = rpy2.robjects.packages.importr('utils')
    dplyr = rpy2.robjects.packages.importr('dplyr')
    xls = rpy2.robjects.packages.importr("readxl")
    rm = rpy2.robjects.packages.importr("survRM2")

    # Import funkcji
    rmst2 = rm.rmst2
    xls = xls.read_excel
    c, rbind, cbind, summary = base.c, base.rbind, base.cbind, base.summary

    # Horyzont badania

    # Model RMST
    time = robjects.FloatVector(ipd.time)
    status = robjects.IntVector(ipd.status)
    arm = robjects.IntVector(ipd.arm)

    rmst = rmst2(time, status, arm) #argument tau określa punkt odcięcia
    print(rmst)
    return rmst
