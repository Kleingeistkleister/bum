class CommandGenerator:
    def __init__(self):
        self.commands = {
            "allocate_oids": self.allocate_oids,
            
            "buttons_ack": self.buttons_ack,
            "buttons_add": self.buttons_add,
            "buttons_query": self.buttons_query,
            
            "clear_shutdown": self.clear_shutdown,
            

            "config_adxl345": self.config_adxl345,
            "config_analog_in": self.config_analog_in,
            "config_buttons": self.config_buttons,
            "config_counter": self.config_counter,
            "config_digital_out": self.config_digital_out,
            "config_endstop": self.config_endstop,
            "config_hd44780": self.config_hd44780,
            "config_i2c": self.config_i2c,
            "config_lis2dw": self.config_lis2dw,
            "config_mpu9250": self.config_mpu9250,
            "config_neopixel": self.config_neopixel,
            "config_pwm_out": self.config_pwm_out,
            "config_spi": self.config_spi,
            "config_spi_angle": self.config_spi_angle,
            "config_spi_shutdown": self.config_spi_shutdown,
            "config_spi_without_cs": self.config_spi_without_cs,
            "config_st7920": self.config_st7920,
            "config_stepper": self.config_stepper,  #################################################
            "config_thermocouple": self.config_thermocouple,
            "config_tmcuart": self.config_tmcuart,
            "config_trsync": self.config_trsync,         

            "debug_nop": self.debug_nop,
            "debug_ping": self.debug_ping,
            "debug_read": self.debug_read,
            "debug_write": self.debug_write,
            
            "emergency_stop": self.emergency_stop,
            "endstop_home": self.endstop_home,
            "endstop_query_state": self.endstop_query_state,
            "finalize_config": self.finalize_config,
            
            "get_canbus_id": self.get_canbus_id,
            "get_clock": self.get_clock,
            "get_config": self.get_config,
            "get_uptime": self.get_uptime,
            
            "hd44780_send_cmds": self.hd44780_send_cmds,
            "hd44780_send_data": self.hd44780_send_data,
            
            "i2c_modify_bits": self.i2c_modify_bits,
            "i2c_read": self.i2c_read,
            "i2c_set_bus": self.i2c_set_bus,
            "i2c_set_software_bus": self.i2c_set_software_bus,
            "i2c_write": self.i2c_write,
            
            "identify": self.identify,
            
            "neopixel_send": self.neopixel_send,
            "neopixel_update": self.neopixel_update,
            
            "query_adxl345": self.query_adxl345,
            "query_adxl345_status": self.query_adxl345_status,
            "query_analog_in": self.query_analog_in,
            "query_counter": self.query_counter,
            "query_lis2dw": self.query_lis2dw,
            "query_lis2dw_status": self.query_lis2dw_status,
            "query_mpu9250": self.query_mpu9250,
            "query_mpu9250_status": self.query_mpu9250_status,
            "query_spi_angle": self.query_spi_angle,
            "query_thermocouple": self.query_thermocouple,
            "queue_digital_out": self.queue_digital_out,
            "queue_pwm_out": self.queue_pwm_out,
            "queue_step": self.queue_step,
            
            "reset": self.reset,
            "reset_step_clock": self.reset_step_clock,
            
            "set_digital_out": self.set_digital_out,
            "set_digital_out_pwm_cycle": self.set_digital_out_pwm_cycle,
            "set_next_step_dir": self.set_next_step_dir,
            "set_pwm_out": self.set_pwm_out,
            "spi_angle_transfer": self.spi_angle_transfer,
            "spi_send": self.spi_send,
            "spi_set_bus": self.spi_set_bus,
            "spi_set_software_bus": self.spi_set_software_bus,
            "spi_transfer": self.spi_transfer,
            
            "st7920_send_cmds": self.st7920_send_cmds,
            "st7920_send_data": self.st7920_send_data,
            
            "stepper_get_position": self.stepper_get_position,
            "stepper_stop_on_trigger": self.stepper_stop_on_trigger,
            
            "tmcuart_send": self.tmcuart_send,
            "trsync_set_timeout": self.trsync_set_timeout,
            "trsync_start": self.trsync_start,
            "trsync_trigger": self.trsync_trigger,
            "update_digital_out": self.update_digital_out,
            
        }
        


    def create_command(self, command_name, *args):
        if command_name in self.commands:
            cmd = self.commands[command_name](*args)
        else:
            raise ValueError(f"Command {command_name} not found")
            return
            return cmd
    
    # Define all the commands as methods
    def allocate_oids(self, count):
        return f"allocate_oids count={count}"

    def buttons_ack(self, oid, count):
        return f"buttons_ack oid={oid} count={count}"

    def buttons_add(self, oid, pos, pin, pull_up):
        return f"buttons_add oid={oid} pos={pos} pin={pin} pull_up={pull_up}"

    def buttons_query(self, oid, clock, rest_ticks, retransmit_count, invert):
        return f"buttons_query oid={oid} clock={clock} rest_ticks={rest_ticks} retransmit_count={retransmit_count} invert={invert}"

    def clear_shutdown(self):
        return "clear_shutdown"

    def config_adxl345(self, oid, spi_oid):
        return f"config_adxl345 oid={oid} spi_oid={spi_oid}"

    def config_analog_in(self, oid, pin):
        return f"config_analog_in oid={oid} pin={pin}"

    def config_buttons(self, oid, button_count):
        return f"config_buttons oid={oid} button_count={button_count}"

    def config_counter(self, oid, pin, pull_up):
        return f"config_counter oid={oid} pin={pin} pull_up={pull_up}"

    def config_digital_out(self, oid, pin, value, default_value, max_duration):
        return f"config_digital_out oid={oid} pin={pin} value={value} default_value={default_value} max_duration={max_duration}"

    def config_endstop(self, oid, pin, pull_up):
        return f"config_endstop oid={oid} pin={pin} pull_up={pull_up}"

    def config_hd44780(self, oid, rs_pin, e_pin, d4_pin, d5_pin, d6_pin, d7_pin, delay_ticks):
        return f"config_hd44780 oid={oid} rs_pin={rs_pin} e_pin={e_pin} d4_pin={d4_pin} d5_pin={d5_pin} d6_pin={d6_pin} d7_pin={d7_pin} delay_ticks={delay_ticks}"

    def config_i2c(self, oid):
        return f"config_i2c oid={oid}"

    def config_lis2dw(self, oid, spi_oid):
        return f"config_lis2dw oid={oid} spi_oid={spi_oid}"

    def config_mpu9250(self, oid, i2c_oid):
        return f"config_mpu9250 oid={oid} i2c_oid={i2c_oid}"

    def config_neopixel(self, oid, pin, data_size, bit_max_ticks, reset_min_ticks):
        return f"config_neopixel oid={oid} pin={pin} data_size={data_size} bit_max_ticks={bit_max_ticks} reset_min_ticks={reset_min_ticks}"

    def config_pwm_out(self, oid, pin, cycle_ticks, value, default_value, max_duration):
        return f"config_pwm_out oid={oid} pin={pin} cycle_ticks={cycle_ticks} value={value} default_value={default_value} max_duration={max_duration}"

    def config_spi(self, oid, pin, cs_active_high):
        return f"config_spi oid={oid} pin={pin} cs_active_high={cs_active_high}"

    def config_spi_angle(self, oid, spi_oid, spi_angle_type):
        return f"config_spi_angle oid={oid} spi_oid={spi_oid} spi_angle_type={spi_angle_type}"

    def config_spi_shutdown(self, oid, spi_oid, shutdown_msg):
        return f"config_spi_shutdown oid={oid} spi_oid={spi_oid} shutdown_msg={shutdown_msg}"

    def config_spi_without_cs(self, oid):
        return f"config_spi_without_cs oid={oid}"

    def config_st7920(self, oid, cs_pin, sclk_pin, sid_pin, sync_delay_ticks, cmd_delay_ticks):
        return f"config_st7920 oid={oid} cs_pin={cs_pin} sclk_pin={sclk_pin} sid_pin={sid_pin} sync_delay_ticks={sync_delay_ticks} cmd_delay_ticks={cmd_delay_ticks}"

    def config_stepper(self, oid, step_pin, dir_pin, invert_step, step_pulse_ticks):
        return f"config_stepper oid={oid} step_pin={step_pin} dir_pin={dir_pin} invert_step={invert_step} step_pulse_ticks={step_pulse_ticks}"

    def config_thermocouple(self, oid, spi_oid):
        return f"config_thermocouple oid={oid} spi_oid={spi_oid}"

    def config_tmcuart(self, oid, uart_oid):
        return f"config_tmcuart oid={oid} uart_oid={uart_oid}"

    def config_trsync(self, oid, pin, invert):
        return f"config_trsync oid={oid} pin={pin} invert={invert}"

    def debug_nop(self):
        return "debug_nop"

    def debug_ping(self):
        return "debug_ping"

    def debug_read(self, addr, count):
        return f"debug_read addr={addr} count={count}"

    def debug_write(self, addr, data):
        return f"debug_write addr={addr} data={data}"

    def emergency_stop(self):
        return "emergency_stop"

    def endstop_home(self, oid, sample_ticks, rest_ticks, pin, pull_up, invert):
        return f"endstop_home oid={oid} sample_ticks={sample_ticks} rest_ticks={rest_ticks} pin={pin} pull_up={pull_up} invert={invert}"

    def endstop_query_state(self, oid):
        return f"endstop_query_state oid={oid}"

    def finalize_config(self):
        return "finalize_config"

    def get_canbus_id(self):
        return "get_canbus_id"

    def get_clock(self):
        return "get_clock"

    def get_config(self):
        return "get_config"

    def get_uptime(self):
        return "get_uptime"

    def hd44780_send_cmds(self, oid, cmds):
        return f"hd44780_send_cmds oid={oid} cmds={cmds}"

    def hd44780_send_data(self, oid, data):
        return f"hd44780_send_data oid={oid} data={data}"

    def i2c_modify_bits(self, oid, addr, reg, clear_bits, set_bits):
        return f"i2c_modify_bits oid={oid} addr={addr} reg={reg} clear_bits={clear_bits} set_bits={set_bits}"

    def i2c_read(self, oid, addr, reg, count):
        return f"i2c_read oid={oid} addr={addr} reg={reg} count={count}"

    def i2c_set_bus(self, oid, bus_num):
        return f"i2c_set_bus oid={oid} bus_num={bus_num}"

    def i2c_set_software_bus(self, oid, scl_pin, sda_pin):
        return f"i2c_set_software_bus oid={oid} scl_pin={scl_pin} sda_pin={sda_pin}"

    def i2c_write(self, oid, addr, reg, data):
        return f"i2c_write oid={oid} addr={addr} reg={reg} data={data}"

    def identify(self):
        return "identify"

    def neopixel_send(self, oid, data):
        return f"neopixel_send oid={oid} data={data}"

    def neopixel_update(self, oid):
        return f"neopixel_update oid={oid}"

    def query_adxl345(self, oid):
        return f"query_adxl345 oid={oid}"

    def query_adxl345_status(self, oid):
        return f"query_adxl345_status oid={oid}"

    def query_analog_in(self, oid):
        return f"query_analog_in oid={oid}"

    def query_counter(self, oid):
        return f"query_counter oid={oid}"

    def query_lis2dw(self, oid):
        return f"query_lis2dw oid={oid}"

    def query_lis2dw_status(self, oid):
        return f"query_lis2dw_status oid={oid}"

    def query_mpu9250(self, oid):
        return f"query_mpu9250 oid={oid}"

    def query_mpu9250_status(self, oid):
        return f"query_mpu9250_status oid={oid}"

    def query_spi_angle(self, oid):
        return f"query_spi_angle oid={oid}"

    def query_thermocouple(self, oid):
        return f"query_thermocouple oid={oid}"

    def queue_digital_out(self, oid, value, cycle):
        return f"queue_digital_out oid={oid} value={value} cycle={cycle}"

    def queue_pwm_out(self, oid, value, cycle):
        return f"queue_pwm_out oid={oid} value={value} cycle={cycle}"
    
    def queue_step(self, oid, interval, count, add):
        return f"queue_step oid={oid} interval={interval} count={count} add={add}"


    def reset(self):
        return "reset"

    def reset_step_clock(self, oid):
        return f"reset_step_clock oid={oid}"

    def set_digital_out(self, oid, value):
        return f"set_digital_out oid={oid} value={value}"

    def set_digital_out_pwm_cycle(self, oid, value, cycle):
        return f"set_digital_out_pwm_cycle oid={oid} value={value} cycle={cycle}"

    def set_next_step_dir(self, oid, dir):
        return f"set_next_step_dir oid={oid} dir={dir}"

    def set_pwm_out(self, oid, value):
        return f"set_pwm_out oid={oid} value={value}"

    def spi_angle_transfer(self, oid, data):
        return f"spi_angle_transfer oid={oid} data={data}"

    def spi_send(self, oid, data):
        return f"spi_send oid={oid} data={data}"

    def spi_set_bus(self, oid, bus_num):
        return f"spi_set_bus oid={oid} bus_num={bus_num}"

    def spi_set_software_bus(self, oid, sck_pin, mosi_pin, miso_pin):
        return f"spi_set_software_bus oid={oid} sck_pin={sck_pin} mosi_pin={mosi_pin} miso_pin={miso_pin}"

    def spi_transfer(self, oid, data):
        return f"spi_transfer oid={oid} data={data}"

    def st7920_send_cmds(self, oid, cmds):
        return f"st7920_send_cmds oid={oid} cmds={cmds}"

    def st7920_send_data(self, oid, data):
        return f"st7920_send_data oid={oid} data={data}"

    def stepper_get_position(self, oid):
        return f"stepper_get_position oid={oid}"

    def stepper_stop_on_trigger(self, oid, trigger, value):
        return f"stepper_stop_on_trigger oid={oid} trigger={trigger} value={value}"

    def tmcuart_send(self, oid, data):
        return f"tmcuart_send oid={oid} data={data}"

    def trsync_set_timeout(self, oid, timeout):
        return f"trsync_set_timeout oid={oid} timeout={timeout}"

    def trsync_start(self, oid):
        return f"trsync_start oid={oid}"

    def trsync_trigger(self, oid, trigger):
        return f"trsync_trigger oid={oid} trigger={trigger}"

    def update_digital_out(self, oid, value):
        return f"update_digital_out oid={oid} value={value}"
