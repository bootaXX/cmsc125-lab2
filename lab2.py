import os


class Process(object):
    """docstring for Process"""
    def __init__(self, name, arrival, burst, priority):
        super(Process, self).__init__()
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.waiting = 0

    def __str__(self):
        str1 = str(self.name) + "," + str(self.arrival)
        str2 = str(self.burst) + "," + str(self.priority)
        return ','.join([str1, str2, str(self.waiting)])


class Schedule(object):
    """docstring for Schedule"""
    def __init__(self, processes):
        super(Schedule, self).__init__()
        self.processes = processes
        self.aveCT = 0

    def averageCT(self):
        sum = 0
        for process in self.processes:
            sum += process.waiting
        self.aveCT = sum / len(self.processes)

    def genWaiting(self):
        prev = self.processes[0]
        for x in range(1, len(self.processes)):
            self.processes[x].waiting = prev.waiting + prev.burst
            prev = self.processes[x]

    def resetSched(self):
        reset = sorted(self.processes, key=lambda process: process.name)
        for process in reset:
            process.waiting = 0
        self.processes = reset

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

    def sortSched(self):
        sortedsched = sorted(self.processes, key=lambda process: process.burst)
        self.processes = sortedsched


class SRPT(Schedule):
    """docstring for FCFS"""
    def __init__(self, processes):
        Schedule.__init__(self, processes)


class Priority(Schedule):
    """docstring for FCFS"""
    def __init__(self, processes):
        Schedule.__init__(self, processes)

    def sortSched(self):
        ssched = sorted(self.processes, key=lambda process: process.priority)
        self.processes = ssched


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

    def getProcesses(self):
        return self.processes

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
                name = int(split[0])
                arrival = int(split[1])
                burst = int(split[2])
                priority = int(split[3])
                proc = Process(name, arrival, burst, priority)
                self.processes.append(proc)


def main():
    file = FileRead("/process1.txt")
    file.extractData()
    file.datatoProcess()
    processes = file.getProcesses()

    # FCFS------------------------------------------------------------------------------------------
    fcfs = FCFS(processes)
    fcfs.genWaiting()
    for process in fcfs.processes:
        print(process)
    fcfs.averageCT()
    print("Average Waiting Time: " + str(fcfs.aveCT))

    # SJF-------------------------------------------------------------------------------------------
    sjf = SJF(processes)
    sjf.resetSched()
    sjf.sortSched()
    sjf.genWaiting()
    for process in sjf.processes:
        print(process)
    sjf.averageCT()
    print("Average Waiting Time: " + str(sjf.aveCT))

    # SRPT-------------------------------------------------------------------------------------------
    srpt = SRPT(processes)

    # PRIORITY---------------------------------------------------------------------------------------
    priority = Priority(processes)
    priority.resetSched()
    priority.sortSched()
    priority.genWaiting()
    for process in priority.processes:
        print(process)
    priority.averageCT()
    print("Average Waiting Time: " + str(priority.aveCT))

    # ROUNDROBIN-------------------------------------------------------------------------------------
    roundrobin = RoundRobin(processes)


if __name__ == '__main__':
    main()
