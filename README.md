# Hackpad2
Revised hackpad submission. A custom hackpad/macropad featuring 4 mechanical key switches, a rotary encoder with a push-button function, an acrylic & 3D-printed sandwich enclosure, and KMK firmware running on CircuitPython.

<img width="787" height="529" alt="PCB" src="https://github.com/user-attachments/assets/5f50a298-0557-4be2-a293-214c8f5e0b44" />

*Note that if these images are still broken, these are the same images as the ones in Assets*

---

## Features

* **Microcontroller:** Seeed Studio XIAO.
* **Inputs:** 4 direct-wired MX mechanical key switches + 1 rotary encoder with integrated push switch.
* **Firmware:** [KMK Firmware](https://github.com/KMKFW/kmk_firmware) on CircuitPython for drag-and-drop keymap edits.
* **CAD:** Sandwich design consisting of a 3D-printed top cover, main base, column and a laser-cut acrylic "window" Assembled using M3 standoffs and machine screws.
*Note: the "column" is not attached to the top because it is 3D printed - it will be attached separately*
* **PCB:** Designed in Kicad:

<img width="715" height="620" alt="Schematics" src="https://github.com/user-attachments/assets/1822cd59-eb57-40c8-b6ff-fd57d8b590d3" />

<img width="778" height="480" alt="CAD" src="https://github.com/user-attachments/assets/e16f5cf3-c7a3-4e62-8648-0d7429a840af" />


---

## Keymaps
  * **Encoder:** Rotate for Previous/Next Track; Press for Play/Pause.
  * **SW1, SW2, SW3:** Undo (`Ctrl+Z`), Copy (`Ctrl+C`), Paste (`Ctrl+V`).
   I might later add multiple command layers

