#!/usr/bin/env python
import nvstream.server as srv


def main():
    s = srv.NVServer()
    s.listen()

if __name__ == '__main__':
    main()
