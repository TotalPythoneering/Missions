# MISSION: Pythoneering 'Truthy' and 'Falsy'.
# STATUS: Research
# VERSION: 1.0.0
# NOTES: https://github.com/TotalPythoneering and https://www.youtube.com/@TotalPythoneering
# DATE: 2026-05-30 06:45:37
# FILE: tstr.py
# AUTHOR: Randall Nagy
#
class BlankStr:
    def __init__(self, a_str=None):
        if not a_str:
            self.a_str = None
        else:
            self.a_str = str(a_str)

    def __eq__(self, obj):
        ''' Caveat operator == '''
        print("__eq__!")
        try:
            return self.a_str == obj.a_str
        except:
            return False

    def __bool__(self):
        ''' Comment out to use __len__() '''
        if not self.a_str: return False
        if self.a_str.isnumeric():
            return bool(int(self.a_str))
        return not self.a_str.isspace()

    def __len__(self):
        ''' bool() uses, too! '''
        if not self.a_str: return 0
        if self.a_str.isspace(): return 0
        return len(self.a_str)

