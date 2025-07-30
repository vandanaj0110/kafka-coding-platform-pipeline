
from kafka import KafkaConsumer
import sys
import json
topic1=sys.argv[1]
topic2=sys.argv[2]
topic3=sys.argv[3]
d={}
a=0
u=''
consumer=KafkaConsumer(topic3, value_deserializer = lambda m: json.loads(m.decode('ascii')))
for message in consumer:
	K=32
	if "stop" in message.value:
		break
	elif message.value[0]=="solution":
		if int(message.value[4])>a:
			a=int(message.value[4])
			u=message.value[1]
	else:
		if message.value[0]=="competition":
			w=int(message.value[9])
			if message.value[7]=="Passed":
				y = 1  
			elif message.value[7]=="TLE":
				y = 0.2
			elif message.value[7]=="Failed":
				y = -0.3
			if message.value[5]=="Hard":
				f = 1
			elif message.value[5]=="Medium":
				f = 0.7
			elif message.value[5]=="Easy":
				f = 0.3
		elif message.value[0]=="problem":
			w=int(message.value[8])
			if message.value[6]=="Passed":
				y = 1  
			elif message.value[6]=="TLE":
				y = 0.2
			elif message.value[6]=="Failed":
				y = -0.3
			if message.value[4]=="Hard":
				f = 1
			elif message.value[4]=="Medium":
				f = 0.7
			elif message.value[4]=="Easy":
				f = 0.3
		q = 10000/w
		r = 1200
		t = K * (y * f) + q
		if message.value[0]=="competition":
			if(message.value[2] in d):
				r=d[message.value[2]]
			l = r + t
			d[message.value[2]]= l
		elif message.value[0]=="problem":
			if(message.value[1] in d):
				r=d[message.value[1]]
			l = r + t
			d[message.value[1]]= l
for i,j in d.items():
	d[i]=int(j)
myKeys = list(d.keys())
myKeys.sort()
sd = {i: d[i] for i in myKeys}
l={"best_contributor": [u], "user_elo_rating": sd}
print(json.dumps(l, indent=4))
consumer.close()
