import cv2

# Open the video file
video_path = "x.mp4"  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Define the coordinates of the pixel to check (x, y)
pixel_x = 100  # Horizontal coordinate
pixel_y = 200  # Vertical coordinate

frame_number = 0

while True:
    ret, frame = cap.read()  # Read the next frame
    if not ret:
        print("Reached the end of the video.")
        break

    if pixel_y >= frame.shape[0] or pixel_x >= frame.shape[1]:
        print("Error: Pixel coordinates are out of frame bounds.")
        break

    pixel_color = frame[pixel_y, pixel_x]
    blue, green, red = pixel_color

    # Save the current frame to disk
    frame_filename = f'frame_{frame_number}.jpg'
    cv2.imwrite(frame_filename, frame)

    # Print the BGR color of the specific pixel for this frame
    print(f"Frame {frame_number}: Pixel ({pixel_x}, {pixel_y}) - BGR: ({blue}, {green}, {red})")
    
    frame_number += 1

# Release the video capture object
cap.release()
