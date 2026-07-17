import time
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.unitree_go.msg.dds_ import WirelessController_

ChannelFactoryInitialize(1, "lo")

sub = ChannelSubscriber("rt/wirelesscontroller", WirelessController_)
sub.Init()

print("Move Xbox sticks / press buttons...")
while True:
    msg = sub.Read()
    if msg is not None:
        print(
                f"lx={msg.lx:5.2f} ly={msg.ly:5.2f} "
                f"rx={msg.rx:5.2f} ry={msg.ry:5.2f} keys={msg.keys}"
        )
    time.sleep(0.05)
