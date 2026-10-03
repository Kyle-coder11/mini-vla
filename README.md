# MiniVLA

A beginner project exploring computer vision and vision-language-action robotics.

## Day 1: Computer Vision Perception

The first stage of this project builds a simple visual perception pipeline using OpenCV and YOLO.

The program can:

- Load an image using OpenCV
- Inspect image dimensions and pixel values
- Draw bounding boxes
- Run a pretrained YOLO object detector
- Extract detected object classes
- Extract confidence scores
- Calculate the center of each detected object

## Pipeline

Image → YOLO → Object Detection → Bounding Box → Object Center

## Example

```text
Object: cup
Confidence: 0.87
Center: (413, 238)

Day 2: Language-Conditioned Target Selection

Day 2 adds a simple language component to the computer vision pipeline.

The user can give an instruction such as:

Find the cup

The program extracts the target object from the instruction and compares it with the objects detected by YOLO.

Day 2 Pipeline

Language Instruction → Extract Target

Image → YOLO → Detected Objects

Detected Objects + Target → Target Matching → Selected Object

Day 2 Example

Detected objects:
- person
- cup
- chair

Give the robot an instruction:
Find the cup

Instruction: Find the cup
Target object: cup

Target found!
Object: cup
Confidence: 0.87
Center: (413, 238)

## Day 3: Robot Action Policy

The project now converts the visual location of a language-selected object into a robot action.

Current actions:

- TURN LEFT
- TURN RIGHT
- MOVE FORWARD

The policy compares the target object's horizontal location with the center of the camera image.

Pipeline:

Image + Language
→ Object Detection
→ Target Grounding
→ Target Location
→ Robot Policy
→ Action
