import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import random
from datetime import datetime
import time
import csv
from os import path

stocks = ['ABT', 'ABBV', 'ACN', 'ACE', 'ADBE', 'ADT', 'AAP', 'AES', 'AET', 'AFL', 'AMG', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'AGN', 'ALXN', 'ALLE', 'ADS', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVGO', 'AVB', 'AVY', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BXLT', 'BAX', 'BBT', 'BDX', 'BBBY', 'BRK-B', 'BBY', 'BLX', 'HRB', 'BA', 'BWA', 'BXP', 'BSK', 'BMY', 'BRCM', 'BF-B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'HSIC', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'GLW', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA', 'DISCK', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ENDP', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ES', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FB', 'FAST', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FSIV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GPS', 'GRMN', 'GD', 'GE', 'GGP', 'GIS', 'GM', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOGL', 'GOOG', 'GWW', 'HAL', 'HBI', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HCN', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'GMCR', 'KMB', 'KIM'. 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LLTC', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MNK', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHFI', 'MCK', 'MJN', 'MMV', 'MDT', 'MRK', 'MET', 'KORS', 'MCHP', 'MU', 'MSFT', 'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NLSN', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'O', 'RHT', 'REGN', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RLC', 'R', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SIAL', 'SPG', 'SWKS', 'SLG', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'TGNA', 'THC', 'TDC', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TJK', 'TMK', 'TSS', 'TSCO', 'RIG', 'TRIP', 'FOXA', 'TSN', 'TYC', 'UA', 'UNP', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'ANTM', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WEC', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']

data = yf.download('DIS', '2005-01-01','2019-01-01')
aaplDfPoints = data['Close']
appleDataPoints = np.array(aaplDfPoints)

# This is the dataset the network can pick a value from randomly. It is reduced to avoid dimensionality problems in the for loop
# while it's training. If the first element of the pickable dataset is chosen still have date which can be passed to the network.
# At the end of the data set the size of the reduction was just a random choice it can be tuned later.
sizeOfTrainingSet = 100
pickableAppleDataPoints = appleDataPoints[sizeOfTrainingSet:-sizeOfTrainingSet]

# We want to decide if we have a buying or a selling point by pattern recognition.
# In this case we have two choices of output:
#         i)  two output options: buy or sell;
#         ii) three output options: buy, sell or wait(do nothing) -> this is the real life scenario.
# The next step is creating the training databese with labelled data.
# It is created by picking the random data points and everyone of them has a 100 data point of history.
# For every picked datapoint it is checked and labelled if it is a buy or a sell point.
# It is done like this:
#         we defined the percentage values of required values to win and to lose and if the price steps out of these boundaries
#         we can define if it was a buying or a selling point.
#         Ex. if we first find a future price which is greater or equal to our winning percentage let's say 50 % it is a buying point
#         but if it is less than or equal to our losing percentage let's say 20 % it is a selling point.
trainSet = list()
labelSet = list()
current = list()
randList = list()
debugList = list()
def createTrainingData(numberOfSamples, numOfPickableDataPoints):
    random.seed(datetime.now())
    picks = np.random.randint(0,numOfPickableDataPoints, numberOfSamples)
    randList.append(picks)
    upperLimitWeight = 1.2
    lowerLimitWeight = 0.95
    for i in range(numberOfSamples):
        picked = picks[i]
        trainSet.append(appleDataPoints[picked + 1:picked + sizeOfTrainingSet + 1])
        label = 2
        currentPrice = pickableAppleDataPoints[picked]
        current.append(currentPrice)
        for j in range(appleDataPoints[picked + sizeOfTrainingSet + 1:].shape[0]):
            if j != appleDataPoints[picked + sizeOfTrainingSet + 1:].shape[0] - 1:
                if appleDataPoints[picked + sizeOfTrainingSet + 1 + j] >= currentPrice * upperLimitWeight:
                    print(currentPrice)
                    label = 0
                    break
                elif appleDataPoints[picked + sizeOfTrainingSet + 1 + j] <= currentPrice * lowerLimitWeight:
                    print(currentPrice)
                    label = 1
                    break
            else:
                if appleDataPoints[picked + sizeOfTrainingSet + 1 + j] > currentPrice:
                    print('End point!')
                    label = 0
                else:
                    print('End point!')
                    label = 1
        labelSet.append(label)
        
createTrainingData(50, pickableAppleDataPoints.shape[0])
fieldsTrainingData = list(range(sizeOfTrainingSet))
fieldsLabels = list(range(len(labelSet)))
trainDataName = 'trainingData.csv'
labelDataName = 'labelData.csv'

def writeToCsv(fieldNames, listToWrite, name):
    if path.exists(name):
        with open(name, 'a') as f:
            write = csv.writer(f)
            write.writerows(listToWrite)
    else:
        with open(name, 'w') as f:
            write = csv.writer(f)
            write.writerow(fieldNames)
            write.writerows(listToWrite)
            
def writeToCsvOneLine(listToWrite, name):
    if path.exists(name):
        # labelToCsv = pd.read_csv(name)
        # dfLabels = pd.DataFrame(listToWrite)
        # col = range(labelToCsv.shape[0])
        # col2 = raneg(labelToCsv.shape[0], labelToCsv.shape[0] + dfLabels.shape[0])
        # col.append(col2)
        # labelToCsv.append(dfLabels)
        # labelToCsvNp = np.array(labelToCsv)
        # dfLabelsNp = np.array(dfLabels)
        # toWrite = list(np.append(labelToCsvNp, dfLabelsNp))
        with open(name, 'a') as f:
            write = csv.writer(f)
            for elem in listToWrite:
                write.writerow([elem])
    else:
        with open(name, 'w') as f:
            write = csv.writer(f)
            write.writerow([0])
            for elem in listToWrite:
                write.writerow([elem])
            
writeToCsv(fieldsTrainingData, trainSet, trainDataName)
writeToCsvOneLine(labelSet, labelDataName)




