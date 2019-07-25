from telegram import ReplyKeyboardMarkup

MAIN_BUTTONS = {
    'bank': '💰 My score',
    'top_up': '💼 To invest',
    'withdraw': '🤑 Withdraw',
    'transactions': '⏳ History',
    'partners': '👥 Partners',
    'help': '❓ About Us',
    'back': '⬅️ Back'
}

_MAIN_KEYBOARD = [
    [
        MAIN_BUTTONS['bank'],
        MAIN_BUTTONS['transactions'],
    ],
    [
        MAIN_BUTTONS['top_up'],
        MAIN_BUTTONS['withdraw']
    ],
    [
        MAIN_BUTTONS['partners'],
        MAIN_BUTTONS['help'],
    ]
]

_BACK_KEYBOARD = [
    [
        MAIN_BUTTONS['back']
    ]
]


def main_keyboard():
    return ReplyKeyboardMarkup(_MAIN_KEYBOARD)


def back_keyboard():
    return ReplyKeyboardMarkup(_BACK_KEYBOARD)
