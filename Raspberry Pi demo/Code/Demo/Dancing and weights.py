import math
from Control import *
from Servo import *
class Action:
    def __init__(self):
        self.servo=Servo()
        self.control=Control()
        self.servo.setServoAngle(15,90)
    def fuwocheng(self):
        xyz=[[0,50,0],[-100,23,0],[-100,23,0],[0,50,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.01)
        for i in range(4):
            for i in range(50,120,1):
                self.control.point[0][1]=i
                self.control.point[3][1]=i
                self.control.run()
                time.sleep(0.01)
            for i in range(120,50,-1):
                self.control.point[0][1]=i
                self.control.point[3][1]=i
                self.control.run()
                time.sleep(0.01)
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.01)
        def tiaowu(self):
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
            
        y=100*math.cos(45/180*math.pi)+23
        x=100*math.sin(45/180*math.pi)
        xyz=[[-x,y,0],[0,0,123],[0,0,-123],[-x,y,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run() 
            time.sleep(0.02)
            
        for i in range(3):
            for i in range(45,-45,-1):
                y=100*math.cos(i/180*math.pi)+23
                x=100*math.sin(i/180*math.pi)
                xyz=[[-x,y,0],[0,0,123],[0,0,-123],[-x,y,0]]
                for i in range(4):
                    xyz[i][0]=(xyz[i][0]-self.control.point[i][0])
                    xyz[i][1]=(xyz[i][1]-self.control.point[i][1])
                    xyz[i][2]=(xyz[i][2]-self.control.point[i][2])
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run() 
            for i in range(-45,45,1):
                y=100*math.cos(i/180*math.pi)+23
                x=100*math.sin(i/180*math.pi)
                xyz=xyz=[[-x,y,0],[0,0,123],[0,0,-123],[-x,y,0]]
                for i in range(4):
                    xyz[i][0]=(xyz[i][0]-self.control.point[i][0])
                    xyz[i][1]=(xyz[i][1]-self.control.point[i][1])
                    xyz[i][2]=(xyz[i][2]-self.control.point[i][2])
                for i in range(4):
                    self.control.point[i][0]+=xyz[i][0]
                    self.control.point[i][1]+=xyz[i][1]
                    self.control.point[i][2]+=xyz[i][2]
                self.control.run() 
        xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
        for i in range(4):
            xyz[i][0]=(xyz[i][0]-self.control.point[i][0])/30
            xyz[i][1]=(xyz[i][1]-self.control.point[i][1])/30
            xyz[i][2]=(xyz[i][2]-self.control.point[i][2])/30
        for j in range(30):
            for i in range(4):
                self.control.point[i][0]+=xyz[i][0]
                self.control.point[i][1]+=xyz[i][1]
                self.control.point[i][2]+=xyz[i][2]
            self.control.run()
            time.sleep(0.02)
        time.sleep(1)
    
        
if __name__=='__main__':
    action=Action()  
    time.sleep(2) 
    while True:
        #action.fuwocheng()
        #action.tiaowu() 
        time.sleep(3)
        
