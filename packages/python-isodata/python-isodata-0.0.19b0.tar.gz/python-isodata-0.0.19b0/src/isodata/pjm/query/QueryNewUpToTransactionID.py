"""QueryNewUpToTransactionID - This message is used to query for the next up to transaction id for a participant. This is a private
report.
"""
# pylint:disable=duplicate-code
from ...pjm import constants as C


def prepare(token, **kwargs):
    """prepare and return all the components of the requests call."""

    xml = "".join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<SOAP-ENV:Envelope SOAP-ENV:encodingStyle="%s" xmlns:SOAP-ENV="%s">' % (C.SOAP_ENCCODING, C.SOAP_ENVELOPE),
        '<SOAP-ENV:Body>',
        '<QueryRequest xmlns="%s"><%s/></QueryRequest>' % (C.PJM_EMKT_XMLNS, kwargs['report']),
        '</SOAP-ENV:Body>',
        '</SOAP-ENV:Envelope>',
    ])

    return {
        'xml': xml,
        'headers': {
            **C.PJM_BASE_HEADERS,
            'Cookie': 'pjmauth=' + token,
            'Content-length':  str(len(xml))
        },
        'url': C.PJM_EMKT_URL_QUERY
    }
