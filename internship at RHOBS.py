import pandas as pd
import pymongo
from pymongo import MongoClient
from pandas import DataFrame
import numpy as np

client= MongoClient('mongodb://rhobs:xeiPhie3Ip8IefooLeed0Up6@15.236.51.148:27017/rhobs')
db = client["rhobs"]
test = db.test
liste = list(test.find())
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
col8=[]
col9=[]

for data in liste:
    col1.append(data['_id'])

for data in liste:
    col2.append(list(data.keys())[1])

for data in liste:
    a = list(data.values())[1]
    col3.append(a['city'])
    col4.append(a['job'])
    col5.append(a['iban'])
    col6.append(a['color'])
    col7.append(a['phone'])
    col8.append(a['birthdate'])
    col9.append(a['music'])

d = {'_id':col1,'Name':col2, 'city':col3,'job':col4,'iban':col5,'color':col6,'phone':col7,'birthdate':col8,'music':col9}
df = pd.DataFrame(d)

from datetime import datetime, date

df.birthdate = pd.to_datetime(df.birthdate)
today= datetime.today().strftime('%Y-%m-%d')
today = pd.to_datetime(today)
df['age'] = today - df['birthdate'] 
df['age'] = df['age'] / np.timedelta64(1, 'Y')

df['music string'] = df['music'].astype('str')
df['The number of listeners'] = df['_id']
df['the average age'] = df['age']

# if you show q1 in variable explorer, 
# it will show The number of listeners by music.
q1 = df.groupby('music string')['The number of listeners'].count()
# if you show q2 in variable explorer,
# it will show The average age by music.
q2 = df.groupby('music string')['the average age'].mean()

# But i want to show all the results with "for loop"


print("Question 1 :")
print(" ")

quest1 = df.groupby('music string').count()
question1 = pd.DataFrame(quest1['The number of listeners'])
question1['Music1'] = question1.index
QUEST1 = question1.values.tolist()

for i in range(len(QUEST1)):
    print(QUEST1[i][0] , '    is the number of listeners of the music :   ' , QUEST1[i][1])

print(" ")
print("Question 2 :")
print(" ")

quest2 = df.groupby('music string').mean()
question2 = pd.DataFrame(quest2['the average age'])
question2['avg age'] = question2.index
QUEST2 = question2.values.tolist()

for i in range(len(QUEST2)):
    print(int(QUEST2[i][0]) , '    is the average age of the music :  ' , QUEST2[i][1])

print(" ")
print("Question 3 :")
print(" ")

def pyram_age(city, SliceSize):
    import plotly.graph_objs as go
    import plotly 
    new_df = df[df['city']== city]
    sliced = new_df.groupby('age').count()
    sliced_df = pd.DataFrame(sliced['Name'])
    sliced_df['Age1'] = sliced_df.index
    if (sliced_df['Age1'].max())% SliceSize == 0 :
        a = sliced_df['Age1'].max()/ SliceSize
    else:
        a = sliced_df['Age1'].max()// SliceSize +1
    s = []
    listAge = sliced_df['Age1'].tolist()
    for i in range(a):
        if i != a-1:
            for j in range(SliceSize):
                
                c = i*SliceSize + j
                if c in listAge:
                    s.append([i*SliceSize , (i+1) * SliceSize -1])
                
        else:
            for j in range(sliced_df['Age1'].max()%SliceSize+1):
                c = i*SliceSize + j
                
                if c in listAge:
                    s.append([i*SliceSize , (i+1) * SliceSize -1])

    sliced_df['Age2'] = s
    sliced_df['Age2'] = sliced_df['Age2'].astype('str')
    sliced_2 = sliced_df.groupby('Age2')['Name'].sum()
    sliced_3 = pd.DataFrame(sliced_2)
    sliced_3['Slice Size Age'] = sliced_3.index
    
    y = sliced_3['Slice Size Age']
    x1 = sliced_3['Name']
    
    fig = go.Figure()

    return (fig.add_trace(go.Bar(
            y=y,
            x=x1,
            name='Male',
            orientation='h')))
    
    