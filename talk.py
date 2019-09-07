import pya3rt
def creat_reply(name):
	apikey = "DZZ3wYssLsf2MnETFnuxfAjQFgQ1AkAh"
	client = pya3rt.TalkClient(apikey)
	res = client.talk("おはよう！")

	print(res['results'][0]['reply'])

creat_reply(input())
