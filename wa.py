import requests as r
import json

class wa:
     def __init__(self, json):
         self.nomor = json['response']['from']
         self.pesan = json['response']['body']
         self.apikey = ''

     def kirim_requests(self, method,data):
         url = f"https://rzawapi.my.id/api/{method}"
         headers = {
             "apikey": f"{self.apikey}",
             "Content-Type": "application/json"
         }
         kirim = r.post(url, data=json.dumps(data), headers=headers)
         return kirim.json()

     def sendMessage(self):
         data = {
         "to": self.nomor,
         "body": "pong"
         }
         kirim = self.kirim_requests('send-message',data)
         return kirim

     def sendImage(self):
         data = {
         "to": self.nomor,
         "body": "https://loremflickr.com/320/240",
         "caption":"image caption"#Kosongkan Jika Tidak Ingin Pakai Caotion
         }
         kirim = self.kirim_requests('send-image',data)
         return kirim

     def sendLocation(self):
         data = {
         "to": self.nomor,
         "body":"Rumah Saya",
         "longitude":"106.631889",
         "latitude":"-6.178306"
         }
         kirim = self.kirim_requests('send-location',data)
         return kirim

     def NoCommand(self):
         data = {
         "to": self.nomor,
         "body": "Maaf Command Tidak Ditemukan"
         }
         kirim = self.kirim_requests('send-message',data)
         return kirim

     def processing(self):
         if self.pesan == 'ping':
             return self.sendMessage()
         elif self.pesan == 'image':
             return self.sendImage()
         elif self.pesan == 'location':
             return self.sendLocation()
         else:
             return self.NoCommand()
