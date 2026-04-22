# Ala-Too-project-Telegram-bot-

Как должно выглядеть (пример)
Python
# Импорт классов для работы с файлами (фото, видео, аудио)
from aiogram.types import FSInputFile

# Router — используется для разделения логики обработки сообщений
# F — фильтр для проверки текста сообщений
from aiogram import Router, F

# Command — фильтр для обработки команд (например: /start)
from aiogram.filters import Command

# Message — объект входящего сообщения от пользователя
# InlineKeyboardButton — кнопка внутри сообщения
# InlineKeyboardMarkup — контейнер для inline-кнопок
# KeyboardButton — кнопка обычной клавиатуры
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

# Bot — основной объект Telegram-бота
# Dispatcher — обрабатывает входящие события (сообщения, команды)
from aiogram import Bot, Dispatcher, types

# MemoryStorage — временное хранилище данных для FSM
from aiogram.fsm.storage.memory import MemoryStorage

# asyncio — библиотека для асинхронного выполнения
import asyncio

# ReplyKeyboardMarkup — клавиатура с кнопками под полем ввода
from aiogram.utils.keyboard import ReplyKeyboardMarkup

# State — отдельное состояние
# StatesGroup — группа состояний (используется в FSM)
from aiogram.fsm.state import State, StatesGroup

# FSMContext — хранит данные пользователя между шагами
from aiogram.fsm.context import FSMContext
📌 Пример обработчика
Python
# Обработчик команды /start
@router.message(Command('start'))
async def cmd_start(message: Message):
    # Отправка текстового сообщения пользователю
    await message.answer(
        'Запуск выполнен.\n'
        'Для регистрации используйте команду /start_2.\n'
        'Для перехода в каталог — /catalog.'
    )
📌 Пример клавиатуры
Python
# Обработчик команды /catalog
@router.message(Command('catalog'))
async def catalog_command(message: Message):
    
    # Создание inline-клавиатуры
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Каталог товаров", callback_data="catalog")],
        [InlineKeyboardButton(text="Партнерство", callback_data="reviews")],
        [InlineKeyboardButton(text="FAQ", callback_data="materials")],
        [InlineKeyboardButton(text="Связаться", callback_data="contact")]
    ])

    # Отправка сообщения с кнопками
    await message.answer('Выберите раздел:', reply_markup=keyboard)
📌 FSM (регистрация)
Python
# Класс состояний регистрации
class Reg(StatesGroup):
    service = State()  # выбор сервиса (iCloud / Google)
    email = State()    # ввод email
Python
# Начало регистрации
@dp.message(Command("start_2"))
async def start_registration(message: Message, state: FSMContext):

    # Установка первого состояния
    await state.set_state(Reg.service)

    await message.answer("Выберите сервис:")
Python
# Обработка выбора сервиса
@dp.message(Reg.service)
async def process_service(message: Message, state: FSMContext):

    # Сохранение выбранного значения
    await state.update_data(service=message.text)

    # Переход к следующему шагу
    await state.set_state(Reg.email)

    await message.answer("Введите email:")
Python
# Обработка ввода email
@dp.message(Reg.email)
async def process_email(message: Message, state: FSMContext):

    # Получение ранее сохраненных данных
    data = await state.get_data()

    await message.answer(
        f"Регистрация завершена.\n"
        f"Сервис: {data['service']}\n"
        f"Email: {message.text}"
    )

    # Очистка состояния
    await state.clear()

# Точка входа в программу
if  ___name___== '__main__':
    asyncio.run(main())
