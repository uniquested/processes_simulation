class Process:
    def __init__(self, burstTime, arrivalTime, priority, waitTime=0, finished=0):
        self.burstTime = burstTime
        self.arrivalTime = arrivalTime
        self.priority = priority
        self.waitTime = waitTime
        self.finished = finished

    def get_parameters(self):
        parameters = []
        parameters.insert(1, self.burstTime)
        parameters.insert(2, self.arrivalTime)
        parameters.insert(3, self.waitTime)
        parameters.insert(4, self.finished)
        parameters.insert(5, self.priority)
        return parameters
