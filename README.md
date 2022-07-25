# Sotch - SOCKS fetcher

Sotch is a simple and small tool to fetch all available SOCKS4/5 proxies from
shodan.io

Usage:
```
./sotch.py -O proxies.txt --api-key <your-shodan-api-key>
```

Help menu:
```
usage: sotch.py [-h] [-O OUTFILE] [--api-key KEY]

Shodan tool to extract and save SOCKS proxies

options:
  -h, --help     show this help message and exit
  -O OUTFILE     Define output file (default is stdout)
  --api-key KEY  (default is D_API_KEY)
```