from array import array
#import mmap

def save2dList(data,dtype = 'i',filename = 'fileArray'):
    """
    Saves a 2 Dimensional python list with arbitrary lengths
    
    input:
        data: a 2d array (python list of lists) of arbitrary lengths
        dtype: datatype of the items, 'i' for integer, 'f' for float
        filename: name of the file to be saved
        
    returns:
        len_list: an ordered list of lengths for each array in the 2d array
    """
    output_file = open(filename, 'wb')
    len_list = []
    for i in range(len(data)):
        len_list.append(len(data[i]))
        tmpArr = array(dtype,data[i])
        tmpArr.tofile(output_file)
    output_file.close()
    
    return len_list

def save2dArray(data,dtype = 'i',filename = 'fileArray'):
    """
    Saves a 2 Dimensional array with arbitrary lengths
    
    input:
        data: a 2d array of arbitrary lengths
        dtype: datatype of the items, 'i' for integer, 'f' for float
        filename: name of the file to be saved
        
    returns:
        len_list: an ordered list of lengths for each array in the 2d array
    """
    output_file = open(filename, 'wb')
    len_list = []
    for i in range(len(data)):
        len_list.append(len(data[i]))
        data[i].tofile(output_file)
    output_file.close()
    
    return len_list

def load2dArray(len_list,dtype = 'i',filename = 'fileArray'):
    """
    Loads a 2 Dimensional array with arbitrary lengths
    
    input:
        len_list: an ordered list of lengths for each array in the 2d array
        dtype: datatype of the items, 'i' for integer, 'f' for float
        filename: name of the file to be saved
        
    returns:
        newArray: a 2d array 
    """
    input_file = open(filename, 'rb')
    newArray = []
    for i in range(len(len_list)):
        float_array = array(dtype)
        float_array.fromfile(input_file,len_list[i])
        newArray.append(float_array)
        
        #if the array must be a list , this could be used
        #newArray.append(float_array.tolist()) 
            
    return newArray

def mmap2dArray(idx,dtype = 'i',filename = 'fileArray'):
    """
    TODO: 
        use mmap to create a memory view object and load specific arrays
        
    input:
        idx: a 2 element array of the start index and end index of the array to load
        dtype: datatype of the items, 'i' for integer,  'f' for float
        filename: name of the file to be saved
        
    returns:
        newArray: an array contained in a 2d array saved as a file
        
    """
    pass
