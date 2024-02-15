import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tabulate import tabulate
from custom_funcs.custom_logger import my_logger


def vizualization(func):
    def inner(*args, **kwargs):
        
        result = func(*args, **kwargs)
        if isinstance(result, list) and result:
            try:
                table_data = [list(item.values()) for item in result]
                headers = [[key for key in item.keys()] for item in result]
                table = tabulate(
                    table_data, headers=headers[0], tablefmt="pretty")

                return my_logger.log(table)
            except Exception as ex:
                my_logger.log(
                    f"while executing query: {ex}", level=40)
                
        elif not result:
            my_logger.log("Returned data are empty!")
        else:
            my_logger.log(
                f"Can`t proceed. The type of returned data are {type(result)}")

    return inner


if __name__ == "__main__":
    my_logger.log("Hi this is custom vizualization function!")
