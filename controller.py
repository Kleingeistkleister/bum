from re import S
import threading, stupidArtnet
import time, queue, commander, connector, stepper, reactor, sys, logging , optparse 
from stupidArtnet import StupidArtnetServer

#uuids
# parra 1:  807d45b5bfeb
# parra 2:
# parra 3:
# parra 4:  3d7db3a77d7d
# parra 5:
# parra 6: a2bb949d00a8
  
class Controller:
    def __init__(self, reactor, main_handler, artnet_handler):
        self.reactor = reactor
        self.main_handler = main_handler
        self.commander = commander.CommandGenerator()
        self.command_queue = queue.Queue()
        self.artnet_handler = artnet_handler

        self.oid = 0        
        self.oid_list = []
        self.init_commands = []

        # Create stepper objects and store commands to the init list
        self.steppers = self.initialize_steppers()

        self.dmx_universe = 0
        self.dmx_start_address = 1
        self.dmx_channel_mode = 4  
        self.dmx_address = self.dmx_start_address
        self.dmx_values_new = [0] * (self.dmx_channel_mode + len(self.steppers))
        self.dmx_values_old = self.dmx_values_new
        self.artnet_listener = artnet_handler.register_listener(self.dmx_universe, callback_function=None)     

        self.is_shutdown = False

        
        # Create artnet handler
        self.artnet = stupidArtnet.StupidArtnetServer()  
        # Register listener
        self.artnet_handler = self.artnet.register_listener(self.dmx_universe, callback_function=None)

        self.allocate_oids()
        self.finalize_config()
        # End config
        print("######################################")
        print(f"Controller created Universe: {self.dmx_universe} Start address: {self.dmx_start_address} Channel mode: {self.dmx_channel_mode}")
        print("######################################")
        for cmd in self.init_commands:
            print(cmd)

    def add_init_command(self, command):
        self.init_commands.append(command)

    def get_commander(self):
        return self.commander

    def readDmx(self):
        buffer = self.artnet_handler.get_buffer(self.artnet_listener)
        if buffer:
            print(buffer)
            self.dmx_values_old = self.dmx_values_new
            self.dmx_values_new = buffer
        else:
            print("no artnet data received")

    def get_new_oid(self):
        self.oid += 1
        return self.oid - 1

    def set_stepper_dmx_values(self, stepper):
        stepper.set_dmx_value.dmx_values[0:self.dmx_channel_mode - 1]

    def write_stepper_config(self):
        for cmd in self.init_commands:
            print(cmd)
            self.main_handler.send_msg(cmd)
            time.sleep(0.01)

    def enable_stepper(self, stepper):
        self.command_queue.put(self.commander.enable_stepper(stepper.get_oid()))

    def stepper_set_next_step_dir(self, stepper, direction):
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
            self.oid_list.append(oid)
            # Create steppers from config
            dmx_stepper = stepper.DMXStepper(
                self, oid, config['step_pin'], config['dir_pin'], config['en_pin'], config['uart_pin'], config['uart_diag_pin'], 
                config['endstop_pin'], config['microsteps'], config['rotation_distance'], config['full_steps_per_rotation'], 
                config['gear_ratio'], config['max_velocity'], config['max_accel'], config['driver'], config['uart_address'], 
                config['stealthchop_threshold']
            )
            steppers.append(dmx_stepper)

        return steppers

    def get_config(self):
        config_response = self.conector(self.commander.get_config())
        return config_response

    def allocate_oids(self):
        self.add_init_command(self.commander.allocate_oids(self.oid))

    def calc_crc(self, data, poly=0x1021, init_crc=0xffff):
        if isinstance(data, str):
            data = data.encode()  # Convert to bytes if data is a string
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

    def finalize_config(self):
        finalize_cmd = self.commander.finalize_config()
        if isinstance(finalize_cmd, str):
            finalize_cmd = finalize_cmd.encode()  # Convert to bytes if finalize_cmd is a string
        crc = 100 #self.calc_crc(finalize_cmd)
        #finalize_cmd_with_crc = finalize_cmd + crc.to_bytes(2, 'big')  # Add CRC to the end of the command
        self.add_init_command("finalize_config crc=100")


    def run(self):
        while 1 and not self.is_shutdown:
            print("#######################")
            self.readDmx()
            self.handle_commands()

    def handle_commands(self):
        while not self.command_queue.empty():
            print("get commands")
            cmd = self.command_queue.get()
            self.main_handler.process_command(cmd)
        print("no commands")    
