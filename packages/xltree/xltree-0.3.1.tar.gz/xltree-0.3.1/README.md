# xltree

エクセルのワークシートの境界線を使って、ツリー構造図を描画します

# 例１：ディレクトリー・パス

Output:  

![View](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__22--0026-XltreeDrive.png)  

👆　わたしのWindows PCのCドライブの例です  
（`xltree>=0.0.10` から） ツリー部分より右側の列、つまり上図でいうと last_modified 列以降も出力します  
（`xltree>=0.3.1` から） セル結合するかしないか選べます  

Input case like a table:  

![Data](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__20--1630-XltreeDriveTableData.png)  

```csv
no,node0,node1,node2,node3,node4,node5,node6,node7,node8,last_modified,size,comment
1,C,Users,Muzudho,OneDrive,Documents,GitHub,,,,2024/10/18 12:31,,
2,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine,Lesserkai.exe,2022/03/07 21:03,266 KB,
3,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine,Lesserkai_ja.txt,2012/12/05 22:37,1 KB,
4,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine,public.bin,2002/05/11 22:12,"5,213 KB",
5,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,ja,Shogidokoro.resources.dll,2024/05/11 20:43,257 KB,
6,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine.xml,,2024/09/13 20:20,4 KB,
7,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,GameResult.xml,,2024/09/13 20:20,"2,357 KB",
8,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Shogidokoro.exe,,2024/05/11 20:43,"4,902 KB",version 5.4.1
9,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Shogidokoro.xml,,2024/09/13 20:20,8 KB,
10,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,お読みください.txt,,2024/05/11 15:24,49 KB,
11,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro.zip,,,2024/04/27 20:23,3.104 KB,
12,C,Users,Muzudho,OneDrive,Documents,Visual Studio 2022,,,,2024/07/22 13:47,,
13,C,Users,Muzudho,OneDrive,Documents,Default.rdp,,,,2023/09/23 14:05,,
```

👆　さきほどの Output の図は、上図の CSV ファイルを読込ませると描いてくれます。  
`node` 列は 0 から始まる連番で増やすことができます。常識的な長さにしてください  

Input case like a tree:  

![Data](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__20--1633-XltreeDriveTreeData.png)  

```csv
node0,node1,node2,node3,node4,node5,node6,node7,node8,last_modified,size,comment
C,Users,Muzudho,OneDrive,Documents,GitHub,,,,2024/10/18 12:31,,
,,,,,Tools,Shogidokoro,Engine,Lesserkai.exe,2022/03/07 21:03,266 KB,
,,,,,,,,Lesserkai_ja.txt,2012/12/05 22:37,1 KB,
,,,,,,,,public.bin,2002/05/11 22:12,"5,213 KB",
,,,,,,,ja,Shogidokoro.resources.dll,2024/05/11 20:43,257 KB,
,,,,,,,Engine.xml,,2024/09/13 20:20,4 KB,
,,,,,,,GameResult.xml,,2024/09/13 20:20,"2,357 KB",
,,,,,,,Shogidokoro.exe,,2024/05/11 20:43,"4,902 KB",version 5.4.1
,,,,,,,Shogidokoro.xml,,2024/09/13 20:20,8 KB,
,,,,,,,お読みください.txt,,2024/05/11 15:24,49 KB,
,,,,,,Shogidokoro.zip,,,2024/04/27 20:23,3.104 KB,
,,,,,Visual Studio 2022,,,,2024/07/22 13:47,,
,,,,,Default.rdp,,,,2023/09/23 14:05,,
```

👆  さきほどの CSV と同じワークブック（.xlsx）を出力できる CSV です。  
（`xltree>=0.0.10` から） no 列は省くことができます。また、中間ノードが空欄になっている箇所は、前行と同じとみなします  

Script:  

```py
from xltree import WorkbookControl


def execute():

    # 出力先ワークブック指定
    wbc = WorkbookControl(target='./tests/temp/tree_drive.xlsx', mode='w')

    # ワークシート描画
    wbc.render_worksheet(target='Drive', based_on='./examples/data/drive_by_table.csv')

    # 何かワークシートを１つ作成したあとで、最初から入っている 'Sheet' を削除
    wbc.remove_worksheet(target='Sheet')

    # 保存
    wbc.save_workbook()
```

👆　上記はスクリプトの記述例です  

# 例２：しりとり

Output:  

![View](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__22--0034-XltreeWordChainGame.png)  

👆　しりとりというゲームの記録です。図（Diagram）の辺（Edge）にテキストを書くのはオプションです  

Input:  

![Data](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__22--0039-XltreeWordChainGameData.png)  

```csv
no,node0,edge1,node1,edge2,node2,edge3,node3,edge4,node4,edge5,node5,edge6,node6,edge7,node7,edge8,node8,result
1,Word Chain Game,Ea,Eagle,E,Euler,R,Rex,,,,,,,,,,,ended with x
2,Word Chain Game,Eb,Ebony,Y,Yellow,W,Wood,D,Door,R,Rocket,T,Tax,,,,,ended with x
3,Word Chain Game,Ec,Eclair,R,Road,D,Dungeon,N,News,S,Sex,,,,,,,ended with x
4,Word Chain Game,Ed,Edelweiss,S,Sox,,,,,,,,,,,,,ended with x
7,Word Chain Game,En,English,Ha,Hand,Dog,Dog,G,Gorilla,A,Arm,M,Moon,N,Nice,,,adjective
6,Word Chain Game,En,English,Ha,Hand,Doo,Door,R,Ring,G,Grape,E,Egg,G,Golf,F,Fox,ended with x
5,Word Chain Game,En,English,Ha,Hand,Dr,Dragon,N,Nob,B,Box,,,,,,,ended with x
8,Word Chain Game,En,English,He,Hex,,,,,,,,,,,,,ended with x
9,Word Chain Game,En,English,Ho,Hook,Kit,Kitchen,N,Nickel,L,Lemon,N,Nickel,,,,,time up
10,Word Chain Game,En,English,Ho,Hook,Kin,King,G,Goal,L,Lemon,N,Nickel,L,Lemon,,,repetition
```

👆　`edge` 列は 1 から始まる連番で増やすことができます。 `node` 列より深い番号を付けても無視されます  

Script:  

```py
from xltree import WorkbookControl


def execute():

    # 出力先ワークブック指定
    wbc = WorkbookControl(target='./examples/temp/word_chain_game.xlsx', mode='w')

    # ワークシート描画
    wbc.render_worksheet(target='Drive', based_on='./examples/data/word_chain_game.csv')

    # 何かワークシートを１つ作成したあとで、最初から入っている 'Sheet' を削除
    wbc.remove_worksheet(target='Sheet')

    # 保存
    wbc.save_workbook()
```

# 例３：偏ったコインを投げて表と裏が出る確率

Output:  

![View](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__22--0035-XltreeUnevenCoin.png)  

👆　スタイルも少しだけ設定できます  

Input:  
省略します  

Scripts: 

```py
from xltree import WorkbookControl


def execute():

    # 各種設定
    settings = {
        # 列の幅
        #'column_width_of_no':                       4,      # A列の幅。no列
        #'column_width_of_root_side_padding':        3,      # B列の幅。ツリー構造図の根側パディング
        #'column_width_of_leaf_side_padding':        3,      # ツリー構造図の葉側パディング
        'column_width_of_node':                     7,      # 例：C, F, I ...列の幅。ノードの箱の幅
        #'column_width_of_parent_side_edge':         2,      # 例：D, G, J ...列の幅。エッジの水平線のうち、親ノードの方
        'column_width_of_child_side_edge':         22,      # 例：E, H, K ...列の幅。エッジの水平線のうち、子ノードの方

        # 行の高さ
        'row_height_of_header':                    13,      # 第１行。ヘッダー
        'row_height_of_lower_side_padding':        13,      # 第２行。ツリー構造図の軸の番号が小さい側パティング
        'row_height_of_upper_side_of_node':        13,      # ノードの上側のセルの高さ
        'row_height_of_lower_side_of_node':         6,      # ノードの下側のセルの高さ
        'row_height_of_node_spacing':               6,      # ノード間の高さ

        # 背景色関連
        'bgcolor_of_tree':                   'FFFFFF',      # ツリー構造図の背景
        'bgcolor_of_header_1':               'CCCCFF',      # ヘッダーの背景色その１
        'bgcolor_of_header_2':               '333366',      # ヘッダーの背景色その２
        'bgcolor_of_node':                   'EEFFCC',      # 背景色

        # 文字色関連
        'fgcolor_of_header_1':               '111122',      # ヘッダーの文字色その１
        'fgcolor_of_header_2':               'EEEEFF',      # ヘッダーの文字色その２

        # 文字寄せ関連
        'horizontal_alignment_of_node':        'left',      # 文字の水平方向の寄せ。規定値 None。'left', 'fill', 'centerContinuous', 'center', 'right', 'general', 'justify', 'distributed' のいずれか。指定しないなら None
        'vertical_alignment_of_node':            None,      # 文字の垂直方向の寄せ。規定値 None。'bottom', 'center', 'top', 'justify', 'distributed' のいずれか。指定しないなら None

        # その他の操作
        'do_not_merge_cells':                   False,      # セル結合しないなら真
    }

    # 出力先ワークブック指定
    wbc = WorkbookControl(target='./examples/temp/uneven_coin.xlsx', mode='w', settings=settings)

    # ワークシート描画
    wbc.render_worksheet(target='UnevenCoin', based_on='./examples/data/uneven_coin.csv')

    # 何かワークシートを１つ作成したあとで、最初から入っている 'Sheet' を削除
    wbc.remove_worksheet(target='Sheet')

    # 保存
    wbc.save_workbook()
```

👆　Settings オブジェクトを使ってください。  
（`xltree>=0.1.0` から） settings は Dictionary 型になりました  
（`xltree>=0.2.0` から） `column_width_of_row_header_separator` は `column_width_of_root_side_padding` に名称変更しました
（`xltree>=0.3.0` から） `row_height_of_column_header_separator` は `row_height_of_lower_side_padding` に名称変更しました

# その他

ソースコードは GitHub で公開しています。GitHub のリポジトリーを確認してください。  
オープンなライセンスで公開しています。変更を加えたフォークも歓迎します。  
