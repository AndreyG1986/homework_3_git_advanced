import json
import logging
from pathlib import Path

# Подготовим папку под логи
LOG_DIR = Path("../logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Настройка логирования: пишем и в файл, и в консоль
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_DIR / "utils.log", mode="w", encoding="utf-8"), logging.StreamHandler()],
)

utils_logger = logging.getLogger("app.utils")

PATH_TO_FILE = Path(__file__).parent.parent / "data" / "operations.json"


def get_list_of_transactions(path: Path):
    """Получение списка транзакций из json файла"""
    try:
        with path.open("r", encoding="utf-8-sig") as f:
            data = json.load(f)
        utils_logger.info("Файл %s успешно обработан", path)
        return data
    except FileNotFoundError:
        utils_logger.error("Файл не найден: %s", path)
        print("Файл не найден")
        return []
    except json.JSONDecodeError as e:
        utils_logger.error("Ошибка JSON в %s: %s", path, e)
        print("Запись содержит ошибки")
        return []


if __name__ == "__main__":
    print(get_list_of_transactions(PATH_TO_FILE))
