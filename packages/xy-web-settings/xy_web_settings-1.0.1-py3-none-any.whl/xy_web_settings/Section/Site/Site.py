# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Site"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:32:14
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Site/Site.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Site.py
  * @Time    :   2023/11/09 15:55:12
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_web_settings.Section.Section import *
from uuid import uuid4


class Site(Section):
    host: str | None = "0.0.0.0"

    debug_port: int | None = 8400

    release_ports: list | None = [
        8401,
        8402,
    ]

    cookie_secret: str | None = uuid4().hex

    login_url: str | None = "/site/user/login"

    logs_path: Path = Path("../workspace/logs/site/")

    info_log: Path = Path("../workspace/logs/site/info.log")

    error_log: Path = Path("../workspace/logs/site/error.log")

    warn_log: Path = Path("../workspace/logs/site/warn.log")

    backup_path: Path = Path("../workspace/backup/site/")

    def _load(self):
        ########## sync_data ##########

        self.host = self._sync_data("host", self.host)

        self.debug_port = self._sync_data("debug_port", self.debug_port)

        self.cookie_secret = self._sync_data("cookie_secret", self.cookie_secret)

        self.login_url = self._sync_data("login_url", self.login_url)

        ########## fetch_path ##########

        self.backup_path = self._fetch_path("backup_path", self.backup_path)

        self.logs_path = self._fetch_path("logs_path", self.logs_path)

        self.info_log = self._fetch_path("info_log", self.info_log)

        self.error_log = self._fetch_path("error_log", self.error_log)

        self.warn_log = self._fetch_path("warn_log", self.warn_log)

        super()._load()
