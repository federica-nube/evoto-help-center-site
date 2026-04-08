---
title: "インストールに関するFAQ"
source_url: "https://support.evoto.ai/ja/installation-faqs/"
source_type: "post"
source_id: "11609"
language: "ja"
translation_group: "6278"
primary_category: "%e3%82%88%e3%81%8f%e3%81%82%e3%82%8b%e3%81%94%e8%b3%aa%e5%95%8f"
tags:
  - "faq-ja"
  - "pc-ja"
---

#### Macで「EvotoはApp Storeからダウンロードされたものではないため開けません」というエラーが出る場合

このエラーが表示された場合は、以下の手順で解決できます。

1. ダイアログで「OK」をクリックします。
2. Appleメニューから「システム環境設定」を開きます。
3. 「セキュリティとプライバシー」を選択します。
4. 「一般」タブを開きます。
5. 左下の鍵アイコンをクリックし、Macの管理者アカウントで認証します。
6. 「ダウンロードしたアプリケーションの実行許可」の項目で「App Storeと確認済みの開発元からのアプリケーションを許可」を選択します。
7. または、一時的に「このまま開く（Open Anyway）」を選択して起動することも可能です。
8. 「システム環境設定」を閉じ、Evotoを再度起動します。

---

#### WindowsでEvotoをウイルス対策ソフトに許可する方法

EvotoがWindowsやウイルス対策ソフトと干渉し、正常に動作しない場合があります。

ウイルス対策ソフトがEvoto関連のプロセスをブロックする場合は、必ず許可してください。以下は主要なソフトでの除外設定方法です。

##### Windows Defender

1. 通知領域からWindows Defenderを開きます。
2. 「ウイルスと脅威の防止」を選択します。
3. 「ウイルスと脅威の防止の設定」を開きます。
4. 「除外の追加または削除」を選択します。
5. 「除外の追加」→対象のファイル、フォルダー、またはプロセスを選択します。
6. 選択を確定します。 （詳細手順はこちら：[Windowsセキュリティでの除外設定方法](https://support.microsoft.com/ja-jp/windows/windows-%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3-%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E3%82%A6%E3%82%A4%E3%83%AB%E3%82%B9%E3%81%A8%E8%84%85%E5%A8%81%E3%81%AE%E4%BF%9D%E8%AD%B7-1362f4cd-d71a-b52a-0b66-c2820032b65e)）

##### McAfee

1. Evotoのインターネット接続を許可します。
2. ブロックされているアプリの一覧からEvotoを選択し、「編集」をクリックします。
3. 「アクセス」の項目で「受信と送信」を選択し、接続タイプを「全デバイスに公開」に変更します。
4. アプリがリストにない場合は「追加」→Evotoを選択→同様に設定します。 （詳細手順はこちら：[McAfeeでの除外設定方法](https://www.mcafee.com/support/s/?language=ja&articleId=TS102056&page=shell&shell=article-view)）

##### Avast

1. 通知領域からAvastを開きます。
2. 「設定」→「一般」→「除外」を選択します。
3. 「ファイルパス」からEvoto.exeがあるフォルダーまたはファイルを指定し、除外に追加します。 （詳細手順はこちら：[Avastでの除外設定方法](https://support.avast.com/ja-jp/article/antivirus-scan-exclusions/#mac)）

##### ESET

1. 通知領域からESETを開き、F5キーで「詳細設定」を開きます。
2. 「アンチウイルスとスパイウェア対策」→「除外」を選択します。
3. 「追加」からEvoto.exeまたはそのフォルダーを指定します。 （詳細手順はこちら：[ESETでの除外設定方法](https://support.eset.com/jp)）

##### Avira

1. 通知領域からAviraのリアルタイム保護を無効化します。
2. Evotoをインストールします。
3. Aviraを展開し、「エクストラ」→「設定」→「PC保護」→「スキャン」→「例外」からEvoto.exeまたはフォルダーを追加します。
4. 同様に「リアルタイム保護」の例外にも追加します。 （詳細手順はこちら：[Aviraでの除外設定方法](https://support.avira.com/hc/en-us/articles/360000105338-How-do-I-exclude-files-from-the-clean-up-process-of-Avira-System-Speedup)）

##### Bitdefender

1. Bitdefenderを開き、「保護」→「機能の表示」→「設定」→「除外」タブを開きます。
2. 「スキャンから除外するファイルとフォルダーの一覧」にEvoto.exeまたはフォルダーを追加します。 （詳細手順はこちら：[Bitdefenderでの除外設定方法](https://www.bitdefender.com/consumer/support/answer/13427/)）

##### Malwarebytes

1. Malwarebytesを開き、「設定」→「マルウェア除外」を選択します。
2. 「ファイルの追加」または「フォルダーの追加」からEvoto.exeまたはそのフォルダーを選択します。 （詳細手順はこちら：[Malwarebytesでの除外設定方法](https://help.malwarebytes.com/hc/en-us/articles/31589553442715-Manage-the-Allow-List-in-Malwarebytes-for-Windows-v4)）
