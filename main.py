import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd
import csv
df=pd.read_csv("math1.csv")
data=df["Math_score"].tolist()

#fig=ff.create_distplot([data],["Math Score"],show_hist=False)
#fig.show()

def random_set(counter):
    dataset=[]
    for i in range(0,counter):
        rand_index=random.randint(0,len(data)-1)
        value=data[rand_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

Entire_mean=statistics.mean(data)
   
print("mean of entire distribution is ",Entire_mean)
std=statistics.stdev(data)
print("Std dev of entire distribution is ",std)


mean_list=[]
for i in range(0,1000):
    set_means=random_set(100)
    mean_list.append(set_means)

std_dev=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print("mean of sampling distribution is ",mean)

first_std_start,first_std_end=mean-std_dev,mean+std_dev
second_std_start,second_std_end=mean-(2*std_dev),mean+(2*std_dev)
third_std_start,third_std_end=mean-(2*std_dev),mean+(2*std_dev)

'''fig=ff.create_distplot([mean_list],["Student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_start,first_std_start],y=[0,0.17],mode="lines",name="Std Dev 1 Start"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="Std Dev 1 End"))

fig.add_trace(go.Scatter(x=[second_std_start,second_std_start],y=[0,0.17],mode="lines",name="Std Dev 2 Start"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="Std Dev 2 End"))

fig.add_trace(go.Scatter(x=[third_std_start,third_std_start],y=[0,0.17],mode="lines",name="Std Dev 3 Start"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="Std Dev 3 End"))
fig.show()
'''


print("std 1 ",first_std_start,first_std_end)
print("std 2",second_std_start,second_std_end)
print("std 3",third_std_start,third_std_end)

dfe=pd.read_csv("math1.csv")
datae=df["Math_score"].to_list()
meane=statistics.mean(datae)
print("mean of sample 1 is",meane)
stdev=statistics.stdev(datae)
print("sd of sample 1 is",stdev)
fig=ff.create_distplot([mean_list],["Student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[meane,meane],y=[0,0.17],mode="lines",name="Mean Sample 1"))
fig.add_trace(go.Scatter(x=[stdev,stdev],y=[0,0.17],mode="lines",name="SD"))

fig.show()

dff=pd.read_csv("math2.csv")
dataf=df["Math_score"].to_list()
meanf=statistics.mean(dataf)
print("mean of sample 2 is",meanf)
stdevf=statistics.stdev(dataf)
print("sd of sample 2 is",stdev)
fig=ff.create_distplot([mean_list],["Std marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[meanf,meanf],y=[0,0.17],mode="lines",name="Mean Sample 2"))
fig.add_trace(go.Scatter(x=[stdevf,stdevf],y=[0,0.17],mode="lines",name="SD"))

fig.show()

dfe=pd.read_csv("math3.csv")
datae=df["Math_score"].to_list()
meane=statistics.mean(datae)
print("mean of sample 3 is",meane)
stdev=statistics.stdev(datae)
print("sd of sample 3 is",stdev)
fig=ff.create_distplot([mean_list],["Student "],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[meane,meane],y=[0,0.17],mode="lines",name="Mean Sample 3"))
fig.add_trace(go.Scatter(x=[stdev,stdev],y=[0,0.17],mode="lines",name="SD"))

fig.show()