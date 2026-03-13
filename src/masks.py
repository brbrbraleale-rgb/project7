


from src.logger import setup_logger

# Создаем и настраиваем логер (через общую функцию setup_logger)
# Это отдельный файл masks.log, нужный формат, уровень DEBUG и handlers
logger = setup_logger('masks')


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает замаскированный номер."""
    # Проверка входных данных для выполнения требования о логировании ошибок
    if not isinstance(card_number, str) or not card_number.isdigit() or len(card_number) != 16:
        # ЛОГИРОВАНИЕ: Ошибочный случай (уровень ERROR)
        logger.error(f"Ошибка маскировки: некорректный формат карты '{card_number}'")
        return "Некорректный номер карты"

    # ЛОГИРОВАНИЕ: Успешный случай (уровень INFO или DEBUG)
    logger.info(f"Успешно замаскирован номер карты: {card_number[:4]}...{card_number[-4:]}")

    first_block = card_number[0:4]
    two_block = card_number[4:6]
    masked_middle = "** ****"
    last_block = card_number[12:16]

    return f"{first_block} {two_block}{masked_middle} {last_block}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета и возвращает маску **XXXX."""
    # Проверяем входные данные
    if not isinstance(account_number, str) or len(account_number) < 4:
        # ЛОГИРОВАНИЕ: Ошибочный случай (уровень ERROR)
        logger.error(f"Ошибка маскировки: некорректный формат счета '{account_number}'")
        return "Некорректный номер счета"

    # ЛОГИРОВАНИЕ: Успешный случай
    logger.info(f"Успешно замаскирован номер счета: ...{account_number[-4:]}")

    masked_account = "**"
    first_block = account_number[-4:]
    return f"{masked_account} {first_block}"


# Пример запуска для проверки:
if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))
    print(get_mask_card_number("не_число"))  # Это для записи ERROR в логе
