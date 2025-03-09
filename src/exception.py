import sys
import logging

def error_message_detail(error, error_detail:sys):
    _, _, traceback_error = error_detail.exc_info()
    file_name = traceback_error.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            file_name, traceback_error.tb_lineno, str(error))

    return error_message

#built in Exception class
class CustomException (Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message
    

