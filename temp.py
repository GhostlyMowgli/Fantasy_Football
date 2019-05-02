# -*- coding: utf-8 -*-


# nfl_stats_explore.py
from bs4 import BeautifulSoup
import urllib 
import datetime

def use_bbg_proxy():
    prxy = {'http': "proxy.bloomberg.com:81"}
    proxy_support = urllib.request.ProxyHandler(prxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    return

# use_bbg_proxy() # uncomment when at work

### the above is required to web scrape at BBG ###
url_root = 'http://www.nfl.com/stats/categorystats?tabSeq=1'
pos = 'statisticPositionCategory=RUNNINGBACK'
season = 'season=2018'
s_type = 'seasonType=REG'

positions = {'qb':'QUARTERBACK',
             'rb':'RUNNINGBACK',
             'wr':'WIDERECEIVER',
             'te':'TIGHTEND',
             'd':'DEFENSE',
             'k':'KICKER'}
def build_link_nfl(position, season='', season_type='REG'):
    url = 'http://www.nfl.com/stats/categorystats?tabSeq=1'
    
    pos = 'statisticPositionCategory='
    sn = 'qualified=true&season='
    s_type = 'seasonType='
    
    roots = [pos, sn, s_type]
    inps = [position, season, season_type]
    
    if season == '':
        season = datetime.date.today().strftime("%Y")
    
    for i in range(len(inps)):
        url += "&{}".format(roots[i])
        url += inps[i]
    
    return url
    
url = build_link_nfl('QUARTERBACK','2018')
html = urllib.request.urlopen(url)
bsobj = BeautifulSoup(html.read())
p1 = bsobj.find_all(href=True)
p2 = [line for line in p1 if 'profile?id=' in str(line)]
player_ids = [str(line)[str(line).index('?')+4:str(line).index('>')-1] for line in p2]
player_names = [str(line)[str(line).index(player_ids[i])+len(player_ids[i])+2:-4] for i, line in enumerate(p2)]