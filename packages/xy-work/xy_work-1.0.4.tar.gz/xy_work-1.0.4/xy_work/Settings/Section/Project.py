# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Runner"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-19 20:22:03
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-21 19:55:13
 * @FilePath: /xy_work/xy_work/Settings/Section/Project.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
"""
  * @File    :   Runner.py
  * @Time    :   2023/04/24 15:30:01
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from pathlib import Path
from xy_settings.Section.Section import Section
from uuid import uuid4


class Project(Section):
    name: str | None
    verbose_name: str | None

    identifier: str = uuid4().hex
    description: str | None

    path: Path | None

    def get_name(self) -> str | None:
        return "xy_work_project"

    def _load(self):
        ##################### fetch_path ###############
        self.path = self._fetch_path("path", default=None)  # type: ignore
        ##################### sync_data ################
        self.name = self._sync_data("name", default=None)
        self.verbose_name = self._sync_data("verbose_name", default=None)
        self.identifier = self._sync_data("identifier", uuid4().hex)  # type: ignore
        self.description = self._sync_data("description", default=None)
        super()._load()
