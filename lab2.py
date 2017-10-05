import os
from operator import attrgetter
import time


class Process(object):
    """docstring for Process"""
    def __init__(self, name, arrival, burst, priority):
        super(Process, self).__init__()
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.waiting = 0
        self.ctr = 0

    def __str__(self):
        str1 = str(self.name) + "," + str(self.arrival)
        str2 = str(self.burst) + "," + str(self.priority)
        return ','.join([str1, str2, str(self.waiting)])

    def __add__(self, other):
        return str(self) + other


class Schedule(object):
    """docstring for Schedule"""
    def __init__(self, processes):
        super(Schedule, self).__init__()
        self.processes = processes
        self.aveCT = 0

    def averageWT(self):
        sum = 0
        for process in self.processes:
            sum += process.waiting
        self.aveWT = sum / float(len(self.processes))

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

    def printGantt(self):
        for process in self.processes:
            print "|"*process.burst,

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

    def genWaiting(self):
        stored = [self.processes[0]]
        currtime = 0
        least = min(stored, key=attrgetter('burst'))
        while(stored):
            least.burst -= 1
            if not least.burst:
                stored.remove(least)

            currtime += 1

            for process in self.processes:
                if process.arrival == currtime:
                    stored.append(process)

            if stored:
                least = min(stored, key=attrgetter('burst'))

            for store in stored:
                if store.name != least.name:
                    store.waiting += 1


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

    def genWaiting(self):
        ctr = 0
        clist = 0
        blist = []
        deduct = 0
        for process in self.processes:
            blist.append(process)

        while blist:
            for bist in blist:
                print "p"+str(bist.name), ctr, bist.burst
                if bist.burst < 5 and bist.burst != 0:
                    bist.waiting = ctr - (clist*4)
                    ctr += bist.burst
                    blist.remove(bist)
                else:
                    ctr += 4
                    bist.burst -= 4
            clist += 1


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
        string = open("processes" + self.file, "r")
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
    file = FileRead("/process3.txt")
    file.extractData()
    file.datatoProcess()
    processes = file.getProcesses()

    # FCFS------------------------------------------------------------------------------------------
    print "FCFS"
    fcfs = FCFS(processes)
    fcfs.genWaiting()
    for process in fcfs.processes:
        print(process)
    fcfs.averageWT()
    print("Average Waiting Time: " + str(fcfs.aveWT))

    # SJF-------------------------------------------------------------------------------------------
    print "SJF"
    sjf = SJF(processes)
    sjf.resetSched()
    sjf.sortSched()
    sjf.genWaiting()
    for process in sjf.processes:
        print(process)
    sjf.averageWT()
    print("Average Waiting Time: " + str(sjf.aveWT))

    # PRIORITY---------------------------------------------------------------------------------------
    print "PRIORITY"
    priority = Priority(processes)
    priority.resetSched()
    priority.sortSched()
    priority.genWaiting()
    for process in priority.processes:
        print(process)
    priority.averageWT()
    print("Average Waiting Time: " + str(priority.aveWT))

    # ROUNDROBIN-------------------------------------------------------------------------------------
    print "ROUNDROBIN"
    roundrobin = RoundRobin(processes)
    roundrobin.resetSched()
    roundrobin.genWaiting()
    for process in roundrobin.processes:
        print(process)
    roundrobin.averageWT()
    print("Average Waiting Time: " + str(roundrobin.aveWT))

    # SRPT-------------------------------------------------------------------------------------------
    print "SRPT"
    srpt = SRPT(processes)
    # srpt.resetSched()
    # srpt.genWaiting()
    # for process in srpt.processes:
    #     print(process)
    # srpt.averageWT()
    # print("Average Waiting Time: " + str(srpt.aveWT))


if __name__ == '__main__':
    main()
