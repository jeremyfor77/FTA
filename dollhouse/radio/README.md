# Dollhouse Radio — how to add songs

1. Drop your music files into THIS folder. MP3, MP4, M4A, WAV, and OGG all work.
2. Right-click `update_playlist.ps1` → **Run with PowerShell**. That rebuilds `playlist.json` from whatever songs are in the folder.
3. Publish the site: ask Claude to push, or commit + push this repo to `main`.

The radio on the page reads `playlist.json` — if a song is in the folder but not in that file, it won't play. Song names on the radio come from the filename (`sunny-day-dance.mp3` shows as "sunny day dance"), so name files nicely.
