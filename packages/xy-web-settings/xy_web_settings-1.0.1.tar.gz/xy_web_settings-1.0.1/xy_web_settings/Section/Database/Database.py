# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Database"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:32:42
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Database/Database.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Database.py
  * @Time    :   2023/11/09 15:56:06
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_web_settings.Section.Section import *
from uuid import uuid4


class Database(Section):
    db_host: str | None = "127.0.0.1"

    db_port: int | None = 3306

    db_name: str | None = uuid4().hex[:10]

    db_user: str | None = uuid4().hex[:10]

    db_password: str | None = uuid4().hex[:10]

    db_path: Path = Path("../workspace/database/")

    db_file: Path = Path("../workspace/database/xy_web.sqlite3")

    backup_path: Path = Path("../workspace/backup/database/")

    def _load(self):
        ########## sync_data ##########

        self.db_host = self._sync_data("db_host", self.db_host)

        self.db_port = self._sync_data("db_port", self.db_port)

        self.db_name = self._sync_data("db_name", self.db_name)

        self.db_user = self._sync_data("db_user", self.db_user)

        self.db_password = self._sync_data("db_password", self.db_password)

        ########## fetch_path ##########

        self.db_path = self._fetch_path("db_path", self.db_path)

        self.db_file = self._fetch_path("db_file_path", self.db_file)

        self.backup_path = self._fetch_path("backup_path", self.backup_path)

        super()._load()
