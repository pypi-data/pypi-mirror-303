# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Resource"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:32:25
 * @FilePath: /xy_web_settings/xy_web_settings/Section/Resource/Resource.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Resource.py
  * @Time    :   2023/11/09 15:55:35
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from pathlib import Path
from xy_web_settings.Section.Section import *


class Resource(Section):
    media_url: str | None = "/media/"

    media_path: Path = Path("../media/")

    static_url: str | None = "/static/"

    static_path: Path = Path("../static/")

    tmp_path: Path = Path("../workspace/tmp/")

    template_path: Path = Path("../template/")

    def _load(self):
        ########## sync_data ##########

        self.media_url = self._sync_data("media_url", self.media_url)

        self.static_url = self._sync_data("static_url", self.static_url)

        ########## fetch_path ##########

        self.media_path = self._fetch_path("media_path", self.media_path)

        self.static_path = self._fetch_path("static_path", self.static_path)

        self.tmp_path = self._fetch_path("tmp_path", self.tmp_path)

        self.template_path = self._fetch_path("template_path", self.template_path)

        super()._load()
