class IMU_DATA: 

#Method that initializes everything to none so we can set a new value
    def __inti__(self , time_startup = None, time_sync_in = None, ypr = None, attitude = None,orientation = None,angular_rate = None,
    accelaration = None,imu_accelaration = None, imu_rate = None, mag = None, temp = None,pres = None,dtime = None,dtheta = None,
    dvel = None, vpe_status = None,sync_in_cnt = None, sync_out_cnt = None, imu_dict_data = None):

        self.time_startup: int = time_startup
        self.time_sync_in: int = time_sync_in
        self.ypr: float = ypr
        self.attitude: float = attitude
        self.orientation: float = orientation
        self.angular_rate: float = angular_rate
        self.accelearation: float = accelaration
        self.imu_accelaration: float = imu_accelaration
        self.imu_rate: float = imu_rate 
        self.mag: float = mag
        self.temp: float = temp
        self.pres: float = pres
        self.dtime: float = dtime
        self.dtheta: float = dtheta
        self.dvel: float = dvel
        self.vpe_status: int = vpe_status
        self.sync_in_cnt: int = sync_in_cnt
        self.sync_out_cnt: int = sync_out_cnt

# if there is any problem when using one of the values , check the type. 

        if imu_dict_data:
            self.prepare_data(imu_dict_data)

        def prepare_data(self, imu_dict: dict):
            for key in vars(self).keys():
                if key in imu_dict:
                    setattr(self, key , imu_dict[key])

        def clear_data(self):
            for key in vars(self).keys():
                setattr(self, key , None)

        def get_all_var_names_ls():
            return list(vars[IMU_DATA().keys()])


        if __name__=='__main__':
            print('IMU_DATA Test Variable Names:')
            print(IMU_DATA.get_all_var_names_ls())


