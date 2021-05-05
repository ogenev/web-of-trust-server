from certs import CertInfoBase


class CertInfo(CertInfoBase):

    def __init__(self):
        self.info = {'like': {'levels': ['none', "don't care", 'good', 'best'],
                              'seeds': ['ogi'],
                              'min level': 'none',
                              'default level': "don't care",
                              'type': 'to'
                              },
                     'hate': {'levels': ['none', "don't care", 'dislike',
                                         'looks CAN kill'],
                              'seeds': ['ogi'],
                              'min level': 'none',
                              'default level': "don't care",
                              'type': 'to'
                              }}

    def cert_seeds(self, idxn):
        return self.info[idxn]['seeds']

    def cert_levels(self, idxn):
        return self.info[idxn]['levels']

    def cert_level_default(self, idxn):
        return self.info[idxn]['default level']

    def cert_level_min(self, idxn):
        return self.info[idxn]['min level']

    def cert_tmetric_type(self, idxn):
        return self.info[idxn]['type']
