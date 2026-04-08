---
title: "Troubleshooting Installation & Antivirus Conflicts"
source_url: "https://support.evoto.ai/installation-faqs/"
source_type: "post"
source_id: "9536"
language: "en"
translation_group: "6278"
primary_category: "faq"
tags:
  - "faq"
  - "pc"
---

This guide addresses common issues where Evoto might be blocked by your operating system or antivirus software, providing steps to ensure smooth installation and operation.

---

#### How to fix "Evoto can’t be opened because it was not downloaded from the App Store" error on Mac?

This error occurs when macOS Gatekeeper, a security feature, prevents applications from opening if they are not downloaded from the App Store or identified developers.

To resolve this error, follow these instructions:

1. Click **OK** on the dialog box that displays the error message.
2. Open **System Settings** (for macOS Ventura 13 and later) or **System Preferences** (for macOS Monterey 12 and earlier).
3. Navigate to **"Privacy & Security"** (or **"Security & Privacy"** for older macOS versions).
4. Go to the **“General”** tab.
5. Click the **lock icon** in the bottom-left corner and authenticate with an administrator account login and password for your Mac.
6. Look for the section **“Allow applications downloaded from:”** and select the option **“App Store and identified developers”**.
7. Alternatively, if you've just seen the error message for Evoto, you may see a specific "Open Anyway" button next to Evoto's name within the "General" tab of Security & Privacy/Privacy & Security. You can click this for a one-time override.
8. Close System Settings/Preferences.
9. Now return to the Evoto app and launch it again. It should open without issues.

---

#### How do I allow Evoto through Windows Antivirus?

Antivirus and anti-malware programs may sometimes flag or restrict Evoto-related processes, preventing the software from running smoothly. By creating an exclusion or whitelist entry, you can ensure Evoto operates without interference.

**Important:** The exact steps and menu paths may vary slightly depending on your antivirus software version. It is recommended to exclude the entire Evoto installation folder (e.g., C:\Program Files\Evoto or C:\Program Files (x86)\Evoto) for comprehensive protection against conflicts.

###### Windows Defender

1. Open **Windows Security** (often found in the notification area or by searching in the Start menu).
2. Select **Virus & threat protection**.
3. Click **Virus & threat protection settings**.
4. Scroll down to the **"Exclusions"** section and click **"Add or remove exclusions"**.
5. Click **"Add an exclusion"** and select **"Folder"**.
6. Navigate to and select the **Evoto installation folder** (e.g., C:\Program Files\Evoto).
7. Click **"Select Folder"** to confirm the exclusion.

*For more detailed instructions, please refer to:*[*Add an exclusion to Windows Security*](https://www.google.com/search?q=https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-ad47-27b9-e67324b2ce26)

###### McAfee

1. Open your **McAfee Security software**.
2. Navigate to **PC Security** (or similar) and then **Firewall**.
3. Look for **"Internet Connections for Programs"** or **"Program Permissions."**
4. **If Evoto is in the list:**
- Select Evoto and click **Edit** (often at the bottom of the list).
- Under **Access**, ensure that **Incoming and Outgoing** is selected, then change the type from **Default** to **Open to all devices**.
- *Note: You can also choose to Use designated ports if you know which specific ports Evoto utilizes.*
- Click **Save**.
5. **If Evoto isn't on the list:**
- Click **Add**.
- Click **Browse** and locate the **Evoto executable file** (e.g., Evoto.exe in the installation folder) to add it.
- Select Evoto and click **Open**.
- Under **Access**, ensure that **Incoming and outgoing** is selected, then change the type from **Default** to **Open to all devices**.
- Click **Save**.
6. After making these changes, Evoto should now run without being blocked.

*For more detailed instructions, please refer to:*[*How to exclude files from virus scans on Windows - McAfee*](https://www.google.com/search?q=https://www.mcafee.com/support/%3FarticleId%3DTS100813%26page%3Dshell%26shellPage%3Ddevice-security/firewall/firewall-rules)

###### Avast

1. Open the **Avast user interface** (usually from the notification area or desktop shortcut).
2. Go to **Settings** (gear icon).
3. Choose **General**.
4. Select **Exclusions**.
5. Click on the **"File Paths"** tab and then click **"Browse"**.
6. Navigate to the **Evoto installation folder** (e.g., C:\Program Files\Evoto).
7. You can choose to exclude the entirety of the folder or just individual executable files (like Evoto.exe). Excluding the folder is generally recommended.
8. Confirm changes and ensure your real-time protection is re-enabled.

*For more detailed instructions, please refer to:*[*Avast Antivirus scan exclusions*](https://support.avast.com/en-us/article/Antivirus-scan-exclusions/)

###### ESET

1. Open **ESET Smart Security** or **ESET NOD32 Antivirus** (from the notification area or desktop shortcut).
2. Press **F5** to open the **Advanced Setup** window.
3. Expand **Antivirus and antispyware**.
4. Select **Exclusions**.
5. Click on **Add** in the right pane.
6. Follow the path to the **Evoto installation folder** (e.g., C:\Program Files\Evoto) and select it to exclude it. You can exclude the containing folder for simplicity.
7. Confirm changes by clicking **OK** and ensure real-time protection is turned on again.

*For more detailed instructions, please refer to:*[*Exclude an application by name from scanning in ESET Windows home products*](https://www.google.com/search?q=https://support.eset.com/en/kb2779-exclude-an-application-by-name-from-scanning-in-eset-windows-home-products)

###### Avira

1. Right-click on the **Avira icon** in the notification area and temporarily **disable real-time protection**.
2. Once Evoto is installed, re-enable Avira's real-time protection.
3. Open the **Avira user interface**.
4. Navigate to **Protection** → **Real-time protection** (or similar path depending on your Avira product).
5. Look for **"Exceptions"** or **"Exclusions"**.
6. Click **"Add"**.
7. Browse to and select the **Evoto installation folder** (e.g., C:\Program Files\Evoto) or the main Evoto.exe file.
8. Confirm changes and ensure real-time protection is enabled again.

*For specific instructions tailored to your Avira product version, please consult Avira's official support documentation.*

###### Bitdefender

1. Open your **Bitdefender security software**.
2. Click on the **Protection** module.
3. Choose **View features** (or similar, if not directly visible).
4. Select **Settings** for the Antivirus protection.
5. Open the **Exclusions** tab.
6. Click on the **"List of files and folders excluded from scanning"** (or similar) and then click **"Add"**.
7. Browse to and add the **Evoto installation folder** (e.g., C:\Program Files\Evoto) or the specific Evoto.exe file you want to exclude.
8. Confirm the selection and ensure Real-time protection is re-enabled.

*For more detailed instructions, please refer to:*[*How to exclude files and folders from Bitdefender Antivirus scan*](https://www.google.com/search?q=https://www.bitdefender.com/consumer/support/article/19875/)

###### Malwarebytes

1. Open **Malwarebytes**.
2. Select **Settings** (gear icon).
3. Choose **Malware Exclusions** (or **"Allow List"**).
4. Click **"Add file"** if you want to exclude a specific executable file (like Evoto.exe) or **"Add folder"** if you want to exclude the entire Evoto installation directory.
5. Follow the path and select the file/folder (e.g., C:\Program Files\Evoto) you want to exclude from future scans.
6. Confirm the selection and run the program.

*For more detailed instructions, please refer to:*[*Manage the Allow List in Malwarebytes for Windows v4*](https://www.google.com/search?q=https://support.malwarebytes.com/hc/en-us/articles/360038479534-Manage-the-Allow-List-in-Malwarebytes-for-Windows-v4)
