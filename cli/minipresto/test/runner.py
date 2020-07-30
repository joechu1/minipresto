#!usr/bin/env/python3
# -*- coding: utf-8 -*-

import minipresto.test.test_config as test_config
import minipresto.test.test_down as test_down
import minipresto.test.test_provision as test_provision
import minipresto.test.test_remove as test_remove
import minipresto.test.test_snapshot as test_snapshot


def main():
    """minipresto unit test runner."""

    test_config.main()
    test_down.main()
    test_provision.main()
    test_remove.main()
    test_snapshot.main()


if __name__ == "__main__":
    main()