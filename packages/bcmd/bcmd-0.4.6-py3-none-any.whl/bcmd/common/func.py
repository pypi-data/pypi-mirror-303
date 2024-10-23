from pathlib import Path

from beni import btask


def checkFileOrNotExists(file: Path):
    btask.check(file.is_file() or not file.exists(), f'必须是文件 {file}')


def checkPathOrNotExists(folder: Path):
    btask.check(folder.is_dir() or not folder.exists(), f'必须是目录 {folder}')
