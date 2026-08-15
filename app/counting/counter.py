class VehicleCounter:

    def __init__(self, line_y=400):

        self.line_y = line_y

        # Previous center position of each tracked vehicle
        self.previous_positions = {}

        # Vehicles already counted
        self.counted_ids = set()

        # Overall counts
        self.counts = {
            "car": 0,
            "motorcycle": 0,
            "bus": 0,
            "truck": 0
        }

        # Incoming counts
        self.in_counts = {
            "car": 0,
            "motorcycle": 0,
            "bus": 0,
            "truck": 0
        }

        # Outgoing counts
        self.out_counts = {
            "car": 0,
            "motorcycle": 0,
            "bus": 0,
            "truck": 0
        }

    def update(self, tracks):

        # Store newly counted vehicles
        new_events = []

        if tracks.boxes.id is None:
            return new_events

        boxes = tracks.boxes.xyxy.cpu().numpy()
        track_ids = tracks.boxes.id.int().cpu().tolist()
        classes = tracks.boxes.cls.int().cpu().tolist()

        for box, track_id, class_id in zip(
            boxes,
            track_ids,
            classes
        ):

            x1, y1, x2, y2 = box

            # Vehicle center
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            current_position = (center_x, center_y)

            if track_id in self.previous_positions:

                previous_x, previous_y = self.previous_positions[track_id]

                vehicle_type = self.get_vehicle_type(class_id)

                if vehicle_type in self.counts:

                    direction = None

                    # =========================
                    # MOVING DOWN = IN
                    # =========================

                    if (
                        previous_y < self.line_y
                        and center_y >= self.line_y
                    ):

                        direction = "IN"

                    # =========================
                    # MOVING UP = OUT
                    # =========================

                    elif (
                        previous_y > self.line_y
                        and center_y <= self.line_y
                    ):

                        direction = "OUT"

                    # =========================
                    # COUNT VEHICLE
                    # =========================

                    if (
                        direction is not None
                        and track_id not in self.counted_ids
                    ):

                        # Overall count
                        self.counts[vehicle_type] += 1

                        # Direction count
                        if direction == "IN":
                            self.in_counts[vehicle_type] += 1

                        elif direction == "OUT":
                            self.out_counts[vehicle_type] += 1

                        # Mark vehicle as counted
                        self.counted_ids.add(track_id)

                        # Send event to analytics
                        new_events.append({
                            "track_id": track_id,
                            "vehicle_type": vehicle_type,
                            "direction": direction
                        })

            # Update vehicle position
            self.previous_positions[track_id] = current_position

        return new_events

    def get_vehicle_type(self, class_id):

        # YOLO COCO class IDs
        vehicle_classes = {
            2: "car",
            3: "motorcycle",
            5: "bus",
            7: "truck"
        }

        return vehicle_classes.get(
            class_id,
            "unknown"
        )

    def get_counts(self):

        return self.counts.copy()

    def get_in_counts(self):

        return self.in_counts.copy()

    def get_out_counts(self):

        return self.out_counts.copy()