import requests
import os
import logging

from time import sleep
from dotenv import load_dotenv

from router import Router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

load_dotenv()

REQUEST_URLS = os.getenv("REQUEST_URLS", "").split(",")
REQUEST_LIMIT = int(os.getenv("REQUEST_LIMIT", 5))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 30))
REQUEST_SLEEP = int(os.getenv("REQUEST_SLEEP", 120))

USER = str(os.getenv("USER", "admin"))
PASSWORD = str(os.getenv("PASSWORD", "admin"))


def make_request():
    """Performing the request to a ping server"""
    for url in REQUEST_URLS:
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            return True

        except requests.RequestException as e:
            logger.error(f"Request Exception: {e} {url}")

        logger.info(f"Waiting {REQUEST_SLEEP} seconds before the next url trial")
        sleep(REQUEST_SLEEP // 4)

    return False


def reboot_router():
    router = Router(USER, PASSWORD)
    devices = router.get_devices()
    info = router.get_info()
    status = router.get_status()
    sleep(5)
    router.reboot()


def main():
    attempt = 0
    while attempt < REQUEST_LIMIT:
        logger.info(f"Attemption {attempt + 1} of {REQUEST_LIMIT}")
        success = make_request()
        if success:
            logger.info("The connection is alive!")
            break
        attempt += 1
        if attempt < REQUEST_LIMIT:
            logger.info(f"Waiting {REQUEST_SLEEP} seconds before the next trial")
            sleep(REQUEST_SLEEP)

    if attempt == REQUEST_LIMIT:
        reboot_router()


if __name__ == "__main__":
    main()
