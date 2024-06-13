import cv2

def get_video_fps(video_path):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None
    
    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Release the VideoCapture object
    cap.release()
    
    return fps

# Example usage:
video_path = "path to your video"
fps = get_video_fps(video_path)

if fps:
    print(f"The video's FPS is: {fps}")
