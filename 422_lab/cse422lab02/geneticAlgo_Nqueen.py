import numpy as np
import random
import math

def fitness(population, n):


      fitness_list=[] 
  

      
      for i in range( len(population) ):#0-9
          totpair=0 #total attacking pairs
          state=population[i]#1st row, is a list
        
          #calculating horizontal pairs
          hor_pair=0
          poplist=list(population[i])
          for j in poplist:
              #print(j,val)
              unique=poplist.count(j)#finds number of unique values for each value inthe list
              #print("unique",unique)
              if unique==1:
                  hor_pair=hor_pair
              else:
                  comb=math.factorial(unique)/(math.factorial(2)*math.factorial(unique-2))#finds combination
                  hor_pair+=int(comb)              
          totpair+=hor_pair
        
          #there will be no vertical attacking pairs
          #calculating diagonal attacking pairs
          diagpair=0 
          for s in range(len(state)):#0-7
              for t in range(len(state)):#0-7
                  if s!=t:
                      temp1=abs(s-t)
                      temp2=abs(state[s]-state[t])
                      if temp1==temp2:
                          diagpair+=1
         
          #diagpair=int(diagpair/2)
          
          totpair+=int(diagpair)
          fitness_list.append(abs(28-totpair))
    
      return np.array(fitness_list)

def fitness2(child,n):#for the child
      fitness_list=[] 
      totpair=0 #total attacking pairs
      state=child

      #calculating horizontal pairs
      hor_pair=0
      poplist=list(state)
      for j in poplist:
          #print(j,val)
            
          unique=poplist.count(j)#finds number of unique values for each value inthe list
          #print("unique ",unique)
          if unique == 1:        
              hor_pair=hor_pair
        
          else:
              
              comb=math.factorial(unique)/(math.factorial(2)*math.factorial(unique-2))#finds combination
              hor_pair+=int(comb)   
              
      totpair+=hor_pair
      
      #there will be no vertical attacking pairs
      #calculating diagonal attacking pairs
      diagpair=0 
      for s in range(len(state)):#0-7
          for t in range(len(state)):#0-7
              if s!=t:
                  temp1=abs(s-t)
                  temp2=abs(state[s]-state[t])
                  if temp1==temp2:
                      diagpair+=1
      
      diagpair=int(diagpair/2)
        
      totpair+=int(diagpair)
      fitness_list.append(abs(28-totpair))
      return np.array(fitness_list)
    

    

def select(population, fit):
  ''' take input:  population and fit
      fit contains fitness values of each of the individuals 
      in the population  
      
      return:  one individual randomly giving
      more weight to ones which have high fitness score'''
      #a = [0,1,2,3,4]
      #size = 1
      #p = [.31, .29, 0.26, 0.14]
  
  fit_list=list(fit)
  #print("fit_list",fit_list)
  p=[]#p contains probability of being chosen of each individual
  for i in fit_list:           
    temp=(i/sum(fit_list))
    p.append(temp) 
    
  #print(p)    
  #print(sum(p))
 # ans= np.random.choice([0,1,2,3,4,5,6,7,8,9], 1, True, p)
    
  ans=np.random.choice(a=[0,1,2,3,4,5,6,7,8,9], size=1, p=p,replace=True)
  
  return population[ans[0]]

  
def crossover(x, y):
  '''take input: 2 parents - x, y. 
     Generate a random crossover point. 
     Append first half of x with second 
     half of y to create the child
     
     returns: a child chromosome'''
  n=len(x)  
  c=random.randint(1,n)# returns a random number between 1-10
  
  tempx=[]
  tempy=[]
  for i in x:
      tempx.append(i)
      
  for j in y:      
      tempy.append(j)
  
  #print("tempx",tempx)
  #print("tempy",tempy)  
  #print("end of tempxy")
    
  temp1_list=tempx[0:c]
  temp2_list=tempy[c:n]
  
  #print(type(temp1_list))
  
  
  child_chromosome = (temp1_list+temp2_list) #is a list
  #print("yoyooy",child_chromosome)
  return child_chromosome

def mutate(child):
  '''take input: a child
     mutates a random 
     gene into another random gene
     
     returns: mutated child'''
  
  a=len(child)#8
  #print(len(child))
  index=random.randint(0,a-1)#returns a random index between 0 and 7
  value=random.randint(0,a-1)

  child[index]=value

  return child 

def GA(population, n, mutation_threshold = 0.3):
  '''implement the pseudocode here by
     calling the necessary functions- Fitness, 
     Selection, Crossover and Mutation
     
     print: the max fitness value and the 
     chromosome that generated it which is ultimately 
     the solution board'''
     
  nmax=100000
  goal=28
  
  for i in range(nmax):
    fit=fitness(population,n)
    new_population=[]
    for j in range(len(population)):
      x=select(population,fit)
      y=select(population,fit)
      #print(x)
      #print(y)
      
      child=crossover(x,y)
      #print("crossover",child)
      if random.uniform(0,1) < mutation_threshold:
        child=mutate(child)
      #print("child",child)
      #print("asdsddsa",fitness2(child,n)) 
      a=fitness2(child,n)
      if a[0] == 28:
        print("maximum fitness value is ", goal)
        print( child )
        return child

      new_population.append(child)

    population=new_population
  print("no solution found in ", nmax, "iterations, try again")
  return 
        
#running code----------------------------
'''for 8 queen problem, n = 8'''
n = 8

'''start_population denotes how many individuals/chromosomes are there
  in the initial population n = 8'''
start_population = 10 

'''if you want you can set mutation_threshold to a higher value,
   to increase the chances of mutation'''
mutation_threshold = 0.3

'''creating the population with random integers between 0 to 7 inclusive
   for n = 8 queen problem'''
population = np.random.randint(0, n, (start_population, n))

'''calling the GA function'''
GA(population, n, mutation_threshold)  
