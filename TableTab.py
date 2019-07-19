import sublime
import sublime_plugin

class InsertPhantomCommand(sublime_plugin.TextCommand, sublime_plugin.ViewEventListener):
    def on_modified(self):
        self.view.erase_phantoms("test")
    def run(self, edit):
        self.view.add_phantom("test", 
                              self.view.sel()[0], 
                              "<div style='\
                              padding: 0rem;\
                              margin: 0rem;\
                              padding-right: 1rem;\
                              padding-top: 0.1rem;\
                              background-color: #fff'>\
                              </div>", 
                              sublime.DRAW_NO_OUTLINE, 
                              None)

class InsertTableTabCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            self.view.insert(edit, region.a, '\uFEFF')

#1111222233334444555566667777|
#11222233334444555566667777|