import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./sample.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# cvtColor : 画像の色空間(色)を変更する関数。
# cvtColorについて : https://kuroro.blog/python/7IFCPLA4DzV8nUTchKsb/

# 第一引数 : 多次元配列(numpy.ndarray)

# 第二引数 : 変更前の画像の色空間(色)と、変更後の画像の色空間(色)を示す定数を設定。
# cv2.COLOR_BGR2HSV : BGR(Blue, Green, Red)形式の色空間(色)を持つ画像をHSV(Hue(色相), Saturation(彩度), Value(明度))形式へ変更する。
# ※ なぜHSV形式に変更するのか? : RGB(Red, Green, Blue)形式やBGR(Blue, Green, Red)形式で色を表現し、inRange関数を利用しても構わない。ただinRange関数の第二引数, 第三引数で指定する値の感覚が掴みにくいため、HSV(Hue(色相), Saturation(彩度), Value(明度))形式で色を表現し、inRange関数の第二引数, 第三引数を指定することをおすすめする。

# 戻り値 : 多次元配列(numpy.ndarray)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# inRange : 2値化(画像を白と黒の2色に変換する)するための関数
# 第一引数 : 多次元配列(numpy.ndarray)
# 第二引数 : 2値化する条件の下限
# 第三引数 : 2値化する条件の上限
# 戻り値 : 多次元配列(numpy.ndarray)
img = cv2.inRange(img, (0, 0, 0), (255, 255, 94))

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', img)
