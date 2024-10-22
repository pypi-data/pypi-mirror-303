# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Source"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:31:43
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Source/Source.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Source.py
  * @Time    :   2023/11/09 15:54:57
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_file.File import File
from xy_web_settings.Section.Section import *


class Source(Section):
    path: Path = Path("../source/")
    library_path: Path = Path("../source/Library/")

    test_path: Path = Path("../workspace/test/")

    server_path: Path = Path("../source/Server")

    def _load(self):
        ########## fetch_path ##########
        self.path = self._fetch_path("path", self.path)
        self.library_path = self._fetch_path("library_path", self.library_path)
        if self.auto_create_path:
            File.touch(self.library_path.joinpath("__init__.py"))
        self.test_path = self._fetch_path("test_path", self.test_path)
        if self.auto_create_path:
            File.touch(self.test_path.joinpath("__init__.py"))
        self.server_path = self._fetch_path("server_path", self.server_path)
        if self.auto_create_path:
            File.touch(self.server_path.joinpath("__init__.py"))
        super()._load()
