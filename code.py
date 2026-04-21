from aiogram.types import FSInputFile
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.utils.keyboard import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from pyexpat.errors import messages

BOT_API_TOKEN = '7952293581:AAHLmwgZ29DQDFi33EBzDQ1p35eRei3JEpc'

bot = Bot(token=BOT_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()



@router.message(Command('start'))
async def cmd_start_2(message: Message):
    await message.answer(
        ' Запуск сообщения по команде /start ,не знаете как пройти регестрацию введите комманду /start_2 '

        ' главное меню /catalog '

        ' хотите что то приобрести /catalog_1 '
    )


@router.message(Command('catalog'))
async def catalog_com(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Каталог товаров", callback_data="catalog")],
        [InlineKeyboardButton(text="Партнерство", callback_data="reviews")],
        [InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data="materials")],
        [InlineKeyboardButton(text="Cвязаться с нами", callback_data="contact")]
    ])
    await message.answer('Выбор:', reply_markup=keyboard)

@dp.message(Command('catalog_1'))
async def show_device_types(message: Message):
    keyboard = [
        [KeyboardButton(text='iOS')],
        [KeyboardButton(text='Android')]
    ]
    device_keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder='Выберите операционную систему'
    )
    await message.answer('Выберите категорию устройств:', reply_markup=device_keyboard)


@dp.message(F.text.lower() == 'photo')
async def photo(message: Message):
    photo = FSInputFile('2b220972-de53-4adf-b672-79f3f4b5c1b8.jpg')
    await message.answer_photo(photo, '')


@dp.message(F.text.lower() == 'photo samsung')
async def photo(message: Message):
    photo = FSInputFile('')
    await message.answer_photo(photo, '')

@dp.message(F.text.lower() == 'audio')
async def audio(message: Message):
    audio = FSInputFile('Ed_Sheeran_-_Shape_of_You_47828367.mp3')
    await message.answer_audio(audio, '')

@dp.message(F.text.lower() == 'video')
async def video(message: Message):
    video = FSInputFile('WhatsApp_Video_2025-02-22_at_17.15.18_(1).mp4')
    await message.answer_video(video, '')


@dp.message(F.text.lower() == 'ios')
async def show_ios_devices(message: Message):
    keyboard = [
        [KeyboardButton(text='iPhone 20 Pro Max')],
        [KeyboardButton(text='iPhone 17 Pro Max')],
        [KeyboardButton(text='iPhone 17 Pro')],
        [KeyboardButton(text='iPhone 17 ')],
        [KeyboardButton(text='iPhone 16 Pro Max')],
        [KeyboardButton(text='iPhone 16 Pro')],
        [KeyboardButton(text='iPhone 16 ')],
        [KeyboardButton(text='MacBook Pro')]
    ]
    ios_keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder='Выберите устройство Apple'
    )
    await message.answer('Выберите устройство Apple:', reply_markup=ios_keyboard)


@dp.message(F.text.lower() == 'android')
async def show_android_devices(message: Message):
    keyboard = [
        [KeyboardButton(text='Samsung s26 ultra')],
        [KeyboardButton(text='Samsung S26 +')],
        [KeyboardButton(text='Samsung S26 ')],
        [KeyboardButton(text='Xiaomi 17 Ultra')],
        [KeyboardButton(text='Xiaomi 17 Pro')],
        [KeyboardButton(text='Xiaomi 17 ')],
    ]
    android_keyboard = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder='Выберите устройство Android'
    )
    await message.answer('Выберите устройство Android:', reply_markup=android_keyboard)


@dp.message(F.text.lower() == 'iphone 20 pro max')
async def show_iphone_info(message: Message):
    await message.answer(
        'iPhone 20 Pro Max 📱\n'
        'Цена: 9999$ 💰🤑🤩\n'
        'Флагманский смартфон Apple \nНапишите "Подтверждаю покупку iPhone", чтобы купить✅')


@dp.message(F.text.lower() == 'iphone 16 pro max')
async def show_iphone_info(message: Message):
    await message.answer(
        'iPhone 16 Pro Max 📱\n'
        'Цена: 1000$ 💰\n'
        'Флагманский смартфон Apple \nНапишите "Подтверждаю покупку iPhone", чтобы купить✅')

@dp.message(F.text.lower() == 'iphone 16 pro')
async def show_iphone_info(message: Message):
    await message.answer(
        'iPhone 16 Pro 📱\n'
        'Цена: 950$ 💰\n'
        'Флагманский смартфон Apple \nНапишите "Подтверждаю покупку iPhone", чтобы купить✅')

@dp.message(F.text.lower() == 'iphone 16')
async def show_iphone_info(message: Message):
    await message.answer(
        'iPhone 16  📱\n'
        'Цена: 800$ 💰\n'
        'Флагманский смартфон Apple \nНапишите "Подтверждаю покупку iPhone", чтобы купить✅')


@dp.message(F.text.lower() == 'iphone 17 pro max')
async def show_iphone_info(message: Message):
    await message.answer(
        'iPhone 17 Pro Max 📱\n'
        'Цена: 1500$ 💰\n'
        'Флагманский смартфон Apple \nНапишите "Подтверждаю покупку iPhone", чтобы купить✅')


@dp.message(F.text.lower() == 'iphone 17 pro')
async def show_iphone_info(message: Message):
    await message.answer(
        'iPhone 17 Pro 📱\n'
        'Цена: 1200$ 💰\n'
        'Флагманский смартфон Apple \nНапишите "Подтверждаю покупку iPhone", чтобы купить✅')


@dp.message(F.text.lower() == 'iphone 17')
async def show_iphone_info(message: Message):
    await message.answer(
        'iPhone 17 📱\n'
        'Цена: 1000$ 💰\n'
        'Флагманский смартфон Apple \nНапишите "Подтверждаю покупку iPhone", чтобы купить✅')



@dp.message(F.text.lower() == 'macbook pro')
async def show_macbook_info(message: Message):
    await message.answer(
        'MacBook Pro 💻\n'
        'Цена: 2000$ 💰\n'
        'Мощный ноутбук от Apple \nНапишите "Подтверждаю покупку MacBook", чтобы купить✅')


@dp.message(F.text.lower() == 'samsung s26 ultra')
async def show_samsung_info(message: Message):
    await message.answer(
        'Samsung S26 Ultra 📱\n'
        'Цена: 1500$ 💰\n'
        'Флагманский смартфон Samsung \nНапишите "Подтверждаю покупку Samsung", чтобы купить✅')


@dp.message(F.text.lower() == 'samsung s26 +')
async def show_samsung_info(message: Message):
    await message.answer(
        'Samsung S26+ 📱\n'
        'Цена: 1300$ 💰\n'
        'Флагманский смартфон Samsung \nНапишите "Подтверждаю покупку Samsung", чтобы купить✅')


@dp.message(F.text.lower() == 'samsung s26')
async def show_samsung_info(message: Message):
    await message.answer(
        'Samsung S26 📱\n'
        'Цена: 1300$ 💰\n'
        'Флагманский смартфон Samsung \nНапишите "Подтверждаю покупку Samsung", чтобы купить✅')


@dp.message(F.text.lower() == 'xiaomi 17 ultra')
async def show_xiaomi_info(message: Message):
    await message.answer(
        'Xiaomi 17 Ultra 📱\n'
        'Цена: 1700$ 💰\n'
        'Флагманский смартфон Xiaomi \nНапишите "Подтверждаю покупку Xiaomi", чтобы купить✅')


@dp.message(F.text.lower() == 'xiaomi 17 pro')
async def show_xiaomi_info(message: Message):
    await message.answer(
        'Xiaomi 17 Pro 📱\n'
        'Цена: 1100$ 💰\n'
        'Флагманский смартфон Xiaomi \nНапишите "Подтверждаю покупку Xiaomi", чтобы купить✅')


@dp.message(F.text.lower() == 'xiaomi 17')
async def show_xiaomi_info(message: Message):
    await message.answer(
        ' Xiaomi 17 📱\n'
        'Цена: 900$ 💰\n'
        'Флагманский смартфон Xiaomi \nНапишите "Подтверждаю покупку Xiaomi", чтобы купить✅ '
    )


@dp.message(F.text.lower().startswith('подтверждаю покупку'))
async def confirm_order(message: Message):
    await message.answer(f' Вы успешно купили Спасибо за покупку! ')


@router.callback_query(lambda c: c.data in ['contact', 'materials', 'reviews', 'catalog'])
async def handle_callback_query(callback_query: types.callback_query):
    data = callback_query.data
    if data == 'contact':
        await callback_query.message.answer('+996778473655')
    if data == 'materials':
        await callback_query.message.answer(
            'Если у вас возникли вопросы , будем рады ответить на них. Обращайтесь и задавайте нам свои вопрос через наш сайт')
    if data == 'reviews':
        await callback_query.message.answer('Мы работаем с такими компаниями как: Gadget.kg , Softech.kg и Sulpak.kg')
    if data == 'catalog':
        await callback_query.message.answer('Телефоны,ноутбуки и остальная техника ')


@dp.message(Command('start_2'))
async def hello(message: Message):
    keyboard = [
        [KeyboardButton(text='icloud'),
         KeyboardButton(text='Google')]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder='Введите почту'
    )
    await message.answer("как пройти регистрацию???", reply_markup=keyboard)


@dp.message(F.text.lower() == 'здравствуйте')
async def start(message: Message):
    await message.reply('Здравствуйте! Чем могу помочь?')


@dp.message(F.text.lower() == 'привет')
async def start(message: Message):
    await message.reply('Привет! Чем могу помочь?')


@dp.message(F.text.lower() == 'hello')
async def start(message: Message):
    await message.reply('Hello! How can i halp you?')


@dp.message(F.text.lower() == 'icloud')
async def with_ios(message: Message):
    await message.reply('Отличный выбор ios лучше android!')


@dp.message(F.text.lower() == 'google')
async def with_android(message: Message):
    await message.reply('Отличный выбор android лучше ios!')




dp.include_router(router)


async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
