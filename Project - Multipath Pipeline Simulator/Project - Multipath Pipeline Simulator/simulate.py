'''
Created on Apr 5, 2014

@author: axxe
'''
from MultistagePipeline import MultistagePipeline
import sys

if __name__ == '__main__':
    try:
        # arch = MultistagePipeline("./config.txt", "./inst.txt", "./reg.txt", "./instructionSet.txt", "./data.txt")
        arch = MultistagePipeline(sys.argv[4], sys.argv[1], sys.argv[3], "./instructionSet.txt", sys.argv[2])
        arch.simulateInstructions()
    #     print "Execution Completed in Cycle: " + str(arch.executionCompleteCycle)
    #     print "Cache Hits: " + str(arch.instructionCacheHit) + " + " + str(arch.dataCacheHit)
    #     print "Cache Miss: " + str(arch.instructionCacheMiss) + " + " + str(arch.dataCacheMiss)
        # arch.printOutputTable()
        arch.writeOutputFile(sys.argv[5])
    except Exception as exc:
        pass
