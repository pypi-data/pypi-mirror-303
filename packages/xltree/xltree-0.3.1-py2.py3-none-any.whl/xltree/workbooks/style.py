import openpyxl as xl
from ..database.library import TableControl


class StyleControl():

    # 行ヘッダーは２列
    NUMBER_OF_COLUMNS_OF_ROW_HEADER = 2

    # ツリー区とプロパティ区を分けるセパレーターは１列
    SEPARATOR = 1

    # １つのノードは３列
    ONE_NODE_COLUMNS = 3


    @staticmethod
    def get_target_column_th(source_table, column_name):
        """書出し先ワークブックでの列番号を返します
        
        例： no, node0, node1, node2
        例： node0, node1, node2
        例： node0, edge1, node1, node2

        no 列、edge{数}列はオプションです

        FIXME: `node0, edge1, foo1, bar1, node1` のように予期しない列が混ざっているケースは？
        """

        # ルートノード
        #column_th_of_source_node_0 = TableControl.get_column_location_by_column_name(df=source_table.df, column_name='node0') + 1

        # 最終ノード
        column_th_of_source_last_node = source_table.analyzer.get_column_th_of_last_node()

        specified_column_location_of_source = TableControl.get_column_location_by_column_name(df=source_table.df, column_name=column_name)

        # 列名から、ノード、エッジ、余り列を見分ける
        # ノード
        result = TableControl.pattern_of_column_name_of_node.match(column_name)
        if result:
            node_th = int(result.group(1))
            return StyleControl.NUMBER_OF_COLUMNS_OF_ROW_HEADER + 1 + node_th * StyleControl.ONE_NODE_COLUMNS

        # エッジ
        result = TableControl.pattern_of_column_name_of_edge.match(column_name)
        if result:
            edge_th = int(result.group(1))
            # FIXME node の前に edge 列があるという前提で大丈夫か？
            return StyleControl.NUMBER_OF_COLUMNS_OF_ROW_HEADER + 1 + edge_th * StyleControl.ONE_NODE_COLUMNS - 1

        # それ以外

        # 書出し先のツリー区の最後
        last_column_th_of_wb = StyleControl.NUMBER_OF_COLUMNS_OF_ROW_HEADER + source_table.analyzer.end_th_of_node * StyleControl.ONE_NODE_COLUMNS

        # プロパティ区
        column_th_of_source_in_property_ward = specified_column_location_of_source - column_th_of_source_last_node -1     # 1 以上になる
        return last_column_th_of_wb + StyleControl.SEPARATOR + column_th_of_source_in_property_ward             # 空列を１つ挟む


    @staticmethod
    def get_number_of_character_of_column(df, column_name):
        """指定の列の文字数を取得"""
        column_th = TableControl.get_column_location_by_column_name(df=df, column_name=column_name) + 1

        column_letter = xl.utils.get_column_letter(column_th)
        series = df[column_name]
        #print(f"{type(series)=}")

        
        if series.dtype == 'int64':
            return int(series.abs().apply("log10").max()) + 1

        # seriesが浮動小数点型なら小数点以下の桁数を返す
        if series.dtype == 'float64':
            return series.abs().astype(str).str.len().max()-1

        # seriesが文字列型なら文字数を返す
        if series.dtype == 'object':
            return series.str.len().max()

        raise ValueError(f'unsupported {series.dtype=}')

