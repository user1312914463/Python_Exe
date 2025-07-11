PythonからEXEコンパイラへ

概要：
PythonからEXEコンパイラは、ユーザがPythonスクリプトを独立した実行可能ファイル（EXE）にコンパイルできる簡単で使いやすいツールです。このツールは、ユーザーがPythonファイル、出力ディレクトリ、アイコンファイルを選択し、コンパイルオプションを設定するのに便利な直感的なグラフィカルユーザーインタフェース（GUI）を提供します。また、ツールの安全性と使用許可を確保するために、鍵検証メカニズムを追加しました。
きのうとくせい
鍵検証：ツールを使用する前に、承認されたユーザーのみが使用できるように、有効な鍵を入力して検証する必要があります。
グラフィカルユーザーインタフェース：直感的なGUIを提供し、ユーザーがファイル選択とコンパイルオプションの設定を容易にする。
コンパイルオプション設定：シングルファイルモード、ウィンドウモード、デバッグモードなどの様々なコンパイルオプションをサポートしています。
設定の保存とロード：ユーザーはコンパイル設定を保存してロードでき、次回の使用に便利です。
リアルタイムログ出力：コンパイル中、コンパイルログをリアルタイム出力し、ユーザーがコンパイルの進行状況を監視するのに便利である。

インストールと依存関係
依存関係:
Python 3.x
PyInstaller：PythonスクリプトをEXEファイルにコンパイルするために使用します。
インストール手順
Python 3.xがインストールされていることを確認し、Python公式サイトからダウンロードしてインストールできます。
PyInstallerのインストール：コマンドライン端末を開き、次のコマンドを実行します。
pip install pyinstaller

プロジェクトコードをローカルにクローンまたはダウンロードします。

使用方法（起動プログラム）：
コマンドライン端末を開き、プロジェクトルートに入ります。
次のコマンド起動プログラムを実行します。
python main.py

鍵の検証：
最初にプログラムを起動すると、キー検証ウィンドウがポップアップ表示されます。
有効な鍵を入力し、「検証」ボタンをクリックして検証します。
検証が成功すると、プログラムは自動的に起動します。検証に失敗すると、残りの試行回数に応じてプロンプトが表示され、エラー回数が制限を超えると鍵ファイルがロックされます。

コンパイル設定：
Pythonファイル：「参照...」ボタンをクリックしてコンパイルするPythonファイルを選択します。
出力ディレクトリ：「参照...」ボタンをクリックしてコンパイルされたEXEファイル出力ディレクトリを選択します。
アイコンファイル（オプション）：「参照...」ボタンをクリックして、EXEファイルに設定するアイコンファイル（拡張子は.ico）を選択します。
コンパイルオプション：
シングルファイルモード：すべての依存関係を1つの個別のEXEファイルにパッケージ化します。
ウィンドウモード（コンソールなし）：コンパイルされたEXEファイルの実行時にコンソールウィンドウは表示されません。
デバッグモード：デバッグモードをオンにして、デバッグコンパイルプロセスを便利にします。
一時ファイルのクリーンアップ：コンパイルが完了したら、一時ファイルをクリーンアップします。
コンソールエンコーディング：コンソール出力のエンコーディングフォーマットを選択します。
設定の保存とロード
設定の保存：「設定の保存」ボタンをクリックして、現在のコンパイル設定をpy _ to _ exe _ config.jsonファイルに保存します。
ロード設定：「ロード設定」ボタンをクリックして、前に保存したコンパイル設定をpy _ to _ exe _ config.jsonファイルからロードします。
コンパイルの開始
コンパイル設定が完了したら、「コンパイルを開始」ボタンをクリックすると、コンパイルプロセスが開始されます。
コンパイル中は、コンパイルログがログ領域にリアルタイムで表示され、プログレスバーにコンパイルの進行状況が表示されます。
コンパイルが完了すると、コンパイル結果を知らせるためのプロンプトボックスが表示されます。

ファイル構造：
plaintext:
exe/
ζ——main.py##プログラムエントリポイント
ζ-key _ verification.py##鍵検証モジュール
ζ——compiler _ gui.py##翻訳インタフェースモジュール
ζ-compilation _ engine.py#コンパイルエンジンモジュール
ζ-config _ manager.py#構成管理モジュール
├── resources/
│-keys.json#キープロファイル
ζ-py _ to _ exe _ config.json#コンパイル設定保存ファイル

！注意事項！
入力された鍵が有効であることを確認してください。そうしないと、ツールが正常に使用されない可能性があります。
Pythonスクリプトの複雑さとシステムパフォーマンスに応じて、コンパイルプロセスには時間がかかる場合があります。
コンパイル中に問題が発生した場合は、ログ出力を確認し、エラー情報に基づいてソートします。
貢献とフィードバック
バグを発見したり、改善提案があったりしたら、QQ：131 2914463を追加してください。同時に、使用体験を共有し、新しい機能のニーズを提案することも歓迎します。