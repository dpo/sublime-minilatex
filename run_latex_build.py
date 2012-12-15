import sublime
import sublime_plugin

class RunLatexBuildCommand(sublime_plugin.WindowCommand):
    def run(self, build_system, reset_to):
        self.window.run_command( "set_build_system", {"file": build_system } )
        self.window.run_command( "build" )
        self.window.run_command( "set_build_system", {"file": reset_to})