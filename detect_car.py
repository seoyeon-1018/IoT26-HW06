from ultralytics import YOLO
from pathlib import Path
import cv2

# Set input and output paths
input_image = Path("/home/iotteam2/Pictures/hw6_yolo/monitor_car.jpg")
output_dir = Path("/home/iotteam2/Pictures/hw6_yolo")
output_image = output_dir / "result_car_detection.jpg"
output_text = output_dir / "result.txt"

# Load the YOLO model
model = YOLO("yolo11n.pt")

# Run object detection on the input image
results = model.predict(
    source=str(input_image),
    conf=0.25,
    save=False
)

# Define vehicle classes to detect
vehicle_classes = {"car", "truck", "bus", "motorcycle"}
detected_vehicles = []

# Check detection results
for result in results:
    names = result.names

    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = names[class_id]
        confidence = float(box.conf[0])

        # Save only vehicle-related detections
        if class_name in vehicle_classes:
            detected_vehicles.append((class_name, confidence))

    # Save the image with detection boxes
    annotated_image = result.plot()
    cv2.imwrite(str(output_image), annotated_image)

# Create detection result message
if detected_vehicles:
    message = "Vehicle detected: " + ", ".join(
        [f"{name} ({confidence:.2f})" for name, confidence in detected_vehicles]
    )
else:
    message = "No vehicle detected."

# Save and print the detection result
output_text.write_text(message, encoding="utf-8")
print(message)
