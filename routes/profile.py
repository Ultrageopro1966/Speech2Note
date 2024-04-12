import telebot  # type: ignore
from data.user_database import UserDatabase
from modules.logger import CustomLogger


class ProfileRoute:

    def __init__(self, bot: telebot.TeleBot, logger: CustomLogger, user_database: UserDatabase) -> None:  # type: ignore
        """
        Initializes the ProfileRoute instance.

        Args:
            bot (telebot.TeleBot): The Telegram bot instance.
            logger (CustomLogger): The logger instance.
            user_database (UserDatabase): The user database instance.
        """
        self.bot = bot
        self.logger = logger
        self.database = user_database

        # Handler for the '/profile' command
        @bot.message_handler(commands=["profile"])
        def profile(message: telebot.types.Message) -> None:  # type: ignore
            """
            Handler method for the '/profile' command.

            Args:
                message (telebot.types.Message): The message object.
            """
            self.__profile(message)

        # Log route initialization
        self.logger.info("Profile route initialized.", "server")

    def __profile(self, message: telebot.types.Message) -> None:  # type: ignore
        """
        Handle user profile requests.

        Args:
            message (telebot.types.Message): The message object received from the user.

        Returns:
            None
        """
        # Retrieve user information from the database
        code, user = self.database.get_user(message.chat.id)

        # If there was an error retrieving user information
        if code != 200:
            # Inform the user about the error
            self.bot.send_message(
                message.chat.id,
                "Произошла ошибка. Попробуйте ещё раз позже.\nМы уже работаем над этим.",
            )

        # If the user is not found in the database
        if user is None:
            # Register the user
            self.database.new_user(message.chat.id, message.from_user.username)
            # Send a welcome message to the user
            self.bot.send_message(
                message.chat.id,
                f"Привет, {message.from_user.username}!\n"
                + "---------------\n"
                + "Ты не можешь видеть профиль, потому что ты не был зарегистрирован.\n"
                + "Но у меня хорошие новости! Я уже тебя зарагестрировал!\n"
                + "Пришли мне аудиофайл, и я помогу тебе создать конспект из него.\n"
                + "---------------\n"
                + "Посмотреть профиль /profile\n"
                + "Получить токены /tokens\n"
                + "Посмотреть цены /prices\n"
                + "Информация о боте /about\n"
                + "---------------",
            )
            return

        # If the user is found in the database
        self.bot.send_message(
            message.chat.id,
            f"Привет, {user.name}!\n"
            + "---------------\n"
            + f"У тебя {user.tokens} токенов.\n"
            + f"Аккаунт создан {user.created_at}\n"
            + "---------------\n"
            + "Пришли мне аудиофайл, и я помогу тебе создать конспект из него.\n"
            + "---------------\n"
            + "Получить токены /tokens\n"
            + "Посмотреть цены /prices\n"
            + "Информация о боте /about\n"
            + "---------------",
        )
