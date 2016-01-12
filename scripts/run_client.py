#!/usr/bin/env python
import nvstream.client as client


def main():
    s = client.NVClient()
    s.get()

if __name__ == '__main__':
    main()
