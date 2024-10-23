"""
功能: 生成 RetroArch ROMS Playlist.
命令: raplaylistgen.exe -s [STEAM_DIR] -r [ROMS_DIR]
"""

import argparse
import json
import pathlib
import typing
from dataclasses import dataclass

# 游戏清单数据库路径
DIR_SRC = pathlib.Path(__file__).parent
DIR_DATA = DIR_SRC / "assets"

# 默认路径
DEFAULT_STEAM_DIR = r"D:\Games\Steam"
DEFAULT_RA_ROMS_DIR = r"M:\21_游戏_ROMS"

IGNORE_EXTENSIONS = (
    ".txt",
    ".gitignore",
    ".gitattributes",
)


@dataclass
class PlayListItem:
    """游戏列表项"""

    path: str
    label: str
    db_name: str
    core_path: str
    core_name: str
    crc32: str

    def as_dict(self):
        return dict(
            path=self.path,
            label=self.label,
            db_name=self.db_name,
            core_path=self.core_path,
            core_name=self.core_name,
            crc32=self.crc32,
        )


@dataclass
class PlayListConfig:
    """用于生成 playlist 配置项"""

    game_list_db_file: pathlib.Path
    roms_root_dir: pathlib.Path
    ra_exe_file_path: pathlib.Path


@dataclass
class RomFileConfig:
    """rom 文件相关匹配信息"""

    dll_name: str
    core_name: str

    def parse(self):
        return self.dll_name, self.core_name


# rom 文件匹配信息字典
ROM_FILE_CFG: typing.Dict[str, RomFileConfig] = dict(
    FBA=RomFileConfig(dll_name="fbneo_libretro", core_name="FBA"),
    FC=RomFileConfig(dll_name="mesen_libretro", core_name="FC"),
    GBA=RomFileConfig(dll_name="mgba_libretro", core_name="GBA"),
    MAME=RomFileConfig(dll_name="fbneo_libretro", core_name="MAME"),
    MD=RomFileConfig(
        dll_name="genesis_plus_gx_libretro",
        core_name="MD",
    ),
    N64=RomFileConfig(dll_name="mupen64plus_next_libretro", core_name="N64"),
    NAOMI=RomFileConfig(dll_name="flycast_libretro", core_name="NAOMI"),
    NDS=RomFileConfig(dll_name="desmume_libretro", core_name="NDS"),
    NeoGeo=RomFileConfig(dll_name="fbneo_libretro", core_name="NeoGeo"),
    PCE=RomFileConfig(
        dll_name="mednafen_pce_fast_libretro",
        core_name="PCE",
    ),
    PSP=RomFileConfig(dll_name="ppsspp_libretro", core_name="PSP"),
    SFC=RomFileConfig(dll_name="snes9x_libretro", core_name="SFC"),
    SFC_JP=RomFileConfig(dll_name="snes9x_libretro", core_name="SFC_JP"),
)
ROM_TYPES = ROM_FILE_CFG.keys()


class PlayList(object):
    def __init__(self, confing: PlayListConfig):
        self.config: PlayListConfig = confing
        self.game_dict: typing.Dict[str, str] = {}

    def load_game_list(self) -> None:
        if not self.config.game_list_db_file.exists():
            print("[*] Game list文件缺失, 退出...")
            return

        with open(self.config.game_list_db_file.as_posix(), mode="r") as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                if len(line) > 0 and line[0] != "/":
                    key, value, _ = line.split("\t")
                    self.game_dict[key] = value

    @staticmethod
    def get_rom_files_in_dir(
        rom_dir: pathlib.Path,
    ) -> typing.List[pathlib.Path]:
        rome_files = sorted([
            f
            for f in rom_dir.glob("*")
            if f.is_file()
            and f.suffix not in IGNORE_EXTENSIONS
            and f.name not in IGNORE_EXTENSIONS
        ])
        if not rome_files:
            print("[*] 未找到rom文件!")
            return []
        return rome_files

    def get_list_item_name(self, num: int, filename: str):
        if filename not in self.game_dict:
            print(f"[*] [{filename}]未找到对应名称")
            return filename
        else:
            return f"{num:0>{3}}_{self.game_dict[filename]}"

    def parse_roms_in_dir(self, rom_type: str, rom_dir: pathlib.Path) -> None:
        if not self.game_dict:
            print("[*] Game dict 缺失, 退出...")
            return

        if rom_type not in ROM_TYPES:
            print("[*] 不支持的 rom 类型, 跳过")
            return

        if not self.config.ra_exe_file_path.exists():
            print("[*] 未设置 retro arch 路径, 退出...")
            return

        if cfg := ROM_FILE_CFG.get(rom_type):
            dll_name, core_name = cfg.parse()

        cores_dir = self.config.ra_exe_file_path.parent / "cores"
        rome_files: typing.List[pathlib.Path] = self.get_rom_files_in_dir(
            rom_dir
        )
        playlists: typing.List[typing.Dict[str, typing.Any]] = []
        for i, rom_file in enumerate(rome_files):
            playlists.append(
                PlayListItem(
                    path=str(rom_file),
                    label=self.get_list_item_name(i, rom_file.stem),
                    db_name=rom_file.stem,
                    core_path=str(cores_dir / (dll_name + ".dll")),
                    core_name=core_name,
                    crc32="00000000|crc",
                ).as_dict()
            )

        list_file_path = (
            self.config.ra_exe_file_path.parent
            / "playlists"
            / (core_name + ".lpl")
        )
        with open(list_file_path.as_posix(), "w") as f:
            json.dump(
                dict(
                    version="1.5",
                    default_core_path="",
                    default_core_name="",
                    label_display_mode=0,
                    right_thumbnail_mode=4,
                    left_thumbnail_mode=0,
                    thumbnail_match_mode=0,
                    sort_mode=0,
                    items=playlists,
                ),
                f,
                indent=4,
            )

    def parse_roms(self) -> None:
        if not self.config.roms_root_dir.is_dir():
            print("[*] 未设置 roms 路径, 退出...")
            return

        rom_folders = [
            f for f in self.config.roms_root_dir.glob("*") if f.is_dir()
        ]
        for rom_folder in rom_folders:
            self.parse_roms_in_dir(
                rom_folder.name, self.config.roms_root_dir / rom_folder.name
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", dest="steam_dir", default=DEFAULT_STEAM_DIR, help="Steam路径"
    )
    parser.add_argument(
        "-r",
        dest="ra_roms_dir",
        default=DEFAULT_RA_ROMS_DIR,
        help="RetroArch ROMS 路径",
    )

    args = parser.parse_args()
    steam_dir = pathlib.Path(args.steam_dir)
    ra_roms_dir = pathlib.Path(args.ra_roms_dir)

    if not steam_dir.exists() or not ra_roms_dir.exists():
        print("[!] 输入参数不正确")
        parser.print_help()
        return

    config = PlayListConfig(
        game_list_db_file=pathlib.Path(DIR_DATA / "mame_cn.lst"),
        ra_exe_file_path=(
            steam_dir / "steamapps" / "common" / "RetroArch" / "retroarch.exe"
        ),
        roms_root_dir=ra_roms_dir,
    )
    playlist = PlayList(config)
    playlist.load_game_list()
    playlist.parse_roms()


if __name__ == "__main__":
    main()
