#Function to clean Type N excel sheets & copy them to SQLite database
def typeN(sheetname):    
    import numpy as np
    import pandas as pd

    file = 'Community Resources Database 2021.xlsx'

    dfo = pd.read_excel(file, sheet_name=sheetname)

    dfo['Category'] = np.NaN #adding a column with null values

    dfnlist = []
    collist = dfo.columns.values.tolist() #list of column names are saved to 'collist'

    dummydf = pd.DataFrame(['dummy'], columns=[collist[0]]) #dummy df with dummy values
   
    dfo = pd.concat([dfo,dummydf],ignore_index=True,axis=0)

    dfnu = dfo.iloc[:,1:] #shows values from column index 1(2nd column) onwards
    nulist = dfnu[dfnu.isnull().all(axis=1)].index.tolist() #list of row numbers for null values

    #data cleaning and manipulation
    for i in range(1,len(nulist)): #range(0,3) or (1,4)
        dfx = dfo.iloc[nulist[i-1]:nulist[i],:]
        label = dfo['Agency Name'].iloc[nulist[i-1]]
        label = str(label)
        #display(label)
        dfx['Category'] = dfx['Category'].fillna(label) #replace nulls with the category values
        #display('dfx')
        #display(dfx)
        dfxlist = dfx.values.tolist() #convert df to list 
        #display(dfxlist)
        dfnlist.extend(dfxlist)

    dfn = pd.DataFrame(dfnlist) #forms dataframe from list
    dfn.columns = collist #copies list of column names to new dataframe

    for i in range(0,len(nulist)-1):
     dfn = dfn.drop(index=nulist[i])

    ##########################################################################
    #SQLite portion
    from sqlalchemy import create_engine

    #Database created
    engine = create_engine('sqlite:///commres.db', echo=False)
    #Converts sheetname to lowercase & replaces 'spaces' with 'underscores'
    tablename = sheetname.lower().replace(" ", "_")
    #Converting dataframe to sql table to be stored in a database
    dfn.to_sql(tablename, engine, if_exists='replace', index=False, index_label=collist)

    engine.dispose()
    
    return None