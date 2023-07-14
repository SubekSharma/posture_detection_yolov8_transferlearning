# Posture Detection YOLOv8 Finetuned on Custom Dataset

This project aims to detect the posture of a computer user in real-time using a fine-tuned version of YOLOv8. The custom dataset used for training consists of two classes: "Good" and "Bad", representing different postures.

## Dataset
The dataset used in this project was created using a smartphone camera. It consists of 52 unique images, with each class containing 26 images. The dataset was manually labeled using the labelImg package in Python.

The training set contains 46 images, with 23 images from each class. The validation set consists of 3 images per class to evaluate the model's performance.

## Model
The YOLOv8 architecture, the latest version of YOLO (You Only Look Once), was chosen as the base model. The weights of the pre-trained YOLOv8 model were initialized and then fine-tuned on the custom dataset. The aim of the fine-tuning process was to adapt the model to detect the specific postures of computer users.

## Usage
To use the trained model for real-time posture detection, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/posture_detection_yolov8_finetuned.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Download the pre-trained weights for YOLOv8: [yolov8.weights](https://link-to-pretrained-weights)
4. Place the downloaded weights in the `weights/` directory.
5. Run the real-time detection script: `python detect_posture.py`

Make sure to have a webcam connected to your system to capture the live video feed. The script will process each frame in real-time and display the detected postures with bounding boxes and labels.

## Results
The fine-tuned YOLOv8 model achieved promising results in detecting and classifying the different postures of computer users. The accuracy and performance were evaluated using the validation set, and the model demonstrated good performance in distinguishing between "Good" and "Bad" postures.

## Future Work
There are several avenues for further improvement and expansion of this project, including:

- Collecting a larger and more diverse dataset to improve the model's generalization capabilities.
- Implementing additional post-processing techniques, such as non-maximum suppression, to improve the accuracy of bounding box predictions.
- Exploring the use of other deep learning architectures and comparing their performance with YOLOv8.

Contributions and feedback are welcome to enhance the accuracy and applicability of the model.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The YOLOv8 implementation used in this project is based on [YOLOv8 PyTorch](https://github.com/ultralytics/ultralytics) by Ultralytics.
- Special thanks to the labelImg package for facilitating the dataset labeling process.

Please feel free to reach out with any questions or suggestions. Enjoy detecting postures with YOLOv8!
