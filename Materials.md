### Hackpad — Bill of Materials (BOM)

## 1. Electronics & Components

| Item | Qty | Specifications / Notes |
| :--- | :---: | :--- |
| **Microcontroller** | 1 | Seeed Studio XIAO (RP2040 or SAMD21 variant) |
| **Key Switches** | 4 | MX-compatible mechanical switches (3-pin or 5-pin PCB mount) |
| **Keycaps** | 4 | 1u MX-compatible keycaps |
| **Rotary Encoder** | 1 | EC11 rotary encoder with push-button switch |
| **Encoder Knob** | 1 | 6mm D-shaft or knurled shaft compatible knob |
| **Custom PCB** | 1 | 1.6mm FR4 PCB (fabricated from `Gerber.zip`) |

---

## 2. Structural & Enclosure Parts

| Item | Qty | Material / Process | Manufacturing Notes |
| :--- | :---: | :--- | :--- |
| **Top Cover** | 1 | 3D Printed (PLA / PETG) | 0.2mm layer height, 20% infill, no supports needed |
| **Spacer Ring** | 1 | 3D Printed (PLA / PETG) | Decoupled support ring for top plate |
| **Switch Plate** | 1 | 1.5mm Laser-Cut Acrylic | Clear or colored acrylic (`Switch_Plate.dxf`) |
| **Bottom Plate** | 1 | 3.0mm Laser-Cut Acrylic | Solid base plate (`Bottom_Plate.dxf`) |

---

## 3. Fasteners & Hardware

| Item | Qty | Specifications |
| :--- | :---: | :--- |
| **M3 Standoffs** | 4 | M3 female-to-female threaded standoffs (length depends on internal clearance) |
| **M3 Screws** | 8 | M3 button-head or socket-head machine screws |
| **Rubber Feet** | 4 | Self-adhesive silicone/rubber bumper pads (for bottom plate stability) |

---

## 4. Software & Firmware Assets

* **CircuitPython Runtime:** `.uf2` bootloader file for Seeed Studio XIAO.
* **KMK Firmware:** Core `kmk/` Python library package.
* **Custom Scripts:** `boot.py` and `main.py`.

```
