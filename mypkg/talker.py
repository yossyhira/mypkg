import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self): #init イニシャライズ 
        self.pub = node.create_publisher(Int16,"countup",10)
        self.n = 0

rclpy.init()
node = Node("talker")
talker = Talker() #initが実行、（）の引数はなし。classでは引数にselfがあるが書かなくてよい

def cb ():
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)
    talker.n += 1

node.create_timer(0.5,cb)
rclpy.spin(node)

