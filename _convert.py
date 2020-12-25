import os
import json
from shutil import copyfile



'''
	# BLOCKS #
'''

def block(input_version, output_version,out_pack,in_pack):

	input_path  = 'D:\\GitHub\\Compliance\\Resource-Pack-32x\\Jappa\\' + input_version + '\\assets\\minecraft\\textures\\'
	output_path = 'D:\\GitHub\\Compliance\\Resource-Pack-32x\\Jappa\\' + output_version + '\\assets\\minecraft\\textures\\'

	with open('dict/block.json') as json_file:
		data = json.load(json_file)

	for texture in data:
		if texture[out_pack] != None:
			try:
				copyfile(input_path + 'block\\' + str(texture[in_pack]), output_path + 'block\\' + str(texture[out_pack]))
			except FileNotFoundError:
				pass

'''
	# ITEMS #
'''

def item(input_version, output_version,in_pack,out_pack):

	input_path  = 'D:\\GitHub\\Compliance\\Resource-Pack-32x\\Jappa\\' + input_version + '\\assets\\minecraft\\textures\\'
	output_path = 'D:\\GitHub\\Compliance\\Resource-Pack-32x\\Jappa\\' + output_version + '\\assets\\minecraft\\textures\\'

	with open('dict/item.json') as json_file:
		data = json.load(json_file)

	for texture in data:
		if texture[out_pack] != None:
			try:
				copyfile(input_path + 'item\\' + str(texture[in_pack]), output_path + 'item\\' + str(texture[out_pack]))
			except FileNotFoundError:
				pass

def convert(input_version, output_version, input_pack, output_pack):
	block(input_version, output_version, input_pack, output_pack)
	item(input_version, output_version, input_pack, output_pack)
		
convert('1.17','1.16.2 - 1.16.4','1_17','1_16_4')