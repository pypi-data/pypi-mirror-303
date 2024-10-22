# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Nginx"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:32:31
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Nginx/Nginx.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Nginx.py
  * @Time    :   2023/11/09 15:55:43
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_web_settings.Section.Section import *


class Nginx(Section):
    path: Path = Path("../workspace/nginx/")

    logs_path: Path = Path("../workspace/nginx/logs/")

    error_log: Path = Path("../workspace/nginx/logs/error.log")

    access_log: Path = Path("../workspace/nginx/logs/access.log")

    def _load(self):
        ########## fetch_path ##########

        self.path = self._fetch_path("path", self.path)

        self.logs_path = self._fetch_path("logs_path", self.logs_path)

        self.error_log = self._fetch_path("error_log", self.error_log)

        self.access_log = self._fetch_path("access_log", self.access_log)

        super()._load()
