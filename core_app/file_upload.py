import logging
import csv
from tracker.models import Measurement, Macro

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


def handle_macro_file_import(user, f):
    macro_file = csv.reader(decode_utf8(f))
    next(macro_file)  # Skip header row

    for counter, line in enumerate(macro_file):
        m = Macro()
        m.user = user
        m.date = line[0]
        m.calories = line[1]
        m.fat = line[2]
        m.carbs = line[3]
        m.fiber = line[4]
        m.protein = line[5]
        m.save()


