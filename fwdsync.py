# Implement forward sync with Skim.

from sublime_plugin import TextCommand
import os.path
import subprocess


class ForwardSyncCommand(TextCommand):

  def run(self, edit, **kwargs):

    skim_location = kwargs.get('skim_location', '/Applications')
    displayline = os.path.join(skim_location,
                               'Skim.app/Contents/SharedSupport/displayline')

    tex_file = self.view.file_name()

    # The PDF file name is the project name.
    pdf_file, _ = os.path.splitext(self.view.window().project_file_name())
    pdf_file += '.pdf'

    line, _ = self.view.rowcol(self.view.sel()[0].end())
    line += 1  # ST line numbers are zero based.

    subprocess.call([displayline, '-r', '-g', str(line), pdf_file, tex_file])
