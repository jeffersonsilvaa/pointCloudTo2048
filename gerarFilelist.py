# ************************************************************
#        Listar os arquivos em um arquivo Filelist
#         Por: Jefferson S. Almeida - 08/03/2020
#        E-mail: jeffersonsilva@lapisco.ifce.edu.br
# ************************************************************

import numpy as np
import os, fnmatch

path = "/home/jefferson/Documentos/pessoas/"

listOfFiles = os.listdir(path)
pattern = "*.txt"
dir = path + 'filelist'
fi = open(dir, "w")
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        fileName = entry[0:-4]
        print(fileName)
        fi.write("%s \n" % fileName)

fi.close()
print('ok')
