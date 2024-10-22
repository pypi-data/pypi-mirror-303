import serial
from serial.tools import list_ports
import re
import threading
from rich import print
from rich.console import Console
from rich.panel import Panel
import queue
from moons_motor.subject import Subject
import time


class StepperModules:
    STM17S_3RN = "STM17S-3RN"


class MoonsStepper(Subject):
    motorAdress = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "'",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
    ]

    def __init__(
        self,
        model: StepperModules,
        VID,
        PID,
        SERIAL_NUM,
        only_simlate=False,
        universe=0,
    ):
        super().__init__()
        self.universe = universe
        self.model = model
        self.only_simulate = only_simlate
        self.device = ""
        self.VID = VID
        self.PID = PID
        self.SERIAL_NUM = SERIAL_NUM
        self.ser = None
        self.listeningBuffer = ""
        self.listeningBufferPre = ""
        self.transmitDelay = 0.010
        self.lock = False
        self.Opened = False
        self.new_data_event = threading.Event()
        self.new_value_event = threading.Event()
        self.on_send_event = threading.Event()
        self.recvQueue = queue.Queue()
        self.sendQueue = queue.Queue()
        self.command_cache = queue.Queue()
        self.usedSendQueue = queue.Queue()

        self.console = Console()

        self.is_log_message = True

        self.microstep = {
            0: 200,
            1: 400,
            3: 2000,
            4: 5000,
            5: 10000,
            6: 12800,
            7: 18000,
            8: 20000,
            9: 21600,
            10: 25000,
            11: 25400,
            12: 25600,
            13: 36000,
            14: 50000,
            15: 50800,
        }

    # region connection & main functions
    @staticmethod
    def list_all_ports():
        ports = list(list_ports.comports())
        simple_ports = []
        port_info = ""
        for p in ports:
            port_info += f"■ {p.device} {p.description} [blue]{p.usb_info()}[/blue]"
            if p != ports[-1]:
                port_info += "\n"
            simple_ports.append(p.description)
        print(Panel(port_info, title="All COMPorts"))
        return simple_ports

    def connect(self, COM=None, baudrate=9600, callback=None):
        if self.only_simulate:
            self.Opened = True
            self.device = f"Simulate-{self.universe}"
            print(f"{self.device} connected")
            if callback:
                callback(self.device, self.Opened)
            return

        def attempt_connect(COM, baudrate):
            try:
                self.ser = serial.Serial(COM, baudrate)
                if self.ser is None:
                    # print("> Device not found")
                    self.Opened = False
                if self.ser.is_open:
                    # print(f"Device: {self.device} | COM: {COM} connected")
                    self.Opened = True
            except:
                print("> Device error")
                self.Opened = False

        if COM is not None and not self.only_simulate:
            attempt_connect(COM, baudrate)
            if callback:
                callback(self.device, self.Opened)
            return
        ports = list(list_ports.comports())
        for p in ports:
            m = re.match(
                r"USB\s*VID:PID=(\w+):(\w+)\s*SER=([A-Za-z0-9]*)", p.usb_info()
            )
            print(m, p.usb_info())
            if (
                m
                and m.group(1) == self.VID
                and m.group(2) == self.PID
                # and m.group(3) == self.SERIAL_NUM
            ):
                print("find vid pid match")
                if m.group(3) == self.SERIAL_NUM or self.SERIAL_NUM == "":
                    print(
                        f"Device: {p.description} | VID: {m.group(1)} | PID: {m.group(2)} | SER: {m.group(3)} connected"
                    )

                    self.device = p.description

                    attempt_connect(p.device, baudrate)
                    if callback:
                        callback(self.device, self.Opened)
                        break
                    break

            if self.only_simulate:
                self.device = "Simulate"
                self.Opened = True
        if not self.Opened:
            print("> Device not found")
            if callback:
                callback(self.device, self.Opened)

    def disconnect(self):
        if self.only_simulate:
            self.listen = False
            self.is_sending = False
            self.Opened = False
            print(f"Simulate-{self.universe} disconnected")
            return
        if self.ser is not None and self.ser.is_open:
            self.listen = False
            self.is_sending = False
            self.Opened = False
            self.ser.flush()
            self.ser.close()
            print(f"{self.device} Disconnected")

    def send(self, command, eol=b"\r"):
        if (self.ser != None and self.ser.is_open) or self.only_simulate:
            self.temp_cmd = command + "\r"

            if "~" in self.temp_cmd:
                # remove ~ in self.temp_cmd
                self.temp_cmd = self.temp_cmd[1:]
            else:
                self.usedSendQueue.put(self.temp_cmd)
            if self.ser is not None or not self.only_simulate:
                self.temp_cmd += "\r"
                self.ser.write(self.temp_cmd.encode("ascii"))
            if self.is_log_message:
                print(
                    f"[bold green]Send to {self.device}:[/bold green] {self.temp_cmd}"
                )
            super().notify_observers(f"{self.universe}-{self.temp_cmd}")
        else:
            print(f"Target device is not opened. Command: {command}")

    def read(self, timeout=1):
        if self.ser is not None and self.ser.is_open:
            print("reading...")
            try:
                start_time = time.time()
                while time.time() - start_time < timeout:
                    if self.ser.in_waiting > 0:
                        response = self.ser.read(self.ser.in_waiting)
                        response = response.decode("utf-8").strip()
                        if self.is_log_message:
                            print(
                                f"[bold blue]Recv from {self.device} :[/bold blue] {response}"
                            )
                        return response
                    time.sleep(0.01)
                print("reading timeout")
                return None
            except Exception as e:
                print(f"Error when reading serial port: {str(e)}")
                return None
        elif self.only_simulate:
            simulated_response = "simulate response"
            if self.is_log_message:
                print(
                    f"[bold blue]Recv from simulate device:[/bold blue] {simulated_response}"
                )
            return simulated_response
        else:
            print("Device not open, read fail.")
            return None

    # endregion

    # region motor motion functions
    def enable(self, motor_address="", enable=True):
        cmd = "ME" if enable else "MD"
        self.send(self.addressed_cmd(motor_address, cmd))

    def move_absolute(self, motor_address="", position=0, speed=0.15):
        self.send(self.addressed_cmd(motor_address, f"VE{speed}"))
        self.send(self.addressed_cmd(motor_address, f"FP{position}"))

    def move_fixed_distance(self, motor_address="", distance=100, speed=0.15):
        self.send(self.addressed_cmd(motor_address, "VE{}".format(speed)))
        self.send(self.addressed_cmd(motor_address, "FL{}".format(int(distance))))

    def start_jog(self, motor_address="", speed=0.15, direction="CW"):
        self.send(self.addressed_cmd(motor_address, "JS{}".format(speed)))
        time.sleep(0.01)
        self.send(self.addressed_cmd(motor_address, "CJ"))
        # self.send(self.addressed_cmd(motor_address, "CS{}".format(speed)))

    def change_jog_speed(self, motor_address="", speed=0.15):
        self.send(self.addressed_cmd(motor_address, "CS{}".format(speed)))

    def stop_jog(self, motor_address=""):
        self.send(self.addressed_cmd(motor_address, "SJ"))

    def stop(self, motor_address=""):
        self.send(self.addressed_cmd(motor_address, "ST"))

    def stop_with_deceleration(self, motor_address=""):
        self.send(self.addressed_cmd(motor_address, "STD"))

    def stop_and_kill(self, motor_address="", with_deceleration=True):
        if with_deceleration:
            self.send(self.addressed_cmd(motor_address, "SKD"))
        else:
            self.send(self.addressed_cmd(motor_address, "SK"))

    def setup_motor(self, motor_address="", kill=False):
        if kill:
            self.stop_and_kill(motor_address)
        self.set_transmit_delay(motor_address, 25)
        self.set_return_format_dexcimal(motor_address)

    def calibrate(self, motor_address="", speed=0.3, onStart=None, onComplete=None):
        self.send(self.addressed_cmd(motor_address, "VE{}".format(speed)))
        # time.sleep(0.01)
        self.send(self.addressed_cmd(motor_address, "DI10"))
        # time.sleep(0.01)
        self.send(self.addressed_cmd(motor_address, "SH3F"))
        # time.sleep(0.01)
        self.send(self.addressed_cmd(motor_address, "EP0"))
        # time.sleep(0.01)
        self.send(self.addressed_cmd(motor_address, "SP0"))

    def alarm_reset(self, motor_address=""):
        self.send(self.addressed_cmd(motor_address, "AR"))

    # speed slow= 0.25, medium=1, fast=5
    def set_transmit_delay(self, motor_address="", delay=15):
        self.send(self.addressed_cmd(motor_address, "TD{}".format(delay)))

    # endregion

    # region motor status functions
    def get_position(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "IP"))
        return self.read()
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()

    def get_temperature(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "IT"))
        # self.new_value_event.wait(timeout=0.5)
        return self.read()
        # return int(self.get_value()) / 10

    def get_sensor_status(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "IS"))
        return self.read()
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()

    def get_votalge(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "IU"))
        return self.read()
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()

    def get_acceleration(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "AC"))
        return self.read()
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()

    def get_deceleration(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "DE"))
        return self.read()
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()

    def get_velocity(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "VE"))
        return self.read()
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()

    def get_distance(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "DI"))
        return self.read()
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()

    def get_jog_speed(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "JS"))
        # self.new_value_event.wait(timeout=0.5)
        # return self.get_value()
        return self.read()

    def get_info(self, motor_address, progress=None):
        self.set_return_format_dexcimal(motor_address)
        self.motor_wait(motor_address, 0.1)
        totalInfoCount = 7
        pos = self.extractValueFromResponse(self.get_position(motor_address))
        if progress:
            progress(round(1 / totalInfoCount, 1))
        temp = (
            int(self.extractValueFromResponse(self.get_temperature(motor_address))) / 10
        )
        if progress:
            progress(round(2 / totalInfoCount, 1))
        vol = int(self.extractValueFromResponse(self.get_votalge(motor_address))) / 10
        if progress:
            progress(round(3 / totalInfoCount, 1))
        accel = self.extractValueFromResponse(self.get_acceleration(motor_address))
        if progress:
            progress(round(4 / totalInfoCount, 1))
        decel = self.extractValueFromResponse(self.get_deceleration(motor_address))
        if progress:
            progress(round(5 / totalInfoCount, 1))
        jogsp = self.extractValueFromResponse(self.get_jog_speed(motor_address))
        if progress:
            progress(round(6 / totalInfoCount, 1))
        info = {
            "pos": pos,
            "temp": temp,
            "vol": vol,
            "accel": accel,
            "decel": decel,
            "jogsp": jogsp,
        }
        if progress:
            progress(round(7 / totalInfoCount))

        return info

    def get_status(self, motor_address) -> str:
        self.set_return_format_dexcimal(motor_address)
        self.send(self.addressed_cmd(motor_address, "RS"))
        self.new_value_event.wait(timeout=0.5)
        return str(self.get_value())

    def set_return_format_dexcimal(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "IFD"))

    def set_return_format_hexdecimal(self, motor_address):
        self.send(self.addressed_cmd(motor_address, "IFH"))

    # endregion

    # region utility functions
    def motor_wait(self, motor_address, wait_time):
        self.send(self.addressed_cmd(motor_address, "WT{}".format(wait_time)))

    def addressed_cmd(self, motor_address, command):
        if motor_address == "":
            return f"~{command}"
        return f"{motor_address}{command}"

    def extractValueFromResponse(self, response):
        pattern = r"=(.*)"
        if response == None:
            return None
        result = re.search(pattern, response)
        if result:
            return result.group(1)
        else:
            return None

    def get_value(self):
        print("Waiting for value")
        self.new_data_event.wait(timeout=0.5)
        print("Recv:" + self.listeningBufferPre)
        self.new_data_event.clear()
        return self.listeningBufferPre
        # if "%" in self.listeningBufferPre:
        #     return "success_ack"
        # if "?" in self.listeningBufferPre:
        #     return "fail_ack"
        # if "*" in self.listeningBufferPre:
        #     return "buffered_ack"
        # self.new_value_event.set()
        # pattern = r"=(\w+(?:\.\w+)?|\d+(?:\.\d+)?)"
        # result = re.search(pattern, self.listeningBufferPre)
        # self.listeningBufferPre = ""
        # self.new_value_event.clear()
        # if result:
        #     return result.group(1)
        # else:
        #     return "No_value_found"


# endregion

# SERIAL => 上次已知父系(尾巴+A) 或是事件分頁
# reg USB\s*VID:PID=(\w+):(\w+)\s*SER=([A-Za-z0-9]+)

# serial_num  裝置例項路徑
# TD(Tramsmit Delay) = 15
