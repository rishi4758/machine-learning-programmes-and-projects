import json
a='''
{
"status":"ok",
"source":"hello",
"value":"uid"

}
'''
b=json.loads(a)
print(b)
