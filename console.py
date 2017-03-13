from colorama import init
import datetime
from termcolor import colored

NEW_LINE = "\r\n"


def write_to_log(text):
    with open("server_log.log", "ab") as log:
        log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + text + NEW_LINE)


class Console(object):
    """Console and logger for the server"""
    def __init__(self):
        super(Console, self).__init__()
        init()

    def good(self, text):
        print colored("[+] " + text, "green")
        write_to_log(text)

    def bad(self, text):
        print colored("[-] " + text, "red")
        write_to_log(text)

