# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals
import os.path as path
import cv2
import face_recognition
import io
from mmdet.apis import init_detector, inference_detector
from pysot.core.config import cfg
from pysot.models.model_builder import ModelBuilder
from pysot.tracker.tracker_builder import build_tracker

import os
import torch
import numpy as np
from glob import glob

torch.set_num_threads(1)

class faceFinder(object):
	def __init__(self,use_scale=False,scale_xy=0.5):
		self.use_scale=use_scale  # turn this on if high resolution
		self.scale_xy=scale_xy

	def useScale(self,use):
		self.use_scale=use

	def setScale(self,scale):
		self.scale_xy=scale

	def findFaces(self,frame):
		if self.use_scale:
			small_frame = cv2.resize(frame, (0, 0), fx=self.scale_xy,fy=self.scale_xy)
		else:
			small_frame=frame
		rgb_small_frame = small_frame[:, :, ::-1]   # bgr->rgb

		# find face
		face_locations = face_recognition.face_locations(rgb_small_frame)   #speed up

		# restore locations
		for face_location_scale in face_locations:
			if self.use_scale:
				face_location=[int(i/self.scale_xy) for i in face_location_scale]  # restore location
			else:
				face_location=face_location_scale

		return face_locations

def encodeFace(frame,face_location):
	rgb_frame=frame[:,:,::-1]
	return face_recognition.face_encodings(rgb_frame,[face_location])[0]

def encodeFaces(frame,face_locations):
	rgb_frame=frame[:,:,::-1]
	return face_recognition.face_encodings(rgb_frame,face_locations)

# def cropFace(frame,face_location,RGBConvert=False):
# 	(top,right,bottem,left)=face_location
# 	if RGBConvert:
# 		return frame[top:bottom,left:right][:,:,::-1]
# 	else:
# 		return frame[top:bottom,left:right]

def cropFace(frame,face_location):
	(top,right,bottom,left)=face_location
	return frame[top:bottom,left:right]

def recordFace(frame,face_location,savepath):
	(top,right,bottom,left)=face_location
	face=frame[top:bottom,left:right]
	cv2.imwrite(savepath,face)

def faceCompare(knownEncodings, unknownEncoding, tolerance= 0.42):
	return face_recognition.compare_faces(knownEncodings,unknownEncoding,tolerance)

def faceDistance(knownEncodings,unknownEncoding):
	return face_recognition.face_distance((knownEncodings,unknownEncoding))

def drawBox(frame,location,color=(0,0,255)):
	top,right,bottom,left=location
	cv2.rectangle(frame,(left,top),(right,bottom),color)
	return frame

def drawBoxes(frame,locations,color=(0,0,255)):
	for location in locations:
		top,right,bottom,left=location
		cv2.rectangle(frame,(left,top),(right,bottom),color)
	return frame

def img2jpgBlob(img):
	is_success,buffer=cv2.imencode('.jpg',img)
	bio=io.BytesIO(buffer)
	return bio.read()

def jpgBlob2img(blob):
	return cv2.imdecode(np.frombuffer(blob,np.int8),-1)

class personDetecter(object):
	def __init__(self):
		self.mmedeRoot='/media/tsz/Data/Work/Tracking/Library/mmdetection'
		self.config_file='configs/faster_rcnn_r50_fpn_1x.py'
		self.checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'
		self.config_file=path.join(self.mmedeRoot,self.config_file)
		self.checkpoint_file=path.join(self.mmedeRoot,self.checkpoint_file)
		self.model = init_detector(self.config_file,self.checkpoint_file, device='cuda:0')

	def findPeople(self,frame):
		detectRes=inference_detector(self.model, frame)
		return detectRes[0]

class siamTracker(object):
	def __init__(self):
		self.pysot_root = '/media/tsz/Data/Work/Tracking/Library/pysot'
		self.model_name = 'siamrpn_alex_dwxcorr'
		self.model_root = path.join(self.pysot_root, 'experiments', self.model_name)
		self.config= path.join(self.model_root, 'config.yaml')
		self.snapshot = path.join(self.model_root, 'model.pth')

	def loadModel(self):
		cfg.merge_from_file(self.config)
		cfg.CUDA = torch.cuda.is_available()
		self.device = torch.device('cuda' if cfg.CUDA else 'cpu')

		# create model
		self.model = ModelBuilder()

		# load model
		self.model.load_state_dict(torch.load(self.snapshot,map_location=lambda storage, loc: storage.cpu()))
		self.model.eval().to(self.device)

		# build tracker
		self.tracker = build_tracker(self.model)

	def init(self,frame,x,y,width,height):
		init_rect = [x, y, width, height]
		self.tracker.init(frame, init_rect)
		outputs = self.tracker.track(frame)
		bbox = list(map(int, outputs['bbox']))
		return [bbox[1],bbox[0]+bbox[2],bbox[1]+bbox[3],bbox[0]]