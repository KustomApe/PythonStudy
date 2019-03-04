
"""
## Pythonとは

Pythonは元々、グイド・ヴァンロッサムというオランダ人によって開発された言語です。

“python”という英単語は「ニシキヘビ」という意味ですが、由来は爬虫類のそれではなく、作者が英BBCの「空飛ぶモンティ・パイソン」というコメディ番組のことを大好きだったからだと言われています。ただし、Python言語のアイコン画像はニシキヘビがモチーフです。

なお、現在のPythonは「Pythonソフトウェア財団」という非営利組織によって開発が進められています。

ヴァンロッサム氏が初めてPythonを公開したのが1991年（Python0.9）で、1994年に正式なPythonとしてPython1.0が公開されました。その後、2000年にPython2.0、2008年にPython3.0が公開されて、今に至ります。

2018年5月現在、Pythonはバージョン2のPython2とバージョン3のPython3の両方を入手できるようになっていますが、本カリキュラムでは新しいPython3の方を使って学習を進めてください。Python2と3の間の互換性は高くないため、カリキュラム記載の内容をPython2で実行しても思うように動作しない可能性があります。

## Pythonの特徴

Pythonの特徴について、技術的に深くならないレベルでご紹介します。

インタプリタ方式
C言語をはじめとした一般的なプログラミング言語は コンパイル方式 です。

コンピュータが理解できるのは「機械語」と言われる0と1のみ（2進数）で構成されているプログラムです。しかし、人間は0と1のみでプログラムを作ることは不可能です。そこで、人間がわかる形式の言語で命令を記述してプログラムを作り、それをコンピュータが実行できるように翻訳（コンパイル）する必要があります。

しかしPythonはコンパイルする必要はありません。インタプリタ と呼ばれる実行エンジンを搭載しているので、人間が理解できるPythonの言語で記述されたプログラムをインタプリタが1つずつ解釈していきながら、処理を実行します。コンパイルの手間が省けるので、手軽にプログラミングできます。とはいえ、コンパイルすること自体はPythonでも可能で、作成したコードが非常に長い場合は、コンパイルすると実行速度が速くなるという恩恵を受けられます。

命令が豊富に用意されているので何でも作れる
Pythonは他言語に比べて命令が豊富に用意されています。標準で搭載されている命令の他、世界中の人々が「自身の手で」作った命令を パッケージライブラリ という形で配布しています。特に、理工学や統計解析といった分野で役に立つパッケージライブラリが非常に多く揃っています。

そのため、わたしたちは「自分が何を作りたいか（何をしたいか）」によってパッケージライブラリを入手し、標準の命令と組み合わせることで、比較的難しい処理も自分で実装することができます。

Djangoと呼ばれるツールを導入することでブラウザで動作するWebアプリケーションが作成できたり、統計分析に関するPythonの命令と学問的知識を深めることでデータサイエンティストの道へ進んだりすることもできます。もちろん、本カリキュラムのゴールである機械学習プログラムの作成もPythonが得意とする分野です。
さまざまなOSに対応している
PythonはWindowsやMacなど、さまざまなOSに対応しています。Cloud9のOSであるLinuxでも使えます。それぞれのOSに適したインタプリタが用意されているので、（OSに依存するコードの書き方さえしなければ）Windowsの環境で作ったプログラムをMacでそのまま実行することが可能です。

技術的に深い話を知りたい方は、以下のサイトも参考にしてみてください。

やる気を高めよう - Python3.6ドキュメント

Python - Wikipedia

## Pythonのプログラムを実行する方法

Pythonに処理をしてもらう方法は主に2通りあります。

3.1 REPLを使う
ひとつは REPL と呼ばれるものを使う方法です。REPLは “Read Evaluate Print Loop” の略称で、1行の命令を実行すると、すぐに結果を表示してくれるという便利な機能です。

REPLがどういうものか、Cloud9で利用してみましょう。Cloud9のワークスペースを開いてください。開いたら、下側のターミナル画面のところに python とだけ入力してエンター（リターン）キーを押してください。REPLが起動します。以下のように行頭が「>> >」になっているのが、REPLが起動している状態です。

では、1行だけ命令を記述してみましょう。以下のように「>> >」の後ろにカーソルを置き、print("Hello, world!") と入力したらエンター（リターン）キーを押してください。行末にセミコロン(
) などを記述する必要はありません。

>> > print("Hello, world!")
Hello, world!
>> >
上のように表示されればOKです。これで晴れてPythonの世界に足を踏み入れました。おめでとうございます！

なお、REPLに “Evaluate（評価）”という言葉が入っているとおり、ちょっとした命令の動作を確認するのにREPLは非常に役に立ちますが、複数行の処理を記述して実行するのは、何かと容易ではなく不向きです。次の、Pythonファイルに保存してから実行する方法が一般的です。

REPLを終了する
さて、一旦REPLを使うのを止めるので、以下のように exit() と入力してエンター（リターン）を押すか、ctrl + d(Macの場合は control + d) を押してREPLを終了してください。

>> > exit()
ec2-user: ~/environment $
3.2 Pythonファイルを作って実行する
REPLのときと同じように、Pythonファイルに print("Hello, world!") と書いて実行してみましょう。

まず、Cloud9左側の作業フォルダ画面で、ワークスペース名が書かれたフォルダの中に「test.py」という名前のファイルを新規作成します。

python_file_01.png

test.pyをダブルクリックして中央のエディタ画面で開きます。その中に print("Hello, world!") と記述してください。記述できたら、ファイルを保存しましょう。

python_file_02.png

このPythonプログラムを実行するには、Cloud9下部のターミナルで、以下のようにコマンドを入力し、実行する必要があります。

$ python test.py
このコマンドを実行すると、ターミナルに Hello, world! と表示されます。

python_file_03.png

3.3 Jupyter Notebook
以上の2つの他に、後半のレッスンで紹介する Jupyter Notebook というものを用いると、より手軽にPythonプログラミングを行うことができます。こちらについては、該当のレッスンまで学習が進んでから紹介します。

## まとめ

Python言語について、歴史や特徴を紹介し、REPLの利用やPythonファイルの作成を通じて「はじめてのPythonプログラミング」を体験しました。まだ1行の命令しか実行していません。もっと複雑なプログラムを作りには、数十行、数百行とコードを記述する必要があります。今はまだ難しい話ですが、学習を進める中で徐々にPythonプログラミングができるようになります。頑張って学習を進めましょう！
"""