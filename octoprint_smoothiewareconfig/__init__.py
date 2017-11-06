# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class smoothiewareConfigPlugin(octoprint.plugin.StartupPlugin):

	##~~ Startup plugin mixin
	def on_after_startup(self):
		self._logger.info("SmoothiewareConfigPlugin loaded!")

	##-- Image upload extenstion tree hook
	def get_extension_tree(self, *args, **kwargs):
		return dict(
			model=dict(
				smoothiwarefiles=["bin"]
			),
			machinecode=dict(
				smoothiwarefiles=["txt"]
			)
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			smoothiewareconfig=dict(
				displayName="OctoPrint-SmoothiewareConfig Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-SmoothiewareConfig",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-SmoothiewareConfig/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Octoprint-SmoothiewareConfig Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = smoothiewareConfigPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
		"octoprint.filemanager.extension_tree": __plugin_implementation__.get_extension_tree
	}

