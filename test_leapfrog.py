#! /usr/bin/env python

import leapfrog


def test_sound_cloud_api():
    """Validate urllib and json approach"""

    data = leapfrog.apiExample()
    assert data['title'] == 'Munching at Tiannas house'


def test_leapfrog():
    """Leapfrog Testing valid inputs"""

    data = leapfrog.leapfrogAPI()
    assert data['propensity'] == 0.26532
    assert data['ranking'] == "C"
    assert data['status'] == "URL Error"


def test_leapfrog_invail():
    """Testing with invalid inputs"""

    data = leapfrog.leapfrogAPI('a', 1, 2)
    assert data['status'] == 'Value Error'

    data = leapfrog.leapfrogAPI(1, 2, 'cakdfjksf')
    assert data['status'] == 'Value Error'
