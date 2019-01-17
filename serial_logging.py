import serial
import threading


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
        regularly for the stopped() condition.
    """

    def __init__(self, target, args=()):
        super(StoppableThread, self).__init__(target=target, args=args)
        self._stop_event = threading.Event()
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())
    
    def run(self):
        #with self.pause_cond:  # don't use with here to avoid RuntimeError raised by Lock.release() if lock is already unlocked during exit
        while self.paused:
            self.pause_cond.wait()
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
    
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
        
        def pause(self):
        self.paused = True
        # If in sleep, we acquire immediately, otherwise we wait for thread
        # to release condition. In race, worker will still see self.paused
        # and begin waiting until it's set back to False
        self.pause_cond.acquire(blocking=False)
        
    #should just resume the thread
    def resume(self):
        self.paused = False
        # Notify so thread will wake after lock released
        self.pause_cond.notify()
        # Now release the lock
        self.pause_cond.release()


def read_from_port(serial_handle):
    while not worker.stopped():
        reading = serial_handle.readline().decode('utf-8', 'ignore')
        try:
            with io.open(output, 'a', encoding="utf-8") as fp:
                fp.write(reading)
        except FileNotFoundError:
            print(f'cannot write UART log to {output}')        


serial_handle =  serial.Serial(serial_port, 115200 , timeout=0)
global worker = StoppableThread(target=read_from_port, args=(serial_handle,))
worker.daemon = True
worker.start()

# pause, send command, and then resume
worker.pause()
serial_handle.write(bytes(f'{cmd} \r', 'utf-8'))
worker.resume()

wroker.stop()
worker.join()
