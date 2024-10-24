# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Runner"
''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-19 20:22:03
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-23 19:50:16
 * @FilePath: /xy_work/xy_work/Settings/Section/Runner.py
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


class Runner(Section):
    path: Path | None
    # 表示Runner.py中的Runner类
    runner: str | None

    def get_name(self) -> str | None:
        return "xy_work_runner"

    def _load(self):
        self.path = Path("../source/Runner/") # self._fetch_path("path", Path("../source/Runner/"))
        self.runner = self._sync_data("runner", "Runner.Runner")
        super()._load()
