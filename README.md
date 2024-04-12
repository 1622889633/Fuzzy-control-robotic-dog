Title: Fuzzy-control-robotic-dog
Freenove Raspberry Pi 

### Introduction:
The project aims to enhance the adaptability and robustness of robotic dogs by employing fuzzy algorithms, specifically focusing on the Freenove Robotic Dog Kit, which is based on the Raspberry Pi 4B platform. The goal is to create an advanced navigation system through centralized scheduling achieved by the cooperation between higher-level commands and lower-level machine operations. This would allow the robotic dog to efficiently execute action commands, navigate complex paths, and adapt to its environment with improved responsiveness.
To accomplish these objectives, the project will develop a path planning system that integrates sensory inputs like ultrasonic sensors and machine vision, enabling precise movement in dynamic settings. A fuzzy logic-based closed-loop control system will be designed to refine the robot's movements, allowing it to perform complex commands and interact with its surroundings more naturally. Additionally, the project involves seamless hardware and software integration to ensure energy efficiency, real-time processing, and the robust performance of control commands.

User Installation Instructions
To set up the software for the Freenove Robotic Dog project using a Raspberry Pi, you will need to follow these step-by-step instructions, assuming you are starting from scratch:

Preparing the Raspberry Pi:

Download the latest Raspberry Pi OS image from the official website.
Use the Raspberry Pi Imager to write the image file to an SD card.
Insert the SD card into the Raspberry Pi, connect the Raspberry Pi to power and peripherals, and boot up the system.
Configure the Raspberry Pi to enable VNC service for remote desktop access through the Raspberry Pi configuration settings.
Setting Up the Development Environment:

Ensure Python3 and PyQt5 are installed on the Raspberry Pi for server and client development.
Start the server application on the Raspberry Pi, which initializes the TCP server and listens for client connection requests.
Upon receiving a connection request, establish a connection and start a session to await commands from the client.
Installing Dependencies and Libraries:
Install all necessary management tools and dependencies required for the project.
Install libraries related to sensor GPIO, Picamera, drivers, and communication essential for controlling the robotic dog.
Using Freenove Client Software:

Use the Freenove Client for Smart Dog software to calibrate the quadruped robot, ensuring the center of gravity is maintained for balanced gait.
Utilize the Freenove app to test and execute commands such as movement, video streaming, LED control, and ultrasonic distance measurement.

3. How to run the code, a simple example or demo code
### Download
Run following command to download all the files in this repository.
`git clone https://github.com/1622889633/Fuzzy-control-robotic-dog.git`
* **Manually download in browser**
	Click the green "Clone or download" button, then click "Download ZIP" button in the pop-up window.
After all the Raspberry Pi library functions and calibration tests have been completed, start the Raspberry Pi and enter the following command from the keyboard：
pip install -r requirements.txt
cd Raspberry Pi demo\Code\Demo
python  Dancing and weights.py
By uncommenting the last subfunction of the code, you can perform subtasks such as dancing, loading, etc.
cd Raspberry Pi demo\Code\Demo
python  main.py

4.More technical details
Through the execution of the above code can complete the task of PID, fuzzy control, fuzzy PID
You can choose PID, fuzzy PID and fuzzy control three kinds, first of all, the robot dog starts to move forward after starting, then ultrasonic real-time detection, when the distance is less than or equal to 10cm, open the colour recognition tracking, the central position of the ball is red, then call the robot dog right turn function, right turn 45 degrees after identifying the right front continues to have a red ball continues to turn 45 degrees right, if the recognition of the central position of the ball is If the ball in the centre is blue, then call the function of left turn of the machine dog, after turning 45 degrees right to identify the left front continues to have red ball, then continue to turn 45 degrees left, if the recognition of the centre of the ball is green, then the machine dog stops.

5.Known Issues/Future Improvements
The Raspberry Pi suffers from delays in processing large continuous image frames, which affects the speed of response for image recognition and subsequent actions, and due to the processing delays, the robot dog does not respond fast enough to dynamic environments, especially when rapid changes in direction are required.
In the future, the camera configuration is adjusted to use a lower resolution for image acquisition, and an algorithm is used to ensure that the ball is located in the centre of the image as much as possible, this can be achieved by adjusting the movement of the robot dog, fine-tuning the position until the ball is centred, and at the same time slowing down the speed of the judgement, and starting to judge the colours after the ball has been located in the central position for 1s, and executing the commands to turn left, turn right, and stop.
