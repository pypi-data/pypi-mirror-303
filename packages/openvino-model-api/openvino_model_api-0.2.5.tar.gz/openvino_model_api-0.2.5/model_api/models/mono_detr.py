"""
 Copyright (C) 2024 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from .image_model import ImageModel
from .types import ListValue
from .utils import DetectedKeypoints, Detection


class MonoDETRModel(ImageModel):
    """
    A wrapper for MonoDETR 3d object detection model.
    """

    __model__ = "mono_3d_det"

    def __init__(self, inference_adapter, configuration=dict(), preload=False):
        """
        Initializes a 3d detection model.

        Args:
            inference_adapter (InferenceAdapter): inference adapter containing the underlying model.
            configuration (dict, optional): configuration overrides the model parameters (see parameters() method).
              Defaults to dict().
            preload (bool, optional): forces inference adapter to load the model. Defaults to False.
        """
        super().__init__(inference_adapter, configuration, preload)
        self._check_io_number(1, 2)

    def postprocess(
        self, outputs: dict[str, np.ndarray], meta: dict[str, Any]
    ) -> DetectedKeypoints:
        """
        Applies SCC decoded to the model outputs.

        Args:
            outputs (dict[str, np.ndarray]): raw outputs of the model
            meta (dict[str, Any]): meta information about the input data

        Returns:
            DetectedKeypoints: detected keypoints
        """
        encoded_kps = list(outputs.values())
        batch_keypoints, batch_scores = _decode_simcc(*encoded_kps)
        orig_h, orig_w = meta["original_shape"][:2]
        kp_scale_h = orig_h / self.h
        kp_scale_w = orig_w / self.w
        batch_keypoints = batch_keypoints.squeeze() * np.array([kp_scale_w, kp_scale_h])
        return DetectedKeypoints(batch_keypoints, batch_scores.squeeze())

    @classmethod
    def parameters(cls) -> dict:
        parameters = super().parameters()
        parameters.update(
            {
                "labels": ListValue(
                    description="List of class labels", value_type=str, default_value=[]
                ),
            }
        )
        return parameters
