import os

from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError
from telebot import types, TeleBot

from .log import add_log

load_dotenv(os.getenv('CLOCKIFY_ENV'))
REPORT_USERNAME = None if os.getenv("TOKEN_REPORT") is None else \
    TeleBot(os.getenv("TOKEN_REPORT")).get_me().username
TRACKER_USERNAME = None if os.getenv("TOKEN_TRACKER") is None else \
    TeleBot(os.getenv("TOKEN_TRACKER")).get_me().username
REPORT_TABLE = "user_report"
ok_status_codes = [200, 201]
cancel = "/cancel"
threads = {}
stop_events = {}
ADMIN_ROLE = "original_admin"
true_flag, false_flag = "True", "False"
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT = 1, 2, 3, 4, 5, 6, 7, 8
monthly, pre_month = "monthly", "previous_month"
commands_report = [types.BotCommand(command="/start", description="Start menu")]
commands_tracker = [
    types.BotCommand(command="/start", description="Start menu"),
    types.BotCommand(command="/api", description="⚙️ Configure the API key"),
]


def telegram_api_exception(bot, func, error):
    username = bot.get_me().username
    if "message is not modified" in str(error):
        add_log(f"Same content and markup in {func}", username)
    else:
        add_log(f"An error occurred in {func}: {error}", username)


def send_cancel_message(message, session, table):
    try:
        if message.text.lower() == cancel:
            user = get_user(message, session, table)
            user.command = None
            session.commit()
            return True
    except SQLAlchemyError as e:
        add_log(f"SQLAlchemyError in send_cancel_message: {e}")
    except Exception as e:
        add_log(f"Exception in send_cancel_message: {e}")


def change_command_to_none(user, session, bot):
    try:
        user.command = None
        session.commit()
    except SQLAlchemyError as e:
        add_log(
            f"SQLAlchemyError in change_command_to_none: {e}", bot.get_me().username
        )
    except Exception as e:
        add_log(f"Exception in change_command_to_none: {e}", bot.get_me().username)


def get_user(message, session, table):
    chat_id = str(message.chat.id)
    return session.query(table).filter_by(telegram_id=chat_id).first()


def get_bot_by_table(table):
    name = table.__tablename__
    if name == REPORT_TABLE:
        return REPORT_USERNAME
    else:
        return TRACKER_USERNAME


def get_bot_by_user(user):
    name = user.__class__.__tablename__
    if name == REPORT_TABLE:
        return REPORT_USERNAME
    else:
        return TRACKER_USERNAME
