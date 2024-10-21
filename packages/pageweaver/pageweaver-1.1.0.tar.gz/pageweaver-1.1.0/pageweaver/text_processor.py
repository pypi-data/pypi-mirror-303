import re

class TextProcessor:
    """
    A utility class for processing text, specifically for LaTeX document preparation.

    Methods
    -------
    escape_latex_special_characters(text: str) -> str
        Escapes special characters in a given text to make it LaTeX compatible.

    remove_non_utf8_characters(text: str) -> str
        Removes non-UTF-8 and non-printable control characters from the text,
        then escapes LaTeX special characters.
    
    The following characters are escaped:
    - Backslash (\)
    - Ampersand (&)
    - Percent (%)
    - Dollar ($)
    - Hash (#)
    - Underscore (_)
    - Curly braces ({})
    - Tilde (~)
    - Caret (^)
    then escapes LaTeX special characters. This method first uses a regular
    expression to remove characters outside the printable ASCII range (0x20 to 0x7E).
    After cleaning the text, it calls `escape_latex_special_characters` to ensure
    the text is LaTeX compatible.
    Examples
    --------
    >>> TextProcessor.escape_latex_special_characters("50% & 100$")
    '50\\% \\& 100\\$'
    >>> TextProcessor.remove_non_utf8_characters("Hello\x00World")
    'HelloWorld'    
    """
    
    @staticmethod
    def remove_non_utf8_characters(text: str) -> str:
        """
        Removes non-UTF-8 and non-printable control characters from the text,
        then escapes LaTeX special characters.

        Parameters
        ----------
        text : str
            The input text to be processed.

        Returns
        -------
        str
            The processed text with non-UTF-8 characters removed and LaTeX special characters escaped.

        Examples
        --------
        >>> TextProcessor.remove_non_utf8_characters("Hello\x00World")
        'HelloWorld'
        """
        # Remove non-UTF-8 and non-printable characters using regex
        text = re.sub(r'[^\x20-\x7E]+', '', text)
        # Escape LaTeX special characters
        text = TextProcessor.escape_latex_special_characters(text)
        return text

    @staticmethod
    def escape_latex_special_characters(text: str) -> str:
        """
        Escapes special characters in a given text to make it LaTeX compatible.

        Parameters
        ----------
        text : str
            The input text to be processed.

        Returns
        -------
        str
            The processed text with LaTeX special characters escaped.

        Examples
        --------
        >>> TextProcessor.escape_latex_special_characters("50% & 100$")
        '50\\% \\& 100\\$'
        """
        latex_special_chars = {
            '\\': r'\textbackslash{}',
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}'
        }
        for char, escaped_char in latex_special_chars.items():
            text = text.replace(char, escaped_char)
        return text