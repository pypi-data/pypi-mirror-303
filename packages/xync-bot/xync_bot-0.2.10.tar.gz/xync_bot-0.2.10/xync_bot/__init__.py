from aiogram.client.default import DefaultBotProperties
from aiogram.types import MenuButtonWebApp, WebAppInfo
import logging
from os import getenv as env
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from tortoise.backends.asyncpg import AsyncpgDBClient

from xync_bot.handlers import main, vpn

load_dotenv()

logging.basicConfig(filemode='a', level=logging.DEBUG)

bot = Bot(token=env('TOKEN'), default=DefaultBotProperties(parse_mode='Markdown'))
dp = Dispatcher(bot=bot)


async def on_startup(wh_url: str, twa_url: str, cn: AsyncpgDBClient, mbt: str = 'Go!'):
    """ SET DEISPATCHER GLOBAL WORKFLOW DATA FOR DB Connection """
    dp['dbc'] = cn
    """ WEBHOOK SETUP """
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != wh_url:
        await bot.set_webhook(url=wh_url, drop_pending_updates=True)
    """ WEBAPP URL SETUP IN MENU """
    await bot.set_chat_menu_button(menu_button=MenuButtonWebApp(text=mbt, web_app=WebAppInfo(url=twa_url)))


async def on_shutdown():
    """ CLOSE BOT SESSION """
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()


dp.startup.register(on_startup)
dp.shutdown.register(on_shutdown)

dp.include_routers(vpn, main)
