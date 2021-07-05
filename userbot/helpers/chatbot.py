from userbot.utils.extdl import install_pip

try:
    import randomstuff
except ModuleNotFoundError:
    install_pip("randomstuff.py")
    import randomstuff

from userbot import RANDOM_STUFF_API_KEY

rs_client = randomstuff.AsyncClient(api_key=RANDOM_STUFF_API_KEY, version="4")
