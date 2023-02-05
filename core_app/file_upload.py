import logging
import csv
from tracker.models import Measurement

logger = logging.getLogger(__name__)


def decode_utf8(line_iterator):
    for line in line_iterator:
        yield line.decode('utf-8')


def handle_measurement_file_import(user, m_type, f):
    measurements_file = csv.reader(decode_utf8(f))
    next(measurements_file)  # Skip header row

    for counter, line in enumerate(measurements_file):
        m = Measurement()
        m.user = user
        m.type = m_type
        m.date = line[0]
        m.value = line[1]
        m.save()

