# write2dArray
A simple python script to write and read arbitrary 2d arrays to a file 

# Overview
Pickle in python is useful for saving and loading data as a python list but is a little slow for some uses.  Knowing the data type, such as a list of integers, alternative file writing methods that are faster can be used.  While numpy is normally good for this, it is not always available (i.e., using an API or IronPython as was my case).  This led me to the python modules Struct and Array.  Based on some reading and StackOverflow, it seems Array is the way to go in my case.  The only problem with the default behaviour and the posts I could find is in the lack of a 2D array version, so I made this script for myself, hopefully helping someone else with the same issue. 

## Advantage
- Faster that pickle for Python 2
- Loading is faster than pickle in Python 3
- Files saved are usable between Python 2 and 3, while pickle is not

### Basic Results
These results are very basic and shouldn't be used as a definite comparison. They are based on a single run and just an illustration.  The pickle version is also only an integer.

- Python 2
  - Integer
    - Pickle (Save,Load): 1.76s,3.9s 
    - Array (Save,Load): 0.94s,0.09s
  - Double
    - Pickle (Save,Load): 1.68s,3.5s 
    - Array (Save,Load): 1.18s,0.14s
    
- Python 3
  - Integer
    - Pickle (Save,Load): 0.3s,0.78s 
    - Array (Save,Load): 0.42s,0.11s
  - Double
    - Pickle (Save,Load): 0.28s,0.7s 
    - Array (Save,Load): 0.54s,0.17s
