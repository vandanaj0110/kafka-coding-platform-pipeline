
from kafka import KafkaConsumer
import sys
import json
topic1=sys.argv[1]
topic2=sys.argv[2]
topic3=sys.argv[3]
d={}
consumer=KafkaConsumer(topic2, value_deserializer = lambda m: json.loads(m.decode('ascii')))
for message in consumer:
	if "stop" in message.value:
		break
	else:
				if message.value[7]=="Passed":
					g = 100  
				elif message.value[7]=="TLE":
					g = 20
				elif message.value[7]=="Failed":
					g = 0
				if message.value[5]=="Hard":
					h = 3
				elif message.value[5]=="Medium":
					h = 2
				elif message.value[5]=="Easy":
					h = 1
				if int(message.value[9])>0:
					q = 10000/float(message.value[9])
				w = 0.25*float(message.value[10])
				e = max(1,(1 + q - w))
				r = g * h * e
				if message.value[1] in d:
					if message.value[2] not in d[message.value[1]]:
						d[message.value[1]][message.value[2]]=0
					d[message.value[1]][message.value[2]]+=int(r)
				else:
					d[message.value[1]]={}
					d[message.value[1]][message.value[2]]=int(r)
myKeys = list(d.keys())
myKeys.sort()
sd={}
p={}
for i in myKeys:
	p={}
	a=list(d[i].keys())
	a.sort()
	for j in a:
		p[j]=d[i][j]
	sd[i]=p
print(json.dumps(sd, indent=4))
consumer.close()
