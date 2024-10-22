
# Pulse VPN

Pulse VPN is a minimal web GUI that helps you connect to Pulse Connect Secure
VPN servers that require Web-based multi-factor authentication (SSO/SAML). This
script is intended to be used in conjunction with the OpenConnect VPN CLI
client using the --protocol=nc option.

You might want to use this script if:

- your organization uses the Pulse Connect Secure VPN with multi-factor
  authentication (MFA) that requires you to enter credentials into a web GUI

- you want to avoid using the official (proprietary) Pulse Connect Secure VPN
  client application

## Install

```bash
sudo apt install openconnect libxcb-cursor-dev
pip install --user pulse-vpn
```

## Acknowledgements

Original project: https://codeberg.org/raj-magesh/pulse-cookie

