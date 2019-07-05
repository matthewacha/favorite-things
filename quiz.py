from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdDNNl6XK32g_6dHpesU0QuYpHEXXdPcEPEDlsGUD_7VNBdc-"\
    "8jk61LcaU75D5deKMWbtKMk-xY1GA81liMia2ES9U-UuFcvXxmNib0uYDTk4JdZMD"\
        "4hpOYGAFBsA5jLbXOcTi5KqBM5SqAvPQT-JqMWvGKyWLwAk7pJzEM0Y6gV5WPmQ='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
