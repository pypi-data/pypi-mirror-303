from pylatex import Document, Section, Command, NoEscape

class DocumentGenerator:
    """
    A class used to generate a LaTeX document with CJK support using Source Han Sans.

    Attributes
    ----------
    doc : pylatex.Document
        The LaTeX document being generated.

    Methods
    -------
    __init__(title, authors, title_lang='en', author_langs=['en'])
        Initializes the DocumentGenerator with title, authors, and language settings.
    
    _format_text(text, lang)
        Formats the text according to the specified language.
    
    _format_authors(authors, author_langs)
        Formats the authors' names according to their respective languages.
    
    add_chapter(chapter_heading, paragraphs, lang='en')
        Adds a chapter with the specified heading and paragraphs to the document.
    
    generate_pdf(filename, clean_tex=True)
        Generates a PDF file from the LaTeX document.
    """

    def __init__(self, title, authors, title_lang='en', author_langs=['en']):
        """
        Initializes the DocumentGenerator with title, authors, and language settings.

        Parameters
        ----------
        title : str
            The title of the document.
        authors : list of str
            A list of authors' names.
        title_lang : str, optional
            The language of the title (default is 'en').
        author_langs : list of str, optional
            A list of languages corresponding to each author (default is ['en']).
        """
        self.doc = Document(documentclass='article', lmodern=False)
        self.doc.preamble.append(Command('usepackage', 'fontspec'))

        self.doc.preamble.append(NoEscape(r'\setmainfont{Noto Sans}'))
        self.doc.preamble.append(NoEscape(r'\newfontfamily\chinesefont{Source Han Sans CN}'))
        self.doc.preamble.append(NoEscape(r'\newfontfamily\japanesefont{Source Han Sans JP}'))
        self.doc.preamble.append(NoEscape(r'\newfontfamily\koreanfont{Source Han Sans KR}'))

        # Set title and author with language support
        self.doc.preamble.append(Command('title', NoEscape(self._format_text(title, title_lang))))
        formatted_authors = self._format_authors(authors, author_langs)
        self.doc.preamble.append(Command('author', NoEscape(formatted_authors)))
        self.doc.preamble.append(Command('date', NoEscape(r'\today')))
        self.doc.append(NoEscape(r'\maketitle'))
        # Add table of contents at the end to ensure it captures all sections
        self.doc.append(NoEscape(r'\tableofcontents'))
        self.doc.preamble.append(Command('usepackage', 'bookmark'))
        self.doc.preamble.append(Command('usepackage', 'libertine'))

    def _format_text(self, text, lang):
        """
        Formats the text according to the specified language.

        Parameters
        ----------
        text : str
            The text to be formatted.
        lang : str
            The language code (e.g., 'cn' for Chinese, 'jp' for Japanese, 'kr' for Korean).

        Returns
        -------
        str
            The formatted text.
        """
        if lang == 'cn':
            return r'\chinesefont ' + text
        elif lang == 'jp':
            return r'\japanesefont ' + text
        elif lang == 'kr':
            return r'\koreanfont ' + text
        else:
            return text

    def _format_authors(self, authors, author_langs):
        """
        Formats the authors' names according to their respective languages.

        Parameters
        ----------
        authors : list of str
            A list of authors' names.
        author_langs : list of str
            A list of languages corresponding to each author.

        Returns
        -------
        str
            The formatted authors' names.
        """
        formatted_authors = []
        for author, lang in zip(authors, author_langs):
            formatted_authors.append(self._format_text(author, lang))
        return ', '.join(formatted_authors)

    def add_chapter(self, chapter_heading, paragraphs, lang='en'):
        """
        Adds a chapter with the specified heading and paragraphs to the document.

        Parameters
        ----------
        chapter_heading : str
            The heading of the chapter.
        paragraphs : list of str
            A list of paragraphs to be included in the chapter.
        lang : str, optional
            The language of the paragraphs (default is 'en').
        """
        with self.doc.create(Section(chapter_heading, numbering=True)):
            for paragraph in paragraphs:
                self.doc.append(NoEscape(self._format_text(paragraph, lang)))
                self.doc.append(NoEscape(r'\par'))  # Add paragraph break
        print(f"Chapter {chapter_heading} saved.")

    def generate_pdf(self, filename, clean_tex=True):
        """
        Generates a PDF file from the LaTeX document.

        Parameters
        ----------
        filename : str
            The name of the output PDF file.
        clean_tex : bool, optional
            Whether to clean up auxiliary files generated during the PDF creation (default is True).
        """
        # Set XeLaTeX as the default compiler for fontspec
        self.doc.generate_pdf(filename, clean_tex=clean_tex, compiler='xelatex')