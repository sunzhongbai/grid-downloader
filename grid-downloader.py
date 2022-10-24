import urllib
import urllib.request
from pathlib import Path
import tarfile
import shutil

for i in range(1, 21):

	url_audio = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}_50kHz.tar'
	#url_audio = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}.tar'
	print(f'Downlaod audio {str(i)} : ' + url_audio)
	urllib.request.urlretrieve(url_audio, filename = f's{str(i)}_50kHz.tar')
	
	print('Start unzip audio {str(i)}')
	with tarfile.open(f's{str(i)}_50kHz.tar', 'r') as tar_audio:
	#with tarfile.open(f's{str(i)}.tar', 'r') as tar_audio:
		print (tar_audio.getmembers())
		#input absolute path

import os

def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar_audio, "/media/datas-2/steinsun/datasets/grid/grid_audio_tmp/")

	print('Move to dataset file')
	shutil.copytree(f'/media/datas-2/steinsun/datasets/grid/grid_audio_tmp/s{str(i)}/', f'/media/datas-2/steinsun/datasets/grid/s{str(i)}/audio/')
	print(f'Audio {str(i)} Done !')

	url_video1 = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/video/s{str(i)}.mpg_6000.part1.tar'
	url_video2 = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/video/s{str(i)}.mpg_6000.part2.tar'

	print(f'Downlaod video {str(i)} : ' + url_video1)
	urllib.request.urlretrieve(url_video1, filename = f's{str(i)}.mpg_6000.part1.tar')
	#http://spandh.dcs.shef.ac.uk/gridcorpus/s1/video/s1.mpg_vcd.zip
	urllib.request.urlretrieve(url_video2, filename = f's{str(i)}.mpg_6000.part2.tar')
	print(f'Start unzip video {str(i)}')
	with tarfile.open(f's{str(i)}.mpg_6000.part1.tar', 'r') as tar_video1:
		print (tar_video1.getmembers())
		#input absolute path
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar_video1, "/media/datas-2/steinsun/datasets/grid/grid_video_tmp/")

	with tarfile.open(f's{str(i)}.mpg_6000.part2.tar', 'r') as tar_video2:
		print (tar_video2.getmembers())
		#input absolute path
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar_video2, "/media/datas-2/steinsun/datasets/grid/grid_video_tmp/")

	#print('Move to dataset file')
	shutil.copytree(f'/media/datas-2/steinsun/datasets/grid/grid_video_tmp/s{str(i)}/video/mpg_6000/', f'/media/datas-2/steinsun/datasets/grid/s{str(i)}/video/')
	print(f'Video {str(i)} Done !')
		

for i in range(22, 35):

	url_audio = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}_50kHz.tar'
	#url_audio = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/audio/s{str(i)}.tar'
	print(f'Downlaod audio {str(i)} : ' + url_audio)
	urllib.request.urlretrieve(url_audio, filename = f's{str(i)}_50kHz.tar')
	
	print('Start unzip audio {str(i)}')
	with tarfile.open(f's{str(i)}_50kHz.tar', 'r') as tar_audio:
	#with tarfile.open(f's{str(i)}.tar', 'r') as tar_audio:
		print (tar_audio.getmembers())
		#input absolute path
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar_audio, "/media/datas-2/steinsun/datasets/grid/grid_audio_tmp/")

	print('Move to dataset file')
	shutil.copytree(f'/media/datas-2/steinsun/datasets/grid/grid_audio_tmp/s{str(i)}/', f'/media/datas-2/steinsun/datasets/grid/s{str(i)}/audio/')
	print(f'Audio {str(i)} Done !')

	url_video1 = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/video/s{str(i)}.mpg_6000.part1.tar'
	url_video2 = f'http://spandh.dcs.shef.ac.uk/gridcorpus/s{str(i)}/video/s{str(i)}.mpg_6000.part2.tar'

	print(f'Downlaod video {str(i)} : ' + url_video1)
	urllib.request.urlretrieve(url_video1, filename = f's{str(i)}.mpg_6000.part1.tar')
	urllib.request.urlretrieve(url_video2, filename = f's{str(i)}.mpg_6000.part2.tar')
	print('Start unzip video {str(i)}')
	with tarfile.open(f's{str(i)}.mpg_6000.part1.tar', 'r') as tar_video1:
		print (tar_video1.getmembers())
		#input absolute path
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar_video1, "/media/datas-2/steinsun/datasets/grid/grid_video_tmp/")

	with tarfile.open(f's{str(i)}.mpg_6000.part2.tar', 'r') as tar_video2:
		print (tar_video2.getmembers())
		#input absolute path
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar_video2, "/media/datas-2/steinsun/datasets/grid/grid_video_tmp/")

	#print('Move to dataset file')
	shutil.copytree(f'/media/datas-2/steinsun/datasets/grid/grid_video_tmp/s{str(i)}/video/mpg_6000/', f'/media/datas-2/steinsun/datasets/grid/s{str(i)}/video/')
	print(f'Video {str(i)} Done !')
