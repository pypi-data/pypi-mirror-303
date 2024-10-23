"""QueryRegulationBilaterals - This message is used to query for the regulation bilateral schedules that are operative for a
particular day. The query response returns all bilaterals for the participant who is a party to the
schedule (as a buyer or a seller). This is a private report.  The bilateral schedules are available at the end of the rebid period for the next day"""
# pylint:disable=duplicate-code
from ...pjm import constants as C
from ...pjm.helper import gen_xml


def prepare(token, **kwargs):
    """prepare and return all the components of the requests call."""

    xml, content_length = gen_xml(with_filters=False, **kwargs)

    return {
        'xml': xml,
        'headers': {
            **C.PJM_BASE_HEADERS,
            'Cookie': 'pjmauth=' + token,
            'Content-length':  content_length
        },
        'url': C.PJM_EMKT_URL_QUERY
    }
