import requests
import keys
import tokens

ethkey=keys.ethapi
bnbkey=keys.bnbapi
polkey=keys.polygonapi
def ethtokbal(adr,key,f):
    f.write('ETH_network:\n')

    url1=f'https://api.etherscan.io/api?module=account&action=balance&address={adr}&tag=latest&apikey={key}'
    ethbal=int(requests.get(url1).json()['result'])

    if ethbal>0 :
        f.write(f'ETH: {str(ethbal/10**18)[:8]}\n')
    for i in tokens.eth:
        url=f'https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={tokens.eth[i][1]}&address={adr}&tag=latest&apikey={key}'
        bal=requests.get(url).json()['result']
        if int(bal)>0:
            f.write(f'{i}: {str(int(bal)/10**tokens.eth[i][0])}\n')

def bnbtokbal(adr,key,f):
    f.write('\nBNB_chain:\n')

    url1 = f'https://api.bscscan.com/api?module=account&action=balance&address={adr}&tag=latest&apikey={key}'
    bnbbal = int(requests.get(url1).json()['result'])

    if bnbbal > 0:
        f.write(f'BNB: {str(bnbbal / 10 ** 18)}\n')
    for i in tokens.bnb:
        url = f'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={tokens.bnb[i][1]}&address={adr}&tag=latest&apikey={key}'
        bal = requests.get(url).json()['result']
        if int(bal) > 0:
            f.write(f'{i}: {str(int(bal) / 10 ** tokens.bnb[i][0])}\n')

def polygonbal(adr,key,f):
    f.write('\nPolygon_chain:\n')

    url1 = f'https://api.polygonscan.com/api?module=account&action=balance&address={adr}&tag=latest&apikey={key}'
    bnbbal = int(requests.get(url1).json()['result'])

    if bnbbal > 0:
        f.write(f'Matic: {str(bnbbal / 10 ** 18)}\n')
    for i in tokens.bnb:
        url = f'https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress={tokens.bnb[i][1]}&address={adr}&tag=latest&apikey={key}'
        bal = requests.get(url).json()['result']
        if int(bal) > 0:
            f.write(f'{i}: {str(int(bal) / 10 ** tokens.bnb[i][0])}\n')

if __name__=='__main__':
    w=True
    while w:
        p=int(input('Select an option:\n1.Check address\n2.End the session\n'))
        if p==1:
            print('Select Networks:\n1.ETH\n2.BNB\n3.Polygon\nfor example: 1 or 23 or 123 etc')
            c=[int(x) for x in input()]
            adr=input('Enter the wallet address:')
            f=open(f'result {adr[:6]}..{adr[-4:]}','w')
            f.write(f'Address : {adr}\n')
            for z in c:
                if z==1:
                    ethtokbal(adr,ethkey,f)
                if z==2:
                    bnbtokbal(adr,bnbkey,f)
                if z==3:
                    polygonbal(adr,polkey,f)
                else:
                    continue
            print('Check File')
        else:
            w=False
    print('End of work')



