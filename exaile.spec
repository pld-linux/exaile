#
# TODO:	- separate plugins/*
#	- solve this:
# ** Message: pygobject_register_sinkfunc is deprecated (GstObject)
# WARNING : Could not enable auto sink, attempting to autoselect.
# Traceback (most recent call last):
#  File "/usr/lib/exaile/exaile.py", line 62, in <module>
#    main()
#  File "/usr/lib/exaile/exaile.py", line 59, in main
#    exaile = main.Exaile()
#  File "/usr/lib/exaile/xl/main.py", line 102, in __init__
#    self.__init()
#  File "/usr/lib/exaile/xl/main.py", line 138, in __init
#    self.__show_splash()
#  File "/usr/lib/exaile/xl/main.py", line 266, in __show_splash
#    import xlgui
#  File "/usr/lib/exaile/xlgui/__init__.py", line 52, in <module>
#    from xlgui import cover
#  File "/usr/lib/exaile/xlgui/cover.py", line 40, in <module>
#    from xl import (
#  File "/usr/lib/exaile/xl/player/__init__.py", line 61, in <module>
#    PLAYER = get_player()()
#  File "/usr/lib/exaile/xl/player/engine_normal.py", line 46, in __init__
#    pre_elems=[pipe.ProviderBin("stream_element")])
#  File "/usr/lib/exaile/xl/player/_base.py", line 50, in __init__
#    self.mainbin = pipe.MainBin(pre_elems=pre_elems)
#  File "/usr/lib/exaile/xl/player/pipe.py", line 64, in __init__
#    self.add(*self._elements)
#TypeError: argument must be a GstElement
#
Summary:	A powerful GTK+2 media player
Summary(pl.UTF-8):	Potężny odtwarzacz multimediów oparty na GTK+2
Name:		exaile
Version:	0.3.2.1
Release:	0.1
# GPL v2 in COPYING; GPL v1+ in license.txt; Artistic/Perl in lib/wmainfo.py
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://launchpad.net/exaile/0.3.2/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	7ecfa9e52a9f2882717b3483518b604b
URL:		http://www.exaile.org/
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	intltool
BuildRequires:	python-pygtk-devel >= 2:2.18.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	which
Requires:	gstreamer-plugins-base >= 0.10
Requires:	gstreamer-plugins-good >= 0.10
Requires:	python-dbus >= 0.71
Requires:	python-gstreamer
Requires:	python-mutagen
Requires:	python-pygobject >= 2.26.0
Requires:	python-pygtk-glade >= 2:2.18.0
Requires:	python-sqlite
Suggests:	brasero
Suggests:	gstreamer-audiosink
Suggests:	gstreamer-mad
Suggests:	k3b
Suggests:	python-gnome-extras-mozilla
Suggests:	serpentine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exaile is a media player aiming to be similar to KDE's AmaroK, but for
GTK+2. It incorporates many of the cool things from AmaroK (and other
media players).

Some of the features are:
- automatic fetching of album art
- handling of large libraries
- lyrics fetching
- artist/album information via the wikipedia
- last.fm support
- optional iPod support (assuming you have python-gpod installed)
- builtin shoutcast directory browser
- tabbed playlists
- blacklisting of tracks
- downloading of guitar tabs from fretplay.com
- submitting played tracks on the iPod to last.fm

%description -l pl.UTF-8
Exaile to odtwarzacz multimediów mający być podobny do AmaroKa, ale
dla GTK+2. Łączy wiele dobrych cech AmaroKa (i innych odtwarzaczy
multimediów).

Niektóre możliwości to:
- automatyczne pobieranie okładki albumu
- obsługa dużych bibliotek
- pobieranie tekstów utworów
- informacje o wykonawcy/albumie z wikipedii
- obsługa last.fm
- opcjonalna obsługa iPoda (przy zainstalowanym pakiecie python-gpod)
- wbudowana przeglądarka katalogów shoutcastów
- playlisty z zakładkami
- czarna lista ścieżek
- ściąganie tabulatur gitarowych z fretplay.com
- przesyłanie ścieżek odtworzonych na iPodzie do last.fm

%prep
%setup -q

# useless, there are bigger correspondent locales
rm -f po/{es_ES.po,frp.po,he_IL.po,it_IT.po,tr_TR.po}

%build
%{__make} \
	PREFIX=%{_prefix} \
	LIBINSTALLDIR=/%{_lib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBINSTALLDIR=/%{_lib}

# unsupported
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/zh

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_sysconfdir}/xdg/exaile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/exaile/settings.ini
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/exaile.1*
# maybe seperate subpackages for plugins?
%{_datadir}/%{name}/plugins
