---
title: "Crop Module"
source_url: "https://support.evoto.ai/crop/"
source_type: "post"
source_id: "625"
language: "en"
translation_group: "625"
primary_category: "crop"
secondary_categories:
  - "crop-rotate"
tags:
  - "pc"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-26-at-16.49.32-155x300.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/20250425161036-300x99.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-26-at-16.52.29-281x300.png"
---

Evoto offers multiple cropping methods to suit different needs, including fixed ratio, free-sizing, and custom input dimensions. After adjusting the crop, click **OK** in the lower right corner to apply the result. **Crop Types** ![](https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-26-at-16.49.32-155x300.png) **Original**Crops the image based on the original dimensions imported into Evoto. **As Shot**Uses the dimensions as captured by the camera. **Fixed Ratio**Enter a fixed width and height ratio to manually crop the image while maintaining the specified proportion. *Note: Supports AI Face Locate and can be saved as a preset so long as there isn’t more than one face in the image and the face isn’t turned more than 75 degrees* **Free**Allows freeform cropping by directly dragging the crop frame on the canvas. Aspect ratio and dimensions can be adjusted freely. **W × H × Resolution**Define exact width, height, and resolution for precise cropping. **ID Photo**Designed for professional headshots and ID photos. With a default of **300 PPI**, this mode ensures high-quality print output. *Note: Best used when the crop unit is set to cm or inches.* **My Crop Preset Customize and save your preferred cropping parameters. Click Create Crop Preset to save settings for future use. *Note: Presets saved in this section will also appear under AI Headshot Cropping and will be removed from both lists when deleted.*** ![](https://support.evoto.ai/wp-content/uploads/2025/04/20250425161036-300x99.jpg) **AI Locate** ![](https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-06-26-at-16.52.29-281x300.png) AI Locate can be toggled on in the following crop types: **Fixed Ratio, 1:1, 4:5, 5:7, 2:3, 16:9, 1.91:1, 2:1, 3:1, 4:3, W × H × Resolution, ID Photo** When enabled, the AI Locate feature intelligently selects complete subjects and adjusts their distance percentage from crop boundaries, including: Crop positioning based on Subject location Crop positioning based on Face location **Person Auto Alignment** The "Person Auto Alignment" feature in AI Locate module (single-person photos only): Vertical alignment using subject's central axis Horizontal alignment using eye-level baseline **Locate Area Options** **Head**: Includes face and hair **Head + Top**: Includes face, hair, and any headwear **Face**: Focuses strictly on the face **Adjustment Sliders** **Top Margin**Adjusts the space between the top of the head and the top edge of the photo. **Head Size**Controls how large the head appears in the final image. **Horizontal Face Position**Sets where the face appears horizontally in the image: **50** = face centered **25** = face shifted left **75** = face shifted right ***Note:****When using W × H × Resolution cropping, you may set a custom resolution. ID Photo cropping defaults to 300 PPI. Other cropping types will use the image’s original resolution.*

****Image Dimensions and Edge Cases**** AI Headshot Crop is disabled when: The image contains more than one person The subject’s face is tilted more than 75 degrees Image dimension and face position settings cannot be left empty. When crop sliders exceed allowable values, they will automatically return to the nearest valid range. If the crop frame is moved outside the face-detection zone, the face position module is disabled until the crop returns to a valid range. **Synchronizing Settings:**When syncing crop settings from Image A to Image B: If **Image B** has no detectable face or contains multiple faces, cropping will **not** be synced. If synced values exceed the supported range in Image B, they will be adjusted to the closest allowable threshold.
