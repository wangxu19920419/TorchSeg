#!/usr/bin/env python3
# encoding: utf-8
# @Time    : 2019/08/21 下午15:41
# @Author  : wangxu
# @Contact : wangxu.ailab@bytedance.com
# @File    : byte_semantic_car.py

import os.path as osp
import numpy as np
import scipy.io as sio
import time
import cv2

import torch

from datasets.BaseDataset import BaseDataset


class BSCar(BaseDataset):
    # def _fetch_data(self, img_path, gt_path, dtype=np.float32):
    #     img = self._open_image(img_path)
    #     gt = self._open_image(gt_path, cv2.IMREAD_GRAYSCALE, dtype=dtype)

    #     return img, gt

    @staticmethod
    def _process_item_names(item):
        item = item.strip()
        img_name = item
        gt_name = item.split('.')[0] + ".png"

        return img_name, gt_name


    @classmethod
    def get_class_names(*args):
        return ['car']
