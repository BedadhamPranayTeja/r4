# r4 Bill of Materials (BOM) 🛒

Derived from the OpenSCAD design files in `parts/`.

## 🧠 Electronics (The Brains)
| Part | Quantity | Notes | Source File |
| :--- | :--- | :--- | :--- |
| **Raspberry Pi 4** | 1 | Main Computer (Run Backend/Frontend) | `electronics.scad` (Part_Pi4) |
| **L298N Driver** | 1 | Motor Driver Module | `electronics.scad` (Detailed_L298N) |
| **ICM-20948** (or MPU9250) | 1 | 9-Axis IMU. ICM is the modern, higher-precision successor. | `electronics.scad` |
| **Pi Camera V2** | 1 | 8MP V2 Module (or V3, or compatible) | `gimbal_parts.scad` |
| **Buck Converter** | 1 | LM2596 (Step-down 7.4V -> 5V) | `electronics.scad` (Detailed_Buck) |
| **HC-SR04** | 1 | Ultrasonic Distance Sensor | `sensors.scad` |
| **IR Sensor** | 1+ | Obstacle/Line Sensor | `sensors.scad` |

## 🦾 Actuators (The Muscles)
| Part | Quantity | Notes | Source File |
| :--- | :--- | :--- | :--- |
| **TT Gear Motor** | 2 | "Yellow" DC Motors (1:48) | `motion.scad` |
| **Wheels** | 2 | 65mm Rubber Wheels | `motion.scad` |
| **SG90 Servo** | 2 | Micro Servo (Pan/Tilt Gimbal) | `hardware.scad` |

## 🔋 Power
| Part | Quantity | Notes |
| :--- | :--- | :--- |
| **18650 Battery** | 2 | Li-ion Cells (7.4V Total) | `electronics.scad` |
| **Battery Holder** | 1 | 2-Cell 18650 Holder | |

## 🔩 Hardware & Vitamins
| Part | Quantity | Notes |
| :--- | :--- | :--- |
| **Caster Wheel** | 1 | Omni-directional front wheel | `motion.scad` |
| **M3 Bolts** | ~20 | Various lengths (Motor mounts, PCB) | `hardware.scad` |
| **M3 Nuts** | ~20 | | |
| **Jumper Wires** | Set | Male-Male, Male-Female | |

---

## 🏗️ 3D Printed Parts
*(Exported from `main.scad`)*
- Chassis Plate
- Motor Mounts (x2)
- Caster Mount
- L298N Mount
- Pi Mount
- Camera Gimbal (Base, U-Bracket, Camera Holder)
