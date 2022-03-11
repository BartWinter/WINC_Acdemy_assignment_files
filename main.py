__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from ast import Index
from functools import cache
from importlib.metadata import files
from importlib.resources import path
from operator import index
import os
from pdb import line_prefix
from posixpath import abspath
import shutil

#Vraag 1

def clean_cache():
    dirName = 'cache'
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    elif os.path.exists(dirName):
        shutil.rmtree("./cache")
        os.makedirs(dirName)

clean_cache()
      

#Vraag 2

def cache_zip(zip_file_path: str, cache_dir_path: str):
    clean_cache()
    shutil.unpack_archive(zip_file_path, cache_dir_path)

cache_zip('./data.zip','./cache')
    

#Vraag 3

def cached_files():
    list_caches_files=[]
    dirs = os.listdir('cache')
    for file in dirs:
        abs_path = os.path.abspath('cache')
        join_path = os.path.join(abs_path, file)
        list_caches_files.append(join_path)
    return list_caches_files

cached_files()


#Vraag 4


def find_password(list_caches_files):
    for file in list_caches_files:
        with open(file) as file_opend:
            for line in file_opend: 
                if 'password' in line:
                    line.split()
                    x = line.split()
                    password = (" ".join(x[1:])) 
                    return password
               
print(find_password(cached_files()))             
           

  
   
   
    
    
    
            
                



            
            
                











       
    








   





