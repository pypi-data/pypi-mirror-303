# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Template"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-21 12:20:21
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 12:21:30
 * @FilePath: /xy_web_settings/xy_web_settings/ModuleData.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Template.py
  * @Time    :   2023/04/24 15:51:36
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""

from pathlib import Path
from importlib_resources import files
import xy_web_settings


class ModuleData:
    def __init__(self) -> None:
        self.path: Path = files(xy_web_settings.__name__).joinpath("data")  # type: ignore
        self.template_path = self.path.joinpath("template")

        self.config_path = self.template_path.joinpath("config")

        self.config_full_path = self.config_path.joinpath("full")

        self.config_simple_path = self.config_path.joinpath("simple")

        self.simple_settings_toml_template = self.config_simple_path.joinpath(
            "settings_toml.template"
        )

        self.full_settings_toml_template = self.config_full_path.joinpath(
            "settings_toml.template"
        )
