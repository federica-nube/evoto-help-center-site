---
title: "AI Culling in Evoto Instant"
source_url: "https://support.evoto.ai/ai-culling-in-evoto-instant/"
source_type: "post"
source_id: "14110"
language: "en"
translation_group: "6865"
primary_category: "instant-feature-deep-dive"
tags:
  - "instant"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-11.41.22-150x300.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-11.46.52-165x300.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.08.32-300x277.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.10.26-300x296.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.11.32-300x294.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.12.42-300x284.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.14.11-165x300.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.16.28-300x73.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.20.42-300x164.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.21.28-300x145.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.21.59-300x141.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.24.41-300x71.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/09/IMG_3447-471x1024.png"
---

Sorting through thousands of photos manually is time-consuming. AI Culling in Evoto Instant automates this step by evaluating both technical quality (sharpness, exposure) and aesthetic factors (facial expressions, posture). It intelligently flags issues such as blinks, blur, overexposure, underexposure, and duplicates—so you can focus on shooting while Instant does the heavy lifting.

---

#### How to Enable AI Culling

You can turn on AI Culling when creating a new project, toggle on **AI Culling** in the setup screen.

- For an existing project, open the project and enable **AI Culling** from the **Workflow** section.
- Once enabled, any new photos imported into the project will be automatically evaluated.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-11.41.22-150x300.png)

.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-11.46.52-165x300.png)

---

#### Setting Up Culling Rules

In the culling settings, you can customize which rules to apply. After making adjustments, click **Apply** to confirm.

##### Available Rules

- **Closed Eyes** – Detects when subjects have their eyes closed. Advance setting includes:
- **Laughing Photos**: choose whether closed-eye detection applies to laughing expressions.
- **Skip Detection in Group Photos**: set a threshold to ignore closed-eye detection when the photo contains more than a specified number of people.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.08.32-300x277.png)

- **Blur** – Flags images where subjects are blurred due to low shutter speed, camera shake, or motion.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.10.26-300x296.png)

- **Underexposure** – Detects photos where insufficient lighting causes loss of detail that cannot be recovered later.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.11.32-300x294.png)

- **Overexposure** – Detects photos where excessive lighting causes detail loss that cannot be restored.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.12.42-300x284.png)

- **Duplicates** – Groups similar photos and ranks them by quality score. Lower-scoring images within each group can be automatically hidden. Advance setting includes:
- Set how many of the best photos to keep within each duplicate group.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.14.11-165x300.png)

---

##### Sensitivity Levels

For **Blur, Underexposure, Overexposure,**and **Duplicates**, you can set a detection sensitivity level: **Low, Medium,**or **High**.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.16.28-300x73.png)

- Higher sensitivity = stricter filtering. More photos will be flagged, fewer will pass.
- Lower sensitivity = looser filtering. More photos will pass, but more flawed images may remain.

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.20.42-300x164.png)

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.21.28-300x145.png)

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.21.59-300x141.png)

For **Duplicates**, sensitivity controls **how similar photos must be to be grouped together**:

- Higher sensitivity = the AI is more effective at finding similarities, so **more** photos will be grouped together.
- Lower sensitivity = the AI is less aggressive, so **fewer** photos will be grouped.

---

##### Upload Settings

You can decide what happens to photos flagged by AI Culling:

![](https://support.evoto.ai/wp-content/uploads/2025/09/Screenshot-2025-09-12-at-14.24.41-300x71.png)

- Upload only the **photos approved by AI Culling**, or
- Upload **all photos** (including those flagged), so you can review later in the cloud.

This flexibility allows you to balance speed with thoroughness depending on your event needs.

---

#### AI Culling in Action

Once enabled, AI Culling works automatically in the background:

- **Culling in Progress** – New photos are analyzed as they enter the project. Each photo receives visual markers showing its culling status (e.g., icons for blur, closed eyes, etc.).
- **Uploading** – Photos that pass the rules are uploaded automatically, or held for manual upload depending on your settings.
- **Filtering** – Use the **Filter** button in the project to view photos by rule (e.g., only blurred photos, only duplicates) and make quick comparisons.

![](https://support.evoto.ai/wp-content/uploads/2025/09/IMG_3447-471x1024.png)

---

AI Culling in Evoto Instant streamlines one of the most repetitive parts of photography—sorting through flawed or duplicate images. By customizing rules, sensitivity levels, and upload settings, you can decide how strict or flexible the process should be. With Instant handling culling in real time, you save hours of manual sorting and deliver cleaner galleries faster.
