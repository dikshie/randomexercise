#!/usr/bin/python 

import numpy as np
import statsmodels.api as sm

tsa = sm.tsa

# simple linear model 
mdata = sm.datasets.macrodata.load().data
endog = np.log(mdata['m1'])
exog = np.column_stack([np.log(mdata['realgdp']), np.log(mdata['cpi'])])
exog = sm.add_constant(exog, prepend=True)
res1 = sm.OLS(endog, exog).fit()

print res1.summary()


#autocorrelation 

acf, ci, Q, pvalue = tsa.acf(res1.resid, nlags=4, alpha=95, qstat=True, unbiased=True)
print acf
print pvalue

#check GLSAR
mod2 = sm.GLSAR(endog, exog, rho=4)
res2 = mod2.iterative_fit()
print res2.params



