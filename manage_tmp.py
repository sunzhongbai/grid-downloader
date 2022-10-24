import urllib
import urllib.request
from pathlib import Path
import tarfile
import shutil
import os

for i in range(34, 35):
	os.chdir('/media/datas-2/steinsun/datasets/grid_bp/video')
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
