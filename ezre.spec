Name: xbox-360-media-center
Version: v1.0
Summary: Local file conversion + YouTube downloader specialized in creating media files compatible with the native Xbox 360 video player, with 1080p support.
Release: 1
License: 3-BSD
URL: https://github.com/alex-free/xbox-360-media-center
Packager: Alex Free
Group: Unspecified

%description
Local file conversion + YouTube downloader specialized in creating media files compatible with the native Xbox 360 video player, with 1080p support.

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/x360mc %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/x360mc
cp %{_sourcedir}/yt-dlp_linux %{buildroot}/usr/share/x360mc/yt-dlp

%files
/usr/bin/x360mc
/usr/share/x360mc
