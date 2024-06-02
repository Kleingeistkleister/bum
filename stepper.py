from calendar import c
from mimetypes import init
import controller


class DMXStepper:
    def __init__(self,controller, oid, step_pin, dir_pin, en_pin, uart_pin, uart_diag_pin, endstop_pin, microsteps, 
                 rotation_distance, full_steps_per_rotation, gear_ratio, max_velocity, max_accel, driver, 
                 uart_address, stealthchop_threshold, dmx_start_address, dmx_channel_mode):
        self.controller                     = controller
        self.commander                      = controller.get_commander()
        self.oid                            = oid
        self.step_pin                       = step_pin
        self.dir_pin                        = dir_pin
        self.en_pin                         = en_pin
        self.uart_pin                       = uart_pin
        self.uart_diag_pin                  = uart_diag_pin
        self.endstop_pin                    = endstop_pin
        self.microsteps                     = microsteps
        self.rotation_distance              = rotation_distance
        self.full_steps_per_rotation        = full_steps_per_rotation
        self.gear_ratio                     = gear_ratio
        self.max_velocity                   = max_velocity
        self.max_accel                      = max_accel
        self.driver                         = driver
        self.uart_address                   = uart_address
        self.stealthchop_threshold          = stealthchop_threshold
        self.dmx_start_address              = dmx_start_address
        self.dmx_channel_mode               = dmx_channel_mode
        self.dmx_values_old                 = [0] * dmx_channel_mode
        self.dmx_values_new                 = [0] * dmx_channel_mode
        self.pulse_ticks                    = 0.00010   ########################################
        self.debug_state                    = True    
        


        if self.debug_state:
            
            print(f"Stepper {self.oid} created with stepPin {self.step_pin} and dirPin {self.dir_pin} enablePin {self.en_pin}")
            print(f"Stepper {self.oid} DMX start address: {self.dmx_start_address} DMX channel mode: {self.dmx_channel_mode}")


        # add commands to controller
        #set up stepper on mcu, with the command config_stepper   0 i for inverted
        #init_command = self.create_config_command()
        init_command = self.config_stepper_command()
        self.controller.command_queue.put(init_command)
           
  

    def config_stepper_command(self):
        return self.commander.config_stepper(self.oid, self.step_pin, self.dir_pin, 0 , self.pulse_ticks)

    def debug_print(self, msg):
        print(f"Stepper debug:                   {self.oid}: {msg}")


    #################################################################################################################################
    # Getters
    #################################################################################################################################
    def get_controller(self):
        return self.controller

    def get_oid(self):
        return self.oid

    def get_step_pin(self):
        return self.step_pin

    def get_dir_pin(self):
        return self.dir_pin

    def get_en_pin(self):
        return self.en_pin

    def get_uart_pin(self):
        return self.uart_pin

    def get_uart_diag_pin(self):
        return self.uart_diag_pin

    def get_endstop_pin(self):
        return self.endstop_pin

    def get_microsteps(self):
        return self.microsteps

    def get_rotation_distance(self):
        return self.rotation_distance

    def get_full_steps_per_rotation(self):
        return self.full_steps_per_rotation

    def get_gear_ratio(self):
        return self.gear_ratio

    def get_max_velocity(self):
        return self.max_velocity

    def get_max_accel(self):
        return self.max_accel

    def get_driver(self):
        return self.driver

    def get_uart_address(self):
        return self.uart_address

    def get_stealthchop_threshold(self):
        return self.stealthchop_threshold

    def get_dmx_start_address(self):
        return self.dmx_start_address

    def get_dmx_channel_mode(self):
        return self.dmx_channel_mode

    def get_dmx_values_old(self):
        return self.dmx_values_old
    
    def get_dmx_values_new(self):
        return self.dmx_values_new


    #################################################################################################################################
    # Setters
    #################################################################################################################################
   
    def set_controller(self, controller):
        self.controller = controller

    def set_oid(self, oid):
        self.oid = oid

    def set_step_pin(self, step_pin):
        self.step_pin = step_pin

    def set_dir_pin(self, dir_pin):
        self.dir_pin = dir_pin

    def set_en_pin(self, en_pin):
        self.en_pin = en_pin

    def set_uart_pin(self, uart_pin):
        self.uart_pin = uart_pin

    def set_uart_diag_pin(self, uart_diag_pin):
        self.uart_diag_pin = uart_diag_pin

    def set_endstop_pin(self, endstop_pin):
        self.endstop_pin = endstop_pin

    def set_microsteps(self, microsteps):
        self.microsteps = microsteps

    def set_rotation_distance(self, rotation_distance):
        self.rotation_distance = rotation_distance

    def set_full_steps_per_rotation(self, full_steps_per_rotation):
        self.full_steps_per_rotation = full_steps_per_rotation

    def set_gear_ratio(self, gear_ratio):
        self.gear_ratio = gear_ratio

    def set_max_velocity(self, max_velocity):
        self.max_velocity = max_velocity

    def set_max_accel(self, max_accel):
        self.max_accel = max_accel

    def set_driver(self, driver):
        self.driver = driver

    def set_uart_address(self, uart_address):
        self.uart_address = uart_address

    def set_stealthchop_threshold(self, stealthchop_threshold):
        self.stealthchop_threshold = stealthchop_threshold

    def set_dmx_start_address(self, dmx_start_address):
        self.dmx_start_address = dmx_start_address

    def set_dmx_channel_mode(self, dmx_channel_mode):
        self.dmx_channel_mode = dmx_channel_mode

    def set_dmx_values_old(self, dmx_values_old):
        self.dmx_values_old = dmx_values_old
        