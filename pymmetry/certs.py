#!/usr/bin/env python
"""	certs.py: Certification base classes.
    Copyright (C) 2001 Luke Kenneth Casson Leighton <lkcl@samba-tng.org>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""


class Certifications:
    def cert_keys(self):
        raise NotImplementedError

    def certs_by_type(self, type_):
        raise NotImplementedError

    def cert_type_keys(self, type_, name):
        raise NotImplementedError

    def add(self, type_, name, level):
        raise NotImplementedError

    def remove(self, type_, name):
        raise NotImplementedError

    def cert_level(self, type_, name):
        raise NotImplementedError


class DictCertifications(Certifications):

    def __init__(self):
        self.info = {}

    def cert_keys(self):
        return self.info.keys()

    def certs_by_type(self, type_):
        return self.info[type_]

    def cert_type_keys(self, type_, name):
        return self.info[type_].keys()

    def add(self, type_, name, level):
        if type_ is not self.info.keys():
            self.info[type_] = {}
        self.info[type_][name] = level

    def remove(self, type_, name):
        if type_ in self.info.keys() and name in self.info[type_].keys():
            del self.info[type_][name]

    def cert_level(self, type_, name):
        return self.info[type_][name]


class CertInfoBase:

    def cert_seeds(self, idxn):
        raise NotImplementedError

    def cert_levels(self, idxn):
        raise NotImplementedError

    def cert_level_default(self, idxn):
        raise NotImplementedError

    def cert_level_min(self, idxn):
        raise NotImplementedError

    def cert_tmetric_type(self, idxn):
        raise NotImplementedError
