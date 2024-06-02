import threading, stupidArtnet
import time, queue, commander,connector, stepper, reactor, sys, logging
from stupidArtnet import StupidArtnetServer

#uuids
# parra 1:  807d45b5bfeb
# parra 2:
# parra 3:
# parra 4:  3d7db3a77d7d
# parra 5:
# parra 6: a2bb949d00a8
  
    
class Controller:
    def __init__(self):
        self.commander = commander.CommandGenerator()
        self.command_queue = queue.Queue()
        self.reactor = reactor.Reactor()
        self.oid = 0
        
        self.dmx_universe = 0
        self.dmx_start_address = 1
        self.dmx_channel_mode = 4
        self.serial_handler = None
       
        self.dmx_address = self.dmx_start_address
       
        self.init_commands = []
        #create stepper objects and store commands to the init list
        self.steppers = self.initialize_steppers()
        self.artnet = stupidArtnet.StupidArtnetServer()  
        
        self.artnet_handler = self.artnet.register_listener( self.dmx_universe, callback_function=None)

        print(f"Controller created Universe: {self.dmx_universe} Start address: {self.dmx_start_address} Channel mode: {self.dmx_channel_mode}")
  
        
        #try:
            #self.reactor.run()
        #except KeyboardInterrupt:
            #sys.stdout.write("\n")
            
        #while not self.command_queue.empty():
          #  self._serial.write(self.command_queue.get())
           # time.sleep(0.01)


    def add_init_command(self, command):
        self.init_commands.append(command)
        
    def get_commander(self):
        return self.commander

    # create a dmx channel address for stepper objects
        
    def get_new_dmx_address(self):
        self.dmx_address += self.dmx_channel_mode
        return self.dmx_address - self.dmx_channel_mode

    def readDmx(self):
        buffer = self.artnet_handler.getBuffer(self.artnet)
        self.valA = int(buffer[self.channelA - 1])
        self.valB = int(buffer[self.channelB - 1])
        self.valC = int(buffer[self.channelC - 1])

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
            
    def calc_crc(self):
        return 0
        
    def enable_stepper(self, stepper):
        self.command_queue.put(self.commander.enable_stepper(stepper.get_oid()))
        
    def stepper_set_next_step_dir(self,stepper, direction):
        cmd = self.command_queue.put(self.commander.stepper_set_next_step_dir(stepper.get_oid(), direction))

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
    

    def set_serial_handler(self, serial_handler):
    
        self.serial_handler = serial_handler
        
    def finalize_config(self):
        self.command_queue.put(self.commander.finalize_config())

  
        
    def alloc_oids(self):
        self.command_queue.put(self.commander.alloc_oids(self.oid))
        
    def calc_crc(data, poly=0x1021, init_crc=0xffff):
        crc = init_crc
        for byte in data:
            crc ^= byte << 8
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ poly
                else:
                    crc <<= 1
                crc &= 0xffff  # Keep CRC within 16 bits
        return crc

    def get_config(self):
        config_response = self.conector(self.commander.get_config())
        return config_response
    


    def finalize_config(self):
        finalize_cmd = self.commander.finalize_config()
        crc = self.calc_crc(finalize_cmd)
        finalize_cmd_with_crc = finalize_cmd + crc.to_bytes(2, 'big')  # Add CRC to the end of the command
        self.command_queue.put(finalize_cmd_with_crc)


        def run(self):
            while True:
                if not self.command_queue.empty():
                    self.serial_handler.write(self.command_queue.get())
                    time.sleep(0.01)
                else:
                    time.sleep(0.01)


def main():
    serialport = "/dev/ttyACM0"  # Provide the serial port here
    baud = 1000000  # Provide the baud rate here
    canbus_iface = "can0"  # Provide the CAN bus interface here
    canbus_nodeid = int(807d45b5bfeb,16)  # Provide the CAN bus node ID here
    print("Create Controller")
    controller = Controller()
    print("Create Serial Handler")
    serial_handler = connector.SerialHandler(controller, controller.reactor, serialport, baud, canbus_iface, canbus_nodeid)
    
    controller.set_serial_handler(serial_handler)
    # Access controller.stepper_commands to get the list of commands for initialization
    print("Stepper initialization commands:")
    while not controller.command_queue.empty():
        cmd = controller.command_queue.get()
        print(cmd)

if __name__ == "__main__":
    main()

