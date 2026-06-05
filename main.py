# Context Management Model context Protocol

from mcp.server.fastmcp import FastMCP
import os
import re

mcp = FastMCP('main.py')

FILE_PATH = ''
FILE_UPLOAD_LIMIT = 500
CONTEXT_TITLE = ''
URL = []


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

@mcp.tool()
def url_context_retrieve() -> list[str] | None:

    with open(FILE_PATH, 'r') as file:
        content = file.read()
    URL = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)

    return URL
