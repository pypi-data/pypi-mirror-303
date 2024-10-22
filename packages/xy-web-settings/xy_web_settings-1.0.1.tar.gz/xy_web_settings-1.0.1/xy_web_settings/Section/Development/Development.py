# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Development"
"""
  * @File    :   Development.py
  * @Time    :   2023/11/09 15:55:58
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from xy_web_settings.Section.Section import *


class Development(Section):
    debug: bool = True

    def _load(self):
        ########## sync_data ##########
        self.debug = self._sync_data("debug", self.debug)
        super()._load()
