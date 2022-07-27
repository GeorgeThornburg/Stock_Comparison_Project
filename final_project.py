import matplotlib.pyplot as plt
import statistics
from matplotlib import interactive
import csv
from tqdm import trange
import yfinance as yf
import pandas as pd

stocks = ['WMB', 'BAC', 'ABC', 'MSFT', 'ACR', 'AKR', 'ZION', 'AXP', 'AMP', 'ZBRA', 'EGHT', 'AGR', 'AMZN',
          'TSLA', 'UNH', 'JNJ', 'NVDA', 'V', 'A', 'HD', 'PFE', 'AA', 'AAC', 'AACG', 'AACI', 'AADI', 'AAIC',
          'AAL', 'AAMC', 'AAME', 'AAN', 'AAOI', 'AAON', 'AAP', 'AAPL', 'AAQC','AAT', 'AATC', 'AAU', 'AAWW',
          'AB', 'ABB', 'ABBV', 'ABCB', 'ABCL', 'ABCM', 'ABEO', 'ABEV', 'ABG', 'ABGI', 'ABIO', 'ABM', 'ABMD',
          'ABNB', 'ABOS', 'ABR', 'ABSI', 'ABST', 'ABT', 'ABTX', 'ABUS', 'ABVC', 'AC', 'ACA', 'ACAB', 'ACAD',
          'ACAH', 'ACAQ', 'ACAX', 'ACB', 'ACBA', 'ACC', 'ACCD', 'ACCO', 'ACDI', 'ACEL', 'ACER', 'ACET', 'ACEV',
          'ACGL', 'ACH', 'ACHC', 'ACHR', 'ACHV', 'ACI', 'ACII', 'ACIU', 'ACIW', 'ACKIT', 'ACLS', 'ACLX', 'ACM',
          'ACMR', 'ACN', 'ACNB', 'ACOR', 'ACQR', 'ACR', 'ACRE', 'ACRO', 'ACRS', 'ACRX', 'ACST', 'ADI', 'ADP',
          'ADPT', 'ADRA', 'ADRT', 'AMD', 'ADSK', 'ADT', 'ADTN', 'ADTH', 'ADTX', 'ADV', 'ADVM', 'ADXN', 'ADXS',
          'AE', 'NTP', 'NTR', 'NTRA', 'NTRB', 'NTRS', 'NTST', 'NTUS', 'NTWK', 'NTZ', 'NU', 'NUBI', 'NUE', 'NURO',
          'NUS', 'NUTX', 'NUVA', 'NUVB', 'NUVL', 'NUWE', 'NUZE', 'NVAC', 'NVAX', 'NVCR', 'NVCT', 'NVEC',
          'NVEE', 'NVEI', 'NVFY', 'NVGS', 'NVIV', 'NVMI', 'NVNO', 'NVO', 'NVOS', 'NVR', 'NVRO', 'NVS', 'NVSA',
          'NVST', 'NVT', 'NVTA', 'NVTS', 'NVVE', 'NVX', 'NWBI', 'NWE', 'NWFL', 'NWG', 'NWL', 'NWLI', 'NWN',
          'NWPX', 'NWS', 'NWsA', 'NX', 'EURUSD=X', 'JPY=X', 'GBPUSD=X', 'AUDUSD=X', 'NZDUSD=X', 'EURJPY=X', 'GBPJPY=X',
          'HKD=X', 'SGD=X', 'INR=X', 'MXN=X', 'PHP=X', 'IDR=X', 'THB=X', 'MYR=X', 'ZAR=X', 'RUB=X', 'NXE', 'NXGL',
          'NXGN', 'NXPI', 'NXPL', 'NXRT', 'NXST', 'NXTC', 'NXTP', 'NYC', 'NYCB', 'NYMT', 'NYMX', 'NYT', 'NYXH',
          'O', 'OB', 'OBCI', 'OBE', 'OBLG', 'OBNK', 'OBSV', 'OBT', 'OC', 'OCAX', 'OCC', 'OCCI', 'OCFC', 'OCFT',
          'OCG', 'OCGN', 'OCN', 'OCSL', 'OCUL', 'OCUP', 'OCX', 'ODC', 'ODFL', 'ODP', 'ODV', 'OEC', 'OEG', 'OEPW',
          'OESX', 'OFC', 'OFED', 'OFG', 'OFIX', 'OFLX', 'OFS'] #newLine



#stocks=['ACOR', 'AMZN']
listForLineGraph = []

def mainFunction(stocks):
    
    #for  i in stocks:
    #    data = yf.download(i, start="2022-01-01", end="2022-07-22")
    #    data.to_csv(i + '.csv')

    for num1 in trange(len(stocks)):
        with open("OFG.csv", "r") as file:            
            csvReader = csv.reader(file)
            count1 = 0
            close1 = []
            date1 = []            
            for col1 in csvReader:
                count1 = count1 + 1
                stockName1 = stocks[num1]                               
                if count1 > 2:                      
                    mc1 = float(col1[4].replace(',',''))                    
                    close1.append(mc1)               
                    date1.append(col1[0])              
                else:
                    continue
                

        for num2 in range(len(stocks)):
            with open("NVDA.csv", "r") as file:            
                csvReader = csv.reader(file)
                count2 = 0
                close2 = []
                date2 = []            
                for col2 in csvReader:
                    count2 = count2 + 1
                    stockName2 = stocks[num2]                               
                    if count2 > 2:                      
                        mc2 = float(col2[4].replace(',',''))                    
                        close2.append(mc2)               
                        date2.append(col2[0])              
                    else:
                        continue
            
            
            pearsonCorrelation(close1, close2, date1, date2, stockName1,stockName2)
    lineGraph(listForLineGraph)  
            
def pearsonCorrelation(close1, close2, date1, date2, stockName1,stockName2):
    
        
    newClose2 = close2[90:128]                                                  #This line and next is the time range
    newDate2 = date2[90:128]                                                     #for stock b to be compared to stock a.
    newClose1 = close1[80 : 135]
    newDate1 = date1[80 : 135]
    
    
    for i in range(0, len(close1), 1):
        
        newClose11 = newClose1[i : i + len(newClose2)]
        newDate11 = newDate1[i : i + len(newClose2)]
        
        
        if len(newClose11) == len(newClose2):            
            
            pearClose1 = [float(x) for x in newClose11]
            pearClose2 = [float(x) for x in newClose2]
            
            xBar = statistics.mean(pearClose1)
            yBar = statistics.mean(pearClose2)
            xStd = statistics.stdev(pearClose1)
            yStd = statistics.stdev(pearClose2)
            num = 0.0
            try:
                for z in range(len(newClose11)):
                    num = num +(pearClose1[z] - xBar) * (pearClose2[z] - yBar)
                corr = num / ((len(pearClose1) - 1) * xStd * yStd)            
            
                if stockName1 != stockName2:                
                    
                    if corr > .96: 
                        #print("\nThe Pearson Correlation is: ", corr)                   #scores that fall within the 'if statement'
                        #print(stockName1 + ": " + newDate11[0] + " - " + newDate11[-1])
                        #print(stockName2 + ": " + newDate2[0] + " - " + newDate2[-1])
                        #print("Over " + str(len(pearClose1)) + " days")
                            
                        listForLineGraph.extend([[stockName1, stockName2, pearClose1, pearClose2, newDate11, newDate2, corr]])                     
                           
                    else:
                        continue
            except:
                pass

            
            
def lineGraph(listForLineGraph):
    
    
    
    df = pd.DataFrame(listForLineGraph)    
    a = df.sort_values(by=[6], ascending = [False])
    data = a.drop_duplicates(subset=[0, 1], keep='first')
    data.to_csv('test.csv', index = False, header = None)
    with open("test.csv", "r") as file:            
        csvReader = csv.reader(file)
        for i in csvReader:
            name1 = i[0]
            x = i[2].strip("[]")
            f = x.split(",")
            num1 = [float(i) for i in f]            
            t = i[4].strip("[]")
            date1 = t.split(",")
            
            name2 = i[1]
            p = i[3].strip("[]")
            s = p.split(",")
            num2 = [float(i) for i in s]            
            u = i[5].strip("[]")
            date2 = u.split(",")
            
            c = i[6]
            
            if date1[-1] != date2[-1]:
                #using subplot function and creating plot one
                # row 2, column 1, count 1
                plt.figure("Pearson Score: " + str(c))
                plt.subplot(2, 1, 1)
                plt.plot(date1, num1)
                plt.title("Positive Correlation: Over " + str(len(num1)) + " days\n\n" + name1 + "\n" + str(date1[0]) + "  - " + str(date1[-1]))
                #plt.gca().invert_xaxis()
                interactive(True)
                                     
                # using subplot function and creating plot two
                # row 2, column 1, count 2                    
                plt.subplot(2, 1, 2)
                plt.plot(date2, num2)
                plt.title(name2 + "\n" + str(date2[0]) + "  - " + str(date2[-1]))
                plt.tight_layout()
                #plt.gca().invert_xaxis()
                interactive(False)
                
                plt.show()
            else:
                continue
            
            
            
            





            
            
                
                
                
                    
                
                
                
    


                    
                
            
            
mainFunction(stocks)
            
            
            
