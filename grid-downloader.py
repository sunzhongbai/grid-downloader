import urllib
import urllib.request
from pathlib import Path
import tarfile
import shutil

for i in range(1, 35):
	url = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}_50kHz.tar'
	#url = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}.tar'
	print('Downlaod ' + url)
	urllib.request.urlretrieve(url)
	
	print('Start unzip')
	#with tarfile.open(f's{str(i)_50kHz.tar}', 'r') as tar:
	with tarfile.open(f's{str(i)}.tar', 'r') as tar:
		print (tar.getmembers())
		#input absolute path
		tar.extractall('/home/szb/datasets/grid_tmp')

	#print('Move to dataset file')
	shutil.copytree(f'./s{str(i)}/', f'/home/szb/datasets/tmp2/s{str(i)}/audio/')
	print(f'Done {str(i)} !')
		
