# ************************************************************
#      Condicionar Nuvens de Pontos para 2048 pontos
#         Por: Jefferson S. Almeida - 08/03/2020
#        E-mail: jeffersonsilva@lapisco.ifce.edu.br
# ************************************************************

from plyfile import PlyData, PlyElement
import random
import numpy as np
import os
from os import path

directory = '/home/jefferson/PycharmProjects/PointCloudRandom/data2048'
data_dtype='uint8'
pointnumber = 2048

if path.exists(directory):
	print('...')
else:
	os.mkdir(directory)

def export_ply(pc, filename):
	vertex = np.zeros(pc.shape[0], dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])
	sh = pc.shape[0]
	for i in range(sh):
		# print(pc[i][0], pc[i][1], pc[i][2])
		vertex[i] = (pc[i][0], pc[i][1], pc[i][2])
	ply_out = PlyData([PlyElement.describe(vertex, 'vertex', comments=['vertices'])], text=True, comments=['created by: Jefferson (jeffersonsilva@lapisco.ifce.edu.br)'])
	ply_out.write(filename)

filenames = [line.rstrip() for line in open("filelist", 'r')]

data = np.zeros((len(filenames), pointnumber, 3))

for i in range(0, len(filenames)):
	plydata = PlyData.read(filenames[i] + ".ply")
	# print(i, plydata.elements[0].count)
	size = plydata.elements[0].count

	dataTemp = np.zeros((len(filenames), size, 3))

	if (size >= pointnumber):
		rand = random.sample(range(size), k=pointnumber)
		rand.sort()

		for j in range(0, len(rand)):
			row = rand[j]
			# print(j, row)
			data[i, j-1] = [plydata['vertex']['x'][row], plydata['vertex']['y'][row], plydata['vertex']['z'][row]]

	elif (size < pointnumber):
		difference = pointnumber - size
		dataDiff = np.zeros((len(filenames), difference, 3))
		dataDiff[:] = [plydata['vertex']['x'][0], plydata['vertex']['y'][0], plydata['vertex']['z'][0]]

		for j in range(0, size):
			dataTemp[0, j-1] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
		data = np.concatenate((dataTemp, dataDiff), axis=1)


	name = directory + '/' + filenames[i] + 'size2048' + '.ply'
	export_ply(data[0], name)
	print(i)
