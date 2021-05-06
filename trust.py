from pymmetry.profile import Profiles, Profile
from pymmetry.certs import DictCertifications
from pymmetry.cert_info import CertInfo
from pymmetry.tm_calc import TrustMetric


class TrustScore:
    def __init__(self, records, source, destination):
        self.records = records
        self.source = source
        self.destination = destination
        self.profile = Profiles(Profile, DictCertifications)

    @classmethod
    def call(cls, records, source, destination):
        return cls(records, source, destination).get_trust_score()

    def get_trust_score(self):
        self.create_certifications()
        trust_metrics = self.calculate_trust_metrics()

        return trust_metrics[self.destination]

    def create_certifications(self):
        profiles = set()

        for record in self.records:
            subject = record['subject']
            issuer = record['issuer']
            level = record['level']

            if subject not in profiles:
                self.profile.add_profile(subject)
                profiles.add(subject)

            if issuer not in profiles:
                self.profile.add_profile(issuer)
                profiles.add(issuer)

            self.profile.add_cert(subject, "like", issuer, level)

    def calculate_trust_metrics(self):
        trust_calc = TrustMetric(CertInfo(), self.profile)

        return trust_calc.tmetric_calc('like', [self.source])
