---
title: "How to Import .XMP and .CUBE Files in Evoto"
source_url: "https://support.evoto.ai/how-to-import-xmp-and-cube-files-in-evoto/"
source_type: "post"
source_id: "1726"
language: "zh-hant"
translation_group: "1726"
primary_category: "quick-tips"
secondary_categories:
  - "tips-tricks"
tags:
  - "tips"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-08-15-at-12.03.58-300x51.png"
---

Color grading is a powerful tool for photographers and editors, and Evoto makes it easy to integrate industry-standard presets into your workflow. This guide will walk you through the simple process of importing .XMP and .CUBE files, allowing you to seamlessly apply your favorite color adjustments.

#### Why Use .XMP and .CUBE Files?

These file formats are widely used to save specific color adjustments and share them across different projects and software. Evoto's compatibility with these formats ensures you can bring your favorite presets directly into your editing process, making color transitions smoother and enhancing your overall workflow.

#### How to Import .XMP and .CUBE Files in Evoto

Importing these files has become a straightforward process.

#####

![](https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-08-15-at-12.03.58-300x51.png)

###### Step 1: Access the Import Preset Option

首先，打開 Evoto 並前往 **Presets** 面板。點擊 **➕（Plus）** 圖示後，選擇 **Import Preset**。接著你會看到 **「Local Files (.xmp/.cube)」** 的選項，這就是匯入流程的起點。

###### 步驟 2：匯入 .XMP 檔案

如果你有 .XMP 檔案，只要選取後匯入 Evoto 即可。匯入完成後，Evoto 會自動在 **「My Presets」** 中建立新的預設，方便你之後快速使用。

###### 步驟 3：匯入 .CUBE 檔案或包含 LUT 資訊的 .XMP 檔案

如果你使用的是 .CUBE 檔案，或是包含 LUT（Look-Up Table）資訊的 .XMP 檔案，匯入方式也一樣簡單。匯入後系統會自動建立一個包含 **Profile** 資訊的預設，並與其他預設一起儲存在同一位置，方便快速存取。

支援匯入這些常見格式，能讓你的編修流程更順暢，並透過無縫的色彩調整發揮更多創作可能。

evoto-7-1-xmp-profile-support
##### New in Evoto 7.1: Missing Profile Detection

If an imported XMP file includes a custom Profile that is not currently installed in Evoto, the system automatically identifies the missing Profile and prompts the user to import it so the intended result can be restored more accurately.

###### Why it matters

- Reduces restoration errors caused by missing custom Profiles.
- Improves compatibility with external color workflows.
- Keeps imported adjustments and final rendering more consistent.
