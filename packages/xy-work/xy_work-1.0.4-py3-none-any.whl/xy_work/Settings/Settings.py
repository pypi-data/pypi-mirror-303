# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Settings"
"""
  * @File    :   Settings.py
  * @Time    :   2023/04/24 15:35:13
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""
from pathlib import Path
from xy_settings.Settings import Settings as xy_s
from .Section.Runner import Runner
from .Section.Project import Project


class Settings(xy_s):
    project: Project | None = Project()
    runner: Runner | None = Runner()
    GLOBAL_CFG_SETTINGS_PATH_KEY = "__xy_work_cfg_path_key"
    default_cfg_relative_path: Path = Path("config/xy_work.toml")

    def reload(self, settings_cfg_path: Path):
        super().reload(settings_cfg_path)
        self.project = self.__make_section(Project)
        self.runner = self.__make_section(Runner)
