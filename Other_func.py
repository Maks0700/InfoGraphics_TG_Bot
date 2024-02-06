from aiogram import Bot

async def sale(bot:Bot,message:str,user_id:int):
    
    
    await bot.send_message(chat_id=int(user_id),text="""*✨СКИДКА 10%✨

 Только СЕГОДНЯ при заказе любого дизайна для Вас действует скидка 10% 

 (напишите кодовое слово «скидка10» в личные сообщения дизайнеру)

 ▫️успевайте, время скидки ограниченно*""",parse_mode="Markdown")
    

    