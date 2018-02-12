'''
Copyright (C) BCIT AI/ML Option 2018 Team with Members Following - All Rights Reserved.
- Jake Jonghun Choi     jchoi179@my.bcit.ca
- Justin Carey          justinthomascarey@gmail.com
- Pashan Irani          pashanirani@gmail.com
- Tony Huang	        tonyhuang1996@hotmail.ca
- Chil Yuqing Qiu       yuqingqiu93@gmail.com
Unauthorized copying of this file, via any medium is strictly prohibited.
Written by Jake Jonghun Choi <jchoi179@my.bcit.ca>
'''



# TEMPORARY LOGGER
#TODO
# Input: A list of strings.
def write_to_the_log_file(strings):
    filename = "logs/temp_log.txt"
    file = open(filename, "a+")

    for string in strings:
        file.write(string + '\n')

    file.close()







