# -*- coding: UTF-8 -*-
__author__ = "helios"

''' 
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-19 18:34:54
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-20 20:58:01
 * @FilePath: /helios/workspace/project/opensource/xy-base/xy_settings/xy_settings/Section/Section.py
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 '''
from pathlib import Path
from xy_file.File import File
from xy_configure.Pair.Section import Section as xySection
from xy_configure.Format.ConfigFormat import ConfigFormat
from xy_settings.SettingsDelegate import SettingsDelegate


class Section(xySection):
    settings_delegate: SettingsDelegate | None = None
    auto_create_path: bool = False

    def __init__(
        self,
        raw_value=None,
        raw_string: str = "",
        raw_base_string: str = "",
        raw_base_string_list: list = [],
        config_format: ConfigFormat = ConfigFormat.AUTO,
        strict: bool = True,
        settings_delegate: SettingsDelegate | None = None,
        auto_create_path: bool = False,
    ):
        self.auto_create_path = auto_create_path
        self.settings_delegate = settings_delegate
        super().__init__(
            raw_value,
            raw_string,
            raw_base_string,
            raw_base_string_list,
            config_format,
            strict,
        )

    def _fetch_path(self, name: str, default: Path) -> Path | None:
        path: Path | None = super()._fetch_path(name, default)  # type: ignore
        path = self._make_path(path=path, auto_create_path=self.auto_create_path)
        if isinstance(path, Path):
            return path
        return None

    def _make_path(self, path: Path, auto_create_path: bool = False) -> Path | None:
        if not isinstance(path, Path):
            return None
        if auto_create_path and isinstance(path, Path):
            path = self.absolute_path(path=path)
            if path.suffix:
                path = File.touch(path)  # type: ignore
            else:
                path.mkdir(parents=True, exist_ok=True)
        return path

    def absolute_path(self, path: Path) -> Path | None:
        if not path.is_absolute():
            settings_cfg_path = None
            if self.settings_delegate and hasattr(
                self.settings_delegate, "fetch_settings_cfg_file_path"
            ):
                settings_cfg_path: Path | None = (
                    self.settings_delegate.fetch_settings_cfg_file_path()
                )
            if isinstance(settings_cfg_path, Path) and settings_cfg_path.exists():
                path = settings_cfg_path.parent.resolve().joinpath(path)
        if isinstance(path, Path):
            return path.resolve()
        return path

    def _load(self):
        super()._load()
        if self.settings_delegate and hasattr(self.settings_delegate, "load_finish"):
            self.settings_delegate.load_finish()
