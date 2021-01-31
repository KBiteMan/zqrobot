#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("💎BTC", callback_data='1'),
            InlineKeyboardButton("💵USDT", callback_data='2'),
        ],
        [InlineKeyboardButton("PayPal", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    textStr = '' \
              '[xx](https://goss.cfp.cn/creative/vcg/800/new/VCG211306186617.jpg)' \
              '担保竭诚为你服务，你可以选择以下方式进行担保'
    update.message.reply_text(textStr, reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"选择了: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start to test this bot.")


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1518463420:AAEC2NAGyx5Xc3vWFGRWcGI6ikWIfixvGTk", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('danbao', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()