import os
import re
from pathlib import Path
from typing import Final

import typer
from beni import bcolor, bfile, bpath, btask
from beni.bfunc import syncCall

from ..common import password
from .venv import getPackageList

app: Final = btask.newSubApp('lib 工具')


@app.command()
@syncCall
async def tidy_dependencies(
    workspace_path: Path = typer.Argument(None, help='workspace 路径'),
    with_version: bool = typer.Option(False, '--with-version', help='是否带版本号')
):
    '整理 pyproject.toml 里面的 dependencies'
    if not workspace_path:
        workspace_path = Path.cwd()
    pyprojectTomlFile = workspace_path / 'pyproject.toml'
    btask.check(pyprojectTomlFile.is_file(), 'pyproject.toml 不存在', pyprojectTomlFile)
    venvFile = bpath.get(workspace_path, f'.venv')
    btask.check(venvFile.is_file(), '.venv 不存在', venvFile)
    basePackages, lockPackages = await getPackageList(venvFile)
    libAry = lockPackages if with_version else basePackages
    oldContent = await bfile.readText(pyprojectTomlFile)
    ignoreLibAry = _getIgnoreLibAry(oldContent)
    ignoreLibAry = sorted(list(set(ignoreLibAry) & set(libAry)))
    libAry = sorted(list(set(libAry) - set(ignoreLibAry)))
    replaceContent = '\n'.join([f"  '{x}'," for x in libAry]) + '\n' + '\n'.join([f"  # '{x}'," for x in ignoreLibAry])
    newContent = re.sub(r'dependencies = \[(.*?)\]', f"dependencies = [\n{replaceContent}\n]", oldContent, 0, re.DOTALL)
    if oldContent != newContent:
        await bfile.writeText(pyprojectTomlFile, newContent)
        bcolor.printYellow(pyprojectTomlFile)
        bcolor.printMagenta(newContent)
        return True
    else:
        bcolor.printGreen('无需修改依赖')
        return False


@app.command()
@syncCall
async def update_version(
    workspace_path: Path = typer.Argument(None, help='workspace 路径'),
    disabled_commit: bool = typer.Option(False, '--disabled-commit', '-d', help='是否提交git'),
):
    '修改 pyproject.toml 版本号'
    if not workspace_path:
        workspace_path = Path.cwd()
    file = workspace_path / 'pyproject.toml'
    btask.check(file.is_file(), '文件不存在', file)
    data = await bfile.readToml(file)
    version = data['project']['version']
    versionList = [int(x) for x in version.split('.')]
    versionList[-1] += 1
    newVersion = '.'.join([str(x) for x in versionList])
    content = await bfile.readText(file)
    if f"version = '{version}'" in content:
        content = content.replace(f"version = '{version}'", f"version = '{newVersion}'")
    elif f'version = "{version}"' in content:
        content = content.replace(f'version = "{version}"', f'version = "{newVersion}"')
    else:
        raise Exception('版本号修改失败，先检查文件中定义的版本号格式是否正常')
    await bfile.writeText(file, content)
    bcolor.printCyan(newVersion)
    if not disabled_commit:
        msg = f'更新版本号 {newVersion}'
        os.system(
            rf'TortoiseGitProc.exe /command:commit /path:{file} /logmsg:"{msg}"'
        )
    bcolor.printGreen('OK')


@app.command()
@syncCall
async def build(
    workspace_path: Path = typer.Argument(None, help='workspace 路径'),
    keep_build_files: bool = typer.Option(False, '--keep-build-files', '-k', help='是否保留构建文件'),
):
    '发布项目'

    # 获取用户名和密码
    u, p = await password.getPypi()

    if not workspace_path:
        workspace_path = Path.cwd()
    workspace_path = workspace_path.resolve()

    def removeUnusedPath():
        bpath.remove(workspace_path / 'dist')
        paths = bpath.listDir(workspace_path)
        for x in paths:
            if x.name.endswith('.egg-info'):
                bpath.remove(x)

    try:
        with bpath.changePath(workspace_path):
            removeUnusedPath()
            scriptPath = (workspace_path / './venv/Scripts').resolve()
            os.system(f'{scriptPath / "python.exe"} -m build')
            os.system(f'{scriptPath / "twine.exe"} upload dist/* -u {u} -p {p}')
    finally:
        if not keep_build_files:
            removeUnusedPath()


# -------------------------------------------------


def _getIgnoreLibAry(content: str) -> list[str]:
    '获取pyproject.toml中屏蔽的第三方库'
    content = re.findall(r'dependencies = \[(.*?)\]', content, re.DOTALL)[0]
    ary = content.strip().split('\n')
    ary = [x.strip() for x in ary if x]
    return sorted([x[1:].replace('"', '').replace("'", '').replace(',', '').strip() for x in filter(lambda x: x.startswith('#'), ary)])
