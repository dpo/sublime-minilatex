import sublime_plugin


class RunLatexBuildCommand(sublime_plugin.WindowCommand):

  def run(self, build_systems=None):

    if build_systems is None:
      return
    reset_to = build_systems[-1]
    for build_system in build_systems[:-1]:
      self.window.run_command( "set_build_system", {"file": build_system } )
      self.window.run_command( "build" )
    self.window.run_command( "set_build_system", {"file": reset_to})
