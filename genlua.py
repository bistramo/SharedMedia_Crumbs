#!/usr/bin/env python3

from pathlib import Path


template = """
local LSM = LibStub("LibSharedMedia-3.0")
local koKR, ruRU, zhCN, zhTW, western = LSM.LOCALE_BIT_koKR, LSM.LOCALE_BIT_ruRU, LSM.LOCALE_BIT_zhCN, LSM.LOCALE_BIT_zhTW, LSM.LOCALE_BIT_western

local MediaType_BACKGROUND = LSM.MediaType.BACKGROUND
local MediaType_BORDER = LSM.MediaType.BORDER
local MediaType_FONT = LSM.MediaType.FONT
local MediaType_STATUSBAR = LSM.MediaType.STATUSBAR

-- -----
-- BACKGROUND
-- -----

-- -----
--  BORDER
-- ----

-- -----
--   FONT
-- -----

-- -----
--   SOUND
-- -----
{sound_files}

-- -----
--   STATUSBAR
-- -----
"""

sound_files = []

with open("soundmap.csv") as f:
    for line in f:
        filename, title = line.strip().split(",")
        sound_files.append(f'LSM:Register("sound", "|cfffff0b5Crumbs - {title}|r", [[Interface\Addons\SharedMedia_Crumbs\sound\{filename}]])')

for f in sound_files:
    print(f)

output = template.format(sound_files="\n".join(sorted(sound_files)))
with open("SharedMedia.lua", "w") as f:
    f.write(output)