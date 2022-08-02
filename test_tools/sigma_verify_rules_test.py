"""Tests for Sigma Verify tool."""
from __future__ import unicode_literals

import unittest

from sigma_verify_rules import run_verifier

class TestSigmaVerifyRules(unittest.TestCase):

    def test_verify_rules_file(self):
        """Test some of the verify rules code."""

        self.assertRaises(IOError,run_verifier,'foo','bar')
        self.assertRaises(IOError,run_verifier,'../data/sigma/rules/',
        '../data/sigma_config.yaml')

    def test_run_verifier(self):
        self.assertRaises(IOError, run_verifier,
        '../data/sigma_config.yaml', '../data/sigma/rules/')

        config = './data/sigma_config.yaml'
        rules = './data/sigma/rules/'

        sigma_ok_rules, sigma_prob_rules = run_verifier(
            config_file_path=config, rules_path=rules)
        self.assertEqual(len(sigma_prob_rules),0)
        found = any(
            'lnx_susp_zenmap' in verified_rule for verified_rule in sigma_ok_rules
        )

        self.assertTrue(found)

if __name__ == '__main__':
    unittest.main()
