class InformalParserInterface:
    def load_data_source(self, path, file_name):
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name):
        """Extract text from the currently loaded file."""
        pass


class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""

    def load_data_source(self, path, file_name):
        """Overrides InformalParserInterface.load_data_source()"""
        print("loading pdf file")
        pass

    def extract_text(self, full_file_name):
        """Overrides InformalParserInterface.extract_text()"""
        print("extracting text from pdf file")
        pass


class EmailParser(InformalParserInterface):
    """Extract text from an email"""

    def load_data_source(self, path, file_name):
        """Overrides InformalParserInterface.load_data_source()"""
        print("loading email")
        pass

    def extract_text_from_email(self, full_file_name):
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text() - issue with informal interfaces
        """
        print("extracting text from email")
        pass


print(issubclass(PdfParser, InformalParserInterface)) # true
print(issubclass(EmailParser, InformalParserInterface)) # true even taking into account that emailParser doesn't
# override extract_text method

print(PdfParser.mro()) # [<class '__main__.PdfParser'>, <class '__main__.InformalParserInterface'>, <class 'object'>]
print(EmailParser.mro()) # [<class '__main__.EmailParser'>, <class '__main__.InformalParserInterface'>, <class 'object'>]


def test_parsers(parser: InformalParserInterface):
    parser.load_data_source("path", "file_name")
    parser.extract_text("full_file_name")


test_parsers(PdfParser())
test_parsers(EmailParser())
