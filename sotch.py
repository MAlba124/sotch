#!/bin/python3

try:
    import sys
    import argparse

    import shodan
except ModuleNotFoundError as err:
    print("[-] Failed to import module! %s" % err)
    sys.exit(1)

D_API_KEY: str = ""

def init_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Shodan tool to extract and save SOCKS proxies'
    )
    parser.add_argument("-O", dest="outfile", type=str,
                        help="Define output file (default is stdout)")
    parser.add_argument("--api-key", dest="key", type=str,
                        help="(default is D_API_KEY)")

    return parser.parse_args()

def main() -> int:
    try:
        args: argparse.Namespace = init_args()
        apikey: str = args.key if args.key != None else D_API_KEY

        api: shodan.client.Shodan = shodan.Shodan(apikey)

        # Just for keeping count :)
        total_proxies_found: int = 0

        protocol_list: list = ["SOCKS5", "SOCKS4"]

        # Open file to save proxies in
        outputfile: file = open(args.outfile, "w") if args.outfile != None \
            else None

        for protocol in protocol_list:
            print("[*] Searching for %s proxies..." % protocol)
            res: dict = api.search(protocol) # Search shodan for proxy
            print("[+] Found %d possible %s proxies" %
                  (len(res["matches"]), protocol))
            total_proxies_found += len(res["matches"])
            for result in res["matches"]:
                ln: str = "Protocol: %s IP: %s\n" % (protocol, result["ip_str"])
                if outputfile != None:
                    outputfile.write(ln) # Write the protocol and IP to the user
                                         # speciffied outputfile if any
                else:
                    print(ln, end="")

        print("[+] Found %d total proxies" % (total_proxies_found))

    # Handle any errors that may occure
    except KeyboardInterrupt:
        if outputfile != None: outputfile.close()
        print("[!] Cought keyboard interupt")
    except Exception as err:
        if outputfile != None: outputfile.close()
        print("[-] Error encountered while executing. %s" % err)
        return 1

    if outputfile != None: outputfile.close()
    return 0

if __name__ == "__main__":
    sys.exit(main())
