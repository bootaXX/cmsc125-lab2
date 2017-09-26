
class Process(object):
    """docstring for Process"""
    def __init__(self, arrival, burst, priority):
        super(Process, self).__init__()
        self.arrival = arrival
        self.burst = burst
        self.priority = priority

    def getArrival(self):
        print(self.arrival)

    def getBurst(self):
        print(self.burst)

    def getPriority(self):
        print(self.priority)


class Schedule(object):
    """docstring for Schedule"""
    def __init__(self, processes):
        super(Schedule, self).__init__()
        self.processes = processes

    def __str__(self):
        return self.processes


class FCFS(Schedule):
    """docstring for FCFS"""
    def __init__(self, processes):
        Schedule.__init__(self, processes)


class SJF(Schedule):
    """docstring for FCFS"""
    def __init__(self, processes):
        Schedule.__init__(self, processes)


class SRPT(Schedule):
    """docstring for FCFS"""
    def __init__(self, processes):
        Schedule.__init__(self, processes)


class Priority(Schedule):
    """docstring for FCFS"""
    def __init__(self, processes):
        Schedule.__init__(self, processes)


class RoundRobin(Schedule):
    """docstring for FCFS"""
    def __init__(self, processes):
        Schedule.__init__(self, processes)


class FileRead(object):
    """docstring for FileRead"""
    def __init__(self, file):
        super(FileRead, self).__init__()
        self.file = file


def main():
    print("Greed")
    schedule = Schedule("schedule")
    fcfs = FCFS("fcfs")
    sjf = SJF("sjf")
    srpt = SRPT("srpt")
    priority = Priority("priority")
    roundrobin = RoundRobin("roundrobin")

    print(schedule)
    print(fcfs)
    print(sjf)
    print(priority)
    print(roundrobin)

if __name__ == '__main__':
    main()
