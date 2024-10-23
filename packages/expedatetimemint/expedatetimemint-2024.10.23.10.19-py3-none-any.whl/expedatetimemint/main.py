import time
import random
from datetime import datetime
from importlib.metadata import version, PackageNotFoundError

# Список эмодзи фруктов и овощей
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
        print(f"{emoji} {current_time} - {package_name} v{pkg_version}")
        time.sleep(1)


if __name__ == "__main__":
    show_time_with_emoji()