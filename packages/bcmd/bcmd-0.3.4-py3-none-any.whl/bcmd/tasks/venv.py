import importlib.resources
import os
import sys
from pathlib import Path
from typing import Final

import typer
from beni import bcolor, bexecute, bfile, bhttp, binput, bpath, btask
from beni.bfunc import syncCall
from beni.btype import Null

from bcmd.common import password

from . import bin

app: Final = btask.app


@app.command()
@syncCall
async def venv(
    packages: list[str] = typer.Argument(None),
    path: Path = typer.Option(None, '--path', '-p', help='指定路径，默认当前目录'),
    disabled_mirror: bool = typer.Option(False, '--disabled-mirror', '-d', help='是否禁用镜像'),
    new_project: bool = typer.Option(False, '--new-project', '-n', help='是否新建项目'),
    quiet: bool = typer.Option(False, '--quiet', '-q', help='是否安静模式'),
    no_lock: bool = typer.Option(False, '--no-lock', help='是否不使用.venv-lock文件来安装（使用在不同系统上增量安装）'),
):
    'python 虚拟环境配置'
    path = path or Path(os.getcwd())
    binPath = path / 'bin'
    binListFile = bpath.get(path, 'bin.list')
    await _inputQiniuPassword(binListFile, binPath)
    packages = packages or []
    for i in range(len(packages)):
        package = packages[i]
        if package.endswith('==now'):
            ary = package.split('==')
            packages[i] = f'{ary[0]}=={await _getPackageLatestVersion(ary[0])}'
    venvPath = bpath.get(path, 'venv')
    assertPath(venvPath)
    if not venvPath.exists() and not quiet:
        await binput.confirm('指定目录为非venv目录，是否确认新创建？')
    if not venvPath.exists():
        await bexecute.run(f'python -m venv {venvPath}')
    venvLockFile = bpath.get(path, '.venv-lock')
    assertFile(venvLockFile)
    venvListFile = bpath.get(path, '.venv')
    assertFile(venvListFile)
    if not venvListFile.exists():
        await bfile.writeText(venvListFile, '')
    await tidyVenvFile(venvListFile, packages)
    if venvLockFile.exists() and not no_lock:
        await tidyVenvFile(venvLockFile, packages)
        targetFile = venvLockFile
    else:
        targetFile = venvListFile
    if sys.platform.startswith('win'):
        pip = bpath.get(venvPath, 'Scripts/pip.exe')
    else:
        pip = bpath.get(venvPath, 'bin/pip')
    await pipInstall(pip, targetFile, disabled_mirror)
    await bexecute.run(f'{pip} freeze > {venvLockFile}')
    # 下载 bin 文件
    if binListFile.exists():
        bin.download(
            names=Null,
            file=binListFile,
            output=binPath,
        )
    # 新建项目
    if new_project:
        with importlib.resources.path('bcmd.resources', 'project') as sourceProjectPath:
            for p in bpath.listPath(sourceProjectPath):
                bpath.copy(p, path / p.name)
    bcolor.printGreen('OK')


async def pipInstall(pip: Path, file: Path, disabled_mirror: bool):
    python = pip.with_stem('python')
    btask.check(python.is_file(), '无法找到指定文件', python)
    btask.check(pip.is_file(), '无法找到指定文件', pip)
    indexUrl = '-i https://pypi.org/simple' if disabled_mirror else ''
    btask.check(not await bexecute.run(f'{python} -m pip install --upgrade pip {indexUrl}'), '更新 pip 失败')
    btask.check(not await bexecute.run(f'{pip} install -r {file} {indexUrl}'), '执行失败')


async def tidyVenvFile(file: Path, packages: list[str]):
    packageNames = [getPackageName(x) for x in packages]
    ary = (await bfile.readText(file)).strip().replace('\r', '').split('\n')
    ary = list(filter(lambda x: getPackageName(x) not in packageNames, ary))
    ary.extend(packages)
    ary.sort()
    await bfile.writeText(file, '\n'.join(ary).strip())


def getPackageName(value: str):
    sep_ary = ['>', '<', '=']
    for sep in sep_ary:
        if sep in value:
            return value.split(sep)[0]
    return value


def assertFile(file: Path):
    btask.check(file.is_file() or not file.exists(), '必须是文件', file)


def assertPath(folder: Path):
    btask.check(folder.is_dir() or not folder.exists(), '必须是目录', folder)


async def _getPackageLatestVersion(package: str):
    '获取指定包的最新版本'
    data = await bhttp.getJson(
        f'https://pypi.org/pypi/{package}/json'
    )
    return data['info']['version']


async def _inputQiniuPassword(binListFile: Path, binPath: Path) -> None:
    '根据需要输入七牛云密码'
    if binListFile.exists():
        aaSet = set([x.strip() for x in (await bfile.readText(binListFile)).strip().split('\n') if x.strip()])
        bbSet = set([x.name for x in bpath.listFile(binPath)])
        if aaSet != bbSet:
            await password.getQiniu()
