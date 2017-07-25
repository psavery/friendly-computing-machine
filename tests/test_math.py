#!/usr/bin/env python3
"""Simple tests for the math module
"""

import friendly_computing_machine as fcm
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.add(2, 5) == 7
    assert fcm.math.add(3, 5) == 8
    assert fcm.math.add(-1, -4) == -5
    assert fcm.math.add(-3, 5) == 2

def test_sub():
    assert fcm.math.sub(5, 2) == 3
    assert fcm.math.sub(2, 5) == -3
    assert fcm.math.sub(3, 5) == -2
    assert fcm.math.sub(-1, -4) == 3
    assert fcm.math.sub(-3, 5) == -8

def test_mult():
    assert fcm.math.mult(5, 2) == 10
    assert fcm.math.mult(2, 5) == 10
    assert fcm.math.mult(3, 5) == 15
    assert fcm.math.mult(-1, -4) == 4
    assert fcm.math.mult(-3, 5) == -15

def test_div():
    assert fcm.math.div(5, 2) == 2.5
    assert fcm.math.div(2, 5) == 0.4
    assert fcm.math.div(3, 5) == 0.6
    assert fcm.math.div(-1, -4) == 0.25
    assert fcm.math.div(-3, 5) == -0.6
