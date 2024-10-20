from typing import Optional


class BaseProjectUtilsException(Exception):
    __summary: str
    __trace_file: str
    __trace_line: int
    __detail: str

    def __init__(self, summary: str, trace_file: str, trace_line: int, detail: Optional[str] = None):
        self.__summary = summary
        self.__trace_file = trace_file
        self.__trace_line = trace_line
        self.__detail = detail

    def __str__(self):
        return f"""
            Error Summary :{self.__summary}
            Error File    :{self.__trace_file}
            Error Line    :{self.__trace_line}
            Error Detail  :
            {self.__detail}
        """
