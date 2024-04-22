# import ultralytics
# from flask import Flask, request, jsonify
# from ultralytics import yolov5

# app = Flask(__name__)
# model = yolov5('yolov5s.pt')  # Initialize your object detection model

# @app.route('/detect', methods=['POST'])
# def detect_objects():
#     # Get image URL from the request
#     image_url = request.json.get('https://fastly.picsum.photos/id/576/200/300.jpg?grayscale&hmac=9GNPADlzUZzvAQmoTeuejrdjLwyY2Lus4ilasJbzX90')

#     # Perform object detection
#     results = model(image_url)

#     # Process detection results
#     # For simplicity, let's just return the detected objects
#     detected_objects = results.pandas().xyxy[0].to_dict(orient='records')

#     return jsonify(detected_objects)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)



from PIL import Image
from io import BytesIO
import requests
from ultralytics import yolov5

# Load YOLOv5 model
model = yolov5()

def detect_objects(image_url):
    try:
        # Download image from URL
        response = requests.get(image_url)
        image_data = response.content

        # Open image using PIL
        image = Image.open(BytesIO(image_data))

        # Perform object detection
        results = model(image)

        # Process detection results
        detected_objects = results.xyxy[0].tolist()  # Convert results to a list

        return detected_objects
    except Exception as e:
        print(f"Error detecting objects: {e}")
        return []

# Example usage
image_url = 'https://example.com/image.jpg'
detected_objects = detect_objects(image_url)
print("Detected Objects:", detected_objects)
