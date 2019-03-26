import urllib
import urllib.request
from pathlib import Path
import tarfile
import shutil

for i in range(18, 21):
	print(f'Start unzip video {str(i)}')
	with tarfile.open(f's{str(i)}.mpg_6000.part1.tar', 'r') as tar_video1:
		print (tar_video1.getmembers())
		#input absolute path
		tar_video1.extractall('/media/datas-2/steinsun/datasets/grid/grid_video_tmp/')

	with tarfile.open(f's{str(i)}.mpg_6000.part2.tar', 'r') as tar_video2:
		print (tar_video2.getmembers())
		#input absolute path
		tar_video2.extractall('/media/datas-2/steinsun/datasets/grid/grid_video_tmp/')

	#print('Move to dataset file')
	shutil.copytree(f'/media/datas-2/steinsun/datasets/grid/grid_video_tmp/s{str(i)}/video/mpg_6000/', f'/media/datas-2/steinsun/datasets/grid/s{str(i)}/video/')
	print(f'Video {str(i)} Done !')
