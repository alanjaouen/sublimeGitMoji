import sublime


class sublimeGitMojiSettings:
    def __init__(self, parent=None):
        self.parent = parent
        self.global_settings = sublime.load_settings(
            "SublimeGitMoji.sublime-settings")

    def get(self, key, default=None):
        window = sublime.active_window()
        view = window.active_view()
        project_sublimeGitMoji_settings = view.settings().get("SublimeGitMoji", {}) or {}
        print(project_sublimeGitMoji_settings.keys)
        if key in project_sublimeGitMoji_settings:
            return project_sublimeGitMoji_settings[key]

        # fall back to old style project setting

        project_data = window.project_data()
        if project_data and "SublimeGitMoji" in project_data:
            project_sublimeGitMoji_settings = project_data["SublimeGitMoji"]
            if key in project_sublimeGitMoji_settings:
                return project_sublimeGitMoji_settings.get(key)

        return self.global_settings.get(key, default)
