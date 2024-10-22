from re import search, compile, purge, Pattern
from string import punctuation, ascii_lowercase, digits
from unicodedata import name
from immutableType import Str_, Bool_, StrError

special_caracteres = punctuation+digits

class Find:

    def __init__(self):
        """
        Init all characters.
        THE INITIALISATION IS VERY SLOW !
        """

        self.__alphabet_avec_variantes = {}
        for i in ascii_lowercase:
            self.__alphabet_avec_variantes[i] = self.__trouver_variantes_de_lettre(i)

        self.__in_word: bool


    def __trouver_variantes_de_lettre(self, base_char: str) -> list:
        """
        Trouves des variantes d'une lettre et ajoute la ponctuation et les caractères digitaux
        :param base_char:
        :return:
        """
        variantes = []
        for codepoint in range(0x110000):  # Limite de l'espace Unicode
            char = chr(codepoint)
            try:
                # Vérifier si le nom du caractère contient la lettre de base "a"
                unicode_name = name(char)

                result = search(r"\b["+f"{base_char.lower()}{base_char.upper()}"+r"]\b", unicode_name)

                if result is not None:
                    variantes.append(char)

            except ValueError:
                # Ignorer les caractères qui n'ont pas de nom Unicode
                pass
        return variantes + [i for i in special_caracteres]


    def __recherche_regex(self, mot: str) -> Pattern:
        """
        Crée le patter correspondant au mot recherché
        :param mot: le mot recherché
        :return: un modèle regex
        """
        correspondances = []

        for i in mot:
            correspondances.append(self.__alphabet_avec_variantes[i])

        pattern = r''.join([rf"[{''.join(sous_liste)}]+[{special_caracteres}]*" for sous_liste in correspondances])

        return compile(self.__modifier_pattern(pattern))

    def __modifier_pattern(self, pattern) -> str:
        """
        Modifie le modèle avec les choix de l'utilisateur
        :param pattern: le modèle de base construit par __recherche_regex
        :return: le modèle
        """
        if not self.in_word:
            pattern = r'\b' + pattern + r'\b'

        return pattern


    def __check_types(self, arg) -> Str_:
        """
        Regarde si l'argument est un str ou non (les booléens sont considéré comme des châines de caractère
        :param arg: l'argument
        :return: Str_ type immuable
        :raise: StrError si l'argument n'est pas une châine de caractère
        """
        try:

            int(arg)

        except:
            return Str_(str(arg))

        raise StrError(arg)


    def __find_all_iteration(self, word: str, sentence: str, regex: Pattern):
        """
        Concatène chaque mot un à un pour vérifier le match
        :param word:
        :param sentence:
        :param regex:
        :return:
        """

        if sentence == '':
            return None # Retourner None si le mot n'est pas trouvé dans la phrase entière

        words = sentence.split()  # Diviser la phrase en mots
        current_concatenation = ""

        for i in range(len(words)):
            current_concatenation += words[i]  # Ajouter le mot actuel à la concaténation

            result = search(regex, current_concatenation)

            if result is not None:
                return result  # Retourner Match si le mot est trouvé dans la concaténation actuelle

        return self.__find_all_iteration(word, ' '.join(words[1:]), regex)




    def find_Badwords(self, word: str, sentence: str, linebreak: bool = True, in_word: bool = False) -> bool:
        """
        Search any configuration of word in the sentence
        :param word: a simple word write in LATIN (not string digit) EX : ``ass`` not ``a*s``
        :param sentence: the sentence who the word is find (or not)
        :param linebreak: Replace \\n by space
        :param in_word: Allow research word in another word
        :return: ``True`` if the word is find, else ``False``
        """

        wordStr = self.__check_types(word)
        sentenceStr = Str_(sentence)
        linebreakBool = Bool_(linebreak)
        self.in_word = Bool_(in_word)

        regex = self.__recherche_regex(wordStr.str_)

        if linebreakBool:
            u = sentenceStr.str_.split('\n')
            sentenceStr.str_ = ' '.join(u)

        result = self.__find_all_iteration(wordStr.str_, sentenceStr.str_, regex)

        if result is None:
            purge()
            return False

        # si la phrase ne contient que des caractères spéciaux
        x = 0
        for i in result.group():
            if i in special_caracteres:
                x += 1

        # on ne fait rien
        if len(result.group()) == x:
            return False

        purge()
        return True
