#https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf
#lesson1:ドローンネットワーク確認
import subprocess

data = subprocess.check_output([
                                'netsh',
                                'wlan',
                                'show',
                                'network']).decode('cp932').split('\n')
#subprocess.runやsubprocess.callなどでもコマンドプロンプトの実行を
# pythonから指定できる

#print(data)
#print(type(data))
name = "TELLO"
address=[]
for item in data:
    words = item.split('\r')[:-1]
    for i in words:
        #print(i,",")
        if name in i:
            i=i.split(" ")
            #print(i[3])
            address.append(i[3])
#print(address)
for j in range(len(address)):
    print(j+1,"：",address[j])
num = int(input("接続するドローンの番号して下さい："))
#print(address[num-1])
try:
    data = subprocess.check_output([
                                    'netsh',
                                    'wlan',
                                    'connect',
                                    address[num-1]]).decode('cp932').split('\n')
    print(data)
except Exception as e:
    print("初回接続のみ手動 or xmlのダウンロードをお願いします。")

#チャレンジ：class化して、ドローン制御の際に毎回最初のwifi接続を楽に実施してみよう。