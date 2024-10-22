# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Log"
"""
  * @File    :   Log.py
  * @Time    :   2023/11/09 15:55:51
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""


from xy_web_settings.Section.Section import *


class Log(Section):
    path: Path = Path("../workspace/logs/")

    info_log: Path = Path("../workspace/logs/info.log")

    error_log: Path = Path("../workspace/logs/error.log")

    warn_log: Path = Path("../workspace/logs/warn.log")

    def _load(self):
        ########## fetch_path ##########

        self.path = self._fetch_path("path", self.path)

        self.info_log = self._fetch_path("info_log", self.info_log)

        self.error_log = self._fetch_path("error_log", self.error_log)

        self.warn_log = self._fetch_path("warn_log", self.warn_log)

        super()._load()
