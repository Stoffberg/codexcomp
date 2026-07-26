import logging

from codexcomp.cli import _configure_logging


def test_debug_logging_redacts_transport_details():
    names = ("httpcore", "httpx", "websockets")
    previous = {name: logging.getLogger(name).level for name in names}
    try:
        assert _configure_logging("debug") == "info"
        assert all(logging.getLogger(name).level == logging.INFO for name in names)
    finally:
        for name, level in previous.items():
            logging.getLogger(name).setLevel(level)


def test_non_debug_logging_is_unchanged():
    assert _configure_logging("warning") == "warning"


def main():
    test_debug_logging_redacts_transport_details()
    test_non_debug_logging_is_unchanged()
    print("cli self-test: ALL PASS")


main()
