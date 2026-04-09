---
title: "編輯常見問題"
source_url: "https://support.evoto.ai/editing-related/"
source_type: "post"
source_id: "2173"
language: "zh-hant"
translation_group: "2173"
primary_category: "faq"
tags:
  - "faq"
  - "original-path"
  - "path"
  - "preset"
  - "preset-token"
  - "preview"
  - "preview-size"
  - "using-evoto"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/05/Screenshot-2025-08-13-at-16.53.22-300x246.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/image-3-1024x548.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/image-4-1024x444.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/05/截屏2025-05-23-14.02.06-1-271x300.png"
---

本節整理了 Evoto 編輯流程中的常見問題，包括如何管理預覽、處理遺失檔案，以及了解預設口令的運作方式。

---

#### 為什麼我的照片預覽尺寸看起來這麼小？

預設預覽尺寸會自動設定為兼顧效能的大小，但你可以自行調高解析度。這項變更只會影響畫面上的顯示方式，不會影響最終匯出的畫質。

若要調整預覽尺寸：

1. 點擊畫面左上角的 **Evoto Menu**。
2. 選擇 **Preferences**。
3. 在對話框中切換到 **Preview** 分頁。
4. 依需求調整 **preview size**，最高可設為 **4000px**。
5. 點擊 **OK** 儲存變更。

![](https://support.evoto.ai/wp-content/uploads/2025/05/Screenshot-2025-08-13-at-16.53.22-300x246.png)

**注意：** 預覽尺寸越大，電腦效能可能越慢。

---

#### 我不小心移動了圖片，該如何找到原始路徑？

![](https://support.evoto.ai/wp-content/uploads/2025/04/image-3-1024x548.png)

- **顯示更多資訊：** 如果遺失圖片仍有預覽圖或縮圖，系統會顯示出來，幫助你快速辨識是哪一張圖片遺失。
- **不打斷操作的提示：** 選取遺失圖片時，系統現在會顯示簡單的介面提示，而不是跳出阻斷式視窗，讓你可以自行決定下一步操作。
- **重新連結遺失圖片：** 你可以將 Evoto 指向圖片的新位置以重新連結檔案，但此功能僅適用於最初匯入的原始圖片。

![](https://support.evoto.ai/wp-content/uploads/2025/04/image-4-1024x444.png)

---

#### 為什麼預設口令無法使用？

當你匯入其他使用者分享的預設口令時，如果對方在你匯入之前已更新或刪除該預設，系統可能會顯示此口令不存在。預設口令會綁定在產生當下的預設狀態。

---

#### 為什麼我在色彩調整時看不到先前的人像修飾效果？

這是常見情況，你的編輯並沒有遺失，而是顯示偏好設定造成的。如果你先做 **人像修飾** 或其他細部調整，再切換到 **色彩調整** 模組，這些修飾效果可能會暫時隱藏。

- **解決方式：** 找到並**關閉** **「即時色彩調整」** 開關。關閉後，色彩調整面板就會再次顯示你先前的所有編輯。

![](https://support.evoto.ai/wp-content/uploads/2025/05/截屏2025-05-23-14.02.06-1-271x300.png)

- **建議：** 雖然沒有強制的編輯順序，但我們建議先做色彩調整，再進行基礎修飾。這樣通常可以避免效果互相干擾，也更方便後續微調。

#### 為什麼「從磁碟刪除」沒有真的刪掉檔案？

這通常表示 Evoto 尚未取得必要的存取權限：

- 開啟 **System Settings**（若你使用的是 macOS Monterey 或更早版本，請開啟 **System Preferences**）。
- 前往 **Privacy & Security**。
- 在側邊欄檢查 Evoto 是否已啟用 **Files and Folders** 與 **Full Disk Access** 權限。
