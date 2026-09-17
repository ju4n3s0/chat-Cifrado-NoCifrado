# Secure Chat — Encrypted vs Unencrypted

Chat app for comparing unencrypted (ws://) and encrypted (wss://) communication using Wireshark.

## Requirements

- Python 3.10+
- pip
- OpenSSL
- Wireshark

## Files

- `server.py` — backend, runs both ws and wss servers
- `index.html` — frontend
- `generate_cert.sh` — generates self-signed TLS cert

## Setup

Install dependencies: pip install web sockets

Generate TLS certificate: bash generate_cert.sh

This creates `cert.pem` and `key.pem`.

## Run

Start the server: python3 server.py

Server listens on:

- `8765` — unencrypted (ws://)
- `8766` — encrypted (wss://)

Open `index.html` in a browser. Set server IP. Choose mode. Connect.

## Accepting the self-signed certificate

Browsers block wss:// with self-signed certs silently.

Visit `https://SERVER_IP:8766` once in the browser first. Accept the security warning. Then wss:// connections work.

## Testing with two clients

Open `index.html` in two browser tabs or two machines. Set different names. Send messages between them.

## Wireshark capture

Filter unencrypted traffic: tcp.port == 8765

Filter encrypted traffic: tcp.port == 8766 

Right-click a packet → Follow → TCP Stream to inspect content.

Unencrypted stream shows plaintext messages.
Encrypted stream shows TLS handshake and encrypted bytes only.

## What stays visible either way

Source/destination IPs, ports, protocol, packet sizes.

## What encryption hides

Message content.

## Security notes

Use only fictional messages. Run only on controlled VMs/network. Do not capture real credentials or third-party traffic.
