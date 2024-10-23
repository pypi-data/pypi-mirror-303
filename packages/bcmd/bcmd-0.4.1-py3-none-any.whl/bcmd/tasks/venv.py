import importlib.resources
import os
import platform
import re
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
    quiet: bool = typer.Option(False, '--quiet', '-q', help='是否安静模式'),
    isDisabledMirror: bool = typer.Option(False, '--disabled-mirror', '-d', help='是否禁用镜像'),
    isNoLock: bool = typer.Option(False, '--no-lock', help='是否不使用.venv-lock文件来安装（使用在不同系统上增量安装）'),
    isRemake: bool = typer.Option(False, '--remake', help='执行前先删除 venv 目录'),
    isNewProject: bool = typer.Option(False, '--new-project', '-n', help='是否新建项目'),
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
    venvFile = bpath.get(path, '.venv')
    assertFile(venvFile)
    if isRemake:
        bpath.remove(venvPath)
    if not venvPath.exists() and not quiet:
        await binput.confirm('指定目录为非venv目录，是否确认新创建？')
    if not venvPath.exists():
        await bexecute.run(f'python -m venv {venvPath}')
    if not venvFile.exists():
        await bfile.writeText(venvFile, '')
    basePackages, lockPackages = await getPackageList(venvFile)
    if isNoLock:
        installPackages = basePackages + packages
    else:
        installPackages = lockPackages + packages
    installPackages = sorted(list(set(installPackages)))
    if sys.platform.startswith('win'):
        pip = bpath.get(venvPath, 'Scripts/pip.exe')
    else:
        pip = bpath.get(venvPath, 'bin/pip')
    await pipInstall(pip, installPackages, isDisabledMirror)
    with bpath.useTempFile() as tempFile:
        await bexecute.run(f'{pip} freeze > {tempFile}')
        basePackages = list(set(packages + basePackages))
        lockPackages = (await bfile.readText(tempFile)).strip().split('\n')
        await updatePackageList(venvFile, basePackages, lockPackages)

    # 下载 bin 文件
    if binListFile.exists():
        bin.download(
            names=Null,
            file=binListFile,
            output=binPath,
        )
    # 新建项目
    if isNewProject:
        with importlib.resources.path('bcmd.resources', 'project') as sourceProjectPath:
            for p in bpath.listPath(sourceProjectPath):
                bpath.copy(p, path / p.name)
    bcolor.printGreen('OK')


async def pipInstall(pip: Path, packages: list[str], disabled_mirror: bool):
    python = pip.with_stem('python')
    btask.check(python.is_file(), '无法找到指定文件', python)
    btask.check(pip.is_file(), '无法找到指定文件', pip)
    indexUrl = '-i https://pypi.org/simple' if disabled_mirror else ''
    with bpath.useTempFile() as file:
        await bfile.writeText(file, '\n'.join(packages))
        btask.check(
            not await bexecute.run(f'{python} -m pip install --upgrade pip {indexUrl}'),
            '更新 pip 失败',
        )
        btask.check(
            not await bexecute.run(f'{pip} install -r {file} {indexUrl}'),
            '执行失败',
        )


def assertFile(file: Path):
    btask.check(file.is_file() or not file.exists(), '必须是文件', file)


def assertPath(folder: Path):
    btask.check(folder.is_dir() or not folder.exists(), '必须是目录', folder)


async def _getPackageDict(venvFile: Path):
    content = await bfile.readText(venvFile)
    pattern = r'\[\[ (.*?) \]\]\n(.*?)(?=\n\[\[|\Z)'
    matches: list[tuple[str, str]] = re.findall(pattern, content.strip(), re.DOTALL)
    return {match[0]: [line.strip() for line in match[1].strip().split('\n') if line.strip()] for match in matches}


_baseName: Final[str] = 'venv'


def _getLockName():
    systemName = platform.system()
    return f'{_baseName}-{systemName}'


async def getPackageList(venvFile: Path):
    result = await _getPackageDict(venvFile)
    lockName = _getLockName()
    return result.get(_baseName, []), result.get(lockName, [])


async def updatePackageList(venvFile: Path, packages: list[str], lockPackages: list[str]):
    packageDict = await _getPackageDict(venvFile)
    lockName = _getLockName()
    packages.sort(key=lambda x: x.lower())
    lockPackages.sort(key=lambda x: x.lower())
    packageDict[_baseName] = packages
    packageDict[lockName] = lockPackages
    content = '\n'.join([f'\n[[ {key} ]]\n{'\n'.join(value)}' for key, value in packageDict.items()]).strip()
    await bfile.writeText(venvFile, content)


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
