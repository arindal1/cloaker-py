import streamlit as st
import cv2
import numpy as np
import time

# Function to capture the background image
def capture_background(cap, num_frames=60):
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            continue
    return frame

# Function to create a mask for a specific color and include everything within the shape
def create_mask(hsv, lower_bound, upper_bound):
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Find contours and fill them
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        cv2.drawContours(mask, [contour], -1, (255), thickness=cv2.FILLED)

    return mask, contours

# Function to replace the colored areas with the background
def apply_cloaking(frame, background, mask):
    mask_inv = cv2.bitwise_not(mask)
    background_part = cv2.bitwise_and(background, background, mask=mask)
    frame_part = cv2.bitwise_and(frame, frame, mask=mask_inv)
    return cv2.addWeighted(background_part, 1, frame_part, 1, 0)

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)
    
    # Inform the user and wait for 5 seconds
    st.title("Invisible Cloak App")
    st.write("Capturing background in 5 seconds. Please move away from the camera.")
    time.sleep(5)
    
    # Capture the background image
    st.write("Capturing background. Please stand still.")
    background = capture_background(cap)
    
    # Define the color range for cloaking (strong blue color)
    lower_bound = np.array([100, 100, 100])
    upper_bound = np.array([140, 255, 255])
    
    masking_on = st.sidebar.checkbox("Toggle Masking", True)  # Checkbox to control masking
    
    st.write("Processing frames.")
    
    # Layout using Streamlit columns and containers
    col1, col2 = st.columns([3, 1])  # Adjust column widths as needed
    
    # Video stream container
    with col1:
        video_stream = st.empty()  # Placeholder for video stream
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert the frame to HSV color space
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            if masking_on:
                # Create a mask for the specified color
                mask, contours = create_mask(hsv, lower_bound, upper_bound)
                
                # Apply the cloaking effect
                cloaked_frame = apply_cloaking(frame, background, mask)
                
                # Draw contours of the detected object (optional)
                cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
            else:
                cloaked_frame = frame
            
            # Display the result as a video stream
            video_stream.image(cloaked_frame, channels="BGR")
    
    # Sidebar container for controls
    with col2:
        st.sidebar.subheader("Controls")
        st.sidebar.markdown("*Toggle the masking effect*")
        if not masking_on:
            st.sidebar.error("Masking turned OFF")
        else:
            st.sidebar.success("Masking turned ON")
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
