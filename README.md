# qrftp
Host a file from your device to your local network with one command and output a QR code to the command line to quickly download the file to your mobile.

- The file is served on port 8000 by default.
- After one download of the file, the port is closed.
- Your device private IP is resolved via the hostname of the device the code is ran on. In most cases this works fine but your /etc/hosts file may specify a loopback address for your hostname which will break things.
- This was made on a whim so weird usage will almost certainly break things.
## Usage:
**qrftp** [filename/filepath]

![command line view of generated QR code for hosted file](https://github-production-user-asset-6210df.s3.amazonaws.com/96323936/238383490-bbea083b-8a29-4298-bc4a-cabb128548b2.PNG)![view from mobile device after scanning QR code](https://github-production-user-asset-6210df.s3.amazonaws.com/96323936/238383510-91311cde-8f74-4c8f-b493-48bd27be67e8.PNG)
