import cv2

from app.tracking.tracker import VehicleTracker
from app.counting.counter import VehicleCounter
from app.analytics.analytics import TrafficAnalytics


def process_video(input_path, output_path):
 
    tracker = VehicleTracker()
    counter = VehicleCounter(line_y=400)
    analytics = TrafficAnalytics()

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        raise RuntimeError(
            f"Could not open video: {input_path}"
        )

    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    print(f"Input resolution: {original_width}x{original_height}")
    print(f"FPS: {fps}")

    # Processing resolution
    width = 1280
    height = 720

    fourcc = cv2.VideoWriter_fourcc(*"avc1")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Resize frame
        frame = cv2.resize(
            frame,
            (width, height)
        )

        # YOLO tracking
        result = tracker.track(frame)
                                            
        # Update counter and get newly counted vehicles
        
        new_events = counter.update(result)
        # Send new vehicle events to analytics
        for event in new_events:

            analytics.record_vehicle(
                 event["vehicle_type"],
                 event["direction"]
            )
        # Draw tracking boxes and IDs
        annotated_frame = result.plot()

        # Draw counting line
        cv2.line(
            annotated_frame,
            (0, counter.line_y),
            (width, counter.line_y),
            (0, 255, 255),
            2
        )

        # =========================
        # GET COUNTS
        # =========================

        in_counts = counter.get_in_counts()
        out_counts = counter.get_out_counts()

        total_in = sum(in_counts.values())
        total_out = sum(out_counts.values())

        # =========================
        # TITLE
        # =========================

        cv2.putText(
            annotated_frame,
            "TRAFFICVISION",
            (30, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        # =========================
        # INCOMING HEADER
        # =========================

        cv2.putText(
            annotated_frame,
            "INCOMING",
            (300, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

        # =========================
        # OUTGOING HEADER
        # =========================

        cv2.putText(
            annotated_frame,
            "OUTGOING",
            (600, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 165, 255),
            2
        )

        # =========================
        # TOTAL
        # =========================

        cv2.putText(
            annotated_frame,
            f"Total: {total_in}",
            (300, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Total: {total_out}",
            (600, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # =========================
        # CARS
        # =========================

        cv2.putText(
            annotated_frame,
            f"Cars: {in_counts['car']}",
            (300, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Cars: {out_counts['car']}",
            (600, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        # =========================
        # MOTORCYCLES
        # =========================

        cv2.putText(
            annotated_frame,
            f"Bikes: {in_counts['motorcycle']}",
            (300, 195),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Bikes: {out_counts['motorcycle']}",
            (600, 195),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        # =========================
        # BUSES
        # =========================

        cv2.putText(
            annotated_frame,
            f"Buses: {in_counts['bus']}",
            (300, 230),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Buses: {out_counts['bus']}",
            (600, 230),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        # =========================
        # TRUCKS
        # =========================

        cv2.putText(
            annotated_frame,
            f"Trucks: {in_counts['truck']}",
            (300, 265),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Trucks: {out_counts['truck']}",
            (600, 265),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        # =========================
        # COUNTING LINE LABEL
        # =========================

        cv2.putText(
            annotated_frame,
            "COUNTING LINE",
            (width // 2 - 100, counter.line_y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

        # Save frame
        out.write(annotated_frame)

        frame_count += 1

        if frame_count % 100 == 0:
            print(f"Processed {frame_count} frames")

    cap.release()
    out.release()



    # =========================
    # FINAL RESULTS
    # =========================

    total_in = sum(counter.in_counts.values())
    total_out = sum(counter.out_counts.values())

    print()
    print("Processing complete!")
    print(f"Processed frames: {frame_count}")
    print(f"Output saved to: {output_path}")

    print()
    print("========== TRAFFIC SUMMARY ==========")

    print(f"INCOMING TOTAL: {total_in}")
    print(f"OUTGOING TOTAL: {total_out}")

    print()
    print("INCOMING VEHICLES:")
    print(f"Cars: {counter.in_counts['car']}")
    print(f"Motorcycles: {counter.in_counts['motorcycle']}")
    print(f"Buses: {counter.in_counts['bus']}")
    print(f"Trucks: {counter.in_counts['truck']}")

    print()
    print("OUTGOING VEHICLES:")
    print(f"Cars: {counter.out_counts['car']}")
    print(f"Motorcycles: {counter.out_counts['motorcycle']}")
    print(f"Buses: {counter.out_counts['bus']}")
    print(f"Trucks: {counter.out_counts['truck']}")

    print("=====================================")

    # =========================
    # ANALYTICS SUMMARY
    # =========================

    summary = analytics.get_summary()

    print()
    print("========== ANALYTICS SUMMARY ==========")

    print(f"Total Vehicles: {summary['total']}")

    print()
    print("INCOMING:")
    print(f"Total: {summary['incoming']['total']}")
    print(f"Cars: {summary['incoming']['car']}")
    print(f"Motorcycles: {summary['incoming']['motorcycle']}")
    print(f"Buses: {summary['incoming']['bus']}")
    print(f"Trucks: {summary['incoming']['truck']}")

    print()
    print("OUTGOING:")
    print(f"Total: {summary['outgoing']['total']}")
    print(f"Cars: {summary['outgoing']['car']}")
    print(f"Motorcycles: {summary['outgoing']['motorcycle']}")
    print(f"Buses: {summary['outgoing']['bus']}")
    print(f"Trucks: {summary['outgoing']['truck']}")

    print("========================================")

    return summary




