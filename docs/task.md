# R4 Robot Control Studio - Project Tasks

## Phase 1: Foundation & Structure (Completed)
- [x] Basic React Frontend Setup
- [x] Basic FastAPI Backend Setup
- [x] WebSocket Communication (Bi-directional)
- [x] Project Restructure (Feature-based Architecture)
- [x] React Strict Mode Handling (Debounce & Cleanup)

## Phase 2: "One Camera" Architecture (Current Priority)
- [x] **MJPEG Video Streaming**
    - [x] Backend: Update [VisionSystem](file:///c:/Users/prana/OneDrive/Desktop/r4/api/app/services/vision.py#7-161) to yield JPEG frames
    - [x] Backend: Create `/video_feed` endpoint
    - [x] Frontend: Replace `getUserMedia` with `<img src="/video_feed" />` texture
- [x] **Control Logic Tuning**
    - [x] Backend: Safety Stop on Gesture Loss
    - [x] Backend: Mode Switching Logic (FIST <-> PALM)
- [x] **Augmented Reality Overlay**
    - [x] Backend: Draw "Skeleton" and "Target Vector" on frames
    - [x] Frontend: Display the "AI View" on the 3D Wall (Achieved via Video Feed)

## Phase 3: Hardware Integration
- [ ] **Serial Communication**
    - [ ] Backend: Integrate `pyserial` to talk to Arduino/ESP
    - [ ] Backend: Convert `move`/`look` commands to Serial Bytes
- [ ] **Motor Control**
    - [ ] Firmware: Arduino Sketch for parsing Serial -> Motor Driver
- [ ] **Servo Control**
    - [ ] Firmware: Arduino Sketch for parsing Serial -> Servo PWM

## Phase 4: Advanced AI
- [ ] **Face Tracking**
    - [ ] Implement "Follow Face" mode in [VisionSystem](file:///c:/Users/prana/OneDrive/Desktop/r4/api/app/services/vision.py#7-161)
- [ ] **Voice Control** (Optional)
    - [ ] Simple command recognition ("Stop", "Go")

## Future / Cancelled
- [ ] **Dockerization** (Skipped for Win/Mac Hardware issues)
