# Copyright 2020-2020 the openage authors. See copying.md for legal info.
#
# pylint: disable=too-few-public-methods

"""
Organize export data (nyan objects, media, scripts, etc.)
into modpacks.
"""
from ....entity_object.conversion.modpack import Modpack
from ..aoc.modpack_subprocessor import AoCModpackSubprocessor


class RoRModpackSubprocessor:
    """
    Creates the modpacks containing the nyan files and media from the RoR conversion.
    """

    @classmethod
    def get_modpacks(cls, gamedata):
        """
        Return all modpacks that can be created from the gamedata.
        """
        aoe1_base = cls._get_aoe1_base(gamedata)

        return [aoe1_base]

    @classmethod
    def _get_aoe1_base(cls, gamedata):
        """
        Create the aoe1-base modpack.
        """
        modpack = Modpack("aoe1-base")

        mod_def = modpack.get_info()

        mod_def.set_version("1.0B")
        mod_def.set_uid(1000)

        mod_def.add_assets_to_load("data/*")

        AoCModpackSubprocessor.organize_nyan_objects(modpack, gamedata)
        AoCModpackSubprocessor.organize_media_objects(modpack, gamedata)

        return modpack
