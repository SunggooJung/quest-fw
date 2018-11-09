<title>LeeCtrl Component Dictionary</title>
# LeeCtrl Component Dictionary


## Telemetry Channel List

|Channel Name|ID|Type|Description|
|---|---|---|---|
|LCTRL_ThrustComm|0 (0x0)|F32|Lee Control commanded body axis thrust|
|LCTRL_MomentCommX|1 (0x1)|F32|Lee Control commanded moment in x|
|LCTRL_MomentCommY|2 (0x2)|F32|Lee Control commanded moment in y|
|LCTRL_MomentCommZ|3 (0x3)|F32|Lee Control commanded moment in z|
|LCTRL_Error_x_w|4 (0x4)|F32|Lee Control x error|
|LCTRL_Error_y_w|5 (0x5)|F32|Lee Control y error|
|LCTRL_Error_z_w|6 (0x6)|F32|Lee Control z error|
|LCTRL_Error_yaw|7 (0x7)|F32|Lee Control yaw error|
|LCTRL_XThrustComm|8 (0x8)|F32|Lee Control commanded thrust in x direction|
|LCTRL_YThrustComm|9 (0x9)|F32|Lee Control commanded thrust in x direction|
|LCTRL_w_q_b__des|10 (0xa)|ROS::geometry_msgs::Quaternion|Lee Control desired orientation|
|LCTRL_w_q_b|11 (0xb)|ROS::geometry_msgs::Quaternion|Lee Control orientation|

## Event List

|Event Name|ID|Description|Arg Name|Arg Type|Arg Size|Description
|---|---|---|---|---|---|---|
|LCTRL_Dummy|0 (0x0)|Lee Control dummy event| | | | |