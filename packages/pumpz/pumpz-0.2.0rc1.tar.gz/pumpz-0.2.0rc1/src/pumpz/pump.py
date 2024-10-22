import math
import sympy
from .utilities import decompose_dict, factor_check

class pump:
    '''
    For pump objects, one for each pump to be controlled
    '''
    def __init__(
        self,
        file,
        dia: float,
        rate_units: str = 'mm',
        vol_units: str = '',
        time: float = 0,
    ):
        '''
        Contains the following attributes of pump() object:
        file: file object
        dia: diameter of syringe
        rate_units: str() of unit for rate. 'mm' for mL/min; 'um' for mcL/min; 'mh' for mL/hr; 'uh' for mcL/h
        vol_units: str() of unit for volume. 'mcL' or 'mL'. 
        time: initial time in seconds
        '''
        self.file = file

        self.dia = dia
        if self.dia < 0.1 or self.dia > 50.0:
            raise Exception('Diameter is invalid. Must be between 0.1 - 50.0 mm')
        
        self.time = time

        self.rate_units = rate_units
        
        # self.loop is used to store current loop, used for self.time and loopstart/loopend
        self.loop = []

        # set self.vol_units depending on user input / lack thereof
        if vol_units == '':
            if self.dia > 14.0: 
                self.vol_units = 'mcL'
            else:
                self.vol_units = 'mL'
        else:
            self.vol_units = vol_units

        # Set to 'inf' or 'wdr' for rate()
        self.__dir = ''

        # Used in rate()
        self.__rat = 0

        # Used in phase labelling
        self.phase_name = ''

        # Used to track phases
        self.phase_num = 1

        # dict of keys phase_name and values phase_number
        self.phase_ref = {}

        # True if sync is useable, some functions take an unknown time to elapse and are therefore incompatible with sync
        self.sync_is_useable = True

        # unused
        # self.sub_program= {}


    def init(*args):
        '''
        Sets PPL to default values. 

        Inputs:
        ===========================
        *args: any number of pump objects
        '''
        for self in args:
            self.file.write(f"dia {self.dia}\nal 1\nbp 1\nPF 0\n")
    
    def __phase_to_string(self, phase) -> str:
        '''
        Inputs:
        ============================
        self: pump object
        phase: phase number OR phase name ( as set by self.label(label: str) )

        Output:
        ============================
        str of phase number in form 'nn' where n is a digit from 0 to 9
        '''
        if type(phase) == type(1):
            if phase > 0 and phase < 99:
                return str(phase).zfill(2)
            else:
                raise Exception(f'phase argument is invalid')
        elif type(phase) == type('string'):
            return str(self.phase_ref(self.phase_name)).zfill(2)
    
    def __phase(self):
        '''
        Writes a phase with current self.phase_name, then empties self.phase_name
        '''
        self.file.write(f'\nphase {self.phase_name}\n')
        self.phase_ref[self.phase_name] = self.phase_num
        self.phase_name = ''
        self.phase_num += 1

    def label(self, label: str) -> str:
        '''
        Label the following phase with input label: str, and returns that same str. 
        '''
        self.phase_name = label
        return label

    def change_rate_units(self, rate_units: str):
        '''
        Inputs:
        ==========================
        rate_units: str() of unit for rate. 'mm' for mL/min; 'um' for mcL/min; 'mh' for mL/hr; 'uh' for mcL/h
        '''
        self.rate_units = rate_units

    def rate(self, rate: float, vol: float, dir: str):
        '''
        Write PPl function 'rat' (rate)

        Input:
        =============================
        self: pump object
        rate: float or int: rate to infuse/withdraw at current rate units
        vol: float or int: volume to infuse/withdraw at pump volume units
        dir: str: either 'inf' for infuse, or 'wdr' for withdraw

        Updates self.time
        '''
        self.__phase()
        self.__dir = dir
        self.__rat = rate

        self.file.write(f"fun rat\nrat {rate} {self.rate_units}\nvol {vol}\ndir {dir}\n")

        if self.vol_units == 'mcL':
            v = vol / 1000
        else:
            v = vol

        if self.rate_units == 'mm': 
            self.time += v / rate * 60 * self.getloop()
        elif self.rate_units == 'um': 
            self.time += v*1000 / rate * 60 * self.getloop() 
        elif self.rate_units == 'mh': 
            self.time += v / rate * 3600 * self.getloop()
        elif self.rate_units == 'uh': 
            self.time += v*1000 / rate * 3600 * self.getloop()
    
    # fil, incr, decr, not included yet

    def beep(self):
        '''
        Writes fun bep to PPL
        '''
        self.__phase()
        self.file.write(f'fun bep\n')

    def pause(self, length: int, phases = 0):
        '''
        Automatically writes fun pas with as few phases as possible. Accepts any positive integer for length input (in seconds).
        '''
        if length <= 99:
            self.__phase()
            self.file.write(f"fun pas {length}\n")
            self.time += length * self.getloop()
            phases += 1
        elif length <= 99 * 3:
            phases += self.pause(99)
            phases += self.pause(length - 99)
        else:
            multiples = factor_check(decompose_dict(sympy.factorint(length)))
            if multiples != (0, 0) and len(multiples) <= 3:
                for i in range(len(multiples) - 1):
                    self.loopstart(multiples[1 + i])
                    phases += 1
                self.pause(multiples[0])
                for i in range(len(multiples) - 1):
                    self.loopend()
                    phases += 1
            else:
                phases += self.pause(length % 50)
                length -= length % 50
                phases += self.pause(length)
        return phases

    def subprogram_label(self, label: int):
        '''
        Writes fun prl to PPL as subprogram start label definition
        Input label: int must be 0 to 99
        '''
        self.__phase()
        self.file.write(f'fun prl {str(label).zfill(2)}\n')

    def subprogram_select(self):
        '''
        Writes fun pri to PPL, subprogram selection input
        '''
        self.__phase()
        self.file.write(f'fun pri')

    def loopstart(self, count: int):
        '''
        Equivalent to PPL 'fun lps', the count is here instead of at the end (like in PPL)
        '''
        self.loop.append(count)
        if len(self.loop) > 3:
            raise Exception("Up to three nested loops, you have too many")
        self.__phase()
        self.file.write(f"fun lps\n")

    def loopend(self):
        '''
        Equivalent to PPL 'fun lop <nn>', count is established at start self.loopstart(count)
        '''
        self.file.write(f"\nphase\nfun lop {self.loop.pop()}\n")

    def getloop(self):
        '''
        Returns how many times a given phase would output due to loops
        '''
        return sympy.prod(self.loop)
    
    def jump(self, phase: str):
        '''
        Writes to PPL 'fun jmp'
        Not compatible with pumpz.sync() or self.time
        Inputs:
        ============================
        self: pump object
        phase: phase number OR phase name ( as set by self.label(label: str) )
        '''
        self.__phase()
        self.sync_is_useable = False
        self.file.write(f'fun jmp {self.__phase_to_string(phase)}')
    
    def if_low(self, phase):
        '''
        Equivalent to PPL 'fun if <nn>'
        Inputs:
        ============================
        self: pump object
        phase: phase number OR phase name ( as set by self.label(label: str) )
        '''
        self.sync_is_useable = False
        self.__phase()
        self.file.write(f'fun if {self.__phase_to_string(phase)}')
    
    def event_trap(self, phase):
        '''
        Equivalent to PPL 'fun evn <nn>'
        Inputs:
        ============================
        self: pump object
        phase: phase number OR phase name ( as set by self.label(label: str) )
        '''
        self.sync_is_useable = False
        self.__phase()
        self.file.write(f'fun evn {self.__phase_to_string(phase)}')
    
    def event_trap_sq(self,phase):
        '''
        Equivalent to PPL 'fun evs <nn>'
        Inputs:
        ============================
        self: pump object
        phase: phase number OR phase name ( as set by self.label(label: str) )
        '''
        self.sync_is_useable = False
        self.__phase()
        self.file.write(f'fun evs {self.__phase_to_string(phase)}')
    
    def event_reset(self):
        '''
        Equivalent to PPL 'fun evr'
        '''
        self.__phase()
        self.file.write(f'fun evr')

    # cld: clear total dispense volume, not implemented

    def trg(self, num: int):
        self.__phase()
        self.file.write(f'fun trg {num}')

    def out(self, n):
        self.__phase()
        self.file.write(f'fun out {int(n)}')

    def stop(*args):
        for self in args:
            self.__phase()
            self.file.write(f"fun stp\n")

    def sync(*args):
        max_time = 0
        for arg in args:
            if arg.time > max_time:
                max_time = arg.time
            if arg.sync_is_useable == False:
                raise Exception(f'sync isn\'t useable with {arg}')
        for arg in args:
            time_diff = max_time - arg.time
            if time_diff > 0:
                arg.pause(math.ceil(time_diff))

