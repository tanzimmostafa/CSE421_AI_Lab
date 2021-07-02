# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 06:23:09 2021

@author: User
"""


import numpy as np
import math
file = open('C:\\Users\\User\\Desktop\\number1.txt','r')

line1=file.readline().strip()#gets the first line
vertex_count=int(line1)#9

#creating adjacency matrix
adj_matrix= np.zeros((vertex_count, vertex_count), dtype='int')
#print(adj_matrix)

line2=file.readline().strip()#gets number of connections
connections=int(line2)#gets 13

for i in range(connections):#loop runs 13times: 0-12
    line=file.readline().strip()
    
    vertices=line.split(' ')
    u=int(vertices[0])
    v=int(vertices[1])
    adj_matrix[u][v]=1
    adj_matrix[v][u]=1
    
#print(adj_matrix)    
    
color=np.empty(vertex_count, dtype= 'object')
color[:]='WHITE'
#parent=np.empty(vertex_count,dtype='object')
#parent[:]=np.NaN
d=np.zeros(vertex_count,dtype='int')
d[:]=math.inf

from queue import Queue

my_queue=Queue(maxsize=vertex_count)

def bfs(s):
    color[s]='GRAY'
    #parent[s]=np.NaN
    d[s]=0
    my_queue.put(s)
    while not my_queue.empty():
        u=my_queue.get()
        for v in range(vertex_count):
            if adj_matrix[u][v] == 1:
                if color[v] == 'WHITE':
                    color[v]='GRAY'
                    d[v]=d[u]+1
                    #parent[v]=u
                    my_queue.put(v)
         
        color[u] = 'BLACK'
    return    

#running 
bfs(0) 
lastline=file.readline().strip()
linapos=int(lastline)#linas's position
#print('position of lina is '+str(linapos))

print(str(d[linapos]) )#Minimum number of moves Nora needs to go to ‘x’ 


#number2------------------------------

file = open('C:\\Users\\User\\Desktop\\number2.txt','r')

line1=file.readline().strip()#gets the first line
vertex_count=int(line1)#9

#creating adjacency matrix
adj_matrix= np.zeros((vertex_count, vertex_count), dtype='int')
#print(adj_matrix)

line2=file.readline().strip()#gets number of connections
connections=int(line2)#gets 12

for i in range(connections):#loop runs 12times: 0-11
    line=file.readline().strip()
    
    vertices=line.split(' ')
    u=int(vertices[0])
    v=int(vertices[1])
    adj_matrix[u][v]=1
    adj_matrix[v][u]=1
    
#print(adj_matrix) 
      
linapos=int( file.readline().strip() )#lina's position
norapos=int( file.readline().strip() )#nora's position
larapos=int( file.readline().strip() )#lara's position
  
color=np.empty(vertex_count, dtype= 'object')
color[:]='WHITE'
d=np.zeros(vertex_count,dtype='int')
d[:]=math.inf

from queue import Queue

my_queue=Queue(maxsize=vertex_count) 

bfs(norapos)
nora_distance=d[linapos]

#for i in d:
   # print(i)

color=np.empty(vertex_count, dtype= 'object')
color[:]='WHITE'
d=np.zeros(vertex_count,dtype='int')
d[:]=math.inf

bfs(larapos)
lara_distance=d[linapos]

#for i in d:
    #print(i)

if nora_distance<lara_distance:
    print('Nora')
elif lara_distance<nora_distance:
    print('Lara')
else:
    print('both')


#number3----------------------------

file = open('C:\\Users\\User\\Desktop\\number3.txt','r')

line1=file.readline().strip()#gets the first line
vertex_count=int(line1)#10

#creating adjacency matrix of reverse graph
adj_matrix= np.zeros((vertex_count, vertex_count), dtype='int')
#print(adj_matrix)

line2=file.readline().strip()#gets number of connections
connections=int(line2)#gets 14

for i in range(connections):
    line=file.readline().strip()
    
    vertices=line.split(' ')
    u=int(vertices[0])
    v=int(vertices[1])
    adj_matrix[v][u]=1   
    
#print(adj_matrix)   


linapos=int( file.readline().strip() )

color=np.empty(vertex_count, dtype= 'object')
color[:]='WHITE'
d=np.zeros(vertex_count,dtype='int')
d[:]=math.inf

from queue import Queue

my_queue=Queue(maxsize=vertex_count) 

bfs(linapos)

total_participants=int( file.readline().strip() )
min_distance=math.inf
p_no=-2#participant number

for j in range(total_participants):#0-4
    pos=int( file.readline().strip() )
    dist=d[pos]#distance of lina from pos
    if dist<min_distance:
        min_distance=dist
        p_no=j+1
        
print(min_distance)



    
    
    



    
    


