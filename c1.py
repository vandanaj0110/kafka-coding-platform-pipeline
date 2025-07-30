
from kafka import KafkaConsumer
import sys
import json
def get_key(my_dict, value):
	l=[]
	for key, val in my_dict.items():
		if val == value:
			l.append(key)
	return l
topic1=sys.argv[1]
topic2=sys.argv[2]
topic3=sys.argv[3]
lang={}
diff={}
consumer=KafkaConsumer(topic1, value_deserializer = lambda m: json.loads(m.decode('ascii')))
for message in consumer:
	if "stop" in message.value:
		break
	elif message.value[0]=='problem':
		if message.value[7] in lang:
			lang[message.value[7]]+=1
		else:
			lang[message.value[7]]=1
		if message.value[3] in diff:
			diff[message.value[3]][0]+=1
			if message.value[6]=="Passed":
				diff[message.value[3]][1]+=1
		else:
			diff[message.value[3]]=[]
			diff[message.value[3]].append(1)
			diff[message.value[3]].append(0)
			if message.value[6]=="Passed":
				diff[message.value[3]][1]+=1
for key, val in diff.items():
	diff[key]=(val[1]/val[0])
key = get_key(lang, max(lang.values()))
d= get_key(diff, min(diff.values()))
d.sort()
l={"most_used_language": key, "most_difficult_category": d}
print(json.dumps(l, indent=4))
consumer.close()
