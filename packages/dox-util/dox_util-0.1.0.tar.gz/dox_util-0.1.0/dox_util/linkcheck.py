from sphinx.builders.linkcheck import CheckExternalLinksBuilder


# Get rid of warnings when not logged into a web service
class LinkChecker(CheckExternalLinksBuilder):
    def process_result(self, result):
        if result.status == "broken" and "403" in result.message:
            result = result._replace(status="working")
            self._broken.pop(result.uri)
            self._good.add(result.uri)
        super().process_result(result)
