class MCUCommands:
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

    def config_thermocouple(self, oid, spi_oid, thermocouple_type):
        return f"config_thermocouple oid={oid} spi_oid={spi_oid} thermocouple_type={thermocouple_type}"

    def config_tmcuart(self, oid, rx_pin, pull_up, tx_pin, bit_time):
        return f"config_tmcuart oid={oid} rx_pin={rx_pin} pull_up={pull_up} tx_pin={tx_pin} bit_time={bit_time}"

    def config_trsync(self, oid):
        return f"config_trsync oid={oid}"

    def debug_nop(self):
        return "debug_nop"

    def debug_ping(self, data):
        return f"debug_ping data={data}"

    def debug_read(self, order, addr):
        return f"debug_read order={order} addr={addr}"

    def debug_write(self, order, addr, val):
        return f"debug_write order={order} addr={addr} val={val}"

    def emergency_stop(self):
        return "emergency_stop"

    def endstop_home(self, oid, clock, sample_ticks, sample_count, rest_ticks, pin_value, trsync_oid, trigger_reason):
        return f"endstop_home oid={oid} clock={clock} sample_ticks={sample_ticks} sample_count={sample_count} rest_ticks={rest_ticks} pin_value={pin_value} trsync_oid={trsync_oid} trigger_reason={trigger_reason}"

    def endstop_query_state(self, oid):
        return f"endstop_query_state oid={oid}"

    def finalize_config(self, crc):
        return f"finalize_config crc={crc}"

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

    def i2c_modify_bits(self, oid, reg, clear_set_bits):
        return f"i2c_modify_bits oid={oid} reg={reg} clear_set_bits={clear_set_bits}"

    def i2c_read(self, oid, reg, read_len):
        return f"i2c_read oid={oid} reg={reg} read_len={read_len}"

    def i2c_set_bus(self, oid, i2c_bus, rate, address):
        return f"i2c_set_bus oid={oid} i2c_bus={i2c_bus} rate={rate} address={address}"

    def i2c_set_software_bus(self, oid, scl_pin, sda_pin, rate, address):
        return f"i2c_set_software_bus oid={oid} scl_pin={scl_pin} sda_pin={sda_pin} rate={rate} address={address}"

    def i2c_write(self, oid, data):
        return f"i2c_write oid={oid} data={data}"

    def identify(self, offset, count):
        return f"identify offset={offset} count={count}"

    def neopixel_send(self, oid):
        return f"neopixel_send oid={oid}"

    def neopixel_update(self, oid, pos, data):
        return f"neopixel_update oid={oid} pos={pos} data={data}"

    def query_adxl345(self, oid, rest_ticks):
        return f"query_adxl345 oid={oid} rest_ticks={rest_ticks}"

    def query_adxl345_status(self, oid):
        return f"query_adxl345_status oid={oid}"

    def query_analog_in(self, oid, clock, sample_ticks, sample_count, rest_ticks, min_value, max_value, range_check_count):
        return f"query_analog_in oid={oid} clock={clock} sample_ticks={sample_ticks} sample_count={sample_count} rest_ticks={rest_ticks} min_value={min_value} max_value={max_value} range_check_count={range_check_count}"

    def query_counter(self, oid, clock, poll_ticks, sample_ticks):
        return f"query_counter oid={oid} clock={clock} poll_ticks={poll_ticks} sample_ticks={sample_ticks}"

    def query_lis2dw(self, oid, rest_ticks):
        return f"query_lis2dw oid={oid} rest_ticks={rest_ticks}"

    def query_lis2dw_status(self, oid):
        return f"query_lis2dw_status oid={oid}"

    def query_mpu9250(self, oid, rest_ticks):
        return f"query_mpu9250 oid={oid} rest_ticks={rest_ticks}"

    def query_mpu9250_status(self, oid):
        return f"query_mpu9250_status oid={oid}"

    def query_spi_angle(self, oid, clock, rest_ticks, time_shift):
        return f"query_spi_angle oid={oid} clock={clock} rest_ticks={rest_ticks} time_shift={time_shift}"

    def query_thermocouple(self, oid, clock, rest_ticks, min_value, max_value, max_invalid_count):
        return f"query_thermocouple oid={oid} clock={clock} rest_ticks={rest_ticks} min_value={min_value} max_value={max_value} max_invalid_count={max_invalid_count}"

    def queue_digital_out(self, oid, clock, on_ticks):
        return f"queue_digital_out oid={oid} clock={clock} on_ticks={on_ticks}"

    def queue_pwm_out(self, oid, clock, value):
        return f"queue_pwm_out oid={oid} clock={clock} value={value}"

    def queue_step(self, oid, interval, count, add):
        return f"queue_step oid={oid} interval={interval} count={count} add={add}"

    def reset(self):
        return "reset"

    def reset_step_clock(self, oid, clock):
        return f"reset_step_clock oid={oid} clock={clock}"

    def set_digital_out(self, pin, value):
        return f"set_digital_out pin={pin} value={value}"

    def set_digital_out_pwm_cycle(self, oid, cycle_ticks):
        return f"set_digital_out_pwm_cycle oid={oid} cycle_ticks={cycle_ticks}"

    def set_next_step_dir(self, oid, dir):
        return f"set_next_step_dir oid={oid} dir={dir}"

    def set_pwm_out(self, pin, cycle_ticks, value):
        return f"set_pwm_out pin={pin} cycle_ticks={cycle_ticks} value={value}"

    def spi_angle_transfer(self, oid, data):
        return f"spi_angle_transfer oid={oid} data={data}"

    def spi_send(self, oid, data):
        return f"spi_send oid={oid} data={data}"

    def spi_set_bus(self, oid, spi_bus, mode, rate):
        return f"spi_set_bus oid={oid} spi_bus={spi_bus} mode={mode} rate={rate}"

    def spi_set_software_bus(self, oid, miso_pin, mosi_pin, sclk_pin, mode, rate):
        return f"spi_set_software_bus oid={oid} miso_pin={miso_pin} mosi_pin={mosi_pin} sclk_pin={sclk_pin} mode={mode} rate={rate}"

    def spi_transfer(self, oid, data):
        return f"spi_transfer oid={oid} data={data}"

    def st7920_send_cmds(self, oid, cmds):
        return f"st7920_send_cmds oid={oid} cmds={cmds}"

    def st7920_send_data(self, oid, data):
        return f"st7920_send_data oid={oid} data={data}"

    def stepper_get_position(self, oid):
        return f"stepper_get_position oid={oid}"

    def stepper_stop_on_trigger(self, oid, trsync_oid):
        return f"stepper_stop_on_trigger oid={oid} trsync_oid={trsync_oid}"

    def tmcuart_send(self, oid, write, read):
        return f"tmcuart_send oid={oid} write={write} read={read}"

    def trsync_set_timeout(self, oid, clock):
        return f"trsync_set_timeout oid={oid} clock={clock}"

    def trsync_start(self, oid, report_clock, report_ticks, expire_reason):
        return f"trsync_start oid={oid} report_clock={report_clock} report_ticks={report_ticks} expire_reason={expire_reason}"

    def trsync_trigger(self, oid, reason):
        return f"trsync_trigger oid={oid} reason={reason}"

    def update_digital_out(self, oid, value):
        return f"update_digital_out oid={oid} value={value}"

    def DELAY(self):
        return "DELAY"

    def DUMP(self):
        return "DUMP"

    def FILEDUMP(self):
        return "FILEDUMP"

    def FLOOD(self):
        return "FLOOD"

    def HELP(self):
        return "HELP"

    def LIST(self):
        return "LIST"

    def SET(self):
        return "SET"

    def STATS(self):
        return "STATS"

    def SUPPRESS(self):
        return "SUPPRESS"


