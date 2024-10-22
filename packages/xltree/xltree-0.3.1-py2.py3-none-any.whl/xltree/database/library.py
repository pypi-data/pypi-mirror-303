import re


class TableControl():


    _pattern_of_column_name_of_node = re.compile(r'node(\d+)')
    _pattern_of_column_name_of_edge = re.compile(r'edge(\d+)')


    @classmethod
    @property
    def pattern_of_column_name_of_node(clazz):
        return clazz._pattern_of_column_name_of_node


    @classmethod
    @property
    def pattern_of_column_name_of_edge(clazz):
        return clazz._pattern_of_column_name_of_edge


    @staticmethod
    def get_column_location_by_column_name(df, column_name):
        return df.columns.get_loc(column_name)


    @staticmethod
    def sort_out_column_names_n_o_node_edge_others(df):
        """列名を edge, node, それ以外の３つに分けます。
        edge と node は最後の要素の数字の +1 を返します。要素がなければ 0 を返します。
        'no' 列は、有るケースと無いケースがあります
        """
        is_n_o_column_exists = False
        edge_th_set = set()
        node_th_set = set()
        others_name_list = []

        # 'no' はインデックスなので、列には含まれない
        for column_name in df.columns.values:
            if column_name == 'no':
                is_n_o_column_exists = True
                continue
            
            result = TableControl.pattern_of_column_name_of_edge.match(column_name)
            if result:
                edge_th_set.add(int(result.group(1)))
                continue

            result = TableControl.pattern_of_column_name_of_node.match(column_name)
            if result:
                node_th_set.add(int(result.group(1)))
                continue
            
            others_name_list.append(column_name)
        
        # node 列は 0 から連番で続いているところまで有効にします
        end_th_of_node = 0
        for i in range(0, len(node_th_set)):
            if i not in node_th_set:
                break

            node_th_set.remove(i)
            end_th_of_node = i + 1

        # 残っている node 列は others リストに入れます
        for node_th in node_th_set:
            others_name_list.append(f'node{node_th}')

        # edge 列は 1 から ［end_th_of_node の手前］まで連番で続いているところだけ有効にします
        end_th_of_edge = 0
        for i in range(1, end_th_of_node):
            if i not in edge_th_set:
                break

            edge_th_set.remove(i)
            end_th_of_edge = i + 1

        # 残っている edge 列は others リストに入れます
        for edge_th in edge_th_set:
            others_name_list.append(f'edge{edge_th}')


        return is_n_o_column_exists, end_th_of_node, end_th_of_edge, others_name_list
