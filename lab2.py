import os


class Process(object):
    """docstring for Process"""
    def __init__(self, name, arrival, burst, priority):
        super(Process, self).__init__()
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.priority = priority

    def __str__(self):
        return ','.join([self.name, self.arrival, self.burst, self.priority])


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
        self.lines = []
        self.processes = []

    def extractData(self):
        string = open("processes/process1.txt", "r")
        for line in string:
            self.lines.append(line)

    def datatoProcess(self):
        flag = True
        for line in self.lines:
            if flag:
                flag = False
            else:
                split = line.split()
                proc = Process(split[0], split[1], split[2], split[3])
                self.processes.append(proc)


def main():
    print("Greed")
    schedule = Schedule("schedule")
    fcfs = FCFS("fcfs")
    sjf = SJF("sjf")
    srpt = SRPT("srpt")
    priority = Priority("priority")
    roundrobin = RoundRobin("roundrobin")
    file = FileRead("/process1.txt")
    file.extractData()
    file.datatoProcess()

    print(schedule)
    print(fcfs)
    print(sjf)
    print(priority)
    print(roundrobin)
    print(file.processes[1])

if __name__ == '__main__':
    main()
