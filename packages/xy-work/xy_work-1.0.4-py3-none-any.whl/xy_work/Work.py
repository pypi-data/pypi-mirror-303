# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Work"
"""
  * @File    :   Work.py
  * @Time    :   2023/04/24 17:56:19
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""
import os
from pathlib import Path
import importlib
import logging
import shutil
import xy_work
from .Settings.Settings import Settings
from xy_configure.Configure import Configure
from datetime import datetime
import sys
import re
from argparse import ArgumentParser
from .ModuleData import ModuleData
from xy_file.File import File


class Work:
    settings: Settings | None = Settings()
    prog: str = xy_work.__name__
    description: str = (
        f""">>>>>>>>>>>> {xy_work.__name__} - v{xy_work.__version__} <<<<<<<<<<<<<"""
    )
    config_relative_path: Path = Path("config/xy_work.toml")
    parser_key = "xy_work_parser"
    command_choices = [
        "project",
        "runner",
    ]

    def argparser_make(
        self,
        prog: str | None = None,
        description: str | None = None,
        *args,
        **kwargs,
    ) -> ArgumentParser:
        if not prog:
            prog = self.prog
        if not description:
            description = self.description
        parser: ArgumentParser = ArgumentParser(
            prog=prog,
            description=description,
            exit_on_error=False,
        )
        parser.add_argument(
            "-c",
            "--command",
            type=str,
            help="""
                命令:
                -----project => 项目
                -----runner  => 运行启动器
            """,
            choices=self.command_choices,
            required=False,
            nargs="?",
            default="runner",
        )
        return parser

    def main(self, *args, **kwargs):
        command = ""
        parser = self.argparser_make(
            prog=self.prog,
            description=self.description,
            args=args,
            kwargs=kwargs,
        )
        try:
            args, _ = parser.parse_known_args()
            command = args.command
        except:
            pass

        match command:
            case "project":
                self.project(xy_work_parser=parser, args=args, kwargs=kwargs)
            case "runner":
                self.runner(xy_work_parser=parser, args=args, kwargs=kwargs)
            case _:
                print("请输入 -c/--command 命令参数")

    def project(self, *args, **kwargs):
        project_parser = self.argparser_make(
            prog=self.prog,
            description=self.description,
            args=args,
            kwargs=kwargs,
        )
        project_parser.add_argument(
            "-n",
            "--name",
            type=str,
            help="""
                项目名称 仅支持英文:
            """,
            required=True,
        )
        name = project_parser.parse_args().name
        if not name:
            raise ValueError("传入的项目名称参数 -n/--name 仅支持英文")
        zh_pattern = re.compile("[\u4e00-\u9fa5]+")
        match = zh_pattern.search(name)
        if match:
            raise ValueError("传入符合要求的项目名称参数 -n/--name 仅支持英文")

        cwd_path = Path.cwd().resolve()
        if (
            os.access(cwd_path, os.R_OK)
            and os.access(cwd_path, os.W_OK)
            and os.access(cwd_path, os.X_OK)
        ):
            project_path = cwd_path.joinpath(name)
            if project_path.exists():
                raise FileExistsError(
                    f"工程目录 [ {project_path} ] 已存在，请进入到其他符合要求的目录进行项目创建"
                )
            config_path = project_path.joinpath("config")
            settings_toml_path = config_path.joinpath("xy_work.toml")
            if settings_toml_path.exists():
                raise FileExistsError(
                    f"""
                        配置文件 [ {settings_toml_path} ] 已存在。
                        请进入到其他符合需求的目录进行工程创建。
                    """
                )
            module_data = ModuleData()
            
            settings_toml_template_string = (
                module_data.xy_work_toml_template_path.read_text()
            )
            settings_toml_string = settings_toml_template_string.format(
                xy_work_project_name=name,
                xy_work_project_identifier=self.settings.project.identifier,
                xy_work_project_verbose_name=name,
                xy_work_project_description=name,
                xy_work_project_path=project_path,
                xy_work_runner_path=self.settings.runner.path,
                xy_work_runner_runner=self.settings.runner.runner,
            )
            settings_toml_path = File.touch(settings_toml_path)
            if (
                isinstance(settings_toml_path, Path)
                and settings_toml_path.exists()
                and settings_toml_path.is_file()
            ):
                try:
                    settings_toml_path.write_text(settings_toml_string)
                except:
                    shutil.rmtree(project_path)
                    raise IOError(f"写入配置信息到项目配置文件失败! Runner.py => {settings_toml_path}")
                try:
                    self.settings.load(settings_cfg_path=settings_toml_path)
                except:
                    pass
                print(f"self.settings.runner.path => {self.settings.runner.path}")
                print(f"type => {type(self.settings.runner.path)}")
                if self.settings.runner and isinstance(
                    self.settings.runner.path, Path
                ):
                    runner_path = self.settings.runner.path
                    if not runner_path.is_absolute():
                        runner_path = settings_toml_path.parent.joinpath(
                            self.settings.runner.path
                        )
                    try:
                        runner_path.mkdir(parents=True, exist_ok=True)
                        File.touch(runner_path.joinpath("__init__.py"))

                        runner_py_path = runner_path.joinpath("Runner.py")
                        runner_py_path = File.touch(runner_py_path)
                        if (
                            isinstance(runner_py_path, Path)
                            and runner_py_path.exists()
                            and runner_py_path.is_file()
                        ):
                            runner_py_string = (
                                module_data.runner_py_template_path.read_text().format(
                                    xy_work_project_name=name
                                )
                            )
                            try:
                                runner_py_path.write_text(runner_py_string)
                            except:
                                shutil.rmtree(project_path)
                                raise IOError(
                                    f"写入源码模板到Runner.py模块文件失败! Runner.py => {runner_py_path}"
                                )
                        else:
                            shutil.rmtree(project_path)
                            raise FileNotFoundError(
                                f"创建Runner.py模块文件失败! Runner.py => {runner_py_path}"
                            )

                    except:
                        shutil.rmtree(project_path)
                        raise FileNotFoundError(
                            f"创建项目失败! 原因: => Runner目录 [ {runner_path} ] 创建失败"
                        )
                    print(f"创建项目 [ {name} ] 成功!!!")
                    print(f"项目路径 ==>>> {project_path}")
                else:
                    shutil.rmtree(project_path)
                    print(f"创建项目失败, 默认配置出现问题，请联系开发者")

            else:
                raise FileNotFoundError("项目创建失败 => 原因: 创建项目配置文件失败!!!")
        else:
            raise PermissionError("请保证用户对当前目录拥有 [可读, 可写, 可执行] 的权限")

    def runner(
        self,
        settings_cfg_file_path: Path | None = None,
        runner_path: Path | None = None,
        runner_module_class_name: str = "Runner.Runner",
        strict: bool = True,
        auto_create_path: bool = False,
        *args,
        **kwargs,
    ):
        if (
            not Configure.check_config_file_path(
                config_file_path=settings_cfg_file_path
            )
            or not Path(settings_cfg_file_path).exists()
            or os.access(settings_cfg_file_path, os.R_OK)
        ):
            settings_cfg_file_path = Path.cwd().joinpath(self.config_relative_path)
        if (
            not settings_cfg_file_path
            or not settings_cfg_file_path.exists()
            or not os.access(settings_cfg_file_path, os.R_OK)
        ):
            env_settings_cfg_file_path_string = os.environ.get(
                self.settings.GLOBAL_CFG_SETTINGS_PATH_KEY
            )
            if env_settings_cfg_file_path_string and isinstance(
                env_settings_cfg_file_path_string, str
            ):
                env_settings_cfg_file_path = Path(env_settings_cfg_file_path_string)
                if env_settings_cfg_file_path.is_absolute():
                    settings_cfg_file_path = env_settings_cfg_file_path
        self.settings.load(
            settings_cfg_path=settings_cfg_file_path,
            strict=strict,
            auto_create_path=auto_create_path,
        )
        if not settings_cfg_file_path and self.settings.default_cfg_relative_path:
            settings_cfg_file_path = self.settings.default_cfg_relative_path
        self.settings.load(
            settings_cfg_path=settings_cfg_file_path,
            strict=strict,
            auto_create_path=auto_create_path,
        )
        if not runner_path or not runner_path.exists():
            if self.settings.runner and self.settings.runner.path:
                if not self.settings.runner.path.is_absolute():
                    runner_path = settings_cfg_file_path.parent.joinpath(
                        self.settings.runner.path
                    )
                else:
                    runner_path = runner_path = self.settings.runner.path
            else:
                raise ModuleNotFoundError("运行工作目录(runner_path)不存在")
        if not runner_module_class_name or len(runner_module_class_name.split(".")) < 2:
            if (
                self.settings.runner
                and self.settings.runner.runner
                and len(self.settings.runner.runner.split(".")) >= 2
            ):
                runner_module_class_name = self.settings.runner.runner
            else:
                raise ModuleNotFoundError(f"运行模块(runner_module_class_name)不存在或者无法调用")

        if (
            not self.settings.configure
            or not self.settings.configure.config_file_path
            or not self.settings.configure.config_file_path.exists()
        ):
            if settings_cfg_file_path and settings_cfg_file_path.exists():
                self.settings.reload(settings_cfg_file_path)
            else:
                raise FileNotFoundError("配置文件读取失败")
        if (
            runner_path
            and runner_path.exists()
            and runner_path.is_dir()
            and runner_module_class_name
        ):
            runner_module_class_list = runner_module_class_name.split(".")
            if len(runner_module_class_list) > 1:
                runner_module_name = ".".join(runner_module_class_list[:-1])
                runner_class_name = runner_module_class_list[-1]
                sys.path.insert(0, str(runner_path))
                runner_module = importlib.import_module(runner_module_name)
                if runner_module and hasattr(runner_module, runner_class_name):
                    runner_class = getattr(runner_module, runner_class_name)
                    if runner_class and callable(runner_class):
                        runner_class(*args, **kwargs)
                        logging.info(
                            f"""
                            >>>> {xy_work.__name__} - v{xy_work.__version__}
                            >>>>>>>>>>>>>>>>>>> 服务启动成功!!! <<<<<<<<<<<<<<<<<<
                            启动时间: {datetime.now()}
                            """
                        )
                    else:
                        raise ValueError(
                            f"!!! -> 服务启动失败， 无法调用模块({runner_module_name})中的({runner_class_name})类"
                        )
                else:
                    raise ValueError(
                        f"!!! -> 服务启动失败， 模块({runner_module_name})中不存在({runner_class_name})类"
                    )
            else:
                raise ValueError(f"服务启动的模块和类至少需要2个名字: 例如 => Runner.Runner ")
        else:
            raise ValueError(
                f"无法使用服务启动路径({runner_path})和服务启动的模块和类({runner_module_class_name})"
            )
