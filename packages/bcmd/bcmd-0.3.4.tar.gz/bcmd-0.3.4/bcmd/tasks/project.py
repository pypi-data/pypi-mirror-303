from pathlib import Path
from typing import Final

import typer
from beni import bcolor, bfile, bpath, btask
from beni.bfunc import syncCall

app: Final = btask.newSubApp('project 工具')


@app.command()
@syncCall
async def gen_init_py(
    workspace_path: Path = typer.Argument(None, help='workspace 路径'),
):
    '将指定目录下的所有文件生成 __init__.py 文件'

    async def makeInitFiles(p: Path):
        if p.name == '__pycache__':
            return
        if p.name.startswith('.'):
            return
        if workspace_path != p:
            initFile = p / '__init__.py'
            if not initFile.exists():
                bcolor.printYellow(initFile)
                await bfile.writeText(initFile, '')
        for x in bpath.listDir(p):
            await makeInitFiles(x)

    if not workspace_path:
        workspace_path = Path.cwd()
    await makeInitFiles(workspace_path)
    bcolor.printGreen('OK')
