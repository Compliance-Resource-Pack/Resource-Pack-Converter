import os
import json

path = 'C:\\Users\\julie\\Desktop\\1.14 - 1.14.4'
data = {
	'block':{},
	'colormap':{},
	'effect':{},
	'entity':{},
	'environment':{},
	'font':{},
	'gui':{},
	'item':{},
	'map':{},
	'misc':{},
	'mob_effect':{},
	'models':{},
	'painting':{},
	'particle':{}
}

folder_list = ['block','colormap','effect','entity','environment','font','gui','item','map','misc','mob_effect','models','painting','particle']

with open('PACK_7.json', 'r') as master:
	master_data = json.loads(master.read())

for folder in folder_list:
	for root, directories, files in os.walk(path + '\\' + folder):
		for filename in files:
			relative_path = root.replace(path + '\\' + folder, '').replace('\\','_')

			if filename.endswith('.png'):
				custom = 'texture:' + relative_path + '_' + filename.replace('.png', '')
				
			if filename.endswith('.mcmeta'):
				custom = 'animation:' + relative_path + '_' + filename.replace('.png', '').replace('.mcmeta', '')

			if filename.endswith('.png') or filename.endswith('.mcmeta'):
				custom = custom.replace(':_', ':')

				dirc = (folder+'/'+relative_path).replace('/_','/').replace('_','/')

				try : 
					master_data[folder][custom][0]
				except KeyError:
					new_name = input(f'{custom} file not found, give is new name: ')
					data[folder][custom] = [dirc, filename, new_name]
				else:
					new_name = master_data[folder][custom][0]
					data[folder][custom] = [dirc, filename, new_name]

with open('PACK_4.json', 'w') as outfile:
	json.dump(data, outfile, indent=2, sort_keys=True)