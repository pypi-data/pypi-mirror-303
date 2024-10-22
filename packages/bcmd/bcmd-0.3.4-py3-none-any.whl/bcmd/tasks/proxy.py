from __future__ import annotations

from typing import Final

import psutil
import pyperclip
import typer
from beni import bcolor, btask
from beni.bfunc import syncCall

app: Final = btask.app


@app.command()
@syncCall
async def proxy(
    port: int = typer.Option(15236, help="代理服务器端口"),
):
    '生成终端设置代理服务器的命令'
    processNameAry:list[str] = []
    process = psutil.Process().parent()
    while process:
        processNameAry.append(process.name())
        process = process.parent()
    msg = ''
    if 'cmd.exe' in processNameAry:
        msg = '\r\n'.join([
            f'set http_proxy=http://localhost:{port}',
            f'set https_proxy=http://localhost:{port}',
            f'set all_proxy=http://localhost:{port}',
            '',
        ])
    elif set(['powershell.exe', 'pwsh.exe']) & set(processNameAry):
        msg = '\r\n'.join([
            f'$env:http_proxy="http://localhost:{port}"',
            f'$env:https_proxy="http://localhost:{port}"',
            f'$env:all_proxy="http://localhost:{port}"',
            '',
        ])
    if msg:
        bcolor.printMagenta('\r\n' + msg)
        pyperclip.copy(msg)
        bcolor.printYellow('已复制，可直接粘贴使用')
    else:
        bcolor.printRed(f'不支持当前终端（{processNameAry}）')
