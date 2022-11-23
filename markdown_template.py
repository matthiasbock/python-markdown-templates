
# Use string library to parse values into template string/file
from string import Template

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
    # Fill template with variables
    #
    def __str__(self):
        # Make a string.Template object
        t = Template(self._template)
        # Subsitute template $variables with this object's attributes
        s = t.substitute(self.__dict__)
        return s

    #
    # Display filled template in current Jupyter notebook
    #
    def show(self):
        return display(Markdown(str(self)))
