from app.video.processor import process_video


if __name__ == "__main__":

    input_video = "videos/input/Road_traffic_30s.mp4"
    output_video = "videos/output/Road_traffic_30s_vne.mp4"

    process_video(input_video, output_video)