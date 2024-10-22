# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Server"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:32:19
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Server/Server.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Server.py
  * @Time    :   2023/11/09 15:55:28
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_web_settings.Section.Section import *


class Server(Section):
    path: Path = Path("../workspace/server/")

    config_path: Path = Path("../workspace/server/config/")

    site_path: Path = Path("../workspace/server/site/")

    admin_path: Path = Path("../workspace/server/admin/")

    logs_path: Path = Path("../workspace/logs/server/")

    info_log: Path = Path("../workspace/logs/server/info.log")

    error_log: Path = Path("../workspace/logs/server/error.log")

    warn_log: Path = Path("../workspace/logs/server/warn.log")

    def _load(self):
        ########## fetch_path ##########

        self.path = self._fetch_path("path", self.path)

        self.config_path = self._fetch_path("config_path", self.config_path)

        self.site_path = self._fetch_path("site_path", self.site_path)

        self.admin_path = self._fetch_path("admin_path", self.admin_path)

        self.logs_path = self._fetch_path("logs_path", self.logs_path)

        self.info_log = self._fetch_path("info_log", self.info_log)

        self.error_log = self._fetch_path("error_log", self.error_log)

        self.warn_log = self._fetch_path("warn_log", self.warn_log)

        super()._load()
