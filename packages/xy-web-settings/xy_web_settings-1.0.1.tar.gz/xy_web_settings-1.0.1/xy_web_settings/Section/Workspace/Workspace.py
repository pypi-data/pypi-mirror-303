# -*- coding: UTF-8 -*-
__author__ = "helios"

''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:31:27
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Workspace/Workspace.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
from pathlib import Path
from xy_web_settings.Section.Section import *


class Workspace(Section):
    path: Path = Path("../workspace/")

    def _load(self):
        self.path = self._fetch_path("path", self.path)

        super()._load()
