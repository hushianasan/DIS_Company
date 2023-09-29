## 要件定義

* 気象庁HPから松山市, 西条市, 宇和島市の過去１０年間の気象データの取得
* 検索とグラフ化するプログラムの作成

## 機能要件
* 気象データの取得機能, APIかJSONか叩く
* 気象データの検索機能
 * 年月と３地点を条件として指定可能であること
   * 検索条件に年のみを指定すると、検索結果に該当年の月ごとの値を表示する。
   * 検索条件に年月を指定すると、検索結果に該当年月の日ごとの値を表示する。
   * 検索条件に3地点を指定すると、検索結果に該当地点の値を表示する。なお、検索条件の年、地点の指定は必須条件とする。
   * 検索結果には降水量、気温（平均、最高、最低）を表示する。
   * 気象データのグラフ化機能。
 
   　検索結果の値を元にグラフ化すること。ただし、グラフ化する項目は指定可能であること。
 
   　グラフの横軸は時間軸、縦軸が各種気象データとする。

## 開発環境(予定)

* VSCode
  * Git
  * Codic

## API, Package(予定)

* Python3
  * Pip

## 指針

* Issue駆動開発

* テスト駆動開発

* ウォーターフォール

* 開発環境は最小構成

* UIはノーコード使用(Notion等でも可, 自動生成も)

* 設計慎重に

* 使用したものはIssueに必ず記すように

* １日の考えと進捗もIssueに

* ガラパゴス化しないと思うのでVMは今回使わないように

## 目標

1. レビューを仰ぐ

2. 要件定義を明確に

3. 環境の構築

4. 関数をうまいこと

## 出典

## 補足

多分わたしはJavaとPHPは使えない。

ガラパゴス化しないよう、なるべく初学者向けで１台のみのパソコンで動くように。
