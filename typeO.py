# Python imports
import pandas as pd

# Framework imports
from sqlalchemy import create_engine


def type_o(sheetname):

    file = 'Community Resources Database 2021.xlsx'

    dfo = pd.read_excel(file, sheet_name=sheetname)

    dfnlist = []
    collist = dfo.columns.values.tolist()  # list of column names are saved to 'collist'

    dummydf = pd.DataFrame(['dummy'], columns=[collist[0]])  # dummy df with dummy values
    
    dfo = pd.concat([dfo, dummydf], ignore_index=True, axis=0)
    
    dfnn = dfo['Category'].dropna()
    nnlist = dfnn.index.tolist()  # list of row numbers for non null values
   
    # Data cleaning and manipulation
    for i in range(0, len(nnlist)-1):
        dfx = dfo.iloc[nnlist[i]:nnlist[i+1], :]
        label = dfo['Category'].iloc[nnlist[i]]
        label = str(label)
        # replace nulls with the category values
        dfx['Category'] = dfx['Category'].fillna(label)
        # display(dfx)
        dfxlist = dfx.values.tolist()  # convert df to list
        # display(dfxlist)
        dfnlist.extend(dfxlist)

    dfn = pd.DataFrame(dfnlist)  # forms dataframe from list
    dfn.columns = collist  # copies list of column names to new dataframe

    for i in range(0, len(nnlist)-1):
        dfn = dfn.drop(index=nnlist[i])

    # Database created
    engine = create_engine('sqlite:///commres.db', echo=False)
    # Converts sheetname to lowercase & replaces 'spaces' with 'underscores'
    tablename = sheetname.lower().replace(" ", "_")
    # Converting dataframe to sql table to be stored in a database
    dfn.to_sql(tablename, engine, if_exists='replace', index=False)

    engine.dispose()
    
    return
