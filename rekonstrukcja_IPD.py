def rekonstrukcja_ipd():
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
    fromkm = rpy2.robjects.packages.importr("IPDfromKM")
    dplyr = rpy2.robjects.packages.importr('dplyr')
    xls = rpy2.robjects.packages.importr("readxl")

    # Import funkcji
    preprocess, getIPD, survreport = fromkm.preprocess, fromkm.getIPD, fromkm.survreport
    xls = xls.read_excel
    c, rbind, cbind, summary = base.c, base.rbind, base.cbind, base.summary

    # wprowadź dane py
    arm0 = xls("arm0.xlsx")
    arm1 = xls("arm1.xlsx")

    nrisk_arm0 = [78, 45, 30, 20, 11, 5, 1, 0]
    nrisk_arm1 = [38, 14, 6, 2, 2, 0, 0, 0]
    trisk = [0, 5, 10, 15, 20, 25, 30, 35]
    maxy = 1

    # przerzuć listy na wektory
    nrisk_arm0 = robjects.IntVector(nrisk_arm0)
    nrisk_arm1 = robjects.IntVector(nrisk_arm1)
    trisk = robjects.IntVector(trisk)

    # przeprowadź proces rekonstrukcji
    preprocess_arm0 = preprocess(arm0, trisk=trisk, nrisk=nrisk_arm0, maxy=maxy)
    getIPD_arm0 = getIPD(preprocess_arm0, armID=1)
    ipd_arm0 = getIPD_arm0.rx2('IPD')
    surv_arm0 = survreport(ipd_arm0, arms=1, interval=6, s=c(0.75, 0.5, 0.25))

    preprocess_arm1 = preprocess(arm1, trisk=trisk, nrisk=nrisk_arm1, maxy=maxy)
    getIPD_arm1 = getIPD(preprocess_arm1, armID=2)
    ipd_arm1 = getIPD_arm1.rx2('IPD')
    surv_arm1 = survreport(ipd_arm1, arms=1, interval=6, s=c(0.75, 0.5, 0.25))  #

    ipd1 = rbind(ipd_arm0, ipd_arm1)

    # przerzuć na py
    ipd2 = pd.DataFrame(ipd1)
    ipd = np.transpose(ipd2)

    # przekształcenie danych
    ipd = ipd.rename(columns={0: "time", 1: "status", 2: "arm"})
    ipd['arm'] = np.where(ipd['arm'] == 1, 0, 1)

    # zapis
    ipd.to_excel("ipd.xlsx", header=True, index=False)

    return ipd

a = rekonstrukcja_ipd()

print(a)