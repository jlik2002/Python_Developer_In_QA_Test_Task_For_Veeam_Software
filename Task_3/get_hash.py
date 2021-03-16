import hashlib
from os import name
import os.path
import sys

def take_hash_file(path_to_file,type_hash='md5',sizeBuffer = 65536):
    if(type_hash=='md5'):
        hash_file = hashlib.md5()
    elif(type_hash=='sha1'):
        hash_file = hashlib.sha1()
    elif(type_hash=='sha256'):
        hash_file = hashlib.sha256()
    else:
        print('NOT FOUND: i dont know this type hash')
        return None
    if(os.path.exists(path_to_file)==False):
        return None
    with open(path_to_file,'rb') as read_file:
        while (True):
            data = read_file.read(sizeBuffer)
            if (not data):
                break
            hash_file.update(data)
    return hash_file.hexdigest()

def get_info_about_file(path_to_file_with_info):
    if(os.path.exists(path_to_file_with_info)==False):
        print('NOT FOUND: i not found file with info')
        return None
    with open(path_to_file_with_info,'r',encoding='utf=8') as file_with_info:
        work_list = []
        for line in file_with_info:
            line=line.replace('\n','')
            if (line.count(' ')==2):
                work_params = line.split(' ')
                work_list.append([work_params[0],work_params[1],work_params[2]])
        return work_list

path_to_info_file = os.path.abspath(sys.argv[1])
dir_check = sys.argv[2]
info_files = get_info_about_file(path_to_info_file)
for item in info_files:
    name_file = item[0]
    hash_type = item[1]
    file_hash = item[2]
    hash_check = take_hash_file(os.path.abspath(dir_check+'/'+name_file),hash_type)
    if (file_hash==hash_check):
        print(name_file+'   OK')
    elif (file_hash!=hash_check and hash_check!=None):
        print(name_file+'   FAIL')
    else:
        print(name_file +'  NOT FOUND')
