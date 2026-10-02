# qrcode-cli

Generate QR codes from the terminal using [segno](https://github.com/heuer/segno).

## Usage

```bash
python3 qr.py "https://github.com" wifi.png
```

- First argument: text or URL to encode.
- Second argument (optional): output filename, defaults to `qr.png`.
- Output is a PNG ready to print or share.
