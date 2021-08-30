import abc


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class PdfParser:
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        print("loading pdf file")
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        print("extracting text from pdf file")
        pass


class EmailParser:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        print("loading email")
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        print("extracting text from email")
        pass


print(issubclass(PdfParser, FormalParserInterface))  # true
print(issubclass(EmailParser, FormalParserInterface))  # true even taking into account that emailParser doesn't
# override extract_text method

print(PdfParser.mro())
print(EmailParser.mro())


def test_parsers(parser: FormalParserInterface):
    parser.load_data_source("path", "file_name")
    parser.extract_text("full_file_name")


test_parsers(PdfParser())


# test_parsers(EmailParser())


class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass


Double.register(float)
issubclass(float, Double)  # true


