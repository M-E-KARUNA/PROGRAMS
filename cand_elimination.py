import pandas as pd
import numpy as np
all_gen_hyp=[]
total_attribute=[]
data1=""
def getG(g,cur_row) :
    _g=[]
    g1=[]
    print(g)
    
    for ind,(value,att) in enumerate(zip(g,total_attribute)):
        
       
        if value!="?":
            continue
        total_values=set(data1[att])
      
        length=len(total_values)
       
        for x in total_values:
            
          
            if length>1 and x!=cur_row[ind]:
                
                g1=g.copy()
                
                g1[ind]=x
                
                _g.append(g1)
                    
    return np.array(_g)       
            
def checkG(_G,cur_data) :
    
    
    for value in cur_data:
        _g=[]
        for g in _G:
            
            differ=(value[:-1]!=g) 
             
            if np.array_equiv(g[differ],np.array(["?"]*list(differ).count(True)) ):
                if value[-1]=="Yes":
                
                
                
                    _g.append(g)
            else:
                if value[-1]=="No":
                    _g.append(g)
            
                
        _G=np.array(_g)
        
        
        
    return _G


def getHyp(path):
    global all_gen_hyp,total_attribute,data1
    data=pd.read_csv(path) 
    total_attribute=np.array(data.columns)[:-1] 
    data1=data
    data=np.array(data)
    print("dataset\n",data)
    S=np.array([" "]*(len(total_attribute))) 
    G=np.array([["?"]*len(S)],dtype="<U8")
    print("initially \nS={}\nG={}".format(S,G)) 
    count=1
    Gtest=0


       
                    
                
        
    









    for i,row in enumerate(data):
        if row[-1]=="Yes":
       
            _G=[]
            for g in G:
          
                valid=row[:-1]!=g 
           
                if np.array_equiv(g[valid],np.array(["?"]*list(valid).count(True))):
                
                    _G.append(g)
               
            G=_G.copy() 
            if count:
                count=0
                S=row[:-1].copy() 
                continue
            differ=(S!=row[:-1]) 
            S[differ]="?"  
             
      
        
        
       
        
        
        else:
            """differ=(S!=row[:-1])
        if not np.array_equiv(S[differ],np.array(["?"]*list(differ).count(True))):
                 pass
                 #do"""
            _G=[]
            for g in G:
                differ=(g!=row[:-1]) 
                if np.array_equiv(g[differ],np.array(["?"]*list(differ).count(True))):
                    Gtest=1
                    _G.extend(getG(g,row[:-1]) ) 
                
                
                else:
                    _G.append(g) 
            _G=np.array(_G)
        
            if Gtest:
                Gtest=0
           
                G=checkG(_G,data[:i+1])
                
            
#print(S)  
#print(np.array(G))
    G=np.array(G)

    print("before comparison\nS={}\nG={}".format(S,G))
    
    for g in G:
        for i in range(len(S)) :
            if g[i]=="?" and S[i]!="?":
                 _g=g.copy() 
                 _g[i]=S[i]
           
                 all_gen_hyp.append(tuple(_g))
    if len(all_gen_hyp)==0:
        all_gen_hyp=G
    else:
        all_gen_hyp=np.array(list(set(all_gen_hyp)) ) 
    print("All Possible Hypothesis",*all_gen_hyp,sep="\n")



if __name__=="__main__":
    getHyp(input("enter the path:")) 
 