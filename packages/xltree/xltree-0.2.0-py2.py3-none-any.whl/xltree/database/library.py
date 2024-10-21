import re


class TableControl():


    @staticmethod
    def get_column_location_by_column_name(df, column_name):
        return df.columns.get_loc(column_name)


    @staticmethod
    def find_list_size_of_column(df, prefix, start_number):
        """'prefix{n}'列を数える。nは0から始まる
        
        列名を左から見ていくと、 node0, node1, node2 といった形で 0から始まる昇順の連番が付いている "node数" 形式の列名が見つかるものとします

        Parameters
        ----------
        df : DataFrame
            データフレーム
        prefix : str
            列名の数字の前の部分。 'node' または 'edge'
        start_number : int
            開始番号。エッジなら 1、ノードなら 0
        """
        expected_node_th = start_number    # 次は 'node{0}' を期待する
        pattern = re.compile(prefix + r'(\d+)')
        for column_name in df.columns.values:
            result = pattern.match(column_name)
            if result:
                node_th = int(result.group(1))
                if expected_node_th == node_th:
                    expected_node_th += 1

        # テーブルにあるノード数
        #print(f"[{datetime.datetime.now()}] Table has {expected_node_th} nodes root node included")

        return expected_node_th     # end 番号に相当
