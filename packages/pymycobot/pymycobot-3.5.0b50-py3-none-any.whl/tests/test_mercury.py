import pytest
import time, sys, os
import random

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from pymycobot import Mercury
from pymycobot.common import DataProcessor, ProtocolCode, ProGripper
from pymycobot import utils



class MercuryTest(DataProcessor):
    def __init__(self, debug=False):
        super(MercuryTest, self).__init__(debug)

m : Mercury
data_check : MercuryTest
gripper_id = 14
HEADER = 0xfe

@pytest.fixture(scope="module")
def setup_robot():
    global m, data_check
    detected = utils.detect_port_of_basic()
    if not detected:
        plist = utils.get_port_list()
        idx = 1
        for port in plist:
            print("{} : {}".format(idx, port))
            idx += 1

        _in = input("\nPlease input 1 - {} to choice:".format(idx - 1))
        port = plist[int(_in) - 1]
    else:
        port = detected
    m = Mercury(port)
    res = m.power_on()
    data_check = MercuryTest()
    assert res == 1
    
# def test_pro_gripper_angle(setup_robot):
#     """角度设置和读取测试"""
#     error_threshold = 2
#     m.set_pro_gripper_angle(gripper_id, 0)
#     time.sleep(2)
#     new_angle_0 = m.get_pro_gripper_angle(gripper_id)
#     m.set_pro_gripper_angle(gripper_id, 100)
#     time.sleep(2)
#     new_angle_100 = m.get_pro_gripper_angle(gripper_id)
#     assert abs(new_angle_0 - 0) <= error_threshold and abs(new_angle_100 - 100) <= error_threshold

# def test_get_pro_gripper_status(setup_robot):
#     """状态读取测试"""
#     status = m.get_pro_gripper_status(gripper_id)
#     assert status == 1
    
# def test_pro_gripper_torque(setup_robot):
#     """力矩设置和读取测试"""
#     random_torque = random.randint(100, 300)
#     m.set_pro_gripper_torque(gripper_id, random_torque)
#     time.sleep(0.1)
#     new_torque = m.get_pro_gripper_torque(gripper_id)
#     assert new_torque == random_torque
    
# def test_pro_gripper_speed(setup_robot):
#     """速度设置和读取测试"""
#     random_speed = random.randint(1, 100)
#     m.set_pro_gripper_speed(gripper_id, random_speed)
#     time.sleep(0.1)
#     new_speed = m.get_pro_gripper_speed(gripper_id)
#     assert new_speed == random_speed
    
# def test_pro_gripper_abs_angle(setup_robot):
#     """绝对角度设置测试"""
#     random_angle = random.randint(0, 100)
#     m.set_pro_gripper_abs_angle(gripper_id, random_angle)
#     new_angle_0 = m.get_pro_gripper_angle(gripper_id)
#     assert abs(new_angle_0 - random_angle) <= 2

def command_check(address, value, robot_command):
    """检查指令格式"""
    global gripper_id
    all_command = [gripper_id, address, value]
    real_command, _, _ = data_check._mesg(robot_command,gripper_id, address, value)
    command_len = len(real_command)
    print(real_command)
    i = 0
    j = 0
    while i < command_len:
        if i == 0:
            assert real_command[i] == HEADER
        elif i == 1:
            assert real_command[i] == HEADER
        elif i == 2:
            assert real_command[i] == len(real_command[i+1:])
        elif i == 3:
            assert real_command[i] == robot_command
        elif i == 4:
            assert real_command[i] == all_command[j]
            j+=1
        elif i == command_len - 1:
            assert real_command[i:] == data_check.crc_check(real_command[:-2])
        elif i > 4:
            print(all_command[j], i,j, real_command[i])
            
            if isinstance(all_command[j], list):
                id = data_check._encode_int16(all_command[j])
                assert id == real_command[i:i+2]
                i += 1
            elif isinstance(all_command[j], int):
                assert real_command[i] == all_command[j]
            j+=1
        i+=1
    
def test_pro_gripper_pause(setup_robot):
    """暂停测试"""
    command_check([ProGripper.SET_GRIPPER_PAUSE], [0], ProtocolCode.MERCURY_SET_TOQUE_GRIPPER)
    # 检测返回的数据是否正常解析
    res = m.set_pro_gripper_pause(gripper_id)
    assert res == 1
            
        
    
if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])