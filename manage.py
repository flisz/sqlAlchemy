#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(url='postgresql://myapp:dbpass@localhost:15432/myapp', debug='True', repository='sql_alchemy')
