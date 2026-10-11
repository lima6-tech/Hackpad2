### Hackpad — Bill of Materials (BOM)

## 1. Electronics & Components

| Item | Qty | Notes |
| :--- | :---: | :--- |
| **Microcontroller** | 1 | Seeed Studio XIAO (RP2040 or SAMD21 variant) |
| **Key Switches** | 4 | Button switch keyboard: SW Cherry MX 1.00u PCB |
| **Keycaps** | 4 | 1u MX-compatible keycaps |
| **Rotary Encoder** | 1 | RotaryEncoder Alps EC11E-Switch Vertical H20mm)|
| **Encoder Knob** | 1 | Compatible knob |
| **Custom PCB** | 1 | 1.6mm FR4 PCB (fabricated from `Gerber.zip`) |

---

## 2. Structural & Enclosure Parts

| Item | Qty | Material | Manufacturing Notes |
| :--- | :---: | :--- | :--- |
| **Top Cover** | 1 | 3D Printed |(`Top.stl`)|
| **Mounting column support** | 1 | 3D Printed | Decoupled support ring for top plate |
| **Acrylic window** | 1 | 3mm Laser-Cut Acrylic | Clear acrylic (`Acrylic_cutout.dxf`) |
| **Bottom base** | 1 | 3D Printed | Solid base plate (`Bottom.stl`) |

---

## 3. Fasteners & Hardware
*This part is AI generated:

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
