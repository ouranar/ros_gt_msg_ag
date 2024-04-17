#本文件测试车体一次的执行时间具体为几秒

import rospy
from ros_gt_msg.msg import gt_control
from package import Controlfunc_gt


if __name__ == "__main__":
    rospy.init_node("/pub_command1")
    pub = rospy.Publisher("/time_1s", gt_control, queue_size=20)
    #当发送消息频率大于本地序列化速度，来不及发送的就会到达queuesize,设置了quesize就默认是异步的，否则就是同步
    rospy.INFO("创建发布节点成功")
    #测试前进/后退/左转/右转/逆时针自转/顺时针自传
    # 1.前进10s
    wheel_forward = Controlfunc_gt.GTControl(10,100,100,0)
    Controlfunc_gt.move(1,"forward",pub,wheel_forward,wheel_forward.x)

    # 2.后退10s
    wheel_backward = Controlfunc_gt.GTControl(10,-100,-100,0)
    Controlfunc_gt.move(1,"backward",pub,wheel_backward,wheel_backward.x)

    # 3.向前左转10s
    wheel_left = Controlfunc_gt.GTControl(10,-50,100,0)
    Controlfunc_gt.move(1,"left",pub,wheel_left,wheel_left.x)

    # 4.向前右转10s
    wheel_right = Controlfunc_gt.GTControl(10,100,-50,0)
    Controlfunc_gt.move(1,"right",pub,wheel_right,wheel_right.x)

    # 5.顺时针自转
    wheel_rotate = Controlfunc_gt.GTControl(10,100,-100,0)
    Controlfunc_gt.move(1,"rotate",pub,wheel_rotate,wheel_rotate.x)

    # 5.逆时针自转
    wheel_rotate = Controlfunc_gt.GTControl(10,-100,100,0)
    Controlfunc_gt.move(1,"rotate",pub,wheel_rotate,wheel_rotate.x)

