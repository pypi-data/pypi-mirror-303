from .library import TableControl


class PreviouslySourceCsvTableAnalyzer():
    """前処理"""


    @staticmethod
    def find_end_edge_th(df):
        return TableControl.find_list_size_of_column(df=df, prefix='edge', start_number=1)


    @staticmethod
    def find_end_node_th(df):
        return TableControl.find_list_size_of_column(df=df, prefix='node', start_number=0)


class SourceCsvTableAnalyzer():


    def __init__(self, df, end_edge_th, end_node_th):
        self._df = df
        self._end_edge_th = end_edge_th
        self._end_node_th = end_node_th


    @staticmethod
    def instantiate(df, end_edge_th, end_node_th):
        return SourceCsvTableAnalyzer(df=df, end_edge_th=end_edge_th, end_node_th=end_node_th)


    @property
    def end_edge_th(self):
        return self._end_edge_th


    @property
    def end_node_th(self):
        return self._end_node_th


    def get_column_name_of_last_node(self):
        """最終ノードの列名"""
        return f'node{self._end_node_th - 1}'


    def get_column_th_of_last_node(self):
        """最終ノードの列番号"""
        return TableControl.get_column_location_by_column_name(df=self._df, column_name=self.get_column_name_of_last_node()) + 1
