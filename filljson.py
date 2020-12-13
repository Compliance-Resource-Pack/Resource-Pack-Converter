import os
import json

path = 'C:\\Users\\julie\\Desktop\\1.17'
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
				data[folder][custom] = [(folder+'/'+relative_path).replace('/_','/').replace('_','/'), filename, None]

with open('PACK_7.json', 'w') as outfile:
	json.dump(data, outfile, indent=2, sort_keys=True)