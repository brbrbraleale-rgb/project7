import functools

def log(filename=None):
    """Декоратор для логирования работы функции в файл или консоль."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            msg = ""
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} ok"
                return result
            except Exception as e:
                # Имя функции, тип ошибки и входные параметры
                error_type = type(e).__name__
                msg = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                raise e
            finally:
                # Логируем результат или ошибку
                if filename:
                    # Используем encoding="utf-8" для корректной работы с текстом по совету германа
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(msg)
        return wrapper
    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

# Вызов для проверки:
my_function(1, 2)
