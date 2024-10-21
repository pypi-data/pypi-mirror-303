import datetime
import pandas as pd


class InputCompletion():
    """入力補完"""


    @staticmethod
    def fill_directory(df, end_node_th, debug_write=False):
        """ディレクトリーの空欄を埋めます
        
        Before:
            a,b,c,d,e,f,g,h,i
                ,j,k,l, ,m,n,o
                , ,p,      q
        
        After:
            a,b,c,d,e,f,g,h,i
            a,j,k,l,e,m,n,o
            a,j,p,l,e,m,n
        """

        last_node_th = end_node_th - 1

        if debug_write:
            print(f"[{datetime.datetime.now()}] このテーブルは{end_node_th}個のノードがある。最終ノードは {last_node_th}")

        row_size = len(df)

        # ２行目から、１行ずつ行う
        for row_th in range(2, row_size + 1):

            # この行について、最終ノード列を調べる
            actual_last_node_th = last_node_th   # 最終ノードから開始
            for node_th in reversed(range(0, end_node_th)):
                column_name = f'node{node_th}'

                # 縮めていく
                actual_last_node_th = node_th

                if not pd.isnull(df.at[row_th, column_name]):
                    break


            if debug_write:
                print(f"[{datetime.datetime.now()}] 第{row_th}行は第{actual_last_node_th}ノードまで")

            # この行について、最終ノード列まで、ノードの空欄は上行をコピーする
            for node_th in range(0, actual_last_node_th + 1):

                column_name = f'node{node_th}'

                if pd.isnull(df.at[row_th, column_name]):
                    df.at[row_th, column_name] = df.at[row_th - 1, column_name]
