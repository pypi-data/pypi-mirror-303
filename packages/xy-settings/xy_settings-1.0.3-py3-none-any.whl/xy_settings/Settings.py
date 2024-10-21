# -*- coding: UTF-8 -*-
__author__ = "helios"
__module__ = "Settings"
__doc__ = "Settings"
"""
  * @File    :   Settings.py
  * @Time    :   2023/04/23 18:08:11
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

import os

from pathlib import Path
from xy_configure.Configure import Configure
from .SettingsDelegate import SettingsDelegate
from xy_configure.Pair.Section import Section


class Settings(metaclass=SettingsDelegate):
    strict: bool = True

    auto_create_path: bool = False

    GLOBAL_CFG_SETTINGS_PATH_KEY = "__xy_global_cfg_path_key"

    settings_dir_path: Path | None = None

    @property
    def settings_cfg_path(self) -> Path | None:
        if self.__configure:
            return self.__configure.config_file_path
        return None

    __configure: Configure | None = None

    @property
    def configure(self) -> Configure | None:
        return self.__configure

    @configure.setter
    def configure(self, configure: Configure | None):
        self.__configure = configure

    def __init__(self) -> None:
        pass

    def __make_section(self, section_type: type) -> Section | None:
        if (
            isinstance(section_type, type)
            and issubclass(section_type, Section)
            and callable(section_type)
        ):
            section = section_type(
                settings_delegate=self, auto_create_path=self.auto_create_path
            )
            if isinstance(section, Section) and isinstance(
                self.configure, Configure
            ):
                try:
                    self.configure.register_section(section)
                    return section
                except:
                    return None
        return None

    def load(
        self,
        settings_cfg_path: Path,
        strict: bool = True,
        auto_create_path: bool = False,
    ):
        if not Configure.check_config_file_path(config_file_path=settings_cfg_path):
            if os.environ.get(self.GLOBAL_CFG_SETTINGS_PATH_KEY) and (
                not settings_cfg_path or not settings_cfg_path.exists()
            ):
                string_path = os.environ.get(self.GLOBAL_CFG_SETTINGS_PATH_KEY)
                if string_path and isinstance(string_path, str):
                    settings_cfg_path = Path(string_path)
            else:
                raise ValueError(f"请传入合法的配置文件路径, 当前仅支持[toml,ini,json,xml]格式的配置文件!")

        if isinstance(settings_cfg_path, str):
            settings_cfg_path = Path(settings_cfg_path)
        if Configure.validate_config_file(settings_cfg_path):
            self.strict = strict
            self.auto_create_path = auto_create_path
            self.reload(settings_cfg_path)
        else:
            raise PermissionError(f"操作配置文件({settings_cfg_path})失败!")

    def reload(self, settings_cfg_path: Path):
        self.settings_dir_path = settings_cfg_path.resolve().parent.resolve()

        if not os.access(self.settings_dir_path, os.R_OK):
            raise PermissionError(f"目录({self.settings_dir_path})没有读取权限!")

        self.configure = Configure()
        self.configure.load(settings_cfg_path)

    def fetch_settings_cfg_file_path(self) -> Path | None:
        if self.configure:
            return self.configure.config_file_path
        else:
            return None

    def load_finish(self):
        pass
