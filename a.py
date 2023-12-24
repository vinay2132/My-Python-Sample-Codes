import pandas as pd
aDictOfSeries = {'one':pd.Series([1,2,3,4,5], index=['z','y', 'x','w','v']),
'two':pd.Series([1,2,5,10], index= ['z', 'y', 'w', 't'])}
df=pd.DataFrame(aDictOfSeries)
df['three']=pd.Series([1,20,30], index=['z', 'v','y'])
print(df)
df['four'] = df['one'] + df['five']
print('\n')
print(df)