import traceback
import sys
import os


class A:

    def f(self):
        try:
            a = "ketan" + 1
            print(a)
        except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            filename, line_num, func_name, text = traceback.extract_tb(exc_tb)[-1]
            print(func_name)
            print(dir())
            # print(eval(func_name))
            # print(e)
            # print(traceback.print_exc())
            # print(traceback.format_exc())
            # print(traceback.extract_stack())
            # ty, value, d = sys.exc_info()
            # print(ty)
            # print(value)
            # print(traceback.extract_tb(d))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            # print(exc_tb.tb_frame)
            # print(exc_tb.tb_frame.f_code)
            # print(exc_tb.tb_frame.f_code.co_filename)
            # print(exc_tb.tb_frame.f_code.co_name)
            # print(globals())
            # x = eval(exc_tb.tb_frame.f_code.co_name)
            # print(x)
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # print(exc_type, fname, exc_tb.tb_lineno)
            # print(type(e).__name__, __file__, e.__traceback__.tb_lineno)
            # print(.__module__)
            # print(e.__doc__)


a = A()
a.f()
