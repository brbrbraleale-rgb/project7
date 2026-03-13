import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования работы функции в файл или консоль."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} ok"
                # Сразу логируем успех
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(msg)
                return result
            except Exception as e:
                error_type = type(e).__name__
                msg = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                # Сразу логируем ошибку
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(msg)
                raise e  # Теперь после raise ничего не стоит, и ошибки unreachable не будет
        return wrapper
    return decorator
