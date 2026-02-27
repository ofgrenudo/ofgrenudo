def get_lan_ip():
    import socket

    print(
        (
            (
                [
                    ip
                    for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                    if not ip.startswith("127.")
                ]
                or [
                    [
                        (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                    ][0][1]
                ]
            )
            + ["no IP found"]
        )[0]
    )


def get_wan_ip():
    # requests suxs, use httpx. be cool.
    import httpx

    ip = httpx.get("https://api.ipify.org").content.decode("utf8")
    print("{}".format(ip))
