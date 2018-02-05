# coding: utf-8

import os
import struct
from sys import platform

from selenium import webdriver

from base.logs.log import Log4Kissenium


class Platform:

    @staticmethod
    def get_os():
        if platform == "linux" or platform == "linux32":
            current_platform = "linux"
        elif platform == "darwin":
            current_platform = "mac"
        elif platform == "win32":
            current_platform = "win"
        return current_platform

    @staticmethod
    def get_arch():
        if struct.calcsize('P') * 8 == 64:
            arch = "amd64"
        else:
            arch = "i386"
        return arch

    @staticmethod
    def get_webdriver(browser):
        # TODO Finish this function
        logger = Log4Kissenium.get_logger("Kissenium")
        os_name = Platform.get_os()
        os_arch = Platform.get_arch()

        logger.debug("Os type is %s and architecture is %s", os_name, os_arch)

        if browser == "Chrome":
            chromedriver = "%s/resources/webdriver/chrome/%s/%s/chromedriver" \
                           % (os.getcwd(), os_name, os_arch)
            os.environ["webdriver.chrome.driver"] = chromedriver
            return webdriver.Chrome(chromedriver)
        elif browser == "Firefox":
            geckodriver = "%s/resources/webdriver/firefox/%s/%s/geckodriver" \
                          % (os.getcwd(), os_name, os_arch)
            logger.debug(geckodriver)
            return webdriver.Firefox(log_path='reports/Kissenium/geckodriver.log',
                                     executable_path=geckodriver)
        else:
            raise ValueError('Unrecognized browser specified in configuration')
