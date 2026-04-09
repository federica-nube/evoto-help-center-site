---
title: "如何掌握 Evoto 的歷史記錄功能"
source_url: "https://support.evoto.ai/understanding-evotos-history-functions-general-history-liquify-history-and-healing-tool-history/"
source_type: "post"
source_id: "1736"
language: "zh-hant"
translation_group: "1736"
primary_category: "quick-tips"
secondary_categories:
  - "tips-tricks"
tags:
  - "tips"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-08-15-at-12.11.30-146x300.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-08-15-at-12.12.47-139x300.png"
---

Evoto’s History functions provide flexible and intuitive tools for tracking, managing, and refining your edits. These tools include the general History panel, as well as dedicated history modules for the Liquify and Healing features. Understanding how each one works will help you take full control of your editing workflow.

#### General History Panel

![](https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-08-15-at-12.11.30-146x300.png)

The floating **History** panel serves as the master timeline for all your edits. Every action is recorded in chronological order, allowing you to:

- View a comprehensive list of all editing steps.
- Revert to a specific point by clicking on an earlier step in the list.
- Reset all edits by clicking the image name or the trash icon.
- Recover changes after a reset by stepping forward through the list.

**Important:** Edits made using the Liquify or Healing Tool are grouped into a single line item within this panel. If you undo this step, all changes made during that session will be reverted at once.

#### Liquify and Healing Tool Histories

![](https://support.evoto.ai/wp-content/uploads/2025/04/Screenshot-2025-08-15-at-12.12.47-139x300.png)

Within the **Liquify** and **Healing Tool** panels, Evoto provides their own dedicated history modules. These panels allow you to:

- Track and undo the last 10 editing actions within the tool.
- Refine your edits step-by-step before finalizing.

當你在 Liquify 或 Healing Tool 面板中點擊 **儲存** 後，該次操作中的所有編輯都會合併成一般歷史記錄面板中的單一步驟。此時：

- The detailed tool-specific history is cleared.
- A new session will begin the next time you enter the tool, with its own separate history.

This design gives you precise, session-based control when using Liquify or Healing, while also consolidating your edits for easier management in the main history view. By using both types of history together, you can work more confidently and efficiently—editing with flexibility while maintaining precise control at every stage.

evoto-7-1-global-undo-redo
##### Global Undo / Redo in Evoto 7.1

Evoto 7.1 expands Undo / Redo support beyond simple effect-level edits, helping users recover from more types of common workflow mistakes.

###### Expanded support includes

- Effect application and synchronization
- Labeling, filtering, and some selection-state changes
- Virtual copy creation and deletion
- Some delete-to-trash actions

###### Behavior note

- Batch actions are generally treated as one undo step.

###### Current limits

- Switching cloud spaces does not support undo or redo.
- Permanent deletion, file renaming, metadata pull/push updates, and culling auto-tagging are still not supported.
- Actions that generate a new TSQ file cannot be undone.
- Undo history is not preserved after restarting the application.
