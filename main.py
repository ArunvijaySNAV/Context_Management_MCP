# Context Management Model context Protocol

from mcp.server.fastmcp import FastMCP
from pathlib import Path
import os
import re

mcp = FastMCP('main.py')

FILE_PATH = ''
FILE_UPLOAD_LIMIT = 500
CONTEXT_TITLE = ''
URL = []
BASE_DIR = path('Context')



file_size_bytes = os.path.getsize(FILE_PATH)
file_storage = file_size_bytes / (1024 * 1024)
file_exists = True if os.path.exists(FILE_PATH) and file_storage <= FILE_UPLOAD_LIMIT else False


@mcp.tool(name='llm_context_save')
def llm_context_save(filepath: str, message: str) -> None:
    """

    :param filepath:
    :param message:
    :return:
    """
    with open(filepath, 'w') as file:
        file.write(message)


@mcp.tool(name='llm_context_retrieve')
def llm_context_retrieve(filepath: str) -> str:

    with open(FILE_PATH, 'r') as file:
        content = file.read()

    return content

@mcp.tool(name='url_context_retrieve')
def url_context_retrieve() -> list[str] | None:

    with open(FILE_PATH, 'r') as file:
        content = file.read()
    URL = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)

    return URL

@mcp.tool()
def list_context_files(filepath: str) -> int :

    directory = Path('contexts')

    count_files = sum(1 for file in directory.iterdir() if file.is_file())
    return count_files