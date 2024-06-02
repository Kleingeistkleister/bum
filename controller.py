import threading
import time, queue, commander, stepper



class Controller:
    def __init__(self):
        self.commander = commander.CommandGenerator()
        self.init_queue = queue.Queue()
        self.oid = 0
        
        self.dmx_start_address = 1
        self.dmx_channel_mode = 4
        self._serial = None
       
        self.dmx_address = self.dmx_start_address
       
        self.init_commands = []
        #create stepper objects and store commands to the init list
        self.steppers = self.initialize_steppers()

    

    def add_init_command(self, command):
        self.init_commands.append(command)
        
    def get_commander(self):
        return self.commander

    # create a dmx channel address for stepper objects
        
    def get_new_dmx_address(self):
        self.dmx_address += self.dmx_channel_mode
        return self.dmx_address - self.dmx_channel_mode

    def get_new_oid(self):
        self.oid += 1
        return self.oid - 1

    def set_stepper_dmx_values(self, stepper):
        stepper.set_dmx_value.dmx_values[0:self.dmx_channel_mode-1]


    #write init commands for steppers
    def write_stepper_config(self):
        for cmd in self.init_commands:
            self._serial.write(cmd)
            time.sleep(0.01)
        


    def initialize_steppers(self):
        steppers = []

        # Add stepper configurations directly
        stepper_configs = [
            {"step_pin": "PE2", "dir_pin": "PB4", "en_pin": "!PC11", "uart_pin": "P2.6", "uart_diag_pin": "P2.6", "endstop_pin": "^PF3",
             "microsteps": 16, "rotation_distance": 40, "full_steps_per_rotation": 200, "gear_ratio": 1, "max_velocity": 300,
             "max_accel": 3000, "driver": "tmc2209", "uart_address": 0, "stealthchop_threshold": 999999},
            {"step_pin": "PF12", "dir_pin": "PF11", "en_pin": "!PB3", "uart_pin": "P2.6", "uart_diag_pin": "P2.6", "endstop_pin": "^PF4",
             "microsteps": 16, "rotation_distance": 40, "full_steps_per_rotation": 200, "gear_ratio": 1, "max_velocity": 300,
             "max_accel": 3000, "driver": "tmc2209", "uart_address": 1, "stealthchop_threshold": 999999},
            {"step_pin": "PD7", "dir_pin": "!PD6", "en_pin": "!PF10", "uart_pin": "P2.6", "uart_diag_pin": "P2.6", "endstop_pin": "^PF5",
             "microsteps": 16, "rotation_distance": 40, "full_steps_per_rotation": 200, "gear_ratio": 1, "max_velocity": 300,
             "max_accel": 3000, "driver": "tmc2209", "uart_address": 2, "stealthchop_threshold": 999999},
            {"step_pin": "PD3", "dir_pin": "PD2", "en_pin": "!PD5", "uart_pin": "P2.6", "uart_diag_pin": "P2.6", "endstop_pin": "^PF6",
             "microsteps": 16, "rotation_distance": 40, "full_steps_per_rotation": 200, "gear_ratio": 1, "max_velocity": 300,
             "max_accel": 3000, "driver": "tmc2209", "uart_address": 3, "stealthchop_threshold": 999999},
            {"step_pin": "PC9", "dir_pin": "PC8", "en_pin": "!PD1", "uart_pin": "P2.6", "uart_diag_pin": "P2.6", "endstop_pin": "^PF7",
             "microsteps": 16, "rotation_distance": 40, "full_steps_per_rotation": 200, "gear_ratio": 1, "max_velocity": 300,
             "max_accel": 3000, "driver": "tmc2209", "uart_address": 4, "stealthchop_threshold": 999999},
            {"step_pin": "PA10", "dir_pin": "PA14", "en_pin": "!PA15", "uart_pin": "P2.6", "uart_diag_pin": "P2.6", "endstop_pin": "^PF8",
             "microsteps": 16, "rotation_distance": 40, "full_steps_per_rotation": 200, "gear_ratio": 1, "max_velocity": 300,
             "max_accel": 3000, "driver": "tmc2209", "uart_address": 5, "stealthchop_threshold": 999999}
        ]

        for config in stepper_configs:
            oid = self.get_new_oid()
            dmx_address = self.get_new_dmx_address()
            #create steppers from config
            dmx_stepper = stepper.DMXStepper(
                self, oid, config['step_pin'], config['dir_pin'], config['en_pin'], config['uart_pin'], config['uart_diag_pin'], 
                config['endstop_pin'], config['microsteps'], config['rotation_distance'], config['full_steps_per_rotation'], 
                config['gear_ratio'], config['max_velocity'], config['max_accel'], config['driver'], config['uart_address'], 
                config['stealthchop_threshold'],
                
                #dmx values
                dmx_address, self.dmx_channel_mode
                
            )
            steppers.append(dmx_stepper)
            

        return steppers

def main():
    controller = Controller()
    # Access controller.stepper_commands to get the list of commands for initialization
    print("Stepper initialization commands:")
    for cmd in controller.init_commands:
        print(cmd)

if __name__ == "__main__":
    main()
