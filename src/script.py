import py7zr
import os
import subprocess
import asyncio
import sys

print("Running process in directory context: {}".format(os.getcwd()))

PREFIX = "Mercedes.7z"


async def run_command(program, *args):
    process = await asyncio.create_subprocess_exec(
        program,
        *args,
        stdout=asyncio.subprocess.PIPE,
    )
    stdout, _ = await process.communicate()
    return stdout.decode()

loop = asyncio.get_event_loop()
commands = asyncio.gather(
    run_command("ls", "src/test/"),
    run_command("ls", "src/test/Mercedes.7z.*"),
    run_command("cat", "src/test/{0}.* > {0}".format(PREFIX)),
)
data = loop.run_until_complete(commands)
[print(d) for d in data]
loop.close()


# FILE = 'Mercedes.7z'

# with py7zr.SevenZipFile(FILE, mode='r') as z:
#     z.extractall(path="/tmp")
