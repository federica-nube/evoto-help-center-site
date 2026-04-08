---
title: "OM SYSTEM（オリンパス）カメラをEvotoでテザー撮影するための設定手順"
source_url: "https://support.evoto.ai/ja/om-system-tethering/"
source_type: "post"
source_id: "6656"
language: "ja"
translation_group: "630"
primary_category: "%e6%9c%aa%e5%88%86%e9%a1%9e"
tags:
  - "pc-ja"
migration_flags:
  - "image"
  - "table"
source_assets:
  - "https://res.evoto.ai/wordpress/b886beec-15d3-4c0b-9d20-5387895acc0f.png"
  - "https://res.evoto.ai/wordpress/1d6fa2ab-dcff-4236-bb57-ded31f6d1a8f.png"
  - "https://res.evoto.ai/wordpress/735152de-06fe-48e9-8a3c-e1241c68b326.png"
  - "https://res.evoto.ai/wordpress/2a591214-7d03-42b7-b3fa-16363f3e651e.png"
  - "https://res.evoto.ai/wordpress/3dd7c20b-2351-4166-b3af-ed6201ff2e72.png"
  - "https://res.evoto.ai/wordpress/bf6e0bf9-b7d1-4888-bef2-25959884cf0a.png"
  - "https://res.evoto.ai/wordpress/bf7e7a5e-0618-470b-a4be-51e2af98cb1c.png"
  - "https://res.evoto.ai/wordpress/d690878c-010f-47d3-b6af-0e9f728ad8f1.png"
  - "https://res.evoto.ai/wordpress/75b0d5d4-5015-42a1-b336-63acda943493.png"
  - "https://res.evoto.ai/wordpress/6125c1bb-71fe-4ff4-9132-d02962d23cc7.png"
  - "https://res.evoto.ai/wordpress/df23ac74-1c9f-4946-af77-c05609dd47ba.jpg"
  - "https://res.evoto.ai/wordpress/b7b667f5-8f99-4d2b-a2a4-b26a55cb62ce.jpg"
  - "https://res.evoto.ai/wordpress/24b4553e-8e8f-40c5-9c13-ae7cddf89c3a.jpg"
  - "https://res.evoto.ai/wordpress/7f238839-acb3-4984-92af-288ab68570b9.jpg"
---

EvotoでOM SYSTEM（旧Olympus）カメラを使用してテザー撮影を行うには、以下の手順に従ってカメラとパソコンを設定してください。 **パソコンとの接続確認** Windows: macOS: 特に追加設定は不要ですが、ドライバの確認を推奨します。 ![](https://res.evoto.ai/wordpress/b886beec-15d3-4c0b-9d20-5387895acc0f.png) OM SYSTEMカメラはmacOSと安定して接続できない場合があります。 より安定した接続のために、**U****SB-Cハブを使用することをお勧めします。直接Macのポートに接続しないようにする** [Zadig:を使用して必要なドライバをインストールする](https://zadig.akeo.ie/)![](https://res.evoto.ai/wordpress/1d6fa2ab-dcff-4236-bb57-ded31f6d1a8f.png) ![](https://res.evoto.ai/wordpress/735152de-06fe-48e9-8a3c-e1241c68b326.png) 可能であれば、Macのポートへの直接接続を避けてください。 Zadigを起動し、Options → List All Devices を選択します。 ![](https://res.evoto.ai/wordpress/2a591214-7d03-42b7-b3fa-16363f3e651e.png) ![](https://res.evoto.ai/wordpress/3dd7c20b-2351-4166-b3af-ed6201ff2e72.png) Replace Driver をクリックしてインストールを開始します。 ![](https://res.evoto.ai/wordpress/bf6e0bf9-b7d1-4888-bef2-25959884cf0a.png) ![](https://res.evoto.ai/wordpress/bf7e7a5e-0618-470b-a4be-51e2af98cb1c.png) インストールが完了するまで待ちます。 Windowsの「デバイスマネージャー」を開き、カメラが「ポータブルデバイス」として表示されているか確認します。 ![](https://res.evoto.ai/wordpress/d690878c-010f-47d3-b6af-0e9f728ad8f1.png) **カメラ本体の設定** カメラ側で以下の設定を行ってください： **1、USBモードの設定** メニュー → 設定 → 表示 (D4) → USBモード ![](https://res.evoto.ai/wordpress/75b0d5d4-5015-42a1-b336-63acda943493.png) → **USB / テザー接続** を選択 ![](https://res.evoto.ai/wordpress/6125c1bb-71fe-4ff4-9132-d02962d23cc7.png) **2、LCDバックライトの設定** メニュー → 設定 → ユーティリティ → バックライトLCD → **「ホールド」** に設定 ![](https://res.evoto.ai/wordpress/df23ac74-1c9f-4946-af77-c05609dd47ba.jpg) **3、スリープの設定** メニュー → 設定 → ユーティリティ → スリープ → **「オフ」** に設定 ![](https://res.evoto.ai/wordpress/b7b667f5-8f99-4d2b-a2a4-b26a55cb62ce.jpg) **4、自動電源オフの設定** メニュー → 設定 → ユーティリティ → 自動電源オフ → **「オフ」** に設定 ![](https://res.evoto.ai/wordpress/24b4553e-8e8f-40c5-9c13-ae7cddf89c3a.jpg) **5、クイックスリープモードの設定** メニュー → 設定 → ユーティリティ → クイックスリープモード → **「オフ」** に設定 ![](https://res.evoto.ai/wordpress/7f238839-acb3-4984-92af-288ab68570b9.jpg) これらの設定を完了すると、Evotoでの安定したテザー撮影が可能になります。 【接続に関する注意点】 ドライバのインストールやUSBポートの使用環境によっては、接続が不安定になることがあります。問題が解決しない場合は、Evotoサポートチームまでお問い合わせください。
