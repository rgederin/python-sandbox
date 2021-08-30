class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class InformalParserInterface(metaclass=ParserMeta):
    def load_data_source(self, path, file_name):
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name):
        """Extract text from the currently loaded file."""
        pass


class PdfParser:
    """Extract text from a PDF"""

    def load_data_source(self, path, file_name):
        """Overrides InformalParserInterface.load_data_source()"""
        print("loading pdf file")
        pass

    def extract_text(self, full_file_name):
        """Overrides InformalParserInterface.extract_text()"""
        print("extracting text from pdf file")
        pass


class EmailParser:
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


print(issubclass(PdfParser, InformalParserInterface))  # true
print(issubclass(EmailParser, InformalParserInterface))  # false

print(PdfParser.mro())  # [<class '__main__.PdfParser'>, <class 'object'>]
print(EmailParser.mro())  # [<class '__main__.EmailParser'>, <class 'object'>]


def test_parsers(parser: InformalParserInterface):
    parser.load_data_source("path", "file_name")
    parser.extract_text("full_file_name")


test_parsers(PdfParser())
# test_parsers(EmailParser()) -> AttributeError: 'EmailParser' object has no attribute 'extract_text'
