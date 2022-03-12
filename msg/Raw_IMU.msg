std_msgs/Header header
uint64 time_startup
uint64 time_sync_in
geometry_msgs/Vector3 ypr # angular velocities
geometry_msgs/Quaternion attitude # orientation in terms of quaternion
geometry_msgs/Vector3 orientation # orientation in terms of euler angles
geometry_msgs/Vector3 angular_rate
geometry_msgs/Vector3 accelaration
geometry_msgs/Vector3 imu_accelaration # uncompensated
geometry_msgs/Vector3 imu_rate # uncompensated
geometry_msgs/Vector3 mag # compensated magnetic measurement
float64 temp # compensated temperature measurement
float64 pres # compensated pressure measurement
float64 dtime # delta time
geometry_msgs/Vector3 dtheta # delta rotation angles
geometry_msgs/Vector3 dvel # delta velocity
uint16 vpe_status
uint32 sync_in_cnt # number of SyncIn trigger events
uint32 sync_out_cnt # number of SyncOut trigger events
