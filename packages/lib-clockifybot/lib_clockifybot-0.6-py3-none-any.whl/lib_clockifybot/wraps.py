from sqlalchemy.exc import SQLAlchemyError

from .config import get_user, get_bot_by_table, get_bot_by_user
from .log import add_log


def process_add_user_in_set_command(command_message, session, table):
    try:
        command, message = command_message[0], command_message[1]
        chat_id, username = str(message.chat.id), message.chat.username
        new_user = table(telegram_id=chat_id, username=username, command=command)
        session.add(new_user)
        session.commit()
    except SQLAlchemyError as e:
        the_error = f"SQLAlchemyError in process_add_user_in_set_command: {e}"
        add_log(the_error, get_bot_by_table(table))
    except Exception as e:
        txt = f"Exception in process_add_user_in_set_command: {e}"
        add_log(txt, get_bot_by_table(table))


def set_command_in_wraps(user, session, command):
    try:
        user.command = command
        session.commit()
    except SQLAlchemyError as e:
        add_log(f"SQLAlchemyError in set_command_in_wraps: {e}", get_bot_by_user(user))
    except Exception as e:
        add_log(f"Exception in set_command_in_wraps: {e}", get_bot_by_user(user))


def set_command(command, session, table):
    def decorator(handler):
        def wrapper(message):
            user = get_user(message, session, table)
            if not user:
                process_add_user_in_set_command([command, message], session, table)
            else:
                set_command_in_wraps(user, session, command)
            return handler(message)

        return wrapper

    return decorator
