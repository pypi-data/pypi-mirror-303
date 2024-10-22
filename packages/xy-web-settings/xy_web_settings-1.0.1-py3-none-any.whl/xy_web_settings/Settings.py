# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Settings"
"""
  * @File    :   Settings.py
  * @Time    :   2023/04/25 22:37:37
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""
from pathlib import Path
from xy_work.Settings.Settings import Settings as xySettings
from .Mode import Mode


class Settings(xySettings):
    GLOBAL_CFG_SETTINGS_PATH_KEY = "__xy_web_global_cfg_path_key"
    default_cfg_relative_path: Path = Path("config/xy_web.toml")
    mode: Mode = Mode.FULL

    def load(
        self,
        settings_cfg_path: Path,
        strict: bool = True,
        auto_create_path: bool = False,
        mode: int = 0,
    ):
        self.mode = Mode(mode)
        return super().load(
            settings_cfg_path,
            strict,
            auto_create_path,
        )
