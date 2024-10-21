# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Runner"
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
        try:
            ##################### fetch_path ###############

            self.path = self._fetch_path("path", self.path)  # type: ignore

            ##################### sync_data ################

            self.name = self._sync_data("name", self.name)
            self.verbose_name = self._sync_data("verbose_name", self.verbose_name)
            self.identifier = self._sync_data("identifier", self.identifier)  # type: ignore
            self.description = self._sync_data("description", self.description)
        except:
            pass
        super()._load()
