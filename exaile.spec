# TODO:
#	separate plugins/*
#
Summary:	A powerful GTK+2 media player
Summary(pl.UTF-8):	Potężny odtwarzacz multimediów oparty na GTK+2
Name:		exaile
Version:	0.3.0.2
Release:	1
# GPL v2 in COPYING; GPL v1+ in license.txt; Artistic/Perl in lib/wmainfo.py
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://launchpad.net/exaile/0.3.0/0.3.0.2/+download/%{name}-%{version}.tar.gz
# Source0-md5:	6036291d14e0b77834e60bb6492ed3cc
URL:		http://www.exaile.org/
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-pygtk-devel >= 2:2.8
Requires:	gstreamer-plugins-base >= 0.10
Requires:	gstreamer-plugins-good >= 0.10
Requires:	python-dbus >= 0.71
Requires:	python-gstreamer
Requires:	python-mutagen
Requires:	python-pygtk-glade >= 2:2.8
Requires:	python-sqlite
Suggests:	brasero
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

# there's bigger and newer es.po
rm -f po/es_ES.po
# what's Franco-Provençal?
rm -f po/frp.po
# there's bigger and newer he.po
rm -f po/he_IL.po
# there's bigger and newer it.po
rm -f po/it_IT.po
# there's bigger and newer tr.po
rm -f po/tr_TR.po

%build
%{__make} \
	PREFIX=/usr

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=/usr \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_sysconfdir}/xdg/exaile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/exaile/settings.ini
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
# maybe seperate subpackages for plugins?
%{_datadir}/%{name}/plugins
