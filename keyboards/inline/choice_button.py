from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import test_callback

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Выбор 1", callback_data=test_callback.new(
#                 item_name = "something", quantity = 23
#             )),
#             InlineKeyboardButton(text="Выбор 2", callback_data="test:something:23"),
#         ],
#         [
#             InlineKeyboardButton(text="Выбор 3", callback_data="cancel")
#         ]
#     ]
# )

choice = InlineKeyboardMarkup(row_width=2)

button1 = InlineKeyboardButton(text="Выбор 1", callback_data=test_callback.new(
                item_name = "something", quantity = 23
            ))
choice.insert(button1)
button2 = InlineKeyboardButton(text="Выбор 2", callback_data="test:something:23")
choice.insert(button2)

cancel_button = InlineKeyboardButton(text="Выбор 3", callback_data="cancel")
choice.insert(cancel_button)
