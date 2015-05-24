"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from lib_util import Util
class UcCodemirrorXBlock(XBlock):
    """
    UcCodemirror XBlock
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    logger = Util .uc_logger()

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the UcCodemirrorXBlock, shown to students
        when viewing courses.
        """

        fragment = Fragment()
        fragment.add_content(Util.load_resource("static/html/uc_codemirror.html"))
        self.logger.info("load uc_codemirror.html")
        fragment.add_css(Util.load_resource("static/css/uc_codemirror.css"))
        self.logger.info("load uc_codemirror.css")
        fragment.add_css(Util.load_resource("static/css/codemirror.css"))
        self.logger.info("load codemirror.css")

        fragment.add_javascript(Util.load_resource("static/js/src/codemirror.js"))
        self.logger.info("load codemirror.js")

        fragment.add_javascript(Util.load_resource("static/js/src/uc_codemirror.js"))
        self.logger.info("load uc_codemirror.js")
        fragment.initialize_js('UcCodemirrorXBlock')
        self.logger.info("initialize_js(UcCodemirrorXBlock)")
        return fragment

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("UcCodemirrorXBlock",
             """<vertical_demo>
                
                </vertical_demo>
             """),
        ]
