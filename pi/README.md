# Pi Backend

This folder contains the standalone backend code intended to run on the Raspberry Pi (or the computing unit of the robot).

It maps 1:1 with the main API logic but is isolated to ensure no accidental dependency on dev-host specific paths or tools.

## Setup


## Setup

1. `pip install -r requirements.txt`

## Running

### Standard (Legacy or USB Webcam)
`uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Pi Camera on Bookworm
Raspberry Pi OS Bookworm uses `libcamera`, which isn't directly compatible with OpenCV's standard capture out-of-the-box. We use `libcamerify` to bridge this.

1. Ensure tools are installed: `sudo apt install libcamera-tools`
2. Run the helper script:
   `bash run.sh`

