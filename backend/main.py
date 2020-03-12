from fastapi import FastAPI
import asyncio
import re


app = FastAPI()


CONV_DEFS = [
    (b'\xe2a', "á"),
    (b'\xe2e', "é"),
    (b'\xe2i', "í"),
    (b'\xe2o', "ó"),
    (b'\xe8o', "ö"),
    (b'\xeeo', "ő"),
    (b'\xe2u', "ú"),
    (b'\xe8u', "ü"),
    (b'\xeeu', "ű"),
]


def to_utf8(b):
    for (k, v) in CONV_DEFS:
        b = b.replace(k, v.encode('utf-8'))
        b = b.replace(k.upper(), v.upper().encode('utf-8'))
    return b.decode('utf-8')


@app.get("/")
async def book_by_isbn(isbn: str):
    proc = await asyncio.create_subprocess_exec(
        "yaz-client",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    cmds = b"open tcp:z3950.mokka.hu\n"
    cmds += b'f @attr 1=7 "' + isbn.encode() + b'"\n'
    cmds += b'show 1\n'
    cmds += b'exit\n'

    stdout, stderr = await proc.communicate(input=cmds)

    data = [
        to_utf8(line)
        for line in stdout.split(b'\n')
        if re.match(b'\d{3}\s.+', line)]
    return {"data": data}
