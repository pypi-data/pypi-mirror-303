import datetime
import pandas as pd
from .library import TableControl


class ColumnsSorting():
    """列ソート、及びその途中の計算結果"""


    def __init__(self):
        # 計算途中結果
        self._is_n_o_column_exists = None
        self._end_th_of_node = None
        self._end_th_of_edge = None


    @property
    def end_th_of_node(self):
        """node0 から連続する最後の node{i} の i を +1 したもの。なければ 0"""
        return self._end_th_of_node


    @property
    def end_th_of_edge(self):
        """edge1 から ［edge{end_th_of_node} の手前］まで連続する最後の edge{i} の i を +1 したもの。なければ 0"""
        return self._end_th_of_edge


    def execute(self, df):
        """実行

        列名をソートする。no,node0,edge1,node1,edge2,node2,remaining_a,remaining_b,... のような感じに

        'no' 列は、（まだインデックスに指定されていないものとし）有るケースと、無いケースがあります。有れば先頭へ、無ければ無視することにします
        """

        self._is_n_o_column_exists, self._end_th_of_node, self._end_th_of_edge, others_name_list = TableControl.sort_out_column_names_n_o_node_edge_others(df)

        column_name_list = []

        # 'no' 列を含むなら先頭へ
        if self._is_n_o_column_exists:
            column_name_list.append('no')

        if self._end_th_of_node < 1:
            raise ValueError(f'node0 列がありませんでした  {self._end_th_of_edge=}  {self._end_th_of_node=}  {others_name_list=}')
        
        # node0 列を追加
        column_name_list.append('node0')

        for i in range(1, self._end_th_of_node):

            # あれば edge{i} 列を追加
            if i < self._end_th_of_edge:
                column_name_list.append(f'edge{i}')

            # node{i} 列を追加
            column_name_list.append(f'node{i}')

        # 残りの列名を追加
        column_name_list.extend(others_name_list)

        return df[column_name_list]


class InputCompletion():
    """入力補完"""


    @staticmethod
    def fill_directory(df, end_th_of_node, debug_write=False):
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

        last_node_th = end_th_of_node - 1

        if debug_write:
            print(f"[{datetime.datetime.now()}] このテーブルは{end_th_of_node}個のノードがある。最終ノードは {last_node_th}")

        row_size = len(df)

        # ２行目から、１行ずつ行う
        for row_th in range(2, row_size + 1):

            # この行について、最終ノード列を調べる
            actual_last_node_th = last_node_th   # 最終ノードから開始
            for node_th in reversed(range(0, end_th_of_node)):
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
