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
import boto3
import cv2
from PIL import Image

import torch
from torchvision import models, transforms

from sciveo.tools.logger import *
from sciveo.tools.common import *
from sciveo.media.pipelines.processors.tpu_base import *
from sciveo.media.pipelines.base import ApiContent


class ImageEmbedding(TPUBaseProcessor):
  def __init__(self, processor_config, max_progress) -> None:
    super().__init__(processor_config, max_progress)

    self.default.update({
      "model_id": 1,
      "output": False
    })

    cache_dir = os.path.join(os.environ['MEDIA_MODELS_BASE_PATH'], "models/")
    self.device = os.environ.get("MEDIA_PROCESSING_BACKEND", "cpu")

    model_name = [
      "softel-resnet18-embedding.pth",
      "softel-resnet34-embedding.pth",
    ][self['model_id']]

    self.model_path = os.path.join(cache_dir, model_name)
    if os.path.isfile(self.model_path):
      debug(model_name, "available", self.model_path)
    else:
      debug("DWN", model_name)
      s3 = boto3.client('s3')
      s3.download_file("sciveo-model", model_name, self.model_path)

    self.api = ApiContent()

    self.preprocessor = transforms.Compose([
      transforms.Resize(256),
      transforms.CenterCrop(224),
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    self.model = torch.load(self.model_path)
    self.model.eval()

  def embed(self, local_path):
    image = Image.open(local_path)
    image_tensor = self.preprocessor(image).unsqueeze(0)
    with torch.no_grad():
      embedding = self.model(image_tensor)
    return embedding.squeeze().numpy()

  def process(self, media):
    debug("process", media['guid'])
    embedding = self.embed(media["local_path"])
    self.api.update(media, {"embedding_resnet_512": list(embedding)})
    return media

  def content_type(self):
    return "image"

  def name(self):
    return "image-embedding"
