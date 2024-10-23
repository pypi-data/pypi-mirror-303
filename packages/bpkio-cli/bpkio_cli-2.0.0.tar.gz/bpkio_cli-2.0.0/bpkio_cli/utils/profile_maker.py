from datetime import datetime

import bpkio_api.helpers.profile as PG
from bpkio_api.helpers.handlers import ContentHandler, DASHHandler, HLSHandler


def make_transcoding_profile(
    handler: ContentHandler, schema_version: str, name: str = ""
):
    analyser = None
    if isinstance(handler, HLSHandler):
        analyser = PG.HlsAnalyser(handler)
    elif isinstance(handler, DASHHandler):
        analyser = PG.DashAnalyser(handler)
    else:
        raise Exception("Unsupported handler type")

    renditions = analyser.extract_renditions()
    packaging = analyser.extract_packaging_info()

    generator = PG.TranscodingProfileGenerator(schema=schema_version)
    profile = generator.generate(renditions, packaging, name)

    # decorate the profile
    profile["_generated_from"] = handler.original_url
    profile["_generated"] = datetime.now().isoformat()

    return (profile, analyser.messages + generator.messages)
