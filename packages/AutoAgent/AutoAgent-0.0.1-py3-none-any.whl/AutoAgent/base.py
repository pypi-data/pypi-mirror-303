# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import json
import requests
from bs4 import BeautifulSoup

## constants
API_NAME_ARXIV = "ArxivPaperAPI"

class BaseAPI(object):
    """docstring for ClassName"""
    def __init__(self, configs):
        self.configs = configs
        
    def api(self, input_dict, model, kwargs):
        """
            Args:
                input_dict: dict, multi-modal input text, image, audio and video
                model: huggingface model of tf or pytoch
                kwargs: key-value args
            Return:
                res_dict: dict, multi-modal text text, image, audio and video
        """
        return res_dict
