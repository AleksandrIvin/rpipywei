import huaweisms.api.user
import huaweisms.api.wlan
import huaweisms.api.sms
import huaweisms.api.device
import huaweisms.api.monitoring

import logging

logger = logging.getLogger(__name__)


class Router(object):
    def __init__(self, login, password) -> None:
        self.ctx = huaweisms.api.user.quick_login(login, password)

    def reboot(self):
        logger.info("Rebooting...")
        huaweisms.api.device.reboot(self.ctx)

    def get_info(self):
        info = huaweisms.api.device.information(self.ctx)
        logger.debug(info)
        return info

    def get_status(self):
        basic_information = huaweisms.api.monitoring.status(self.ctx)
        logger.debug(basic_information)
        return basic_information

    def get_devices(self):
        # connected devices
        device_list = huaweisms.api.wlan.get_connected_hosts(self.ctx)
        logger.debug(device_list)
        return device_list

    def get_sms(self):
        # connected devices
        sms_list = huaweisms.api.sms.get_sms(self.ctx)
        logger.info(sms_list)
        return sms_list
