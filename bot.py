from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

TOKEN = '5699670562:AAEycECb_3mpO39QiC_QJ06EqvBKf6bDtM8'
channel_id = -1001655261828


bot = Bot(TOKEN)
dp = Dispatcher(bot)

import parsing
import database

matan_msg_id = 298

def spisok(names):
    folders = dict()
    for x in names:
        i = 0
        while i < len(x) and x[i].isalpha():
            i += 1
        if folders.get(x[:i]):
            folders[x[:i]] += [x]
        else:
            folders[x[:i]] = [x]
    return folders



async def makeMatan():
    namesMatan = parsing.parseMatan()
    # await bot.send_message(channel_id, 'cuccum')
    insert_info = []
    for x in namesMatan:
        if namesMatan[x] == 0:
            with open('Matan\\' + x, 'rb') as f:
                msg = await bot.send_document(channel_id, f)
                print(msg.message_id)
                insert_info.append((msg.message_id, x))
        if namesMatan[x] == 2:
            with open('Matan\\' + x, 'rb') as f:
                await bot.edit_message_media(f, channel_id, database.get_id(x))
                print(msg.message_id)


    # print(insert_info)
    database.insert(insert_info)
    # await bot.send_message(message.from_user.id, '<a href="http://math.hse.ru">text</a>', parse_mode=types.ParseMode.HTML)


    fldrs = spisok(list(namesMatan.keys()))
    textmatan = f'<b>МАТАН</b>'
    for x in fldrs:
        print(fldrs)
        if database.is_exists(x):
            pass
        else:
            text = f'<b>{x}</b>'
            for file in fldrs[x]:
                text += f'\n<a href="https://t.me/lutisfgag/{database.get_id(file)}">{file}</a>'

            idd = await bot.send_message(channel_id, text,
                                         parse_mode=types.ParseMode.HTML,
                                         disable_web_page_preview=True)
            database.add_folder_id(idd.message_id, x)

        textmatan += f'\n<a href="https://t.me/lutisfgag/{database.get_folder_id(x)}">{x}</a>'
    await bot.edit_message_text(textmatan, channel_id,
                                matan_msg_id, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)

@dp.message_handler(commands=['update'])
async def update(message: types.Message):
    await makeMatan()


# async def sendcum(wait_for):
#     while True:
#         await asyncio.sleep(wait_for)
#         namesMatan = parsing.parseMatan()
#         await bot.send_message(channel_id, 'cuccum')
#         insert_info = []
#         for x in namesMatan:
#             if namesMatan[x] == 0:
#                 with open(x, 'rb') as f:
#                     msg = await bot.send_document(channel_id, f)
#                     print(msg.message_id)
#                     insert_info += (msg.message_id, x)
#         # print(insert_info)
#         # database.insert(msg.message_id, insert_info)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.create_task(sendcum(60))
    # executor.start_polling(dp, skip_updates=True)
    executor.start_polling(dp, skip_updates=True)
