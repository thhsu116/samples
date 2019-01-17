import pythoncom
import win32com.client
from threading import Thread

def marshall_win32_handle(self, handle):
    return pythoncom.CoMarshalInterThreadInterfaceInStream(pythoncom.IID_IDispatch, handle)

def Worker(Thread):
    def run(self):
        self._args = list(self._args)
        pythoncom.CoInitialize()
        self._args[0] = win32com.client.Dispatch(
            pythoncom.CoGetInterfaceAndReleaseStream(self._args[0], pythoncom.IID_IDispatch)
        )
        self._target(*self._args, **self._kwargs)
        pythoncom.CoUninitialize ()

# marshalled win32 apps handle as input to target_function
worker = Worker(target=target_function, args=(marshall_win32_handle(handle),))
worker.start()
worker.join()
