from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import emoji
import flag
import unicodedata
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


def keyboard_main()->ReplyKeyboardMarkup: #создаем клавиатуру для кнопок
    keyboard_main=ReplyKeyboardMarkup(resize_keyboard=True)
    but_infographics=KeyboardButton(text="Инфографика")
    but_design_instagram=KeyboardButton(text="Дизайн инстаграма")
    but_creative=KeyboardButton(text="Креативы")
    but_vk=KeyboardButton(text="Дизайн Вконтакте")
    keyboard_main.row(but_infographics,but_creative).add(but_design_instagram,but_vk)
    return keyboard_main

def keyboard_infographic()->InlineKeyboardMarkup:
    keyboard_main_infographic=InlineKeyboardMarkup(row_width=3)
    but_infogr=InlineKeyboardButton(text="Дополнительные услуги!!",callback_data="infogr")
    but_link=InlineKeyboardButton(text="Написать",url="https://t.me/an_designer1")
    return keyboard_main_infographic.add(but_infogr,but_link)


def keyboard_instagram()->InlineKeyboardMarkup():
    keyboard_main_instagram=InlineKeyboardMarkup(row_width=3)
    but_insta=InlineKeyboardButton(text="Дополнительные услуги!!",callback_data="inst")
    but_link=InlineKeyboardButton(text="Написать",url="https://t.me/an_designer1")
    return keyboard_main_instagram.add(but_insta,but_link)

def keyboard_vkontakte()->InlineKeyboardMarkup():
    keyboard_main_vkontakte=InlineKeyboardMarkup(row_width=5)
    but_vkontakte=InlineKeyboardButton(text="Дополнительные услуги",callback_data="vk")
    but_link=InlineKeyboardButton(text="Написать",url="https://t.me/an_designer1")
    return keyboard_main_vkontakte.add(but_vkontakte,but_link)

def keyboard_creatives()->InlineKeyboardMarkup():
    keyboard_main_creatives=InlineKeyboardMarkup(row_width=5)
    but_link=InlineKeyboardButton(text="Написать",url="https://t.me/an_designer1")
    return keyboard_main_creatives.add(but_link)



    
    
    

    







