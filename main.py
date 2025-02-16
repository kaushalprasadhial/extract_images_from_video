import cv2
import os

def save_every_Nth_frame(video_path, output_folder, freq, max_frames=None):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # Create output directory if it doesn't exist
    os.makedirs(os.path.join(output_folder, video_name), exist_ok=True)

    # Open video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Stop if video ends

        # Save every 10th frame
        if frame_count % freq == 0:
            frame_filename = os.path.join(output_folder, f"{video_name}_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1
            if max_frames and saved_count==max_frames:
                break

        frame_count += 1

    cap.release()
    print(f"Saved {saved_count} frames to {output_folder}")

def save_images(video_paths, output_folder, freq, max_frames=None):
    for video_path in video_paths:
        save_every_Nth_frame(video_path, output_folder, freq, max_frames)

# Example usage
video_paths = {"input_video.mp4"}  # Change this to your video file path
output_folder = "output_frames"
save_images(video_paths, output_folder, 25*15, 200)
