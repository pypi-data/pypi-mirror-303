from functools import update_wrapper
from time import perf_counter
from typing import Callable, Tuple, Any, Dict, Union

from TimerLib import logger


class TimerSync:
    """Класс таймер для измерения работы синхронных функций."""

    def __init__(self, func: Callable) -> None:
        """
        Метод инициализации аттрибутов экземпляра класса.

        :param func: Вызываемая функция
        """
        self.func: Callable = func
        update_wrapper(wrapper=self, wrapped=func)

    def __call__(self, *args: Tuple[Any], **kwargs: Dict[Union[tuple, Union[str, int]], Any]) -> Any:
        """
        Метод для вызова экземпляра класса.

        :param args: Кортеж с позиционными параметрами
        :param kwargs: Кортеж с именованными параметрами
        :return: Результат работы вызываемой функции
        """
        start_time = perf_counter()
        result = self.func(*args, **kwargs)
        logger.debug(f"Время выполнения функции {self.func.__name__} -> {perf_counter() - start_time:.10f}")
        return result
