# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import json
import requests

from ...base import BaseAPI
from ...constants import *

class DialogueVisualizationAPI(BaseAPI):

    """docstring for ClassName"""
    def __init__(self, configs):
        super(DialogueVisualizationAPI, self).__init__(configs)
        self.name = API_NAME_DIALOGUE_CHALLENGE
        self.base_url = "http://www.deepnlp.org/workspace/share/dialogue/collection/%s"
        self.collection_id = "tencent"
        self.default_nickname = "Zhang"

    def api(self, args, kwargs):
        """
            Args:
                args: tuple of args,  (input)
                kwargs: key value dict
            Return:
                res_dict: dict
        """
        res_dict = {}
        try:
            nickname = kwargs["nickname"] if "nickname" in kwargs else self.default_nickname
            dialogue_url = self.base_url % (self.collection_id)
            dialogue_url = dialogue_url + "?name=" + nickname
            res_dict["url"] = dialogue_url
            return res_dict
        except Exception as e:
            print (e)
            return res_dict
