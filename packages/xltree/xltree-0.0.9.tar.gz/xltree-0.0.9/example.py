#
# python example.py 2
#
# 例を実行しよう
#

import traceback
import datetime
import sys

from examples.no_1 import execute as execute_no_1
from examples.no_2 import execute as execute_no_2
from examples.no_3 import execute as execute_no_3


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    """コマンドから実行時"""

    try:
        args = sys.argv

        if 1 < len(args):
            if args[1] == '1':
                execute_no_1()

            elif args[1] == '2':
                execute_no_2()

            elif args[1] == '3':
                execute_no_3()

            else:
                raise ValueError(f'unsupported {args[1]=}')
        
        else:
            raise ValueError(f'unsupported {len(args)=}')


    except Exception as err:
        print(f"""\
[{datetime.datetime.now()}] おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
