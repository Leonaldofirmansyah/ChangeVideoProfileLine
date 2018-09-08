from linepy import *
from akad.ttypes import *

print('[DEBUG] Memulai Bot')
#client = LineClient()
client = LineClient(authToken='Evz3wB8Xb8JaXCi4moO8.BiZaU0CscPFZuROUN7iSEa.J8WsjVZK5hwh6/gPW6drpYkdnrmJW79fCke9UOOeLv4=')
client.log("Auth Token : " + str(client.authToken))
channel = LineChannel(client)
#objek = LineObject(client) #this is for trial :3
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

print('[DEBUG] Bot Started ^_^')

print("****************Welcome*************")
print('Bot Name: Sb Simple')
print('Version: 1.2')
print('Codename: Adamantite Black')

while True:
	try:
		ops = poll.singleTrace(count=50)
		print("=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=\n")
		print(ops)
		print("=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		if ops != None:
			for op in ops:
				if op.type == 26 or op.type == 25:
					msg = op.message
					text = str(msg.text)
					msg_id = msg.id
					if msg.toType == 0: #bkn room
						receiver = msg._from
						sender = msg.to
					else:
						receiver = msg.to #room
						sender = msg._from
					try:
						if msg.contentType == 0:
							if msg.toType == 2 or 1 or 0:
								client.sendChatChecked(receiver, msg_id)
								contact = client.getContact(sender)
								if text.lower() == '/update':
									client.sendMessage(receiver, "Uploading, Mohon Tunggu Sejenak Hingga Pesan Finish Upload Muncul :3")
									client.updateProfileVideoPicture('image2.png','demo.mp4',fap=0) 
									#cara masukinnya client.updateProfileVideoPicture('gambar.jpg','video_profil.mp4',fap=0) 
									#fap = 0 artinya anda sudah punya screenshot untuk videonya yg bakal di upload ke line
									#fap = 1 artinya anda blm punya screenshot untuk diupload dan bakal digenerate langsung oleh bot :3
									client.sendMessage(receiver,"Finished Upload Ty :3")
									client.sendMessage(receiver, "Terimakasuh telah menggunakan bot ini")
					except Exception as d:
						print('[ERROR] You Got Error On Chat Bot Command Section :p')
						print(str(d))
				poll.setRevision(op.revision)
	except Exception as e:
		print('[ERROR] Well You Got Error On Your Bot -,-')
		print(str(e))
