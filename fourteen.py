seqCount = 0
startNum = 0
for n in range(1, 1000000):
	count = 1
	seq = n
	while seq!= 1 and seq > 0:
		if seq % 2 == 0:
			seq = seq/2
		else:
			seq = 3 * seq + 1
		count = count+ 1
	if (count > seqCount):
		seqCount = count 
		startNum = n

print(start)
print(sequenceCount)

	





