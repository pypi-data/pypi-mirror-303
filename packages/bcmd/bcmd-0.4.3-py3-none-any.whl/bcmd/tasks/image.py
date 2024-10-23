import os
from enum import StrEnum
from pathlib import Path
from typing import Final

import typer
from beni import bcolor, bfile, bpath, btask
from beni.bfunc import syncCall
from PIL import Image

app: Final = btask.newSubApp('图片工具集')


class _OutputType(StrEnum):
    '输出类型'
    normal = '0'
    replace_ = '1'
    crc_replace = '2'


@app.command()
@syncCall
async def convert(
    path: Path = typer.Option(None, '--path', '-p', help='指定目录或具体图片文件，默认当前目录'),
    src_format: str = typer.Option('jpg|jpeg|png', '--src-format', '-s', help='如果path是目录，指定源格式，可以指定多个，默认值：jpg|jpeg|png'),
    dst_format: str = typer.Option('webp', '--dst-format', '-d', help='目标格式，只能是单个'),
    rgb: bool = typer.Option(False, '--rgb', help='转换为RGB格式'),
    quality: int = typer.Option(85, '--quality', '-q', help='图片质量，0-100，默认85'),
    output_type: _OutputType = typer.Option(_OutputType.normal, '--output-type', help='输出类型，0：普通输出，1：删除源文件，2：输出文件使用CRC32命名并删除源文件'),
):
    '图片格式转换'
    path = path or Path(os.getcwd())
    fileList: list[Path] = []
    if path.is_file():
        fileList.append(path)
    elif path.is_dir():
        extNameList = [x for x in src_format.strip().split('|')]
        fileList = [x for x in bpath.listFile(path, True) if x.suffix[1:].lower() in extNameList]
    if not fileList:
        return bcolor.printRed(f'未找到图片文件（{path}）')
    for file in fileList:
        with Image.open(file) as img:
            if rgb:
                img = img.convert('RGB')
            with bpath.useTempFile() as tempFile:
                img.save(tempFile, format=dst_format, quality=quality)
                outputFile = file.with_suffix(f'.{dst_format}')
                if output_type == _OutputType.crc_replace:
                    outputFile = outputFile.with_stem(await bfile.crc(tempFile))
                bpath.copy(tempFile, outputFile)
                if output_type in [_OutputType.replace_, _OutputType.crc_replace]:
                    if outputFile != file:
                        bpath.remove(file)
                bcolor.printGreen(f'{file} -> {outputFile}')
