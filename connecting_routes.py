
'''
# network analytics for connecting_routes :


Problem Statement: -

# a datasets consisting of information for the connecting routes. Create network analytics models on datasets and measure degree centrality, degree of closeness centrality, and degree of in-between centrality.
# ●	Create a network using edge list matrix(directed only).
# ●	Columns to be used for dataset
 
# connecting routes=c("flights", " ID", "main Airport”, “main Airport ID", "Destination ","Destination  ID","haults","machinary")


# CRISP-ML(Q) process model describes six phases:
# 
# 1. Business and Data Understanding
# 2. Data Preparation
# 3. Model Building
# 4. Model Evaluation
# 5. Deployment
# 6. Monitoring and Maintenance
'''


'''
1st STEP:
1. Business and Data Understanding :
'''

# Objective(s): Improve Efficiency and Optimization of Connecting Routes in the Airline Industry.
# Constraints : minimize the time for flight delays 
    

'''Success Criteria'''

# Business Success Criteria: satisfying customers

# ML Success Criteria: Build a better connections between flights.       

# Economic Success Criteria: Incresing airlined industries revenue based on additional service offered on optimized routes.

'''
data collection
'''
# dataset of connecting routes is availbale in our lMS website.
# this dataset is included various airlines records.
# rows - 67663 rows, Each row in the dataset represents a specific flight route.
# columns - 09 columns contain essential information about airlined id, source airport, equipments.                


'''
# data description : 
airline: code for identifier the airline.
airline ID: The unique ID for the airline.
source airport: The code for the source airport.
source airport id: The unique ID for the source airport.
destination airport: The code for the destination airport.
destination airport id: The unique ID for the destination airport.
stops: The number of stops on the flight (0 in your example).
equipment: The type of aircraft or equipment used for the flight 

'''




'''
2nd STEP: 
Data preparation (data cleaning)    
'''

import pandas as pd
#connecting_routes = pd.read_csv(r"D:\360DigiTMG\DATA SCIENTIST learning\DATA SCIENCE\STUDY MATERIAL\UNSUPERVISED LEARNING\5.Network Analytics\datasets\flight_hault.csv")
connecting_routes = pd.read_csv(r"D:\360DigiTMG\DATA SCIENTIST learning\DATA SCIENCE\STUDY MATERIAL\UNSUPERVISED LEARNING\5.Network Analytics\datasets\connecting_routes.csv")

# Credentials to connect to sql Database
from sqlalchemy import create_engine
user = 'root'  # user name
pw = 'root'  # password
db = 'routes_db'  # database name
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")

# to_sql() - function to push the dataframe onto a SQL table.
connecting_routes.to_sql('routes_tbl', con = engine, if_exists = 'replace', chunksize = 1000, index = False)

sql = 'select * from routes_tbl;'
df = pd.read_sql_query(sql, engine) 




df.shape
df.dtypes
df.info()
df.describe() 
df.isnull().sum() # here i got some null values are present equipment column.

# to check any duplicated rows are present or not. 
df.duplicated().sum()
# I see not any duplicated rows are present here

# now i check outliers are present or not
df.plot(kind = 'box', subplots = True, sharey = False, figsize = (15, 8)) 
# not any outliers are present here 



'''
3rd STEP: 
Model Building (data mining)    
'''



df = df.iloc[0:50, 1:8] 
df.columns



import networkx as nx 

for_g = nx.Graph()
for_g = nx.from_pandas_edgelist(df, source = 'source airport', 
                                target = 'destination apirport')



# to save our model 
import joblib
joblib.dump(for_g, 'routes')  

a = joblib.load("routes") 



# #  centrality:-
# 
# 
# **Degree centrality** is defined as the number of links incident upon a node (i.e., the number of ties that a node has). ... Indegree is a count of the number of ties directed to the node (head endpoints) and outdegree is the number of ties that the node directs to others (tail endpoints).
# 
# **Eigenvector Centrality** The adjacency matrix allows the connectivity of a node to be expressed in matrix form. So, for non-directed networks, the matrix is symmetric.Eigenvector centrality uses this matrix to compute its largest, most unique eigenvalues.
# 
# **Closeness Centrality** An interpretation of this metric, Centralness.
# 
# **Betweenness centrality** This metric revolves around the idea of counting the number of times a node acts as a bridge.



routes = pd.DataFrame({"closeness":pd.Series(nx.closeness_centrality(for_g)),
                     "Degree": pd.Series(nx.degree_centrality(for_g)),
                     "eigenvector": pd.Series(nx.eigenvector_centrality(for_g)),
                     "betweenness": pd.Series(nx.betweenness_centrality(for_g))}) 





import matplotlib.pyplot as plt


# Visual Representation of the Network 
for_g = nx.Graph()
for_g = nx.from_pandas_edgelist(df, source = 'source airport', target = 'destination apirport')

f = plt.figure()
pos = nx.spring_layout(for_g, k = 0.015)
nx.draw_networkx(for_g, pos, ax=f.add_subplot(111), node_size = 15, node_color = 'red')
plt.show()
f.savefig("routes_graph.png") 




'''
solution :
    
    The solution can identify new routes or flight connections that can increase revenue for the airline. 
By offering more attractive routes and improving connectivity, the airline can attract more passengers and 
generate higher ticket sales.

'''



































