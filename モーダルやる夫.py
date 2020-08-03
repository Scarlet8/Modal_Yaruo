#下準備
import pandas as pd
import os,sys,tkinter,tkinter.filedialog,tkinter.messagebox
from time import sleep

pre_num = (input('\n'*4 + 'やりたい作業の番号を選んでください(半角数字)\n\n\
[1]：血統コラムからモーダルを作成\n\n\
[2]：馬体診断コラムからモーダルを作成\n\n\
[3]：馬三郎ファイルからトレセンリポートコラムとモーダルを作成\n\n\
[4]：トレセンリポートコラムからモーダルを作成' \
+ '\n\n' + '入力してください→：' ))

try:
    info_num = int(pre_num)

except ValueError: #数字以外のエラー処理
    print('\n'*4 + '＜＜警告＞＞有効な半角数字を入力してください！' + '\n'*4 )
    pre_num = (input('やりたい作業の番号を選んでください(半角数字)\n\n\
    [1]：血統コラムからモーダルを作成\n\n\
    [2]：馬体診断コラムからモーダルを作成\n\n\
    [3]：馬三郎ファイルからトレセンリポートコラムとモーダルを作成\n\n\
    [4]：トレセンリポートコラムからモーダルを作成' \
    + '\n\n' + '入力してください→：' ))
    try:
        info_num = int(pre_num)
    except ValueError:
        print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
        sleep(1)
        sys.exit(1)

if info_num > 4 : #5以上のエラー処理
    print('\n'*4 + '＜＜警告＞＞1から4までの半角数字を入力してください！' + '\n'*4 )
    info_num = int(input('やりたい作業の番号を選んでください(半角数字)\n\n\
    [1]：血統コラムからモーダルを作成\n\n\
    [2]：馬体診断コラムからモーダルを作成\n\n\
    [3]：馬三郎ファイルからトレセンリポートコラムとモーダルを作成\n\n\
    [4]：トレセンリポートコラムからモーダルを作成' \
    + '\n\n' + '入力してください→：' ))
    if info_num > 4:
        print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
        sleep(1)
        sys.exit(1)
    elif ValueError:
        print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
        sleep(1)
        sys.exit(1)

elif info_num < 1: #1未満のエラー処理
    print('\n'*4 + '＜＜警告＞＞1から3までの半角数字を入力してください！' + '\n'*4 )
    info_num = int(input('やりたい作業の番号を選んでください(半角数字)\n\n\
    [1]：血統コラムからモーダルを作成\n\n\
    [2]：馬体診断コラムからモーダルを作成\n\n\
    [3]：馬三郎ファイルからトレセンリポートコラムとモーダルを作成\n\n\
    [4]：トレセンリポートコラムからモーダルを作成' \
    + '\n\n' + '入力してください→：' ))
    if info_num < 1:
        print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
        sleep(1)
        sys.exit(1)
    elif ValueError:
        print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
        sleep(1)
        sys.exit(1)

if info_num == 2: #馬体診断の分岐処理
    batai_num = (input('\n'*4 + '馬体診断した人の番号を選んでください(半角数字)\n\n\
    [1]：吉田順一\n\n\
    [2]：加藤剛史\n\n\
    [3]：細江純子\n\n\
    [4]：池江泰郎\n\n\
    [5]：小島太\n\n\
    [6]：坂口正大\n\n\
    [7]：佐藤哲三\n\n'\
    + '\n\n' + '入力してください→：' ))

    try:
        batai_num = int(batai_num)

    except ValueError: #数字以外のエラー処理
        print('\n'*4 + '＜＜警告＞＞有効な半角数字を入力してください！' + '\n'*4 )
        batai_num = (input( '馬体診断した人の番号を選んでください(半角数字)\n\n\
    [1]：細江純子\n\n\
    [2]：加藤剛史\n\n\
    [3]：吉田順一\n\n\
    [4]：池江泰郎\n\n\
    [5]：小島太\n\n\
    [6]：坂口正大\n\n\
    [7]：佐藤哲三\n\n'\
    + '\n\n' + '今度こそ正しく入力してください→：' ))

        try:
            batai_num = int(batai_num)
        except ValueError:
            print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
            sleep(1)
            sys.exit(1)

    if batai_num > 7 : #8以上のエラー処理
        print('\n'*4 + '＜＜警告＞＞1から7までの半角数字を入力してください！' + '\n'*4 )
        try:
            batai_num = int(input('馬体診断した人の番号を選んでください(半角数字)\n\n\
    [1]：吉田順一\n\n\
    [2]：加藤剛史\n\n\
    [3]：細江純子\n\n\
    [4]：池江泰郎\n\n\
    [5]：小島太\n\n\
    [6]：坂口正大\n\n\
    [7]：佐藤哲三\n\n'\
     + '\n'*4 + '今度こそ正しく入力してください→：'))
        except ValueError:
            print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
            sleep(1)
            sys.exit(1)
        if batai_num > 7:
            print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
            sleep(1)
            sys.exit(1)

    elif batai_num < 1: #1未満のエラー処理
        print('\n'*4 + '＜＜警告＞＞1から7までの半角数字を入力してください！' + '\n'*4 )
        try:
            batai_num = int(input('馬体診断した人の番号を選んでください(半角数字)\n\n\
    [1]：吉田順一\n\n\
    [2]：加藤剛史\n\n\
    [3]：細江純子\n\n\
    [4]：池江泰郎\n\n\
    [5]：小島太\n\n\
    [6]：坂口正大\n\n\
    [7]：佐藤哲三\n\n'\
    + '\n'*4 + '今度こそ正しく入力してください→：'))
        except ValueError:
            print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
            sleep(1)
            sys.exit(1)
        if batai_num < 1:
            print('\n'*4 + '最初からやり直してください\n\nアプリを終了します' + '\n'*4 )
            sleep(1)
            sys.exit(1)

author = ['0','吉田','加藤','細江','池江','小島','坂口','佐藤']

#TARGETから出力したCSVを読み込む
root = tkinter.Tk()
cd = os.getcwd()
root.withdraw()
tkinter.messagebox.showinfo('モーダルやる夫','TARGETから出力したCSVファイルを選択してください！\n★★★ファイル名がレース名.csvになってないとダメです★★★')
ret1 = tkinter.filedialog.askopenfilename(title = 'TARGETから出力したCSVファイルを選ぶ', initialdir = cd , multiple = False )
if ret1 == "": #キャンセル押したときに終了
    sleep(1)
    sys.exit(1)

try: #デコード処理
    df1 = pd.read_csv( ret1 , sep = ',', encoding = 'utf-8', names = \
    ['レースID','馬ID','馬名','性別','年齢','所属','調教師名','父','母','母父','前走レース名','前走人気','前走着順'] , dtype = object )

except UnicodeDecodeError:
    df1 = pd.read_csv( ret1 , sep = ',', encoding = 'cp932', names = \
    ['レースID','馬ID','馬名','性別','年齢','所属','調教師名','父','母','母父','前走レース名','前走人気','前走着順'] , dtype = object )

except UnicodeDecodeError:
    df1 = pd.read_csv( ret1 , sep = ',', encoding = 'shift-jis', names = \
    ['レースID','馬ID','馬名','性別','年齢','所属','調教師名','父','母','母父','前走レース名','前走人気','前走着順'] , dtype = object )


#ヤマザキ春の置換祭り
#重賞レース名
df1['前走レース名'] = df1['前走レース名'].str.replace('シルクロード','シルクロードS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ダイヤモンド','ダイヤモンドS')
df1['前走レース名'] = df1['前走レース名'].str.replace('フェブラリー','フェブラリーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('クイーンカッ','クイーンC')
df1['前走レース名'] = df1['前走レース名'].str.replace('チューリップ','チューリップ賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('フィリーズレ','フィリーズR')
df1['前走レース名'] = df1['前走レース名'].str.replace('フラワーカッ','フラワーC')
df1['前走レース名'] = df1['前走レース名'].str.replace('ダービー卿チ','ダービー卿CT')
df1['前走レース名'] = df1['前走レース名'].str.replace('ニュージーラ','ニュージーランドT')
df1['前走レース名'] = df1['前走レース名'].str.replace('アーリントン','アーリントンC')
df1['前走レース名'] = df1['前走レース名'].str.replace('ＮＨＫマイル','NHKマイルC')
df1['前走レース名'] = df1['前走レース名'].str.replace('京王杯ス','京王杯SC')
df1['前走レース名'] = df1['前走レース名'].str.replace('ヴィクトリア','ヴィクトリアマイル')
df1['前走レース名'] = df1['前走レース名'].str.replace('エプソムカッ','エプソムC')
df1['前走レース名'] = df1['前走レース名'].str.replace('函館スプリン','函館スプリントS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ラジオNIKKEI','ラジオNIKKEI賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('アイビスサマ','アイビスSD')
df1['前走レース名'] = df1['前走レース名'].str.replace('キーンランド','キーンランドC')
df1['前走レース名'] = df1['前走レース名'].str.replace('オータムH','京成杯AH')
df1['前走レース名'] = df1['前走レース名'].str.replace('セントライト','セントライト記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('スプリンター','スプリンターズS')
df1['前走レース名'] = df1['前走レース名'].str.replace('サウジアラビ','サウジアラビアRC')
df1['前走レース名'] = df1['前走レース名'].str.replace('アイルランド','府中牝馬S')
df1['前走レース名'] = df1['前走レース名'].str.replace('ファンタジー','ファンタジーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('アルゼンチン','アルゼンチン共和国杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('デイリー杯２','デイリー杯2歳S')
df1['前走レース名'] = df1['前走レース名'].str.replace('エリザベス女','エリザベス女王杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('東京スポーツ','東スポ杯2歳S')
df1['前走レース名'] = df1['前走レース名'].str.replace('マイルチャン','マイルCS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ステイヤーズ','ステイヤーズS')
df1['前走レース名'] = df1['前走レース名'].str.replace('チャレンジカ','チャレンジC')
df1['前走レース名'] = df1['前走レース名'].str.replace('チャンピオン','チャンピオンズC')
df1['前走レース名'] = df1['前走レース名'].str.replace('阪神ジュベナ','阪神JF')
df1['前走レース名'] = df1['前走レース名'].str.replace('フューチュリ','朝日杯FS')

#古馬2勝クラス、3勝クラス特別レース名
df1['前走レース名'] = df1['前走レース名'].str.replace('ベストウィッ','ベストウィッシュC')
df1['前走レース名'] = df1['前走レース名'].str.replace('ヤングジョッ','YJSF')
df1['前走レース名'] = df1['前走レース名'].str.replace('ベテルギウス','ベテルギウスS')
df1['前走レース名'] = df1['前走レース名'].str.replace('フォーチュン','フォーチュンC')
df1['前走レース名'] = df1['前走レース名'].str.replace('クリスマスカ','クリスマスC')
df1['前走レース名'] = df1['前走レース名'].str.replace('フェアウェル','フェアウェルS')
df1['前走レース名'] = df1['前走レース名'].str.replace('グッドラック','グッドラックH')
df1['前走レース名'] = df1['前走レース名'].str.replace('ギャラクシー','ギャラクシーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('サンタクロー','サンタクロースS')
df1['前走レース名'] = df1['前走レース名'].str.replace('グレイトフル','グレイトフルS')
df1['前走レース名'] = df1['前走レース名'].str.replace('クリスマスキ','クリスマスキャロル賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('ディセンバー','ディセンバーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('タンザナイト','タンザナイトS')
df1['前走レース名'] = df1['前走レース名'].str.replace('アクアライン','アクアラインS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ラピスラズリ','ラピスラズリS')
df1['前走レース名'] = df1['前走レース名'].str.replace('名古屋日刊ス','名古屋日刊スポーツ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('シャングリラ','シャングリラ賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('オリエンタル','オリエンタル賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('福島民友カッ','福島民友C')
df1['前走レース名'] = df1['前走レース名'].str.replace('オータムリー','オータムリーフS')
df1['前走レース名'] = df1['前走レース名'].str.replace('フルーツライ','フルーツラインC')
df1['前走レース名'] = df1['前走レース名'].str.replace('アンドロメダ','アンドロメダS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ドンカスター','ドンカスターC')
df1['前走レース名'] = df1['前走レース名'].str.replace('ルミエールオ','ルミエールAD')
df1['前走レース名'] = df1['前走レース名'].str.replace('オクトーバー','オクトーバーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ブラジルカッ','ブラジルC')
df1['前走レース名'] = df1['前走レース名'].str.replace('ポートアイラ','ポートアイランドS')
df1['前走レース名'] = df1['前走レース名'].str.replace('グリーンチャ','グリーンチャンネルC')
df1['前走レース名'] = df1['前走レース名'].str.replace('セプテンバー','セプテンバーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('大阪スポーツ','大阪スポーツ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('オークランド','オークランドRCT')
df1['前走レース名'] = df1['前走レース名'].str.replace('ムーンライト','ムーンライトH')
df1['前走レース名'] = df1['前走レース名'].str.replace('札幌スポニチ','札幌スポニチ賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('西日本スポー','西日本スポーツ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('北九州短距離','北九州短距離S')
df1['前走レース名'] = df1['前走レース名'].str.replace('小倉日経オー','小倉日経OP')
df1['前走レース名'] = df1['前走レース名'].str.replace('西部スポニチ','西部スポニチ賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('西部日刊スポ','西部日刊スポーツ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('札幌日経オー','札幌日経OP')
df1['前走レース名'] = df1['前走レース名'].str.replace('札幌日刊スポ','札幌日刊スポーツ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('九州スポーツ','九州スポーツ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('福島テレビオ','福島テレビOP')
df1['前走レース名'] = df1['前走レース名'].str.replace('函館日刊スポ','函館日刊スポーツ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('バーデンバー','バーデンバーデンC')
df1['前走レース名'] = df1['前走レース名'].str.replace('シンガポール','シンガポールTC賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('マレーシアカ','マレーシアC')
df1['前走レース名'] = df1['前走レース名'].str.replace('さくらんぼ特','さくらんぼ特別')
df1['前走レース名'] = df1['前走レース名'].str.replace('テレビユー福','テレビユー福島賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('ホンコンジョ','ホンコンJCT')
df1['前走レース名'] = df1['前走レース名'].str.replace('スレイプニル','スレイプニルS')
df1['前走レース名'] = df1['前走レース名'].str.replace('オーストラリ','オーストラリアT')
df1['前走レース名'] = df1['前走レース名'].str.replace('フリーウェイ','フリーウェイS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ＢＳイレブン','BSイレブン賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('ブリリアント','ブリリアントS')
df1['前走レース名'] = df1['前走レース名'].str.replace('福島中央テレ','福島中央テレビ杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('大阪―ハンブ','大阪―ハンブルクC')
df1['前走レース名'] = df1['前走レース名'].str.replace('サンシャイン','サンシャインS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ブラッドスト','ブラッドストーンS')
df1['前走レース名'] = df1['前走レース名'].str.replace('アクアマリン','アクアマリンS')
df1['前走レース名'] = df1['前走レース名'].str.replace('バレンタイン','バレンタインS')
df1['前走レース名'] = df1['前走レース名'].str.replace('アルデバラン','アルデバランS')
df1['前走レース名'] = df1['前走レース名'].str.replace('アレキサンド','アレキサンドライトS')
df1['前走レース名'] = df1['前走レース名'].str.replace('中京スポニチ','中京スポニチ賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('ジャニュアリ','ジャニュアリーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('ニューイヤー','ニューイヤーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('カーバンクル','カーバンクルS')
df1['前走レース名'] = df1['前走レース名'].str.replace('メトロポリタ','メトロポリタンS')
df1['前走レース名'] = df1['前走レース名'].str.replace('カーバンクル','カーバンクルS')

#2、3歳特別レース名
df1['前走レース名'] = df1['前走レース名'].str.replace('クリスマスロ','クリスマスローズS')
df1['前走レース名'] = df1['前走レース名'].str.replace('きんもくせい','きんもくせい賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('フェニックス','フェニックス賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('カーネーショ','カーネーションC')
df1['前走レース名'] = df1['前走レース名'].str.replace('プリンシパル','プリンシパルS')
df1['前走レース名'] = df1['前走レース名'].str.replace('スイートピー','スイートピーS')
df1['前走レース名'] = df1['前走レース名'].str.replace('フローラルウ','Fウォーク賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('マーガレット','マーガレットS')
df1['前走レース名'] = df1['前走レース名'].str.replace('セントポーリ','セントポーリア賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('ジュニアカッ','ジュニアC')

#地方重賞
df1['前走レース名'] = df1['前走レース名'].str.replace('ＴＣＫG3','TCK女王盃')
df1['前走レース名'] = df1['前走レース名'].str.replace('川崎記G1','川崎記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('佐賀記G3','佐賀記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('エンプG2','エンプレス杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('黒船賞G3','黒船賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('ダイオG2','ダイオライト記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('名古屋G3','名古屋大賞典')
df1['前走レース名'] = df1['前走レース名'].str.replace('マリーG3','マリーンC')
df1['前走レース名'] = df1['前走レース名'].str.replace('東京スG3','東京スプリント')
df1['前走レース名'] = df1['前走レース名'].str.replace('かきつG3','かきつばた記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('かしわG1','かしわ記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('かきつG3','かきつばた記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('兵庫ＣG2','兵庫CS')
df1['前走レース名'] = df1['前走レース名'].str.replace('さきたG2','さきたま杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('北海道G3','北海道SC')
df1['前走レース名'] = df1['前走レース名'].str.replace('関東オG2','関東オークス')
df1['前走レース名'] = df1['前走レース名'].str.replace('帝王賞G1','帝王賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('ジャパG1','JDD')
df1['前走レース名'] = df1['前走レース名'].str.replace('スパーG3','スパーキングLC')
df1['前走レース名'] = df1['前走レース名'].str.replace('マーキG3','マーキュリーC')
df1['前走レース名'] = df1['前走レース名'].str.replace('クラスG3','クラスターC')
df1['前走レース名'] = df1['前走レース名'].str.replace('サマーG3','サマーチャンピオン')
df1['前走レース名'] = df1['前走レース名'].str.replace('ブリーG3','ブリーダーズGC')
df1['前走レース名'] = df1['前走レース名'].str.replace('テレ玉G2','オーバルスプリント')
df1['前走レース名'] = df1['前走レース名'].str.replace('白山大G3','白山大賞典')
df1['前走レース名'] = df1['前走レース名'].str.replace('日本テG2','日本テレビ盃')
df1['前走レース名'] = df1['前走レース名'].str.replace('日本ＴG2','日本テレビ盃')
df1['前走レース名'] = df1['前走レース名'].str.replace('東京盃G2','東京盃')
df1['前走レース名'] = df1['前走レース名'].str.replace('ＬプレG2','レディスプレリュード')
df1['前走レース名'] = df1['前走レース名'].str.replace('マイルG1','マイルCS南部杯')
df1['前走レース名'] = df1['前走レース名'].str.replace('エーデG3','エーデルワイス賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('JBCスプG1','JBCスプリント')
df1['前走レース名'] = df1['前走レース名'].str.replace('JBCクラG1','JBCクラシック')
df1['前走レース名'] = df1['前走レース名'].str.replace('JBCＬクG1','JBCレディスC')
df1['前走レース名'] = df1['前走レース名'].str.replace('JBC２歳G1','JBC2歳優駿')
df1['前走レース名'] = df1['前走レース名'].str.replace('浦和記G2','浦和記念')
df1['前走レース名'] = df1['前走レース名'].str.replace('兵庫ジG2','兵庫ジュニアGP')
df1['前走レース名'] = df1['前走レース名'].str.replace('クイーG3','クイーン賞')
df1['前走レース名'] = df1['前走レース名'].str.replace('名古屋G3','名古屋グランプリ')
df1['前走レース名'] = df1['前走レース名'].str.replace('全日本G1','全日本2歳優駿')
df1['前走レース名'] = df1['前走レース名'].str.replace('兵庫ゴG3','兵庫ゴールドT')
df1['前走レース名'] = df1['前走レース名'].str.replace('東京大G1','東京大賞典')

#その他英数字
alphabet_table = str.maketrans('ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' )
alphabet_s_table = str.maketrans('ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ', 'abcdefghijklmnopqrstuvwxyz' )
number_table = str.maketrans('０１２３４５６７８９', '0123456789' )
df1['前走レース名'] = df1['前走レース名'].str.translate(alphabet_table)
df1['前走レース名'] = df1['前走レース名'].str.translate(alphabet_s_table)
df1['前走レース名'] = df1['前走レース名'].str.translate(number_table)
df1['前走レース名'] = df1['前走レース名'].str.replace(r'ｸﾗｽ',r'クラス')
df1['前走レース名'] = df1['前走レース名'].str.replace(r'*','')

#5文字以上の調教師
df1['調教師名'] = df1['調教師名'].str.replace(r'浅野洋一',r'浅野洋一郎')
df1['調教師名'] = df1['調教師名'].str.replace(r'五十嵐忠',r'五十嵐忠男')
df1['調教師名'] = df1['調教師名'].str.replace(r'大久保龍',r'大久保龍志')
df1['調教師名'] = df1['調教師名'].str.replace(r'大根田裕',r'大根田裕之')
df1['調教師名'] = df1['調教師名'].str.replace(r'加藤士津',r'加藤士津八')
df1['調教師名'] = df1['調教師名'].str.replace(r'久保田貴',r'久保田貴士')
df1['調教師名'] = df1['調教師名'].str.replace(r'佐々木晶',r'佐々木晶三')
df1['調教師名'] = df1['調教師名'].str.replace(r'鈴木慎太',r'鈴木慎太郎')
df1['調教師名'] = df1['調教師名'].str.replace(r'中内田充',r'中内田充正')
df1['調教師名'] = df1['調教師名'].str.replace(r'長谷川浩',r'長谷川浩大')
df1['調教師名'] = df1['調教師名'].str.replace(r'浜田多実',r'浜田多実雄')
df1['調教師名'] = df1['調教師名'].str.replace(r'和田正一',r'和田正一郎')

#セン馬
df1['性別'] = df1['性別'].str.replace(r'セ',r'セン')

#パドック切断対策
df1['レースID'] = df1['レースID'].str.replace(r'RX','')
df1['レースID'] = df1['レースID'].str.replace(r'UX','')
df1['馬ID'] = df1['馬ID'].str.replace(r'RX','')
df1['馬ID'] = df1['馬ID'].str.replace(r'UX','')

#前走着順の丸数字対策
maru_number_table = str.maketrans('①②③④⑤⑥⑦⑧⑨', '123456789' )
df1['前走着順'] = df1['前走着順'].str.translate(maru_number_table)
df1['前走着順'] = df1['前走着順'].str.replace(r'⑩',r'10')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑪',r'11')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑫',r'12')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑬',r'13')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑭',r'14')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑮',r'15')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑯',r'16')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑰',r'17')
df1['前走着順'] = df1['前走着順'].str.replace(r'⑱',r'18')

#2代目の種牡馬の表記対応
number_table2 = str.maketrans('０１２３４５６７８９', '0123456789' )
df1['父'] = df1['父'].str.translate(number_table2)
df1['母'] = df1['母'].str.translate(number_table2)
df1['母父'] = df1['母父'].str.translate(number_table2)
df1['父'] = df1['父'].str.replace(r'2',r'II')
df1['母'] = df1['母'].str.replace(r'2',r'II')
df1['母父'] = df1['母父'].str.replace(r'2',r'II')

if info_num == 1 : #血統パート
    tkinter.messagebox.showinfo('モーダルやる夫','望田ファイルを選択してください！')
    ret2 = tkinter.filedialog.askopenfilename(title = '望田ファイルを選ぶ', initialdir = cd , multiple = False)
    if ret2 == "": #キャンセル押したときに終了
        sleep(1)
        sys.exit(1)

    try: #デコード処理
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'shift-jis' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm = pd.read_table(ret2, sep = '\n' , encoding = 'utf-8' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'euc-jp' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'cp932' ,names = ['コンテンツ'] , dtype = object)

    #半角スペースのエラー対策
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace(' <strong>','<strong>')

    #<strong>で始まる文のリストを作成、最初の要素の1行前までを切り落とす
    tgtxt = dfm.query('コンテンツ.str.startswith("<strong>")', engine = 'python')
    tgtnum = tgtxt.index[0]
    dfm = dfm.drop(range(tgtnum))
    dfm = dfm.reset_index()

    #ヤマザキ春の置換祭り
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\u3000','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\t','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\n','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('<strong>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('</strong>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('父スピード×',r'父スピード　×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('父底力×',r'父底力　×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('短距離×',r'短距離　×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('中距離×',r'中距離　×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('長距離×',r'長距離　×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('スピード◎',r',◎')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('スピード○',r',○')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('スピード△',r',△')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('スピード×',r',×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('底力◎',r',◎')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('底力○',r',○')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('底力△',r',△')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('底力×',r',×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('コース◎',r',◎')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('コース○',r',○')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('コース△',r',△')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('コース×',r',×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('距離◎',r'望田,◎')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('距離○',r'望田,○')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('距離△',r'望田,△')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('距離×',r'望田,×')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('　','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace(' ','')


    dfn1 = [dfm['コンテンツ'][i*3] for i in range(int(len(dfm)/3))] #1行目が馬名
    dfn2 = [dfm['コンテンツ'][i*3+1] for i in range(int(len(dfm)/3))] #2行目がコメント
    dfn3 = [dfm['コンテンツ'][i*3+2] for i in range(int(len(dfm)/3))] #3行目が評価

    DF_NEW = pd.DataFrame({'馬名': dfn1 ,'コメント': dfn2,'評価': dfn3}) #TARGETのデータフレームに結合するために新しく整形

    df3 = pd.merge(df1,DF_NEW,on = '馬名') #2つのデータフレームを結合
    df3str = df3.values.tolist()
    race = str(df3['レースID'][0])
    nkID = race[:4] + race[8:] #TARGETのレースIDをnetkeiba用に変換
    year = race[2:4]
    filename = os.path.basename(ret1) #ファイル名からレース名を取得

    defaultname1 = str('ped_analysis_' + nkID + '.csv')
    fTyp1 = [("*.csv","*.csv")]
    iDir1 = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('モーダルやる夫','モーダルファイルの出力先を選択してください！')
    file1 = tkinter.filedialog.asksaveasfilename(initialfile = defaultname1 , filetypes = fTyp1,initialdir = iDir1)

    if file1 == "": #キャンセル押したときに終了
        sleep(1)
        sys.exit(1)

    with open(file1, mode = 'w', encoding = 'utf-8') as f: #モーダルファイルに書き込む
        for row in df3str:
            f.write(nkID + ',' + str(row[1]) + ',' + year + filename.rstrip('.csv') + '(' + str(row[2]) + '),' +  str(row[13]) + ',' + str(row[14]) + '\n')
        else:
            tkinter.messagebox.showinfo('モーダルやる夫','☆☆☆出力完了しました☆☆☆')
            print('\n\n\n☆☆☆出力完了しました☆☆☆')
            sleep(1)
            sys.exit(1)

elif info_num == 2 : #馬体パート
    tkinter.messagebox.showinfo('モーダルやる夫','馬体診断コラムの原稿ファイルを選択してください！')
    ret2 = tkinter.filedialog.askopenfilename(title = '馬体診断コラムの原稿ファイルを選ぶ', initialdir = cd , multiple = False)
    if ret2 == "": #キャンセル押したときに終了
        sleep(1)
        sys.exit(1)

    try: #デコード処理
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'shift-jis' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm = pd.read_table(ret2, sep = '\n' , encoding = 'utf-8' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'euc-jp' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'cp932' ,names = ['コンテンツ'] , dtype = object)

    #半角スペースのエラー対策
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace(' <strong>','<strong>')

    #本文が始まる所まで切り落とす
    if batai_num == 7:#哲三さん
        tgtxt2 = dfm.query('コンテンツ.str.startswith("<strong>")', engine = 'python')
        tgtnum2 = tgtxt2.index[1]
        dfm = dfm.drop(range(tgtnum2))

    elif batai_num < 7 : #哲三さん以外
        tgtxt2 = dfm.query('コンテンツ.str.startswith("<strong>")', engine = 'python')
        tgtnum2 = tgtxt2.index[0]
        dfm = dfm.drop(range(tgtnum2))


    #キャプションを正規表現で抽出
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace(r'<div class.+?<p>▲([0-9]{1,3})月([0-9]{1,3})日撮影</p></div>', r'▲\1月\2日撮影' , regex = True)

    #置換祭り
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\u3000','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\t','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\n','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('<strong>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('</strong>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('<p>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('</p>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('　','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace(' ','')

    dfm = dfm.reset_index()

    dfn1 = [dfm['コンテンツ'][i*4] for i in range(int(len(dfm)/4))]
    dfn2 = [dfm['コンテンツ'][i*4+1] for i in range(int(len(dfm)/4))]
    dfn3 = [dfm['コンテンツ'][i*4+2] for i in range(int(len(dfm)/4))]
    dfn4 = [dfm['コンテンツ'][i*4+3] for i in range(int(len(dfm)/4))]

    DF_NEW = pd.DataFrame({'馬名': dfn1 , '所属': dfn2, 'キャプション': dfn3, 'コメント':dfn4}) #TARGETのデータフレームに結合するために新しく整形

    df3 = pd.merge(df1,DF_NEW,on = '馬名') #2つのデータフレームを結合
    df3str = df3.values.tolist()
    race = str(df3['レースID'][0])
    nkID = race[:4] + race[8:]
    year = race[2:4]
    filename = os.path.basename(ret1)

    defaultname1 = str('batai_check_' + nkID + '.csv')
    fTyp1 = [("*.csv","*.csv")]
    iDir1 = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('モーダルやる夫','馬体診断モーダルファイルの出力先を選択してください！')
    file1 = tkinter.filedialog.asksaveasfilename(initialfile = defaultname1 , filetypes = fTyp1,initialdir = iDir1)
    if file1 == "":
        sleep(1)
        sys.exit(1)

    with open(file1,mode = 'w',encoding = 'utf-8') as f: #モーダルファイルに書き込む
        for row in df3str:
            f.write(nkID + ',' + str(row[1]) + ',' + year + filename.rstrip('.csv') + '(' + str(row[2]) + '),' + \
            str(row[15]) + ',' + str(row[14]) + ',' + str(author[batai_num]) + '\n')
        else:
            tkinter.messagebox.showinfo('モーダルやる夫','☆☆☆出力完了しました☆☆☆')
            print('\n\n\n☆☆☆出力完了しました☆☆☆')
            sleep(1)
            sys.exit(1)

elif info_num == 3 : #トレセンパート（馬三郎ファイルから）
    #馬三郎ファイルを読み込む
    tkinter.messagebox.showinfo('モーダルやる夫','馬三郎ファイル（コメント）を選択してください！')
    ret2 = tkinter.filedialog.askopenfilename(title = '馬三郎ファイル（コメント）を選ぶ', initialdir = cd , multiple = False)
    if ret2 == "":
        sleep(1)
        sys.exit(1)

    try:
        dfm  = pd.read_table(ret2, sep = ',' , encoding = 'euc-jp' ,names = ['馬名','コメント'] , dtype = object)
    except UnicodeDecodeError:
        dfm = pd.read_table(ret2, sep = ',' , encoding = 'utf-8' ,names = ['馬名','コメント'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = ',' , encoding = 'shift-jis' ,names = ['馬名','コメント'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = ',' , encoding = 'cp932' ,names = ['馬名','コメント'] , dtype = object)


    #置換祭り
    #<矢作師>みたいなところを新しい列で追加
    dfm['発言者'] = dfm['コメント']
    dfm['発言者'] = dfm['発言者'].str.replace(r'.+?。<', '<' , regex = True)
    dfm['発言者'] = dfm['発言者'].str.replace(r'.+?。＜', '＜' , regex = True)
    dfm['発言者'] = dfm['発言者'].str.replace(r'<([^\x20-\x7E]+?)>', r'\1騎手' , regex = True)
    dfm['発言者'] = dfm['発言者'].str.replace(r'＜([^\x20-\x7E]+?)＞', r'\1騎手' , regex = True)
    dfm['発言者'] = dfm['発言者'].str.replace('調教師騎手','調教師')
    dfm['発言者'] = dfm['発言者'].str.replace('師騎手','調教師')
    dfm['発言者'] = dfm['発言者'].str.replace('助手騎手','助手')
    dfm['発言者'] = dfm['発言者'].str.replace('厩務員騎手','厩務員')


    dfm['コメント'] = dfm['コメント'].str.replace(r'<([^\x20-\x7E]+?)>', '' , regex = True)
    dfm['コメント'] = dfm['コメント'].str.replace(r'＜([^\x20-\x7E]+?)＞', '' , regex = True)
    dfm['コメント'] = dfm['コメント'].str.replace('。<','。,')
    dfm['コメント'] = dfm['コメント'].str.replace('。＜','。,')
    dfm['コメント'] = dfm['コメント'].str.replace('>','')
    dfm['コメント'] = dfm['コメント'].str.replace('＞','')
    dfm['コメント'] = dfm['コメント'].str.replace('\t','')
    dfm['コメント'] = dfm['コメント'].str.replace('\n','')
    dfm['コメント'] = dfm['コメント'].str.replace('　','')
    dfm['コメント'] = dfm['コメント'].str.replace(' ','')

    #二つのデータフレームをまとめてリスト化

    df3 = pd.merge(df1,dfm,on = '馬名')
    df3str = df3.values.tolist()
    race = str(df3['レースID'][0])
    nkID = race[:4] + race[8:]
    year = race[2:4]
    filename = os.path.basename(ret1)

    #コラム原稿出力

    defaultname1 = 'トレセンリポート原稿.txt'
    fTyp3 = [(".txt",".txt")]
    iDir3 = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('モーダルやる夫','コラム原稿の出力先を選択してください！')
    file3 = tkinter.filedialog.asksaveasfilename(initialfile = defaultname1, filetypes = fTyp3,initialdir = iDir3)
    with open(file3,mode = 'w',encoding='utf-8') as f:
        f.write('<div class="Photo_Block_01"><img src="style/netkeiba.ja/image/column/toresen/画像名.jpg" alt="馬名" style="width:100%"><p>▲キャプション</p></div>\n' \
         +'<div class="ColumnRead">' + filename.rstrip('.csv') +'の出走予定馬'+str(len(df3str))+'頭のレース1週間前の厩舎情報をお届けします。</div>\n')
        for row in df3str:
            f.write('<strong>'+str(row[2])+'</strong>\n' \
            +str(row[5])+'・'+str(row[6])+'厩舎　'+str(row[3])+str(row[4]) \
            +'\n父'+str(row[7])+'、母'+str(row[8])+'、母父'+ str(row[9]) + '/前走' + str(row[10]) + 'は'+ str(row[11]) + '人気' + str(row[12]) + '着\n\n' \
            +str(row[14])+'\n「'+str(row[13]).rstrip('。')+'」\n\n')
        else:
            tkinter.messagebox.showinfo('モーダルやる夫','！！！モーダル作成に移行します！！！')

    #モーダル出力
    sleep(0.5)
    defaultname2 = str('trecen_repo_' + nkID + '.csv')
    fTyp4 = [(".csv",".csv")]
    iDir4 = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('モーダルやる夫','モーダルファイルの出力先を選択してください！')
    file4 = tkinter.filedialog.asksaveasfilename(initialfile = defaultname2 , filetypes = fTyp4,initialdir = iDir4)
    with open(file4,mode = 'w',encoding='utf-8') as f:
        for row in df3str:
            f.write(nkID + ',' + str(row[1]) + ',' + year + filename.rstrip('.csv') + '(' + str(row[2]) + ')' + ',' + str(row[14]) + '「' + str(row[13].rstrip('。')) + '」\n')
        else:
            sleep(1)
            tkinter.messagebox.showinfo('モーダルやる夫','☆☆☆出力完了しました☆☆☆')
            print('\n\n\n☆☆☆出力完了しました☆☆☆')
            sleep(1)
            sys.exit(1)

elif info_num == 4 : #トレセンパート（コラムから）
    tkinter.messagebox.showinfo('モーダルやる夫','トレセンコラムの本文ファイルを選択してください！')
    ret2 = tkinter.filedialog.askopenfilename(title = 'トレセンコラムの本文ファイルを選ぶ', initialdir = cd , multiple = False)
    if ret2 == "": #キャンセル押したときに終了
        sleep(1)
        sys.exit(1)

    try: #デコード処理
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'shift-jis' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm = pd.read_table(ret2, sep = '\n' , encoding = 'utf-8' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'euc-jp' ,names = ['コンテンツ'] , dtype = object)
    except UnicodeDecodeError:
        dfm  = pd.read_table(ret2, sep = '\n' , encoding = 'cp932' ,names = ['コンテンツ'] , dtype = object)

    #半角スペースのエラー対策
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace(' <strong>','<strong>')

    #<strong>で始まる文のリストを作成、最初の要素の1行前までを切り落とす
    tgtxt = dfm.query('コンテンツ.str.startswith("<strong>")', engine = 'python')
    tgtnum = tgtxt.index[0]
    dfm = dfm.drop(range(tgtnum))
    dfm = dfm.reset_index()

    #ヤマザキ春の置換祭り
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\u3000','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\t','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('\n','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('<strong>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('</strong>','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace('　','')
    dfm['コンテンツ'] = dfm['コンテンツ'].str.replace(' ','')


    dfn1 = [dfm['コンテンツ'][i*3] for i in range(int(len(dfm)/3))] #1行目が馬名
    dfn2 = [dfm['コンテンツ'][i*3+1] for i in range(int(len(dfm)/3))] #2行目がコメント
    dfn3 = [dfm['コンテンツ'][i*3+2] for i in range(int(len(dfm)/3))] #3行目が評価

    DF_NEW = pd.DataFrame({'馬名': dfn1 ,'コメント': dfn2,'評価': dfn3}) #TARGETのデータフレームに結合するために新しく整形

    df3 = pd.merge(df1,DF_NEW,on = '馬名') #2つのデータフレームを結合
    df3str = df3.values.tolist()
    race = str(df3['レースID'][0])
    nkID = race[:4] + race[8:] #TARGETのレースIDをnetkeiba用に変換
    year = race[2:4]
    filename = os.path.basename(ret1) #ファイル名からレース名を取得

    #モーダル出力
    sleep(0.5)
    defaultname2 = str('trecen_repo_' + nkID + '.csv')
    fTyp4 = [(".csv",".csv")]
    iDir4 = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('モーダルやる夫','モーダルファイルの出力先を選択してください！')
    file4 = tkinter.filedialog.asksaveasfilename(initialfile = defaultname2 , filetypes = fTyp4,initialdir = iDir4)
    with open(file4,mode = 'w',encoding='utf-8') as f:
        for row in df3str:
            f.write(nkID + ',' + str(row[1]) + ',' + year + filename.rstrip('.csv') + '(' + str(row[2]) + ')' + ',' + str(row[14]) + '「' + str(row[13].rstrip('。')) + '」\n')
        else:
            sleep(1)
            tkinter.messagebox.showinfo('モーダルやる夫','☆☆☆出力完了しました☆☆☆')
            print('\n\n\n☆☆☆出力完了しました☆☆☆')
            sleep(1)
            sys.exit(1)
