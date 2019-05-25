#
# Copyright (c) 2016-2019, Marcin Barylski
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation 
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
# OF SUCH DAMAGE.
# 

import unittest
import sys
sys.path.insert(0, '..\\primes\\')
import primes
import shapes

#############################################################
# Unit tests
#############################################################

class TestMethods(unittest.TestCase):
    def test_isprime(self):
        p = primes.Primes(False)
        self.assertTrue(p.is_prime(2))
        self.assertTrue(p.is_prime(3))
        self.assertTrue(p.is_prime(5))
        self.assertTrue(p.is_prime(7))
        self.assertTrue(p.is_prime(11))

    def test_isprime_cuda(self):
        p = primes.Primes(False)
        self.assertTrue(p.is_prime_cuda(2))
        self.assertTrue(p.is_prime_cuda(3))
        self.assertTrue(p.is_prime_cuda(5))
        self.assertTrue(p.is_prime_cuda(7))
        self.assertTrue(p.is_prime_cuda(11))

    def test_isnotprime(self):
        p = primes.Primes(False)
        self.assertFalse(p.is_prime(1))
        self.assertFalse(p.is_prime(4))
        self.assertFalse(p.is_prime(6))
        self.assertFalse(p.is_prime(8))
        self.assertFalse(p.is_prime(10))
        self.assertFalse(p.is_prime(3379995))

    def test_isnotprime_cuda(self):
        p = primes.Primes(False)
        self.assertFalse(p.is_prime_cuda(1))
        self.assertFalse(p.is_prime_cuda(4))
        self.assertFalse(p.is_prime_cuda(6))
        self.assertFalse(p.is_prime_cuda(8))
        self.assertFalse(p.is_prime_cuda(10))
        self.assertFalse(p.is_prime_cuda(3379995))

    def test_get_ith_prime(self):
        p = primes.Primes(False)
        p.add_to_primes_set(2)
        p.add_to_primes_set(3)
        p.add_to_primes_set(5)
        p.add_to_primes_set(7)
        p.sort_primes_set()
        self.assertEqual(p.get_ith_prime(0), 2)
        self.assertEqual(p.get_ith_prime(1), 3)
        self.assertEqual(p.get_ith_prime(2), 5)

    def test_next_sign(self):
        self.assertEqual(shapes.next_sign(1), -1)
        self.assertEqual(shapes.next_sign(-1), 1)

    def test_next_sign_negative(self):
        self.assertEqual(shapes.next_sign(0), 1)
        self.assertEqual(shapes.next_sign(-5), 1)
        self.assertEqual(shapes.next_sign(5), 1)

    def test_next_delta_xy_noturn(self):
        self.assertEqual(shapes.next_delta_xy (0, 1, False), (0, 1))
        self.assertEqual(shapes.next_delta_xy (1, 0, False), (1, 0))
        self.assertEqual(shapes.next_delta_xy (0, -1, False), (0, -1))
        self.assertEqual(shapes.next_delta_xy (-1, 0, False), (-1, 0))

    def test_next_delta_xy_turn(self):
        self.assertEqual(shapes.next_delta_xy (0, 1, True), (-1, 0))
        self.assertEqual(shapes.next_delta_xy (1, 0, True), (0, 1))
        self.assertEqual(shapes.next_delta_xy (0, -1, True), (1, 0))
        self.assertEqual(shapes.next_delta_xy (-1, 0, True), (0, -1))

    def test_get_sum_of_decimal_digits(self):
        self.assertEqual(shapes.get_sum_of_decimal_digits (1), 1)
        self.assertEqual(shapes.get_sum_of_decimal_digits (2), 2)
        self.assertEqual(shapes.get_sum_of_decimal_digits (10), 1)
        self.assertEqual(shapes.get_sum_of_decimal_digits (29), 11)
        self.assertEqual(shapes.get_sum_of_decimal_digits (3435343698124), 55)

#############################################################
# Main - run unit tests
#############################################################

unittest.main()
