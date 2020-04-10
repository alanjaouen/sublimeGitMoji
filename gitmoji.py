import json
import sublime
import sublime_plugin


def parse_json():
    my_file = sublime.load_binary_resource(
        "/".join(("Packages", __package__, "gitmojis.json")))
    return json.loads(my_file.decode("utf-8"))['gitmojis']


class SelectGitmojiCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        data = parse_json()
        data = [[emoji['emoji'], emoji['description'], "{} {}".format(
            emoji['emoji'], emoji['description'])] for emoji in data]
        list_item = [item[-1] for item in data]

        def callback(selection):
            if selection >= 0:
                emoji = data[selection][0]
                self.view.run_command("insert", {"characters": emoji})

        self.view.window().show_quick_panel(list_item, callback)


class SelectGitmojiShortcodeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        data = parse_json()
        data = [[emoji['code'], emoji['description'], "|{}| {}".format(
            emoji['code'], emoji['description'])] for emoji in data]
        list_item = [item[-1] for item in data]

        def callback(selection):
            if selection >= 0:
                emoji = data[selection][0]
                self.view.run_command("insert", {"characters": emoji})

        self.view.window().show_quick_panel(list_item, callback)
