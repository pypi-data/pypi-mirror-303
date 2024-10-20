# xltree

エクセルのワークシートの境界線を使って、ツリー構造図を描画します

# 例１：ディレクトリー・パス

Output:  

![View](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__18--1815-XltreeDrive.png)  

👆　わたしのWindows PCのCドライブの例です  

Input case like a table:  

![Data](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__18--1832-XltreeDriveData.png)  

```csv
no,node0,node1,node2,node3,node4,node5,node6,node7,node8
1,C,Users,Muzudho,OneDrive,Documents,Tools,GitHub,,
2,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine,Lesserkai.exe
3,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine,Lesserkai_ja.txt
4,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine,public.bin
5,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,ja,Shogidokoro.resources.dll
6,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Engine.xml,
7,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,GameResult.xml,
8,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Shogidokoro.exe,
9,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,Shogidokoro.xml,
10,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro,お読みください.txt,
11,C,Users,Muzudho,OneDrive,Documents,Tools,Shogidokoro.zip,,
12,C,Users,Muzudho,OneDrive,Documents,Tools,Visual Studio 2022,,
13,C,Users,Muzudho,OneDrive,Documents,Tools,Default.rdp,,
```

👆　さきほどの Output の図は、上図の CSV ファイルを読込ませると描いてくれます。  
`node` 列は 0 から始まる連番で増やすことができます。常識的な長さにしてください  

Input case like a tree:  

![Data](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__20--1052-XltreeDriveData.png)  

```csv
node0,node1,node2,node3,node4,node5,node6,node7,node8
C,Users,Muzudho,OneDrive,Documents,Tools,GitHub,,
,,,,,,Shogidokoro,Engine,Lesserkai.exe
,,,,,,,,Lesserkai_ja.txt
,,,,,,,,public.bin
,,,,,,,ja,Shogidokoro.resources.dll
,,,,,,,Engine.xml,
,,,,,,,GameResult.xml,
,,,,,,,Shogidokoro.exe,
,,,,,,,Shogidokoro.xml,
,,,,,,,お読みください.txt,
,,,,,,Shogidokoro.zip,,
,,,,,,Visual Studio 2022,,
,,,,,,Default.rdp,,
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

![View](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__19--0020-XltreeWordChainGameView.png)  

👆　しりとりというゲームの記録です。図（Diagram）の辺（Edge）にテキストを書くのはオプションです  

Input:  

![Data](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__19--0021-XltreeWordChainGameData.png)  

```csv
no,node0,edge1,node1,edge2,node2,edge3,node3,edge4,node4,edge5,node5,edge6,node6,edge7,node7,edge8,node8,edge9,node9
1,Word Chain Game,Ea,Eagle,E,Euler,R,Rex,$,ended with x,,,,,,,,,,
2,Word Chain Game,Eb,Ebony,Y,Yellow,W,Wood,D,Door,R,Rocket,T,Tax,$,ended with x,,,,
3,Word Chain Game,Ec,Eclair,R,Road,D,Dungeon,N,News,S,Sex,$,ended with x,,,,,,
4,Word Chain Game,Ed,Edelweiss,S,Sox,$,ended with x,,,,,,,,,,,,
7,Word Chain Game,En,English,Ha,Hand,Dog,Dog,G,Gorilla,A,Arm,M,Moon,N,Nice,$,adjective,,
6,Word Chain Game,En,English,Ha,Hand,Doo,Door,R,Ring,G,Grape,E,Egg,G,Golf,F,Fox,$,ended with x
5,Word Chain Game,En,English,Ha,Hand,Dr,Dragon,N,Nob,B,Box,$,ended with x,,,,,,
8,Word Chain Game,En,English,He,Hex,$,ended with x,,,,,,,,,,,,
9,Word Chain Game,En,English,Ho,Hook,Kit,Kitchen,N,Nickel,L,Lemon,N,Nickel,$,time up,,,,
10,Word Chain Game,En,English,Ho,Hook,Kin,King,G,Goal,L,Lemon,N,Nickel,L,Lemon,$,repetition,,
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

![View](https://github.com/muzudho/pyxltree/raw/main/docs_dev/img/202410__pg__19--0311-XltreeSettings.png)  

👆　スタイルも少しだけ設定できます  

Input:  
省略します  

Scripts: 

```py
from xltree import Settings, WorkbookControl


def execute():

    # 各種設定
    settings = Settings(
            # 省略可能
            dictionary = {
                # 列の幅
                #'column_width_of_no':                       4,      # A列の幅。no列
                #'column_width_of_row_header_separator':     3,      # B列の幅。空列
                'column_width_of_node':                     7,      # 例：C, F, I ...列の幅。ノードの箱の幅
                #'column_width_of_parent_side_edge':         2,      # 例：D, G, J ...列の幅。エッジの水平線のうち、親ノードの方
                'column_width_of_child_side_edge':         22,      # 例：E, H, K ...列の幅。エッジの水平線のうち、子ノードの方

                # 行の高さ
                'row_height_of_header':                    13,      # 第１行。ヘッダー
                'row_height_of_column_header_separator':   13,      # 第２行。空行
                'row_height_of_upper_side_of_node':        13,      # ノードの上側のセルの高さ
                'row_height_of_lower_side_of_node':         6,      # ノードの下側のセルの高さ
                'row_height_of_node_spacing':               6,      # ノード間の高さ

                # 背景色関連
                'bgcolor_of_header_1':               'CCCCFF',      # ヘッダーの背景色その１
                'bgcolor_of_header_2':               '333366',      # ヘッダーの背景色その２
                'bgcolor_of_node':                   'EEFFCC',      # 背景色

                # 文字色関連
                'fgcolor_of_header_1':               '111122',      # ヘッダーの文字色その１
                'fgcolor_of_header_2':               'EEEEFF',      # ヘッダーの文字色その２

                # 文字寄せ関連
                'horizontal_alignment_of_node':        'left',      # 文字の水平方向の寄せ。規定値 None。'left', 'fill', 'centerContinuous', 'center', 'right', 'general', 'justify', 'distributed' のいずれか。指定しないなら None
                'vertical_alignment_of_node':            None,      # 文字の垂直方向の寄せ。規定値 None。'bottom', 'center', 'top', 'justify', 'distributed' のいずれか。指定しないなら None
            })

    # 出力先ワークブック指定
    wbc = WorkbookControl(target='./examples/temp/uneven_coin.xlsx', mode='w', settings=settings)

    # ワークシート描画
    wbc.render_worksheet(target='UnevenCoin', based_on='./examples/data/uneven_coin.csv')

    # 何かワークシートを１つ作成したあとで、最初から入っている 'Sheet' を削除
    wbc.remove_worksheet(target='Sheet')

    # 保存
    wbc.save_workbook()
```

👆　Settings オブジェクトを使ってください  

# その他

ソースコードは GitHub で公開しています。GitHub のリポジトリーを確認してください。  
オープンなライセンスで公開しています。変更を加えたフォークも歓迎します。  
