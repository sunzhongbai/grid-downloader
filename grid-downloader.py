import urllib
import urllib.request
from pathlib import Path
import tarfile
import shutil

for i in range(1, 35):
	url_auido = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}_50kHz.tar'
	#url = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}.tar'
	print(f'Downlaod audio {str(i)} : ' + url_audio)
	urllib.request.urlretrieve(url_audio)
	
	print('Start unzip audio {str(i)}')
	with tarfile.open(f's{str(i)_50kHz.tar}', 'r') as tar_audio:
		print (tar_audio.getmembers())
		#input absolute path
		tar_audio.extractall('/home/szb/datasets/grid_tmp')

	print('Move to dataset file')
	shutil.copytree(f'./s{str(i)}/', f'/home/szb/datasets/tmp2/s{str(i)}/audio/')
	print(f'Audio {str(i)} Done !')

	url_video1 = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/video/s{str(i)}.mpg6000.part1.tar'
	url_video2 = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/video/s{str(i)}.mpg6000.part2.tar'

	print(f'Downlaod audio {str(i)} : ' + url_audio)
	urllib.request.urlretrieve(url_video1)
	urllib.request.urlretrieve(url_video2)
	print('Start unzip audio {str(i)}')
	with tarfile.open(f's{str(i)}.mpg6000.part1.tar', 'r') as tar_video1:
		print (tar.getmembers())
		#input absolute path
		tar_video1.extractall('/home/szb/datasets/grid_tmp')

	with tarfile.open(f's{str(i)}.mpg6000.part2.tar', 'r') as tar_video2:
		print (tar.getmembers())
		#input absolute path
		tar_video2.extractall('/home/szb/datasets/grid_tmp')

	#print('Move to dataset file')
	shutil.copytree(f'.//s{str(i)}/', f'/home/szb/datasets/tmp2/s{str(i)}/video/')
	print(f'Video {str(i)} Done !')
		
