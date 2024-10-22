# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Backup"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:32:46
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Backup/Backup.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Backup.py
  * @Time    :   2023/11/09 15:56:14
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_web_settings.Section.Section import *


class Backup(Section):
    path: Path = Path("../workspace/backup/")

    def _load(self):
        ########## fetch_path ##########

        self.path = self._fetch_path("path", self.path)

        super()._load()
