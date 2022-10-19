from Core__ import __CORE


class Preambule:

    def __init__(self, language_package=["russian", "babel"], code_table=["utf8", "inputenc"], math="amsmath"):

        def __BuiltModule(arr): return ("\\usepackage[%s]{%s}" % (arr[0], arr[1])) if type(
            arr) == type(list()) else ("\\usepackage{%s}" % (arr))

        self.Language = __BuiltModule(language_package)
        self.CodeTable = __BuiltModule(code_table)
        self.Math = __BuiltModule(math)

        self.Modules = [self.Language, self.CodeTable, self.Math]

    def GetModules(self):
        string = ""

        for i in self.Modules:
            string += i + '\n'
        return string + "\n"


class Document(__CORE):

    def __init__(self, paper_type="a4paper", text_size="14pt", document_type="article"):
        self.PaperType = paper_type
        self.TextSize = text_size
        self.DocumentType = document_type
        self.Preambule = Preambule().GetModules()
        self.__FILESTREAM = ''

    def GenerateTamplateBegin(self):
        TempString = ""
        DocumentClass = "\\documentclass[%s,%s]{%s}\n" % (
            self.PaperType, self.TextSize, self.DocumentType)

        TempString += DocumentClass
        TempString += self.Preambule
        TempString += "\\begin{document}\n"

        return TempString


    def GenerateTamplateEnd(self):
        TempString = "\n\\end{document}"
        return TempString

    def Begin(self, filename):
        if ".txt" in filename:
            self.__FILE_STREAM = super().StdOut(filename)
            self.__FILE_STREAM.write(self.GenerateTamplateBegin())
        else:
            self.__FILE_STREAM = super().StdOut("%s.txt" % (filename))
            self.__FILE_STREAM.write(self.GenerateTamplateBegin())

    def End(self):

        self.__FILE_STREAM.write(self.GenerateTamplateEnd())
        self.__FILE_STREAM.close()


if __name__ == '__main__':
    pass