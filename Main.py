from aiogram import types,Dispatcher,Bot,executor
from api_token import api_token
from icecream import ic

from keyboadrs import *
from aiogram.dispatcher.filters import Text

from aiogram.types import MediaGroup,InputMediaPhoto

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime,timedelta
from Other_func import *
from api_token import api_token
bot=Bot(api_token)
dp=Dispatcher(bot)

async def check_start(_):
     ic("Success!!")





#Создаем хэндлер для кнопки старт
#Затем идет приветствие бота для пользователя(с указанием имени)
@dp.message_handler(commands=["start"])
async def cmd_start(message:types.Message):
    
    await message.answer(f'''*👋Привет {message.from_user.first_name}!! На связи Анна👩‍💻

Хочешь создать стильный и привлекательный дизайн для своего проекта?🤔
Тогда обращайся ко мне!📱

Уже больше года я занимаюсь дизайном и за это время оформила более 180 проектов✨

От меня уходят с ярким и эффективным дизайном🎉

Заказывая у меня, тебе не придется искать сотни дизайнеров для своего бизнеса.
Я предлагаю полный спектр услуг в одном месте 🤩
Переходи на мой телеграмм-канал!!!
⬇️   ⬇️   ⬇️   ⬇️


https://t.me/andesigner5 *''',parse_mode="Markdown",reply_markup=keyboard_main())
    
    
    apschedule=AsyncIOScheduler()
    apschedule.add_job(sale,trigger="date",run_date=datetime.now()+timedelta(minutes=7),kwargs={"bot":bot,"message":message.text,"user_id":message.chat.id})
    apschedule.start()
    

#Создаем хэндлер для обработки команды(текста введеного в поле сообщения) Инфографика
#Отправляем фотки с указанием прайса листа и его описанием
#Указываем markdown parse_mode для обработки текста из символов из интернета (далее этот parde_mode указывается везде)
@dp.message_handler(Text(equals="Инфографика",ignore_case=True))
async def info_gr(message:types.Message):
   with open ("InfoGraphics_generally_info.jpg","rb") as photo_info:
        
        await bot.send_photo(message.chat.id,photo=photo_info)
        await message.answer(text=""""*📍Создам продающий и сочный дизайн карточек, которые будут выделяться среди Ваших конкурентов.

В стоимость моих услуг входит:
1. Анализ конкурента
2. Отбор фото
3. Обработка и обрезка фото
4. Разработка дизайна
5. Копирайтинг, создание продающих офферов и текста

Цена: от 399 рублей
Сроки: 1-3 дня

Для заказа карточек нажмите кнопку "Написать", и мы обсудим Ваш проект!*""",parse_mode="Markdown",reply_markup=keyboard_infographic())
        
        
@dp.message_handler(Text(equals="Дизайн инстаграма",ignore_case=True)) # Обработка кнопки инстаграма
async def insta_but(message:types.Message):
    with open("Insta_generally_info.jpg","rb") as photo_info:
        await bot.send_photo(message.chat.id,photo=photo_info)
        await message.answer(text="""*📍Создам продающий дизайн для Вашего Instagram, который будет выделяться среди Ваших конкурентов

Базовое оформление:

1. Анализ конкурентов
2. Подбор палитры и шрифтов
3. Отбор фото
4. Дизайн ленты на 12 постов
5. До 6 обложек актуального    
6. Дизайн аватара

Цена: от 3499 рублей
Сроки: 1-3 дня 

Для заказа нажмите кнопку "Написать", и мы обсудим Ваш проект!*""",parse_mode="Markdown",reply_markup=keyboard_instagram())


photos_read=["Test_photo_1.jpg","Test_photo_2.png"]
@dp.message_handler(Text(equals="Дизайн Вконтакте",ignore_case=True))
async def vk_but(message:types.Message):
    media_gr=[InputMediaPhoto(open(photo_path,"rb")) for photo_path in photos_read]
    await bot.send_media_group(message.chat.id,media=media_gr)
    await message.answer("""*📍Создам продающий дизайн для Вашей группы ВКонтакте , который будет выделяться среди Ваших конкурентов

Базовое оформление:

1. Обложка сообщества (ПК версия) 
2. Обложка сообщества (мобильная версия) 
3. Аватарка
4. Кнопки меню (до 6 штук)
5. Услуги (до 6 штук)

Цена: от 2999 рублей 
Сроки: 1-3 дня

Для заказа  нажмите кнопку "Написать", и мы обсудим Ваш проект!*""",parse_mode="Markdown",reply_markup=keyboard_vkontakte())
    


# Пишем общий хэндлер для обработки кнопки 
@dp.message_handler(Text(equals="Креативы",ignore_case=True))
async def cr_but(message:types.Message):
    with open("Creatives-min.png","rb") as photo_cr:
        await bot.send_photo(message.chat.id,photo=photo_cr)
        await message.answer("""*📍Создам продающий дизайн для Вашего креатива, который будет выделяться среди Ваших конкурентов

Чек-листы 
Прайсы 
Презентации
Сертификаты 
Визитки 
Рекламные макеты 

Цена: от 1499 рублей
Сроки: 1-3 дня 

Для заказа нажмите кнопку "Написать", и мы обсудим Ваш проект!* """,parse_mode="Markdown",reply_markup=keyboard_creatives())

@dp.callback_query_handler()
async def proccess_cmd(callback:types.CallbackQuery):
    if callback.data=="infogr":
        with open ("InforGraphics_extra_info.png","rb") as photo_infogr:
            await callback.bot.send_photo(callback.message.chat.id,photo=photo_infogr)
    elif callback.data=="inst":
        with open("Insta_extra_info.jpg","rb") as photo_inst:
            await callback.bot.send_photo(callback.message.chat.id,photo=photo_inst)
    elif callback.data=="vk":
        with open("Vk_extra_info.png","rb") as photo_vk:
            await callback.bot.send_photo(callback.message.chat.id,photo=photo_vk)
    
        
@dp.message_handler(content_types="text")
async def cmd_start(message:types.Message):
    
         await message.reply("Пожалуйста, пользуйтесь только встроенными кнопками!!!")
                     
    
if __name__=="__main__":
    executor.start_polling(dp,on_startup=check_start,skip_updates=False)