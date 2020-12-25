import os
import os.path
from os import path
import json

def fill(folder,start,PATH):
	data = []
	ID   = 0

	GLOBAL_PATH = PATH + '1.17'   #7
	
	PATH_1_17   = PATH + '1.17'   #7
	PATH_1_16_4 = PATH + '1.16.4' #6
	PATH_1_16_1 = PATH + '1.16.1' #5
	PATH_1_15_2 = PATH + '1.15.2' #5
	PATH_1_14_4 = PATH + '1.14.4' #4
	PATH_1_13_2 = PATH + '1.13.2' #4
	# naming convention update

	for root, directories, files in os.walk(GLOBAL_PATH + '\\' + folder):
		for file in files:
			if file.endswith('.png') or file.endswith('.mcmeta'):
				ID += 1

				if path.isfile(PATH_1_17 + '\\' + folder + '\\' + file):
					FILE_1_17 = file
				else:
					FILE_1_17 = None

				if path.isfile(PATH_1_16_4 + '\\' + folder + '\\' + file):
					FILE_1_16_4 = file
				else:
					FILE_1_16_4 = None

				if path.isfile(PATH_1_16_1 + '\\' + folder + '\\' + file):
					FILE_1_16_1 = file
				else:
					FILE_1_16_1 = None

				if path.isfile(PATH_1_15_2 + '\\' + folder + '\\' + file):
					FILE_1_15_2 = file
				else:
					FILE_1_15_2 = None

				if path.isfile(PATH_1_14_4 + '\\' + folder + '\\' + file):
					FILE_1_14_4 = file
				else:
					FILE_1_14_4 = None

				if path.isfile(PATH_1_13_2 + '\\' + folder + '\\' + file):
					FILE_1_13_2 = file
				else:
					FILE_1_13_2 = None

				subdata = {
					'1_17':file, 
					'1_16_4':FILE_1_16_4, 
					'1_16_1':FILE_1_16_1, 
					'1_15_2':FILE_1_15_2,
					'1_14_4':FILE_1_14_4,
					'1_13_2':FILE_1_13_2
				}
				data.append(subdata)

	with open(folder + '.json', 'w') as outfile:
		json.dump(data, outfile, indent=2, sort_keys=False)

LOCAL_PATH = 'C:\\Users\\julie\\Desktop\\'
fill('block','b',LOCAL_PATH)
fill('item','i',LOCAL_PATH)