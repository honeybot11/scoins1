import samino
from threading import Thread
client = samino.Client("32D3085F471DF87A00FB4CE43052685FE93239644F24F4E6E9B3D4EEBF0C4C764F0B76788481A7F955")

pswd = input("Password: ")
for email in open("emails.txt").read().split():
    client.login(email,pswd)
    coins = client.get_wallet_info().totalCoins
    print(f"Coins Before the ad: {coins}")
    for _ in range(25):
        Thread(target=client.watch_ad).start()
        print(f"Claim {_}")
    coins = client.get_wallet_info().totalCoins
    print(f"Coins After ad {coins}")