import aiohttp

version = "2.9.1"
server_version = "jj/{} via aiohttp/{}".format(version, aiohttp.__version__)


__all__ = ("version", "server_version")
