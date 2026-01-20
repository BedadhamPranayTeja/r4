# r29 Robot Specifications 🦾

**Target Platform**: Full Humanoid Research Robot
**Total Degrees of Freedom (DOF)**: 29

## Kinematic Breakdown

### 1. Mobility Platform (2 DOF)
*   **Base**: Differential Drive
    *   Left Wheel
    *   Right Wheel

### 2. Core Body (2 DOF)
*   **Torso**:
    *   Waist Yaw (Rotation)
    *   Waist Pitch (Bending)

### 3. Head (3 DOF)
*   **Neck**:
    *   Yaw (Pan)
    *   Pitch (Tilt)
    *   Roll (Tilt Sideways)

### 4. Arms (14 DOF)
*Redundant 7-DOF manipulators for advanced reach and collision avoidance.*

**Per Arm (x7):**
1.  **Shoulder Pitch**
2.  **Shoulder Yaw**
3.  **Elbow Roll (Upper)**
4.  **Elbow Flexion**
5.  **Elbow Roll (Lower)**
6.  **Wrist Pitch**
7.  **Wrist Yaw**

### 5. Hands (8 DOF)
*Optimized for Power vs. Precision grasping.*

**Per Hand (x4):**
1.  **Thumb Abduction** (Critical: Spreads thumb for different grasp types)
2.  **Thumb Flexion** (Grip)
3.  **Fingers PIP** (Index/Middle/Ring/Pinky Main Knuckles - Linked)
4.  **Fingers DIP** (Fingertips - Linked)

---

## Control Architecture Note
Due to the high complexity (Redundant 7-DOF Arms, Synchronized Hand Grasping), this robot **cannot** be controlled effectively with the simple `r4` custom stack.

**Requirement**:
*   **ROS 2** (Robot Operating System 2)
*   **MoveIt** (For Inverse Kinematics & Motion Planning)
*   **ros2_control** (For hardware synchronization)
