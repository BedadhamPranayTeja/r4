#!/bin/bash
# Wrapper for Bookworm to allow OpenCV to see the camera as a V4L2 device
# Requires: sudo apt install libcamera-tools

if command -v libcamerify &> /dev/null
then
    echo "Starting r4 with libcamerify..."
    libcamerify uvicorn app.main:app --host 0.0.0.0 --port 8000
else
    echo "Warning: libcamerify not found. Installing libcamera-tools might be needed."
    echo "Trying standard run..."
    uvicorn app.main:app --host 0.0.0.0 --port 8000
fi
