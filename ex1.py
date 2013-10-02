#!/usr/bin/python

from random import gauss
from math import exp

#
# stock prices are assumed to fluctuate
# dS = \miu S dt + \lambda S dW_t
# this equation can be discretization

def BlackScholes(St0,strike,riskless,vol,time,trials,payout=lambda strike,ST: max(ST-strike,0)):
        return reduce(lambda x,y: x+payout(strike,reduce(lambda x,y: x*exp((riskless-.5*vol**2)*(1.0/365) + vol*(1.0/365)**.5*gauss(0,1)),range(time),St0)),range(trials))/trials


result=BlackScholes(41.75,45,.0535,.34,61,10000,lambda strike,ST:max(strike-ST,0))
print result, 'USD'
