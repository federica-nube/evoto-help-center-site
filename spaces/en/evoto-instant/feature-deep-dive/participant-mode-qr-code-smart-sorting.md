---
title: "Participant Mode & QR Code Smart Sorting"
source_url: "https://support.evoto.ai/participant-mode-qr-code-smart-sorting/"
source_type: "post"
source_id: "23968"
language: "en"
translation_group: "8003"
primary_category: "instant-feature-deep-dive"
tags:
  - "instant"
---

**Participant Mode** solves the challenge of high-volume photo management. By uploading a roster with names and emails, the system generates unique QR codes for every participant.

This enables **AI Grouping** to sort photos automatically during the shoot and generates unique gallery links and access codes for each participant, ensuring data privacy and security.

### Project Setup & Roster Import

To start, you must define who you are photographing by importing a participant list.

#### Project Creation

-
- Select **School Mode** when creating a project.
- The system defaults to **Participant Mode** with **Password Protection** enabled.

> Note: If you wish to change the security settings (e.g., to Password-Free), you can do so in the Basic Info tab. You can switch between School and Classic modes initially, but once a roster or photo is added to a School Project, you cannot switch back.

#### Importing Data

-
- Go to the **Participant** tab and upload your roster. Please use the downloadable template on-site.
- **Format:** Supports .csv, .xls, .xlsx (up to 10MB).
- **Requirements:** "Name" and "Email" are required fields.
- **Validation:** The system automatically checks for duplicates and formatting errors (e.g., invalid emails).

#### Managing the List

-
- You can search for names or use "Re-import" to append new participants to the list.

> Note: Y ou cannot edit participant details (such as spelling) directly in the app. To fix an error, you must delete the entry and re-import it. Deleting a participant will also delete all photos associated with them.

### QR Code Workflow

The system generates a unique QR code for every participant, linking the physical shoot to the digital gallery.

- **Generating Codes:** Select participants in the list and click **Download QR Code**. You can choose a layout (1 or 2 cards per page) to print.
- You scan the card during the shoot to tell the system, "The next photos belong to this student."
- The card contains the unique Gallery Link and Access Code for the parent/student to log in later.

#### Shooting & Sorting Methods

There are three ways to organize photos into participant folders. Choose the method that fits your on-site workflow.

##### Method A: Mobile AI Auto-Grouping

This method uses real-time QR code detection while **tethered** to the mobile app.

1. **Workflow:** Photograph the student holding their **QR card** first, then take their portraits.
2. **Auto-Sort:** The AI detects the QR code and automatically routes all subsequent photos into that student's folder until a new code is scanned.
3. **Requirements:**
- Requires an internet connection.
- Note: The photo containing the QR code is also uploaded to the gallery.

##### Method B: Mobile Manual Sorting (Tethered Only)

You can also shoot without printed QR cards by manually selecting names.

1. **Workflow:** Connect your camera and tap **Enter Manual Grouping Mode** on the app.
2. **Operation:**
- Tap a name from the roster list.
- Begin shooting; photos will route to that student.
- Tap **Complete & Next** to automatically switch to the next person on the list (or manually tap another name to switch).
3. **Status:** The list tracks subjects as Not Started, In Progress, or Completed.

##### Method C: Web AI Sorting (Post-Shoot)

If you prefer to sort after the event, you can process images in bulk on the Web Portal.

1. **Workflow:** Shoot with QR cards on-site. Afterwards, upload all photos to the web project's **All-AI Grouping** module.
2. **Operation:** Once uploaded, the system will scan for QR codes and move images to the correct folders automatically.

> Handling Unsorted Photos: If a QR code is blurry or the image format is unsupported (e.g., certain RAWs), the photos will appear in the "Ungrouped" folder. Simply select the photos and move them to the correct folder manually. This is available on both the Web Portal and Mobile App.

### Delivery & Privacy

Participant Mode enforces strict privacy standards for schools.

- **No Face Recognition:** To ensure privacy compliance, the "Find Me" (Face Recognition) feature is **disabled** in this mode.
- **Access Control:**
- **Verification:** Parents access the gallery via their unique link or by scanning their QR card. If password protection is enabled, they must enter their 4-digit **Access Code** (e.g., A3K9). Note: Currently, there is no limit on retry attempts for incorrect codes.
- **Private View:** Once verified, they see **only** their own photos.
- **Sending Emails:**
- Use the **Share Email** button to send individual gallery links to all participants in bulk.
