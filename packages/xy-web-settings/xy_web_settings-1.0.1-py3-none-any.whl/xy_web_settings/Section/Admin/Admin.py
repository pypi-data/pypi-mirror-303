# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Admin"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:32:51
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Admin/Admin.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Admin.py
  * @Time    :   2023/11/09 15:56:21
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_web_settings.Section.Section import *


class Admin(Section):
    name: str | None = "Admin"

    host: str | None = "0.0.0.0"

    debug_port: int | None = 8403

    release_port: int | None = 8404

    logs_path: Path = Path("../workspace/logs/admin/")

    admin_log: Path = Path("../workspace/logs/admin/admin.log")

    backup_path: Path = Path("../workspace/backup/admin/")

    def _load(self):
        ########## sync_data ##########

        self.name = self._sync_data("name", self.name)

        self.host = self._sync_data("host", self.host)

        self.debug_port = self._sync_data("debug_port", self.debug_port)

        self.release_port = self._sync_data("release_port", self.release_port)

        ########## fetch_path ##########

        self.backup_path = self._fetch_path("backup_path", self.backup_path)  # type: ignore

        self.logs_path = self._fetch_path("logs_path", self.logs_path)  # type: ignore

        self.admin_log = self._fetch_path("admin_log", self.admin_log)  # type: ignore

        super()._load()
