# Feature Category : sourcing_channel, residence_area_type
import pandas as pd
from sklearn import preprocessing

def categorize(df):
    '''
    This method takes panda.dataframe having single category column as its data as param.
    It then does apply sklearn.preprocessing.LabelEncoder() on the category column
    and then transforms singular category column into multiple columns using sklearn.preprocessing.OneHotEncoder()
    '''
    prefix = df.columns[0]+'_'
    print('prefix :', prefix)
    # Convert string values to numbers in target column
    le = preprocessing.LabelEncoder()
    df1 = df.apply(le.fit_transform)
    new_cols = [prefix+c for c in le.classes_]
    # Split One Column As Many
    enc = preprocessing.OneHotEncoder() # 1. Instantiate
    arr2d = enc.fit_transform(df1).todense() # 2&3. Fit n Transform returns 2d-array as sparse Matrix
    df2  = pd.DataFrame(arr2d, columns=new_cols) # Convert array-Matrix to Pandas' DataFrame
    return df2    