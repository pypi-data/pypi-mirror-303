from enum import Enum
import datetime, sys
import os, re

from .colours import bright_magenta, bright_blue, bright_green
from .colours import bright_red, red, bright_yellow, dimmed
from dotenv import load_dotenv

class LogLevel(Enum):
    FATAL      = 0
    ERROR      = 1
    WARN       = 2
    INFO       = 3
    DEBUG      = 4
    SILLY      = 5

class Connectors(Enum):
    SINGLE      = "▪",

class Logger:
    def __init__(self, log_level=LogLevel.DEBUG, log_file=None):
        self.log_level = log_level
        self.log_file = log_file
        self.__check_env()

    def __check_env(self):
        load_dotenv()

        if not os.getenv("LOG_LEVEL"):
            return LogLevel.DEBUG
        
        if os.getenv("LOG_LEVEL").upper() not in LogLevel.__members__:
            return LogLevel.DEBUG

        return LogLevel[os.getenv("LOG_LEVEL").upper()]
    
    def __remove_ansi(self, message: str):
        ansi = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        return ansi.sub('', message)

    def __timestamp(self):
        return dimmed(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"))
    
    def __get_tag(self, level: LogLevel):
        tags = {
            LogLevel.FATAL:     red("fatal:"),
            LogLevel.ERROR:     bright_red("error:"),
            LogLevel.WARN:      bright_yellow("warn:"),
            LogLevel.INFO:      bright_green("info:"),
            LogLevel.DEBUG:     bright_blue("debug:"),
            LogLevel.SILLY:     bright_magenta("silly:")
        }
        return tags.get(level, "info")
    
    def __get_colour(self, level: LogLevel, tag: str):
        colours = {
            LogLevel.FATAL:     red(tag),
            LogLevel.ERROR:     bright_red(tag),
            LogLevel.WARN:      bright_yellow(tag),
            LogLevel.INFO:      bright_green(tag),
            LogLevel.DEBUG:     bright_blue(tag),
            LogLevel.SILLY:     bright_magenta(tag)
        }
        return colours.get(level, bright_green)

    def __write(self, message: str, tag: str, level: LogLevel):
        if level.value <= self.log_level.value:
            level_tag   = f"{self.__get_tag(level):<{15}}"
            domain_tag  = f"[{self.__get_colour(level, tag)}]"
            timestamp   = self.__timestamp()
            connector   = ''.join(Connectors.SINGLE.value)
            message     = self.__get_colour(level, message)
            log_message = f"{timestamp} {level_tag} {connector} {domain_tag} {message}\n"

            if  self.log_file:
                with open(self.log_file, 'a') as f:
                    remove_ansi = self.__remove_ansi(log_message)
                    return f.write(remove_ansi)

            sys.stdout.write(log_message)


    def set_file(self, log_file: str):
        """
        Set the log file to write to

        :param log_file: The file to write to
        :type  log_file: str

        :return: None
        """
        self.log_file = log_file

    def remove_file(self):
        """
        Remove the log file

        :return: None
        """
        self.log_file = None

    def fatal(self, message: str, tag: str):
        """
        Log a fatal message

        :param message: The message to log
        :type  message: str

        :param tag: The tag to associate with the message
        :type  tag: str

        :return: None
        """
        self.__write(message, tag, LogLevel.FATAL)
    
    def error(self, message: str, tag: str):
        """
        Log an error message

        :param message: The message to log
        :type  message: str

        :param tag: The tag to associate with the message
        :type  tag: str

        :return: None
        """
        self.__write(message, tag, LogLevel.ERROR)

    def warn(self, message: str, tag: str):
        """
        Log a warning message

        :param message: The message to log
        :type  message: str

        :param tag: The tag to associate with the message
        :type  tag: str

        :return: None
        """
        self.__write(message, tag, LogLevel.WARN)
    
    def info(self, message: str, tag: str):
        """
        Log an informational message

        :param message: The message to log
        :type  message: str

        :param tag: The tag to associate with the message
        :type  tag: str

        :return: None
        """
        self.__write(message, tag, LogLevel.INFO)

    def debug(self, message: str, tag: str):
        """
        Log a debug message

        :param message: The message to log
        :type  message: str

        :param tag: The tag to associate with the message
        :type  tag: str

        :return: None
        """
        self.__write(message, tag, LogLevel.DEBUG)
    
    def silly(self, message: str, tag: str):
        """
        Log a silly message

        :param message: The message to log
        :type  message: str

        :param tag: The tag to associate with the message
        :type  tag: str

        :return: None
        """
        self.__write(message, tag, LogLevel.SILLY)

    def log(self, message: str, tag: str, level: LogLevel):
        """
        Log a message with a specific log level

        :param message: The message to log
        :type  message: str

        :param tag: The tag to associate with the message
        :type  tag: str

        :param level: The log level to use
        :type  level: LogLevel

        :return: None
        """
        self.__write(message, tag, level)