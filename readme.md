# Xbox 360 Media Center (X360MC)

_By Alex Free_.

Local file conversion + YouTube downloader specialized in creating media files compatible with the native Xbox 360 video player, with 1080p support. Said output files can be streamed from a PC server over your LAN, copied to a USB flash drive, or FTP'd to the HDD.

| [Homepage](https://alex-free.github.io/xbox-360-media-center) | [Github](https://github.com/alex-free/xbox-360-media-center) |

## Table Of Contents

* [Downloads](#downloads)
* [Usage](#usage)
* [Additional Info](#additional-info)
* [Frequently Asked Questions](frequently-asked-questions)
* [Bundled Software](#bundled-software)
* [Credits](#credits)
* [License](license.md)
* [Building](build.md)

## Downloads

The portable releases include all the dependencies required to run Xbox 360 Media Center. The `.deb` and `.rpm` Linux package files will download any required dependencies on your first run if they are not already installed on your system using your package manager.

### Version 1.0 (4/4/2025)

Changes:

* Initial release.

----------------------------------------------------

* [xbox-360-media-center-v1.0-mac-os-x86\_64-portable.zip](https://github.com/alex-free/xbox-360-media-center/releases/download/v1.0/xbox-360-media-center-v1.0-mac-os-x86_64-portable.zip) _Portable Release for Mac OS 10.13 and above (64 bit)_

* [xbox-360-media-center-v1.0-linux-x86\_64-portable.zip](https://github.com/alex-free/xbox-360-media-center/releases/download/v1.0/xbox-360-media-center-v1.0-linux-x86_64-portable.zip) _Portable Release for x86\_64 Linux (64 bit)_

* [xbox-360-media-center-v1.0.deb](https://github.com/alex-free/xbox-360-media-center/releases/download/v1.0/xbox-360-media-center-v1.0.deb) _Deb package file for x86\_64 Linux (64 bit)_

* [xbox-360-media-center-v1.0-1.x86_64.rpm](https://github.com/alex-free/xbox-360-media-center/releases/download/v1.0/xbox-360-media-center-v1.0-1.x86_64.rpm) _RPM package file for x86\_64 Linux (64 bit)_

---------------------------------------

## Usage

`x360mc -c <input media file>     Convert media file to an Xbox 360 compatible H.264 MP4 (up to 1080p).`

`x360mc -c <input folder of media files>      Recursively convert a folder of .mkv or .mp4 files to Xbox 360 compatible H.264 MP4s (up to 1080p).`

`x360mc -yl <YouTube URL>     Download YouTube video as an Xbox 360 compatible H.264 MP4 using the lower bitrate set and highest resolution availble up to 1080p (must have double quotes around URL).`

`x360mc -yh <YouTube URL>     Download YouTube video as an Xbox 360 compatible H.264 MP4 using the highest bitrate set and highest resolution available up to 1080p (must have double quotes around URL).`

`x360mc -yu       Update YouTube-DLP.`

## Additional Info

You can setup a server to stream files with using Gnome Linux desktop by going to your settings app and turning on media file sharing. Windows has this functionality built in as well.

All converted files will have `-x360mc` at the end of their filename before the file extension, to differentiate from the original sources. For recursive conversions, a folder inside of the given input folder with `-x360mc` appended to the folder name will contain all the converted files instead.

You must install the Optional media update from December 12th 2011 to playback the converted media files here. I have included this in the portable releases if you need it for RGH/JTAG/BadUpdate consoles that can't download it via Xbox Live (which happens automatically if your connected to the internet on an unmodified console). If you are using the Linux package file releases, you can download it separately from [here](https://digiex.net/attachments/optional-media-update-12-12-2011-zip.7794/).

To install the Optional media update from December 2011 manually on an RGH/JTAG/BadUpdate console, copy the `FFFE07DF` folder from the portable release or the separate download to `\Content\0000000000000000\` on your HDD. Keep in mind that if your using a BadUpdate console, the update won't work until you run the exploit on your console.

## Frequently Asked Questions

Q: Why?
A: I grew up on Xbox 360. Everyone I knew and myself streamed YouTube with it over a decade ago now. I watched my first Anime on mine, and some OG YIFY/YTS movies. Something that always bothered me was that some media files just don't work and exit with a cryptic error code. This is because the native Xbox 360 video player is both extremely picky about the video/audio codecs it supports and extremely outdated (last updated codecs are from 2011). Xbox 360 Media Center however is even better then what I had in 2016. The native YouTube app only does 720p (while this does 1080p) and has Ads. Also, with my console now being a BadUpdate exploited one I can't use the official YouTube app anymore anyways. Lastly, this guarantees the media files will be compatible with the native Xbox 360 video player and won't give you some annoying cryptic error code.

Q: But like, just use a Smart TV/Roku/Fire TV/Your Computer?
A: If your asking this, Xbox 360 Media Center isn't for you and that's OK!

Q: What's the output quality?
A: Basically for local file conversion you get OG circa 2017 YIFY video quality, with better audio (audio bitrate is the same as YouTube, 128K Low Complexity AAC). This keeps file sizes low, is a standard of quality most people can understand, and guarantees compatibility. For YouTube, your getting the straight up H.264 AAC formats that they offer still to this day (no conversion happens for YouTube which is why it is so fast). There are 2 sets of H.264 video formats available. If you use the `-yl` argument, you will get the lower bitrate H.264 videos. If you use the `-yh` argument, you will get the highest bitrate H.264 videos. All downloaded youtube videos use the highest AAC LC audio (133k) available.

Q: What input media files are supported?
A: Literally anything as long as it is 1080p 30FPS or lower. Do not give it anything with a higher resolution and or frame rate.

Q: The local file conversion is really slow on my system, how can I make it go faster?
A: Try to find a h264 source. H265/HEVC and other modern formats are slower. Also lower resolutions (i.e. 720p) will increase conversion time substantially. My ancient Mac mini Late 2012 can almost do 1x speed for 720p H.264. You can also just use the fastest CPU you can find for raw performance.

Q: YouTube functionality stopped working?
A: Update youtube-dlp with the command `x360mc -yu`.

Q: I'm streaming videos over my LAN and some are stuttering/not starting/freezing during playback?
A: This is most likely do to an unstable network connection and or the server software, and not the converted media files themselves. There is a chance that if you exit out of the video and then resume it, the video will play better. Another thing you can do if using WiFI is to physically move the Xbox 360 to a location closer to the router/farther away from interference of other WiFi devices. Lastly, if playing YouTube videos you can opt for the lower bitrate videos by specifying the `-yl` argument (i.e. `x360mc -yl <video url>`. But really if you can, use an Ethernet cable with your Xbox 360 for the most stable connection to prevent these issues when using a LAN. If you can't do that, copy the files to a USB drive or FTP them to your HDD. The HDD is gonna be the most stable and fastest storage you have (you can also copy the converted media files from the USB drive to your HDD if you can't use your LAN). If your still having some kind of issue with even the HDD, open an issue on Github and tell me about it.

Q: My video is showing a black screen with audio?
A: This is some kind of bug that happens when you've been using the native Xbox 360 video player a lot (either that or with the streaming server software itself, not sure). Go back to Xbox home (exiting the video player) and start it again.

Q: My folder is empty when I browse it with the native Xbox 360 video player?
A: The file name/folder names may be too small. All filenames/folder names must be 32 characters or longer due to limitations in the video player (even when streaming). Additionally, no files may be bigger then 4GBs.

Q: Why does this use HandBrake internally and not FFmpeg?
A: FFmpeg converted media files just won't work with the native Xbox 360 video player. I have tried everything. Don't waste your time if your developing something similar!

Q: The Linux package releases don't use my distribution's yt-dlp?
A: Nope! The Linux distributions are too slow at updating yt-dlp, so even the Linux package releases use their own internal yt-dlp that may be updated with the command `x360mc -yu`.

Q: Why is Mac OS 10.13 the lowest supported?
A: The latest HandBrakeCLI requires Mac OS 10.13 as a minimum. Every other dependency actually only requires Mac OS X 10.9.

## Bundled Software

* [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases) (LGPLv3 license). Portable Linux build use a static version of ffmpeg v7.0.2 from [here](https://johnvansickle.com/ffmpeg/). Portable Mac build use a build of FFmpeg v7.1.1 from [here](https://evermeet.cx/ffmpeg/). The Linux package file releases use the FFmpeg from your Linux distro (which will automatically be installed if they are not detected as such).

* [HandBrake](https://github.com/BtbN/FFmpeg-Builds/releases) (GPLv2 license). The Portable Linux build use v1.9.2 from [Fedora](https://rpmfind.net/linux/rpm2html/search.php?query=handbrake), made portable with my [PLED](https://github.com/alex-free/pled) tool for all Linux distributions. The portable Mac build use v1.9.2 from [here](https://handbrake.fr/downloads2.php). The Linux package file releases use the HandBrake from your Linux distro (which will automatically be installed if they are not detected as such).

* [YouTube-DLP](https://github.com/yt-dlp/yt-dlp) (Unlicense). All releases (portable and linux package files) use the latest downloads in the [Alternatives](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#alternatives) section at the time of each release. This can be updated by Xbox 360 Media Center with the command `x360mc -u`.

## Credits

* [2017 YTS Encoding Settings](https://gist.github.com/kuntau/a7cbe28df82380fd3467).
* [Xbox 360 Optional Media Update Download On Digiex](https://digiex.net/threads/xbox-360-optional-media-update-download.3143/).
