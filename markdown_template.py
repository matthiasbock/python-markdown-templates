
# Use string library to parse values into template string/file
from string import Template

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
            f = open(filename, "r")
            s = f.read()
            f.close()
        self.s = s

    #
    # Fill template with variables
    #
    def __str__(self):
        # Make a string.Template object
        t = Template(self.s)
        # Subsitute template $variables with this object's attributes
        s = t.substitute(self.__dict__)
        return s

    #
    # Display filled template in current Jupyter notebook
    #
    def show(self):
        return display(Markdown(str(self)))
