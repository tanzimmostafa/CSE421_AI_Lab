import numpy as np
import math
import random


file=open('input.txt','r')

line1=file.readline().strip()
depth=int(line1)*2
line2=file.readline().strip()
branch=int(line2)

vertices=0
for i in range(0,depth+1):
    vertices+=(branch**i)
    
#print("vertices",vertices)    

adj_matrix= np.zeros((vertices, vertices), dtype='int')

limit=0
for j in range(0,depth):
    limit+=(branch**j)    
#print("limit",limit)

temp=0    
for i in range(limit):#0-12
    for j in range(branch):#3times
        temp=temp+1       
        adj_matrix[i][temp]=1

#print (adj_matrix)     


line3=file.readline().strip()
minm=int( (line3.split(" "))[0] )#1
maxm=int( (line3.split(" "))[1] )#20

leaf_values=np.zeros(vertices,dtype=int)
leafnodes=branch**depth#number of leaf nodes,9
for s in range((vertices-leafnodes),vertices):#0-12
    leaf_values[s]=random.randint(minm,maxm)

print("leaf_values", leaf_values)

#leaf_values=[0,0,0,0,3,12,8,2,4,6,14,5,2]

#-------------------------------------------
comp=0
def minimax(position, depth, maximizingPlayer):
    global comp
    if depth == 0:
        return leaf_values[position]
    
    if maximizingPlayer is True:
        maxEval = -math.inf
        for i in range(vertices): #0-12
            if adj_matrix[position][i] == 1:
                eval = minimax(i,depth-1,False)                
                maxEval=max(maxEval,eval)
        
        return maxEval

    else:
        minEval=math.inf
        for j in range(vertices):
            if adj_matrix[position][j] == 1:
                eval=minimax(j,depth-1,True)
                comp+=1
                minEval=min(minEval,eval)
        
        return minEval
    
        
a=minimax(0,2,True)   
#print(comp)     
#---------------------------alpha beta pruning
comparison=0

def minimax(position, depth, alpha, beta, maximizingPlayer):
    global comparison 
    #comparison+=1
    if depth == 0:
        return leaf_values[position]
    
    if maximizingPlayer is True:
        maxEval = -math.inf
        for i in range(vertices): #0-12
            if adj_matrix[position][i] == 1:
                eval = minimax(i,depth-1, alpha,beta, False)
                maxEval=max(maxEval,eval)
                alpha=max(alpha,eval)
                if beta <= alpha:
                    break
                      
        return maxEval

    else:
        minEval=math.inf
        for j in range(vertices):
            if adj_matrix[position][j] == 1:
                eval=minimax(j,depth-1,alpha,beta,True)
                comparison+=1
                minEval=min(minEval,eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        
        return minEval

#print(minimax(0,2,-math.inf,math.inf,True)) 
#print(comparison) 
#--------------------------------

ans=minimax(0,2,-math.inf,math.inf,True)

print("Depth:",depth)
print("Branch:",branch)
print("Terminal States(Leaf Nodes):",branch**depth)
print("Maximum amount:",ans )
print("Comparisons:",comp) #before alpha-beta pruning
print("Comparisons:",comparison) #after alpha beta pruning







