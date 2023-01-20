import time

import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, executor, types, exceptions
import datetime

import asyncio
import logging
import parsing
import databaseMatan
import databaseGeom


lastupd = datetime.datetime(2000, 7, 10, 3, 3, 3)



channel_id = -1001655261828
matan_msg_id = 298
geom_msg_id = 527
errorlog = ''


logging.basicConfig(level=logging.INFO)


bot = Bot(TOKEN)
dp = Dispatcher(bot)

def spisok(names):
    folders = dict()
    for x in names:
        i = 0
        while i < len(x) and x[i].isalpha():
            i += 1
        if x[:i] == "Семинар":
            if folders.get("Семинары"):
                folders["Семинары"] += [x]
            else:
                folders["Семинары"] = [x]
        elif folders.get(x[:i]):
            folders[x[:i]] += [x]
        else:
            folders[x[:i]] = [x]
    return folders


async def makeGeom():
    namesGeom = parsing.parseGeom()
    # await bot.send_message(channel_id, 'cuccum')
    insert_info = []
    for x in namesGeom:
        if namesGeom[x] == 0:
            with open('Geom\\' + x, 'rb') as f:
                msg = await bot.send_document(channel_id, f)
                # print(msg.message_id)
                insert_info.append((msg.message_id, x))
        if namesGeom[x] == 2:
            with open('Geom\\' + x, 'rb') as f:
                await bot.edit_message_media(f, channel_id, databaseGeom.get_id(x))
                # print(msg.message_id)


    # print(insert_info)
    databaseGeom.insert(insert_info)
    # await bot.send_message(message.from_user.id, '<a href="http://math.hse.ru">text</a>', parse_mode=types.ParseMode.HTML)


    fldrs = spisok(list(namesGeom.keys()))
    textGeom = f'<b>ГЕОМА</b>'
    for x in fldrs:
        # print(fldrs)
        if databaseGeom.is_exists(x):
            text = f'<b>{x}</b>'
            for file in fldrs[x]:
                text += f'\n<a href="https://t.me/lutisfgag/{databaseGeom.get_id(file)}">{file}</a>'
            await bot.edit_message_text(text, channel_id,
                                        databaseGeom.get_folder_id(x),
                                        parse_mode=types.ParseMode.HTML,
                                        disable_web_page_preview=True)
        else:
            text = f'<b>{x}</b>'
            for file in fldrs[x]:
                text += f'\n<a href="https://t.me/lutisfgag/{databaseGeom.get_id(file)}">{file}</a>'

            idd = await bot.send_message(channel_id, text,
                                         parse_mode=types.ParseMode.HTML,
                                         disable_web_page_preview=True)
            databaseGeom.add_folder_id(idd.message_id, x)

        textGeom += f'\n<a href="https://t.me/lutisfgag/{databaseGeom.get_folder_id(x)}">{x}</a>'
    try:
        await bot.edit_message_text(textGeom, channel_id,
                                    geom_msg_id, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
    except aiogram.utils.exceptions.MessageNotModified:
        print('vsem pohui na geomu')

async def makeMatan():
    namesMatan = parsing.parseMatan()
    insert_info = []
    for x in namesMatan:
        if namesMatan[x] == 0:
            with open('Matan\\' + x, 'rb') as f:
                msg = await bot.send_document(channel_id, f)
                # print(msg.message_id)
                insert_info.append((msg.message_id, x))
        if namesMatan[x] == 2:
            with open('Matan\\' + x, 'rb') as f:
                await bot.edit_message_media(f, channel_id, databaseMatan.get_id(x))
                # print(msg.message_id)


    # print(insert_info)
    databaseMatan.insert(insert_info)
    # await bot.send_message(message.from_user.id, '<a href="http://math.hse.ru">text</a>', parse_mode=types.ParseMode.HTML)


    fldrs = spisok(list(namesMatan.keys()))
    textmatan = f'<b>МАТАН</b>'
    for x in fldrs:
        # print(fldrs)
        if databaseMatan.is_exists(x):
            text = f'<b>{x}</b>'
            for file in fldrs[x]:
                text += f'\n<a href="https://t.me/lutisfgag/{databaseMatan.get_id(file)}">{file}</a>'

            await bot.edit_message_text(text, channel_id, databaseMatan.get_folder_id(x),
                                         parse_mode=types.ParseMode.HTML,
                                         disable_web_page_preview=True)
        else:
            text = f'<b>{x}</b>'
            for file in fldrs[x]:
                text += f'\n<a href="https://t.me/lutisfgag/{databaseMatan.get_id(file)}">{file}</a>'

            idd = await bot.send_message(channel_id, text,
                                         parse_mode=types.ParseMode.HTML,
                                         disable_web_page_preview=True)
            databaseMatan.add_folder_id(idd.message_id, x)

        textmatan += f'\n<a href="https://t.me/lutisfgag/{databaseMatan.get_folder_id(x)}">{x}</a>'
    try:
        await bot.edit_message_text(textmatan, channel_id,
                                    matan_msg_id, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
    except aiogram.utils.exceptions.MessageNotModified:
        print('vsem pohui na matan')


@dp.message_handler(commands=['update'])
async def update(message: types.Message):
    global lastupd
    if message.from_user.id == 879292729 or message.from_user.id == 1016488432:
        await makeMatan()
        await makeGeom()
        lastupd = datetime.datetime.now()
    else:
        await bot.send_message(message.from_user.id, "каждый день, каждый час новое кино, кто мне друг, кто мне враг" +
                                                     " думаю никто шоу биз реп игра тупо шапито алишерка" +
                                                     " в этом цирке самый главный клоун")


@dp.message_handler(commands=['lastupd'])
async def update(message: types.Message):
    await bot.send_message(message.from_user.id, lastupd.strftime("%d.%m.%Y %H:%M:%S"))



async def upd():
    global lastupd
    global errorlog
    while True:
        await asyncio.sleep(60)
        await makeMatan()
        await makeGeom()
        if len(errorlog):
            await bot.send_message(879292729, errorlog)
            await bot.send_message(1016488432, errorlog)
            errorlog = ''
        lastupd = datetime.datetime.now()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # executor.start_polling(dp, skip_updates=True)
    loop.create_task(upd())
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except Exception as e:
            errorlog += e + '\n\n'
