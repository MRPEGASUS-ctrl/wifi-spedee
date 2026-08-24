#!/usr/bin/env python3
import time
import sys

def get_net_bytes():
    """Membaca total bytes secara aman khusus untuk Linux/Termux."""
    try:
        with open('/proc/net/dev', 'r') as f:
            lines = f.readlines()
            rx_bytes = 0
            tx_bytes = 0
            for line in lines[2:]:
                data = line.split(':')
                if len(data) > 1:
                    fields = data[1].split()
                    # Kolom ke-0 adalah received bytes, kolom ke-8 adalah transmitted bytes
                    rx_bytes += int(fields[0])
                    tx_bytes += int(fields[8])
            return rx_bytes, tx_bytes
    except Exception:
        return 0, 0

def format_bytes(bytes_num):
    kb = bytes_num / 1024
    if kb >= 1024:
        return f"{kb / 1024:.2f} MB/s"
    return f"{kb:.2f} KB/s"

def draw_bar(speed_bytes, max_speed=5 * 1024 * 1024):
    length = 20
    fraction = min(speed_bytes / max_speed, 1.0)
    filled = int(length * fraction)
    return "█" * filled + "-" * (length - filled)

def main():
    print("\033[92m======================================")
    print("        WIFI SPEDEE - MONITOR        ")
    print("======================================\033[0m")
    print("Tekan Ctrl+C untuk menghentikan.\n")

    last_rx, last_tx = get_net_bytes()
    last_time = time.time()

    try:
        while True:
            time.sleep(1)
            current_time = time.time()
            current_rx, current_tx = get_net_bytes()

            elapsed = current_time - last_time
            if elapsed > 0:
                speed_down = (current_rx - last_rx) / elapsed
                speed_up = (current_tx - last_tx) / elapsed
            else:
                speed_down = 0
                speed_up = 0

            sys.stdout.write("\033[K")
            print(f" ⬇ DOWNLOAD : {format_bytes(speed_down):<10} [{draw_bar(speed_down)}]")
            sys.stdout.write("\033[K")
            print(f" ⬆ UPLOAD   : {format_bytes(speed_up):<10} [{draw_bar(speed_up)}]")
            
            sys.stdout.write("\033[F\033[F")
            sys.stdout.flush()

            last_rx, last_tx = current_rx, current_tx
            last_time = current_time

    except KeyboardInterrupt:
        print("\n\n\033[91m[!] wifi spedee dihentikan.\033[0m")
        sys.exit()

if __name__ == "__main__":
    main()
