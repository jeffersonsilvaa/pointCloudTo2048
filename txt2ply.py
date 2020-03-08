# ************************************************************
#         Converter nuvem de pontos .txt para .ply
#           Funciona para o formato [x, y, z]
#         Por: Jefferson S. Almeida - 08/03/2020
#        E-mail: jeffersonsilva@lapisco.ifce.edu.br
# ************************************************************

import numpy as np
import os, fnmatch, shutil
from plyfile import PlyData, PlyElement
from os import path

def export_ply(pc, filename):
    sh = pc.shape[0]
    vertex = np.zeros(pc.shape[0], dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])

    for i in range(sh):
        # print(pc[i][0], pc[i][1], pc[i][2])
        vertex[i] = (pc[i][0], pc[i][1], pc[i][2])
    ply_out = PlyData([PlyElement.describe(vertex, 'vertex', comments=['vertices'])], text=True, comments=['created by: Jefferson (jeffersonsilva@lapisco.ifce.edu.br)'])
    ply_out.write(filename)

# fileTXT = "TreeA1_000000"
dir = "/home/jefferson/Documentos/pessoas/"
# fileName = path + fileTXT + ".txt"
past = "ply"
directory = dir + past

if path.exists(directory):
    print('...')
else:
    os.mkdir(directory)
    print("Directory '% s' created" % directory)

files = []

for r, d, f in os.walk(dir):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
    x, y, z = np.loadtxt(f, delimiter=' ', usecols=(0, 1, 2),  unpack=True)
    name = f[0:-4] + '.ply'
    data = np.zeros((3, len(x), 3))
    for j in range(0, len(x)):
        data[0, j] = x[j], y[j], z[j]
    export_ply(data[0], name)

listOfFiles = os.listdir(dir)
pattern = "*.ply"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        orig = dir + entry
        dir2 = directory + '/' + entry
        shutil.move(orig, dir2)

print('ok! Files moved to ply path.')
