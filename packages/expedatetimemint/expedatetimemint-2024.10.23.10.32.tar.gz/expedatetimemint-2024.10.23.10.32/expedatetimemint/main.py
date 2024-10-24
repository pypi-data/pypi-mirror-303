import time
import random
from datetime import datetime
from importlib.metadata import version, PackageNotFoundError
import logging

# Set up basic configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

emojis = [
    '🍎', '🍌', '🍇', '🍉', '🍓', '🥑', '🍍', '🍑', '🥕', '🍆', '🍒', '🍋',
    '🍅', '🥒', '🍏', '🍊', '🍈', '🥥', '🥝', '🍐', '🍠', '🥭', '🍋', '🥦',
    '🫒', '🧄', '🧅',
]

package_name = "expedatetimemint"


def show_time_with_emoji():
    try:
        pkg_version = version(package_name)
    except PackageNotFoundError:
        pkg_version = "unknown version"

    while True:
        emoji = random.choice(emojis)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{emoji} {current_time} - {package_name} version: {pkg_version}")
        time.sleep(1)


def main():
    logging.info('🚀 Started main(): ')
    show_time_with_emoji()


if __name__ == "__main__":
    main()