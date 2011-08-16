#
# TODO:	- separate plugins/*
#
Summary:	A powerful GTK+2 media player
Summary(pl.UTF-8):	Potężny odtwarzacz multimediów oparty na GTK+2
Name:		exaile
Version:	0.3.2.2
Release:	1
# GPL v2 in COPYING; GPL v1+ in license.txt; Artistic/Perl in lib/wmainfo.py
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://launchpad.net/exaile/0.3.2/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	b3fd87e40af6592df0b511183ca49408
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
%{__rm} po/frp.po

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
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/zh

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
