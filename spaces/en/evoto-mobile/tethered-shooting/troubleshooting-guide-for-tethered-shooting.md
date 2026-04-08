---
title: "Troubleshooting Guide for Tethered Shooting"
source_url: "https://support.evoto.ai/troubleshooting-guide-for-tethered-shooting/"
source_type: "post"
source_id: "15831"
language: "en"
translation_group: "7074"
primary_category: "tethered-shooting"
secondary_categories:
  - "uncategorized-en"
tags:
  - "mobile"
migration_flags:
  - "image"
source_assets:
  - "https://support.evoto.ai/wp-content/uploads/2025/10/1-300x259.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/10/2-300x259.jpg"
  - "https://support.evoto.ai/wp-content/uploads/2025/10/image-2-300x63.png"
  - "https://support.evoto.ai/wp-content/uploads/2025/10/de0daf85972c4ad03933db1bd8ec272e-300x49.png"
---

#### Platform Issues

The current version of **Evoto** can run on devices with **Windows, macOS, iOS, iOS, and Android** systems, including computers, tablets, and mobile phones.

##### PC Version

- **macOS 14.2:** Tethered shooting is not available; please upgrade your system to use this feature.
- **macOS 13.0 and above:** Required for tethered shooting with Panasonic, Leica, Olympus (OM System), and other supported cameras.
- **macOS 15.0 and above:** You need to enable **Files and Folders** permissions under **Privacy Settings**.

![](https://support.evoto.ai/wp-content/uploads/2025/10/1-300x259.jpg)

![](https://support.evoto.ai/wp-content/uploads/2025/10/2-300x259.jpg)
- **macOS 10.15:** For wired tethered shooting, you need to enable **Files and Folders → Removable Volumes** permissions.

##### Mobile Version

- **iOS/iOS 16.0 and above:** Required for tethered shooting with Panasonic, Leica, Olympus (OM System), and other supported cameras.
- **iOS/iOS 18.0:** If you cannot open permissions and Evoto does not appear under **Files and Folders Permissions**, tethered shooting will not work; please upgrade your system.
- **iOS/iOS Beta 26.1:** Tethered shooting is not supported; upgrade with caution.
- **Android phones:** Some devices require enabling OTG. Go to **Settings → Search → Enter “OTG” → OTG Connection** and turn it on. If no OTG option appears, your phone has OTG enabled by default.
- **Fujifilm cameras with mobile devices:** Often the camera may be recognized incorrectly as the main device, charging the mobile device (tablet, phone, etc.). There is currently no solution for this issue.

##### How to Check if Physical Connection is Successful

- **Windows:** Open **Device Manager** and check if the camera appears under **Portable Devices**. If visible, the physical connection is successful.
- Some Sony cameras may install Sony control software and show **libusbk** in Device Manager. Uninstall this driver (check **Delete the driver software for this device**) and refresh Device Manager to see the camera correctly as a portable device.

![](https://support.evoto.ai/wp-content/uploads/2025/10/image-2-300x63.png)
- **macOS:** Open the **Photos** app and check for a device named after the camera model.
- **mobile device:** Open **Photos** and check for the camera model.
- **iPhone:** Open **Photos** and check for the camera model.
- **Android phones:** Pull down the notification bar and check if a device is connected to the phone.

#### Camera-Side Issues

For camera setup instructions, please refer to the corresponding help guides. This document only summarizes specific camera-related issues.

##### Wired Tethering

###### Canon

**Official Canon error code explanation:**[https://cam.start.canon/zh/C003/manual/html/UG-06_Network_0210.html](https://cam.start.canon/zh/C003/manual/html/UG-06_Network_0210.html)

**Model: 5D4**

**Issue 1:** Slow image transfer speed on Windows PC; black preview screen; image takes a long time to transfer.

**Solution:** Connect to a USB 3.0 or higher port. Confirm connection using USB Device Tree Viewer.

![](https://support.evoto.ai/wp-content/uploads/2025/10/de0daf85972c4ad03933db1bd8ec272e-300x49.png)

**Issue 2:** On macOS, the “Photos” app can recognize and read the camera’s SD card, but Evoto cannot tether.

**Solution:**

- If on macOS 14.2, please upgrade the system.
- If using a version earlier than 14.2, update the camera firmware.

**Issue 3:** When live view is enabled, captured images appear extremely dark or nearly black.

**Solution:** Known affected models: 5D4 / 1DX2. Firmware update recommended.

**Issue 4:** Flash cannot be used in tethered shooting.

**Solution:** Currently no fix. Disable live view when flash is needed.

**Model: All**

**Issue 1:** The image quality setting on the camera shows “20M,” but transferred photos on the computer are only a few MB in size.

**Explanation:** The “Image Quality” setting (e.g., “L 20M 5472×3648”) indicates 20 megapixels—not file size. Compare the image size saved on the SD card with the one transferred during tethering; they should be identical.

**Model: R62 / R8 and similar**

**Issue 1:** After successful tethering, photos fail to import into Evoto or the capture button becomes unresponsive.

**Solution:** Reset the camera to factory settings. Known affected models: Canon R6 Mark II / R8.

---

###### Sony

**Model: All**

**Issue 1:** Tethering successful, but photos do not transfer.

**Solution:** Set to “Destination Only” or “Dest. + Camera”.

**Issue 2:** Photo transfer only works for the first few shots, then stops—or the first few fail, and later ones succeed.

**Solution:** Reset camera settings: `MENU → (Setup) → [Initialize] → Factory Reset`. Then power off the camera, remove and reinsert the battery, and restart.

**Issue 3:** Connection drops immediately after tethering, or during photo capture.

**Solution:**

- Disable USB Power Supply in camera settings.
- Use cables shorter than 2 meters for mobile devices.

**Model: ILCE-7RM5 (A7R5), ILME-FX3**

**Issue 1:** Tethering successful but cannot transfer images; live view shows a black screen.

**Solution:** Update firmware.

**Model: ILCE-6000 (A6000), ILCE-7RM2 (A7R2)**

**Issue 1:** Cannot save photos to SD card during tethering.

**Solution:** No available workaround.

---

###### Nikon

**Model: All**

**Issue 1:** Connection drops immediately after tethering, or during photo capture.

**Solution:**

- Set “USB Power Delivery” to **Off** in camera settings.
- Use tethering cables shorter than 2 meters for mobile devices.

---

###### Fujifilm

**Model:** All

**Issue 1:** The camera draws power from the PC or mobile device, but this usually doesn’t affect tethered shooting.

**Solution:** Try disabling the USB power supply option in the camera settings.

**Model:** X-T5 / X-H2 / X-H2S, etc.

**Issue 1:** When connected to a mobile device (phone or tablet) via USB, the mobile device fails to recognize the camera and tethering cannot be established.

**Solution:** This is a hardware-level conflict and currently has no solution.

**Issue 2:** When connecting to a OnePlus Ace 3 phone via USB, there’s no response, and the camera may become unresponsive.

**Solution:** This is a hardware-level conflict and currently has no solution.

---

###### Panasonic

**Model:** All

**Issue 1:** When tethering with a mobile device (phone or tablet) that doesn’t have a memory card inserted, image transfer after shooting fails.

**Solution:** Under development.

---

###### Olympus (OM System)

**Model:** All

**Issue 1:** When tethering with a mobile device (phone or tablet) that doesn’t have a memory card inserted, image transfer after shooting fails.

**Solution:** Under development.

##### Wireless Tethering

###### Canon

**Model:** All

**Issue 1:** Wireless transfer is slow.

**Solution:**

- Test the speed using Canon’s own wireless tethering software to see if there’s any improvement.
- Alternatively, enable the camera’s hotspot and connect the PC or mobile device directly to it to reduce router interference and increase speed.
- If currently using a 2.4GHz network, switch to a 5GHz network for faster transfer.

**Issue 2:** In-camera settings: `Menu → Shooting Settings → Image Quality → RAW+JPEG (JPEG format: L/M/S, etc.).` Even if wireless transfer is set to JPEG only: `Menu → Wireless → Connect to EOS Utility → Set Direct Transfer → Transfer JPEG Only`, the camera still transfers both RAW and JPEG files during wireless tethering.

**Solution:** Currently unresolved.

**Issue 3:** The Evoto software can detect the camera name, but connection fails after clicking “Connect.”

**Solution:** Set the camera to pairing mode and perform the pairing process directly within Evoto.

---

###### Sony

**Model:** All

**Issue 1:** Wireless transfer is slow.

**Solution:**

- Check if the connection is on a 2.4GHz network; switching to 5GHz can greatly improve transfer speed.
- In Remote PC settings, choose to transfer only JPEGs for preview purposes, while saving RAW files on the SD card in the camera.

**Issue 2:** The camera shows “Connected via wireless tethering,” but Evoto displays a connection failure when attempting to connect.

**Solution:** Check if any nearby devices are currently connected to the camera via wireless tethering. If so, disable tethering on those devices first.

---

###### Nikon

**Models:** Z6II, Z7II, etc.

**Issue 1:** After connecting the camera to an external Wi-Fi network, the software cannot detect the camera no matter what.

**Solution:** Check the router address of the Wi-Fi network your PC or mobile device is connected to. For example, if your router address is **192.168.1.1**, set your camera’s IP address manually using the same first three groups of numbers (e.g., **192.168.1.153**). Make sure the last number is unique within your network. After saving the settings, you should be able to connect your camera wirelessly for tethered shooting.

---

###### Fujifilm

**Models:** X-T5, etc.

**Issue 1:** When wirelessly tethered, captured photos are not saved on the camera’s SD card.

**Solution:** This behavior is by design and currently cannot be changed.

**Models:** X-T5, X-H2, X-H2S, etc.

**Issue 2:** The camera has been successfully connected to Wi-Fi and set to *Wireless Tethering Mode*, but Evoto still cannot detect the camera.

**Solution:** Reconnect to the Wi-Fi network and make sure the password is correct, or try connecting to a different Wi-Fi network for tethering.
