import json
import sublime
import sublime_plugin
from sublimeGitMoji.settings import sublimeGitMojiSettings


def parse_json():
    my_file = sublime.load_binary_resource(
        "/".join(("Packages", __package__, "gitmojis.json")))
    return json.loads(my_file.decode("utf-8"))['gitmojis']

class SelectGitmojiGlobalCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        setting = sublimeGitMojiSettings()
        default_data = parse_json()
        custom_data = setting.get(key='custom_gitmojis', default=[])
        print(custom_data)
        data = default_data + custom_data
        data = [[emoji[self.to_insert], emoji['description'], self.presentation.format(
            emoji[self.to_insert], emoji['description'])] for emoji in data]
        list_item = [item[-1] for item in data]

        def callback(selection):
            if selection >= 0:
                emoji = data[selection][0]
                self.view.run_command("insert", {"characters": emoji})

        self.view.window().show_quick_panel(list_item, callback)


class SelectGitmojiCommand(SelectGitmojiGlobalCommand):

    to_insert = 'emoji'
    presentation = '{} {}'


class SelectGitmojiShortcodeCommand(SelectGitmojiGlobalCommand):

    to_insert = 'code'
    presentation = '|{}| {}'
