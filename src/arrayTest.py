import time
import arrayIO.arrayIO as arrayIO
try: import cPickle as pickle
except: import pickle
import os 
from array import array

def main():
    #change path to script directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    #move up one level to see the sampleData folder
    os.chdir('..')

    #load the data which is in a format for both python 2 and python 3
    originalData = pickle.load(open('sampleData/arrSampleFile','rb'))
    
    #try to make a results folder
    try: os.mkdir('results')
    except: pass
    
    #change this toggle to test saving float or integer arrays
    testFloat = False
    
    if testFloat == True:
        float_data = []
        for arr in originalData:
            float_data.append( [ float(x) for x in arr ] )
        originalData = float_data
        
        #set the data type
        dtype = 'f'
    else: 
        #set the data type
        dtype = 'i'
        
    start = time.time()
    with open('results/arrPickleFile','wb') as f: pickle.dump(originalData,f)
    print('Pickle Save Time: ',time.time()-start)

    start = time.time()
    originalData = pickle.load(open('results/arrPickleFile','rb'))
    print('Pickle Load Time: ',time.time()-start)
    
    start_t = time.time()        
    arrayData = [ array(dtype,x) for x in originalData ]    
    print("Array Conversion Time: ",time.time()-start_t)
    
    start_t = time.time()
    len_list = arrayIO.save2dArray(arrayData,dtype = dtype,filename = 'results/fileArray')
    print("List of Arrays Save Time: ",time.time()-start_t)
    
    start_t = time.time()
    len_list = arrayIO.save2dList(originalData,dtype = dtype,filename = 'results/fileArray')
    print("List of Lists Save Time: ",time.time()-start_t)
    
    start_t = time.time()
    loadedArray = arrayIO.load2dArray(len_list,dtype = dtype,filename = 'results/fileArray')
    print("Array Load Time: ",time.time()-start_t)
    
    #print a random value in the 2d array to check if the original is same    
    import random as ri
    idx1 = ri.randint(0,len(originalData))
    idx2 = ri.randint(0,len(originalData[idx1]))
    print("data["+str(idx1)+']['+str(idx2)+']', " Original: ",
                originalData[idx1][idx2], " Loaded: ",loadedArray[idx1][idx2])

main()
