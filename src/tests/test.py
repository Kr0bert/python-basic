import logging
import pytest

logger = logging.getLogger(__name__)

def test_initial():
    logger.info(f"Test initial OK")
    assert True