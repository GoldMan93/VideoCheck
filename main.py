import cv2
import os

# Open the video file
video_path = "x.mp4"
cap = cv2.VideoCapture(video_path)

# Define the coordinates of the pixel to check (x, y)
pixel_x = 100
pixel_y = 200

# Create the folder to save frames
save_folder = "video_frames"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

frame_number = 0

# Target RGB (blue, green, red)
target_RGB = (90, 70, 60)
colour_shift = 10

while True:
    ret, frame = cap.read()  # Read the next frame
    if not ret:
        print("Reached the end of the video.")
        break

    if pixel_y >= frame.shape[0] or pixel_x >= frame.shape[1]:
        print("Error: Pixel coordinates are out of frame bounds.")
        break

    # Get the BGR color of the specific pixel
    pixel_color = frame[pixel_y, pixel_x]
    blue, green, red = pixel_color

    # Check if the blue value is out of the target range
    if blue < (target_RGB[0] - colour_shift) or blue > (target_RGB[0] + colour_shift):
        # Draw a circle around the specific pixel
        frame_with_circle = frame.copy()
        cv2.circle(
            frame_with_circle,
            (pixel_x, pixel_y),
            radius=10,
            color=(0, 0, 255),
            thickness=2,
        )

        # Save the frame with the circle to the designated folder as a .jpg file
        frame_filename = os.path.join(save_folder, f"frame_{frame_number}.jpg")
        cv2.imwrite(frame_filename, frame_with_circle)
        print(
            f"Frame {frame_number}: Pixel ({pixel_x}, {pixel_y}) - BGR: ({blue}, {green}, {red}) saved as {frame_filename}"
        )

    frame_number += 1

# Release the video capture object
cap.release()
