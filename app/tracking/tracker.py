from ultralytics import YOLO


class VehicleTracker:

    def __init__(self, model_path="yolo11n.pt"):
        self.model = YOLO(model_path)

    def track(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False,
            classes=[2, 3, 5, 7]
        )

        return results[0]