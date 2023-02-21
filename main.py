import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup
API_TOKEN = '6037149560:AAETTf67LAD5OKYgqpQTpPDmHpgunxigXCo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
kanalid = '-1001580138328'

def kannelsend():
    btn = InlineKeyboardButton(text="Boshlash ✅" ,callback_data="boshlash")
    btn2 = InlineKeyboardButton(text="Admin 🫡" ,url="https://t.me/mrxayitov")
    mark = InlineKeyboardMarkup(row_width=1).add(btn, btn2)
    return mark



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Assalomu alaykum hush kelibsiz bot telegram kanalga har 4 soatda yangi post joylab boradi. \nSizga ham huddi shunday bot kerak bolsa adminga murojat qiling xizmat pullik.", reply_markup=kannelsend())
    
@dp.callback_query_handler()
async def cb_handler(call: types.CallbackQuery):
    if call.data == "boshlash":
        if call.from_user.id == 693313498:
            num = 746
            while True:
                await bot.send_message(chat_id=call.from_user.id, text="Post joylash muvaffaqiyatli yoqildi ✅")
                num+=1
                
                r = requests.get("https://t.me/Rustiliharkunii/"+str(num))
                txt = r.content
                sup = BeautifulSoup(txt,'lxml')
                # soup = sup.prettify()
                fn = sup.find("meta", {"name": "twitter:description"} )
                context = fn["content"]
                kuchukcha = context.find("@")
                mazl = context.find("http")
                panjara = context.find("#")
                teng = context.find("=")
                
                if kuchukcha > 0:
                    await bot.send_message(chat_id=kanalid, text=context[0:kuchukcha], parse_mode="HTML")
                elif mazl > 0:
                    await bot.send_message(chat_id=kanalid, text=context[0:mazl], parse_mode="HTML")
                elif panjara > 0:
                    await bot.send_message(chat_id=kanalid, text=context[0:panjara], parse_mode="HTML")
                elif teng > 0:
                    
                    await bot.send_message(chat_id=kanalid, text=str(context).replace(">",""),parse_mode="MARKDOWN")
                elif context == "":
                    await bot.send_message(chat_id=kanalid, text="Qoshimcha botimiz https://t.me/zemo_videobot", parse_mode="HTML")
                else :
                    await bot.send_message(chat_id=kanalid, text=context, parse_mode="HTML")
                time.sleep(14400)

        else:
            await bot.send_message(chat_id=call.from_user.id, text=f"Kechirasiz {call.from_user.first_name} siz admin emassiz \nBizning kanal: @ruscha_toplam")







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
