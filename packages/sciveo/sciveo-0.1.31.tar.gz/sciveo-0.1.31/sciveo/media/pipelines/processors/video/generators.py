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

import os
import cv2
import gc
from PIL import Image

import torch
from transformers import AutoProcessor, AutoModelForCausalLM

from sciveo.tools.common import *
from sciveo.media.pipelines.processors.tpu_base import *
from sciveo.media.pipelines.processors.image.generators import ImageToText
from sciveo.media.pipelines.base import ApiContent


class VideoToText(ImageToText):
  def __init__(self, processor_config, max_progress) -> None:
    super().__init__(processor_config, max_progress)

  def process(self, media):
    debug("process", media['guid'])
    local_path = media["local_path"]

    cap = cv2.VideoCapture(local_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames // 2)
    ret, frame = cap.read()
    cap.release()
    if ret:
      predict = self.predict_image_text(frame)
      return self.set_media(media, predict)
    else:
      return media

  def content_type(self):
    return "video"

  def name(self):
    return "video-to-text"
