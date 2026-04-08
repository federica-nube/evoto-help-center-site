---
title: "匯入和匯出"
source_url: "https://support.evoto.ai/zh-hant/%e5%8c%af%e5%85%a5%e5%92%8c%e5%8c%af%e5%87%ba/"
source_type: "post"
source_id: "8053"
language: "zh-hant"
translation_group: "600"
primary_category: "%e5%a6%82%e4%bd%95%e9%96%8b%e5%a7%8b"
tags:
  - "pc-zh-hant"
migration_flags:
  - "image"
  - "table"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/lrcat-import.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/lrcat-tag-300x69.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/lrcat-export-300x189.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/export-settings-copy-1024x529.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-27-17.07.50-300x201.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-27-17.09.12-300x162.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Export-Adjustments-300x183.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Watermark-209x300.png"
  - "https://help.evoto.ai/~gitbook/image?url=https%3A%2F%2F2970798312-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9XghnFYmwxM9PPDFe9AG%252Fuploads%252FPbGPaangwQHP1uNtFHZl%252Fimage.png%3Falt%3Dmedia%26token%3Db52f13b0-37c3-4d56-b547-4409053b6a29&width=768&dpr=4&quality=100&sign=c06130aa&sv=2"
  - "https://help.evoto.ai/~gitbook/image?url=https%3A%2F%2F2970798312-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9XghnFYmwxM9PPDFe9AG%252Fuploads%252FeOJqhpkys6B31RLaz3QN%252Fimage.png%3Falt%3Dmedia%26token%3Db12a3691-507f-415c-b3bd-c840cbb06acc&width=768&dpr=4&quality=100&sign=d19615d6&sv=2"
  - "https://help.evoto.ai/~gitbook/image?url=https%3A%2F%2F2970798312-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9XghnFYmwxM9PPDFe9AG%252Fuploads%252FilPm1uscvNYRUpRwuVPX%252Fimage.png%3Falt%3Dmedia%26token%3D5b208d25-d7ce-4a57-972f-bb56942fa666&width=768&dpr=4&quality=100&sign=e713702e&sv=2"
---

本指南涵蓋如何在 Evoto 中手動匯入和匯出影像。如果您正在尋找使用熱資料夾的自動化工作流程信息，請參閱我們的 [自動導入和導出指南](https://support.evoto.ai/auto-import-export/)。

### 匯入

#### Evoto 支援的文件類型

Evoto 支援 JPEG、TIFF 和 PNG 格式，並支援處理大多數相機 RAW 檔案類型。 Evoto RAW 處理基於我們自主研發的強大 RAW 引擎。我們會定期更新庫並進行改進，以完美支援新相機。請注意，Evoto 目前不支援大於 1 GB 且像素大於 12000*12000 的映像檔。

#### 支援導入的檔案數量

Evoto 不限制每個項目匯入的照片數量，但限制一次可以匯入的照片數量。

每次最多可匯入 15,000 張照片。

#### 導入 Lightroom 目錄 (.lrcat)

Evoto 支援匯入 Lightroom Catalog (.lrcat) 文件，實現 Evoto 與 Lightroom 之間的無縫同步，從而實現更快的編輯和渲染。

**a如何導入 *.lrcat* 文件**

- 將 .lrcat 檔案拖曳到 Evoto 中。
- 或者，建立一個新專案並選擇.lrcat 檔案。
- 匯入後，您可以選擇將目錄中的哪些集合或篩選集匯入 Evoto。

![](https://support.evoto.ai/wp-content/uploads/2025/04/lrcat-import.png)

**項目識別：**

- 基於 .lrcat 檔案的項目在項目清單中有明顯標記

![](https://support.evoto.ai/wp-content/uploads/2025/04/lrcat-tag-300x69.png)

**導入選項：**

- **匯入原始影像：**僅當 .lrcat 檔案中引用的原始影像儲存在外部磁碟機上時才啟用此功能。

---

#### 支援的導入方法

- **在檔案總管中右鍵點選：**快速匯入支援的影像格式。
- **拖放**：將圖像拖曳到 Evoto 應用程式圖示上（不支援 Windows 工作列拖放）。
- **從其他軟體右鍵：**將影像從 Lightroom 或其他編輯器直接傳送到 Evoto。

---

### 出口

#### 匯出 Lightroom 目錄

從您的 .lrcat 專案中，按一下「*匯出*」按鈕下拉式選單，然後選擇「*匯出為 lrcat 檔案*」。請確保在使用此選項之前選擇了所有必要的圖像。

![](https://support.evoto.ai/wp-content/uploads/2025/04/lrcat-export-300x189.png)

**導出至：**

- **原始** .**lrcat** **資料夾**
- 匯出到包含原始 .lrcat 檔案的資料夾並在 Lightroom 中新增堆疊。
- **特定資料夾**
- 建立一個新的 .lrcat 包含已編輯影像和元資料的檔案。 Lightroom 會將已編輯的影像視為新文件，並套用 Evoto 的調整功能。
- **桌面**
- 與上述行為相同，但將新的 **.lrcat 檔案儲存到桌面**。

選擇後，您將在 *Export to* location （匯出到位置） 設定下看到兩個附加選項：

- **替換原始文件：** 使用 Evoto 編輯的版本覆蓋 Lightroom 中的原始非 RAW（JPG、TIFF、PNG）影像。系統會自動建立原始影像的備份。
- **將顏色設定匯出為 .lrcat：**如果您不啟用替換，則只有顏色變更和元資料會傳回 Lightroom。

**選擇匯出位置：**

您可以儲存更新的.lrcat：

- 到您的原始 Lightroom 目錄，覆蓋它
- 作為自訂位置中的新 .lrcat
- *這使得它以後很容易與原始目錄合併。*

***注：****僅當原始專案以 .lrcat 格式導入時，匯出為 .lrcat 檔才可作為一個選項*

---

#### 自訂導出設定

![](https://support.evoto.ai/wp-content/uploads/2025/04/export-settings-copy-1024x529.jpg)

#### 導出號碼

這表示待導出影像總數（第一個數字）乘以導出次數（第二個數字），該次數基於所選的導出預設數量。如果未選擇任何預設，則匯出次數預設為 1。 「*未編輯*」表示匯出佇列中未套用編輯的影像數量。

---

#### 導出預設

您可以在這裡保存和管理各種解析度的匯出配置。保存收藏夾以便快速存取。您可以同時選擇並套用多個預設，Evoto 將為每個預設匯出單獨的版本。

---

#### 效果預設

如果您尚未編輯過影像，則可以將效果預設套用於匯出的影像。這對於需要嚴格控制影像設定的自動匯入和匯出工作流程非常理想。如果影像已編輯，系統將在此部分預設使用「目前效果」。

*注意：即使您已套用編輯，也可以套用其他預設，並且 Evoto 將為每種選取的樣式產生單獨的版本*

---

#### 匯出設定

選擇儲存匯出影像的位置：

- **匯出至：**設定匯出檔案位置
- **現有文件：** 選擇如何處理匯出的現有文件。選項包括「新增後綴」（用於新增數字以建立唯一的檔案名稱）、「跳過」或「替換」。
- **路徑：顯示匯出影像的檔案路徑。**

**自動建立子資料夾：自動為匯出的檔案建立命名資料夾。**

---

#### 文件命名方法

Evoto提供了幾種文件命名方法：

1. **原始檔名**：保留原始名稱。
2. **自訂檔案名稱（# 個中的 # 個）**：新增自訂名稱和編號序列。
3. **拍攝日期 – 原始檔案名稱**：將拍攝日期新增至檔案名稱前面。
4. **自訂檔案名稱 - 序列**：為自訂檔案名稱加上編號後綴。
5. **原始檔案名稱 - 自訂文字**：將自訂文字新增至原始檔案名稱的末尾。
6. **原始檔案名稱 - 預設名稱：**在原始檔案名稱末尾新增效果預設的名稱（編輯期間套用）
7. **原始檔名 - 匯出預設**：在原始檔名末端新增匯出預設的名稱（匯出視窗中套用的解析度預設）
8. **原始檔案名稱 - 預設名稱 - 匯出預設**：在原始檔案名稱末端新增效果預設的名稱（編輯期間套用）和匯出預設的名稱（匯出視窗中套用的解析度預設）
9. **原始檔案名稱 - 預設名稱 - 自訂文字**：在原始檔案名稱末尾新增效果預設的名稱（編輯期間套用）和自訂文本

---

#### 影像尺寸

###### 秤類型

透過以下方式縮放影像導出：

- 按百分比
- 寬度與高度
- 像素
- 長邊
- 短邊
- 寬度
- 高度

您也可以透過以下方式設定影像解析度：

- 像素/英吋
- 像素/厘米

---

#### 文件設定

![](https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-27-17.07.50-300x201.png)

##### 圖片格式：

- **原始格式**
- **JPG**：（8 位）
- **TIFF**：（8 位元或 16 位元）

##### 品質:

- *僅適用於 JPG 匯出。*
- 限製檔案大小：
- 輸入目標尺寸，Evoto 將盡可能將影像壓縮到該值。
- 百分比：
- -
- 選擇：低、中、高或最佳，或使用滑桿進行調整

![](https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-27-17.09.12-300x162.png)

---

#### 出口調整

Evoto 包括針對螢幕和列印的客製化輸出銳利化設置

![](https://support.evoto.ai/wp-content/uploads/2025/04/Export-Adjustments-300x183.png)

- **選項：**
- 對於螢幕：
- 低/標準/高
- 對於列印：
- 低/標準/高
- 無銳化（預設）

---

#### 水印

Evoto 提供上傳自訂浮水印並調整其的選項：

- 旋轉
- 大小
- 不透明度
- 在影像上的位置

![](https://support.evoto.ai/wp-content/uploads/2025/04/Watermark-209x300.png)

---

### 導入和匯出疑難排解

##### 導入後影像預覽模糊

如果您的影像在匯入 Evoto 後顯得模糊，這可能是由於預覽設定造成的，而不是影像實際解析度的反映。

- Evoto 支援所有 RAW 檔案類型，並且**不會**降低原始影像的解析度。
- 預覽品質會根據您的電腦規格自動調整，這可能會導致顯示解析度降低，從而影響效能。

為了提高預覽清晰度：

1. 前往**設定 → 預覽 → 預覽大小**。
2. 根據需要增加預覽尺寸 - Evoto 最多支援 **4000 像素**，這是目前可用的最大預覽解析度。

***注意事項：** 預覽尺寸設定僅影響影像在 Evoto 中的顯示方式，不會影響匯出影像的品質或解析度。*

##### 匯出後文件大小發生變化

從 Evoto 匯出圖片後，您可能會注意到檔案大小有所差異。這是正常現象，通常是由於以下原因造成的：

- Evoto 使用最佳化的影像處理演算法，可以在編輯過程中改變內部像素結構。
- 根據所使用的內容、匯出格式和設置，這些更改可能會導致檔案大小變小或變大。

儘管檔案大小有所不同，匯出的影像仍將保持匯出配置指定的品質。

##### 目標資料夾中未找到匯出的影像

如果匯出的映像未出現在所選資料夾中，則問題可能與檔案權限有關。

請檢查以下內容：

- 確認**目標資料夾或磁碟機**允許 Evoto 寫入檔案。
- 某些**外部磁碟機**或**系統管理的資料夾**可能會限制寫入權限，預設只允許讀取權限。
- 確保 Evoto 對所選的匯出位置具有必要的**寫入權限。**

***注意**：授予對目標資料夾的完全寫入權限或選擇其他匯出目標通常可以解決此問題。*

##### 關於匯出設定品質的一些注意事項

當您將影像匯出為 JPG 或預設格式時，您可以透過兩種方式選擇品質：

- 限製檔案大小：

您可以為導出的圖像設定特定的檔案大小。但請注意，如果檔案未達到限制，則檔案大小將盡可能接近該值。

![](https://help.evoto.ai/~gitbook/image?url=https%3A%2F%2F2970798312-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9XghnFYmwxM9PPDFe9AG%252Fuploads%252FPbGPaangwQHP1uNtFHZl%252Fimage.png%3Falt%3Dmedia%26token%3Db52f13b0-37c3-4d56-b547-4409053b6a29&width=768&dpr=4&quality=100&sign=c06130aa&sv=2)

- 百分比：

您可以輸入 1 到 100 之間的特定數字來設定質量百分比。但請注意，即使您輸入的值很小，例如 1%，影像仍會以安全的百分比匯出，以確保導出影像的品質。

![](https://help.evoto.ai/~gitbook/image?url=https%3A%2F%2F2970798312-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9XghnFYmwxM9PPDFe9AG%252Fuploads%252FeOJqhpkys6B31RLaz3QN%252Fimage.png%3Falt%3Dmedia%26token%3Db12a3691-507f-415c-b3bd-c840cbb06acc&width=768&dpr=4&quality=100&sign=d19615d6&sv=2)

##### 保留圖像的原始標題/描述

如果您想保留圖像的原始標題或描述，您可以在 Evoto-->首選項-->導出-->圖像標題/描述-->顯示原始資訊中進行設定。

![](https://help.evoto.ai/~gitbook/image?url=https%3A%2F%2F2970798312-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9XghnFYmwxM9PPDFe9AG%252Fuploads%252FilPm1uscvNYRUpRwuVPX%252Fimage.png%3Falt%3Dmedia%26token%3D5b208d25-d7ce-4a57-972f-bb56942fa666&width=768&dpr=4&quality=100&sign=e713702e&sv=2)

---

#### 匯出錯誤程式碼

有關匯出過程中錯誤消息的更多資訊，請參閱我們的[匯出錯誤代碼](https://support.evoto.ai/error-codes-in-exporting-images/)清單
