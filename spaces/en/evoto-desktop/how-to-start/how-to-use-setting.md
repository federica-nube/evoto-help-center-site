---
title: "System Settings"
source_url: "https://support.evoto.ai/how-to-use-setting/"
source_type: "post"
source_id: "598"
language: "en"
translation_group: "598"
primary_category: "how-to-start"
tags:
  - "pc"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-27-11.06.22-300x247.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-26-20.08.30-300x58.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-26-20.11.31-272x300.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-26-20.12.21-300x248.png"
---

Evoto's system settings allow you to optimize performance, manage cache, control preview behavior, and customize export options to best suit your workflow and hardware.
---

### Performance

These settings help improve processing speed depending on your device's capabilities.
![](https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-27-11.06.22-300x247.png)

---

#### Rendering Speed Settings

Evoto offers several settings to improve rendering performance, particularly during complex edits or high-volume workflows. Adjusting these options can accelerate preview and export processes while balancing resource usage and output quality.
##### Preview Speed

These settings help speed up effect previews by allocating more system resources to the rendering process:
- **Portrait Effect Rendering Acceleration:**Uses more of your computer’s processing power to accelerate the rendering of portrait-related effects during preview.
- ****Color Effect Rendering Acceleration**:******Uses more processing power to accelerate the rendering of color-related adjustments during preview.****

---

##### Export Speed

Evoto applies effects a second time when exporting images to ensure maximum quality. You can enable the following setting to speed up this process:
- **Portrait Effect Rendering Acceleration (Export):** Allocates more processing power to portrait effect rendering during export for faster performance. *Note: Evoto must be restarted after enabling this setting for it to take effect.*

---

##### Group Portrait Optimization

For photos with many subjects (typically 15 or more), Evoto provides an option to improve processing speed:
- **Improve Effect Processing Speed of Group Portraits:**Speeds up rendering for large group portraits. This may slightly reduce the precision of certain effects but greatly enhances processing speed. Disabling this feature will ensure greater group effect accuracy but will result in slower processing speeds.

---

#### Memory Usage Settings

Optimizing memory usage helps maintain a stable and responsive editing environment. These options control how Evoto manages memory during both preview and export phases: Preview Phase:
- **Improve Memory Utilization:** Enhances how efficiently memory is used during effect previews.
- **Optimize Memory Space:** Frees up additional memory resources to improve preview performance.

Export Phase:
- **Improve Memory Utilization:** Increases export speed by improving memory management during the export process.
- **Optimize Memory Space:** Maximizes available memory to ensure stable and efficient exporting.

Note: A restart of Evoto is required for memory settings to take effect.
---

#### Network Settings

- Request Timeout Duration - Change the duration the system will try to find a stable internet connection before presenting a timeout error message. The system default is 3 minutes (180 seconds)

---

### Export

- **Max Simultaneous Exports** Evoto sets this automatically based on your system. Increasing the number may impact system performance. Adjust only if necessary.
- **Image Caption/Description** Choose whether exported image metadata includes:
- **Evoto** (default)
- **Original Information** (from the source image)

---

### Cache

Manage Evoto’s cache settings via:
- **Windows**: Go to *Personal Center → Settings → Cache*
- **macOS**: Use *Evoto → Preferences* or press Command + ,

Cache settings include:
- **Cache Expiration**: Set automatic cache clearance between 3–15 days.
- **Manual Cache Clearing**: Click **Clear Cache** to remove stored data immediately. *Note: This will delete all history of manual adjustments such as liquify, manual brush strokes, and brush repairs*
- **Maximum Cache Size**: Set a storage limit. When exceeded, cache will be automatically cleared.

---

### Preview

Preview settings allow you to customize how images appear while editing, without affecting final exports.
- **Color Space**Choose the preview color space:
- **sRGB** (default, recommended for web use)
- **Adobe RGB** (for wider color gamut on supported displays)
- **Preview Size (px)**Adjust the preview resolution. Evoto selects a default based on your system. This does *not* affect exported image quality.
- **Full-Size Preview in Real-time Color Adjustments:** With this option on, previews in Real-Time Color Adjustments mode will be at full resolution no matter that Preview Size (px) settings
- **Thumbnail Settings**Manage how image thumbnails are displayed in the Gallery.
- **Effect Loading Settings** *(applies only if “Show Edited Images” is enabled in Thumbnail Settings)* The preview preloading feature will help you to to preload the effect applied to the other pictures while you are syncing, to save you waiting time. This feature will help you while you sync the effect to other images. When you click on the picture you have synced, you will see the final feature-applied result without waiting Please note if you are using a Windows computer, you have to have hardware with at least 8GB of memory. A MacBook computer is not restricted to this requirement.
- **Synced Preview Position and Scale Settings**When enabled, Evoto remembers your last-used zoom level and position for each image. You can further adjust this behavior in the Preview Settings popup as needed.

---

### Software Usage

Share My Usage Information You can choose whether to share your usage data with Evoto. This data is linked to your account and used solely to personalize your experience and help improve our services. All shared data is collected anonymously. You may disable data sharing at any time from this menu. Content Analysis Evoto may analyze your content using machine learning and similar techniques to enhance product quality. All analysis is anonymous, and you can opt out at any time. Note that in some limited cases, this setting may not apply. Learn more .
---

### Preferences

#### Pop-up Frequency Settings

By default, Evoto is set to show the Sync Settings pop-up only once per project. This means:
- The first time you sync or copy/paste settings, you'll see a pop-up where you can choose which adjustments to apply.
- After that, syncing or pasting will automatically apply the previously selected settings without showing the pop-up again.

If you'd prefer to see the settings selection box every time you sync or copy/paste:
1. Click the **Settings** button next to **Sync** in the bottom-right corner of the screen.

![](https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-26-20.08.30-300x58.png)
2. In the pop-up window, click **Pop-up Frequency Settings** in the upper-right corner.

![](https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-26-20.11.31-272x300.png)
3. Change the setting to **Always Trigger**.

![](https://support.evoto.ai/wp-content/uploads/2025/04/截屏2025-05-26-20.12.21-300x248.png)
4. Click **OK** to save and close.

With this setting enabled, you'll be able to confirm or adjust which edits get applied with every sync or paste action.
---

Tethered Shooting Auto-connect to Camera Enable this option to automatically connect your camera to Evoto when using a tether cable. If disabled, you will need to manually connect your camera each time it is plugged in.
---

#### Workspace Switch Settings

Auto Switch to Edit When enabled, importing images into an empty project will automatically switch the workspace to Edit view.
