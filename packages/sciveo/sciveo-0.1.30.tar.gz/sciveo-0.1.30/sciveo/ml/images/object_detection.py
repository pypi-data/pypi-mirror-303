#
# Pavlin Georgiev, Softel Labs
#
# This is a proprietary file and may not be copied,
# distributed, or modified without express permission
# from the owner. For licensing inquiries, please
# contact pavlin@softel.bg.
#
# 2024
#

import math
import numpy as np

from sciveo.ml.images.tools import *


"""
Object Detection Bounding Boxes (bbox) of type [x, y, w, h]

If need to use [x1, y1, x2, y2] need to use the inverted convertor bbox_convert_inverted().

IoU between 2 object detections: iou(bbox1, bbox2)

"""

# convert from [x, y, w, h] -> [x1, y1, x2, y2]
def bbox_convert(bbox):
  x1 = bbox[0]
  y1 = bbox[1]
  x2 = x1 + bbox[2]
  y2 = y1 + bbox[3]
  return [x1, y1, x2, y2]

# convert from [x1, y1, x2, y2] -> [x, y, w, h]
def bbox_convert_inverted(bbox):
  x = bbox[0]
  y = bbox[1]
  w = bbox[2] - x
  h = bbox[3] - y
  return [x, y, w, h]

def bbox_norm(bbox, w, h):
  return (bbox[0] / w, bbox[1] / h, bbox[2] / w, bbox[3] / h)

def bbox_denorm(bbox, w, h):
  return (int(bbox[0] * w), int(bbox[1] * h), int(bbox[2] * w), int(bbox[3] * h))

def bbox_center(bbox):
  return (int(bbox[0] + bbox[2] / 2), int(bbox[1] + bbox[3] / 2))

def bbox_area(bbox):
  return bbox[2] * bbox[3]

def iou(bbox1, bbox2):
  x1 = max(bbox1[0], bbox2[0])
  y1 = max(bbox1[1], bbox2[1])
  x2 = min(bbox1[0] + bbox1[2], bbox2[0] + bbox2[2])
  y2 = min(bbox1[1] + bbox1[3], bbox2[1] + bbox2[3])

  if x1 < x2 and y1 < y2:
    a = (x2 - x1) * (y2 - y1)
  else:
    a = 0

  a1 = bbox_area(bbox1)
  a2 = bbox_area(bbox2)
  return a / (a1 + a2 - a)

def bbox_distance(bbox1, bbox2):
  return points_distance(bbox_center(bbox1), bbox_center(bbox2))


"""

Simple Draw object detectios helpers

"""
def image_shape(image):
  return image.shape[1], image.shape[0]

# Draw label bounding boxes of type [x, y, w, h], if [x1, y1, x2, y2] then set convert=False
def draw_label_bboxes(image, bboxes, color, convert=True):
  w, h = image_shape(image)
  for bbox in bboxes:
    if convert:
      bbox = bbox_convert(bbox)
    bbox = bbox_denorm(bbox, w, h)
    cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2, 1)
  return image
