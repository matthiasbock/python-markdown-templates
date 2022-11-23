
# Use string library to parse values into template string/file
from string import Template

# Required for Python versions below 3.11
import re

# For the ability to import variables from files
import json

# Generate output suitable for Jupyter notebook
from IPython.display import display, Markdown


#
# Opens a Markdown formatted file
# and replaces all $variables with
# values from the object itself
#
class MarkdownTemplate():
    #
    # Initialize a Markdown template from file or string
    #
    def __init__(self, s=None, filename=None):
        if filename != None:
            s = self.fromFile(filename)
        self._template = s

    #
    # Load Markdown template from file
    #
    def fromFile(self, filename):
        f = open(filename, "r")
        self._template = f.read()
        f.close()
        return self._template

    #
    # Save filled Markdown template to file
    #
    def toFile(self, filename):
        md = str(self)
        f = open(filename, "w")
        f.write(md)
        f.close
        return md

    #
    # Load template variable values from JSON file
    #
    def loadJSON(self, filename):
        # Read file
        f = open(filename, "r")
        s = f.read()
        f.close()

        # Parse as JSON
        j = json.loads(s)

        # Copy values from JSON to this object
        for key in j.keys():
            if key != "_template":
                self.__dict__[key] = j[key]

    #
    # Return the string.Template for this object
    #
    def getTemplate(self):
        if self._template is None:
            return None
        return Template(self._template)

    #
    # Return the list of the currently loaded template's variables
    #
    def getVariables(self):
        if self._template is None:
            return []
        try:
            # New in version 3.11 (see https://docs.python.org/3/library/string.html)
            return self.getTemplate().get_identifiers()
        except:
            # The above fails with Python versions before 3.11
            pass
        rVariable = re.compile("\$([a-zA-Z\_]+)")
        vars = rVariable.findall(self._template)
        return vars

    #
    # Fill template with variables
    #
    def __str__(self):
        # Make a string.Template object
        t = self.getTemplate()
        # Subsitute template $variables with this object's attributes
        s = t.safe_substitute(self.__dict__)
        return s

    #
    # Display filled template in current Jupyter notebook
    #
    def show(self):
        return display(Markdown(str(self)))
