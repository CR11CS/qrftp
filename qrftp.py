#!/usr/bin/python3

import functools
import http.server
import qrcode
import socket
import socketserver
import sys
from pathlib import Path
PORT = 8000


def main(text):
    try:
        # Create QR code instance
        qr = qrcode.QRCode(version=1, box_size=10, border=5)

        # Add data to QR code instance
        qr.add_data(text)
        qr.make(fit=True)
        qr.print_ascii(invert=True)
    except:
        print("ERROR: Unhandled exception while trying to generate QR code", file=sys.stderr)
        sys.exit(1)

    # Host file on websocket
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Hosting file at {full_text}")
            httpd.handle_request()
    except:
        print("ERROR: Unhandled exception while trying to initiate fileserver")
        sys.exit(1)


if __name__ == "__main__":
    # Establish file location
    try:
        specified_file = sys.argv[1]
        filepath = Path(specified_file).resolve()
        if not filepath.exists():
            raise FileNotFoundError
    except ValueError:
        if not sys.argv[1]:
            print("Command usage: qrftp [filename/filepath]", file=sys.stderr)
            sys.exit(1)
    except FileNotFoundError:
        print(f"ERROR: File '{specified_file}' not found", file=sys.stderr)
        sys.exit(1)
    except:
        print("ERROR: Unhandled exception while trying to get file", file=sys.stderr)
        sys.exit(1)

    # Establish local IP address
    try:
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
    except socket.gaierror:
        print("ERROR: General socket error", file=sys.stderr)
        sys.exit(1)
    except socket.herror:
        print("ERROR: Failed to get device hostname", file=sys.stderr)
        sys.exit(1)
    except socket.timeout:
        print("ERROR: Socket timeout", file=sys.stderr)
        sys.exit(1)
    except:
        print("ERROR: Unhandled socket exception", file=sys.stderr)
        sys.exit(1)

    # Establish server directory instead of default directory of CWD
    Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=filepath.parent)

    # Establish text string to be provided to QR code generator
    bare_filename = filepath.name
    full_text = f"http://{ipaddress}:{PORT}/{bare_filename}"
    main(full_text)
