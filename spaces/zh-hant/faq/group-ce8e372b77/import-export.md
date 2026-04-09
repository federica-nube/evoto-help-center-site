---
title: "匯入與匯出常見問題"
source_url: "https://support.evoto.ai/import-export/"
source_type: "post"
source_id: "2176"
language: "zh-hant"
translation_group: "2176"
primary_category: "faq"
tags:
  - "blurry"
  - "export"
  - "exported"
  - "file-size"
  - "import"
  - "imported"
  - "percentage"
  - "quality"
  - "size"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/05/Screenshot-2025-08-13-at-17.04.59-300x244.png"
---

本節整理了在 Evoto 中匯入與匯出圖片時的常見問題。

#### 為什麼圖片匯入 Evoto 後看起來模糊？

Evoto 支援各種類型的 RAW 檔案，且不會降低原始圖片的解析度。不過，為了兼顧效能，預設預覽設定會依照你的電腦規格自動調整。

若要提升預覽畫質：

1. 前往 **Settings** → **Preview** → **Preview size**。
2. 雖然 Evoto 通常會自動提供預設值，但你可以把預覽尺寸調高到 **4000px**，這是目前支援的最大解析度。
3. 這個設定只會影響 Evoto 內的顯示效果，不會影響最終匯出的畫質。

![](https://support.evoto.ai/wp-content/uploads/2025/05/Screenshot-2025-08-13-at-17.04.59-300x244.png)

#### 為什麼從 Evoto 匯出後，檔案大小會改變？

當你在 Evoto 中編輯圖片時，不同功能所使用的演算法會改變圖片的像素資料，因此匯出後檔案大小也可能發生變化。請放心，這不會影響匯出畫質；最終品質仍會依照你匯出時所選擇的設定為準。

#### 我已經匯出圖片，但指定資料夾是空的，為什麼？

如果匯出的圖片沒有出現在指定資料夾中，通常與檔案權限有關。有些磁碟或資料夾允許 Evoto **讀取** 檔案，但限制了 **寫入** 權限，導致 Evoto 無法將匯出的圖片存到該位置。請檢查資料夾設定，確認 Evoto 已擁有必要的 **寫入** 權限。
