from .library import TableControl


class SourceCsvTableAnalyzer():


    def __init__(self, df, end_th_of_edge, end_th_of_node):
        self._df = df
        self._end_th_of_edge = end_th_of_edge
        self._end_th_of_node = end_th_of_node


    @staticmethod
    def instantiate(df, end_th_of_edge, end_th_of_node):
        return SourceCsvTableAnalyzer(df=df, end_th_of_edge=end_th_of_edge, end_th_of_node=end_th_of_node)


    @property
    def end_th_of_edge(self):
        return self._end_th_of_edge


    @property
    def end_th_of_node(self):
        return self._end_th_of_node


    def get_column_name_of_last_node(self):
        """最終ノードの列名"""
        return f'node{self._end_th_of_node - 1}'


    def get_column_th_of_last_node(self):
        """最終ノードの列番号"""
        return TableControl.get_column_location_by_column_name(df=self._df, column_name=self.get_column_name_of_last_node()) + 1
