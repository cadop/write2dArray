# write2dArray
A simple python script to write and read arbitrary 2d arrays to a file 

# Overview
Pickle in python is useful for saving and loading data as a python list but is a little slow for some uses.  Knowing the data type, such as a list of integers, alternative file writing methods that are faster can be used.  While numpy is normally good for this, it is not always available (i.e., using an API or IronPython as was my case).  This led me to the python modules Struct and Array.  Based on some reading and StackOverflow, it seems Array is the way to go in my case.  The only problem with the default behaviour and the posts I could find is in the lack of a 2D array version, so I made this script for myself, hopefully helping someone else with the same issue. 

## Advantage
- Faster that pickle for Python 2
- In most cases is faster than pickle in Python 3
- Files saved are usable between Python 2 and 3, while pickle is not

## Usage
Run the arrayTest.py file in the src folder.

### Note
For the testing below and the default of the script, the data type returned is a list of arrays.  This is because converting from an array to a list during the load operation takes a non trivial amount of time.  It is left as an array so the user can conver themselves, but in many cases where the data is being used or indexed, the array type is fine to use. 

### Basic Results
These results are very basic and shouldn't be used as a definite comparison just illustration of expectations with the sample data.  The comparison is also assuming the data starts as python lists.  These are converted to arrays during saving.

- Python 2
  - Integer
    - Pickle (Save,Load): 1.8s,3.9s 
    - Array (Save,Load): 1.0s,0.1s
  - Float
    - Pickle (Save,Load): 2.5s,3.7s 
    - Array (Save,Load): 0.8s,0.08s
    
- Python 3
  - Integer
    - Pickle (Save,Load): 0.2s,0.7s 
    - Array (Save,Load): 0.4s,0.1s
  - Float
    - Pickle (Save,Load): 0.5s,0.4s 
    - Array (Save,Load): 0.3s,0.09s
