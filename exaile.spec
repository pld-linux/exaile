#
# TODO:	- separate plugins/*
#
Summary:	A powerful GTK+3 media player
Summary(pl.UTF-8):	Potężny odtwarzacz multimediów oparty na GTK+3
Name:		exaile
Version:	4.1.4
Release:	1
# GPL v2 in COPYING; GPL v1+ in license.txt; Artistic/Perl in lib/wmainfo.py
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	https://github.com/exaile/exaile/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1b378662752824764ea51eb620118f79
URL:		https://exaile.org/
BuildRequires:	gettext-tools
BuildRequires:	help2man
BuildRequires:	python3 >= 3.6
BuildRequires:	python3-pygobject3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.000
BuildConflicts:	python3-bsddb3
Requires:	gstreamer
Requires:	gstreamer-plugins-good
Requires:	librsvg
Requires:	python3-berkeleydb
Requires:	python3-dbus
Requires:	python3-discid
Requires:	python3-feedparser
Requires:	python3-musicbrainzngs
Requires:	python3-mutagen >= 1.42.0-8
Requires:	python3-pycairo
Requires:	python3-pygobject3
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Recommends:	gstreamer-plugins-bad
Recommends:	gstreamer-plugins-ugly
Recommends:	python3-pillow
Recommends:	udisks2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exaile is a media player aiming to be similar to KDE's AmaroK, but for
GTK+3. It incorporates many of the cool things from AmaroK (and other
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
dla GTK+3. Łączy wiele dobrych cech AmaroKa (i innych odtwarzaczy
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

%package -n bash-completion-%{name}
Summary:	Bash completion for exaile music player
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów odtwarzacza muzyki exaile
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-%{name}
Bash completion for exaile.

%description -n bash-completion-%{name} -l pl.UTF-8
Bashowe dopełnianie parametrów odtwarzacza muzyki exaile.

%package -n fish-completion-%{name}
Summary:	Fish completion for exaile music player
Summary(pl.UTF-8):	Dopełnianie parametrów w fish dla odtwarzacza muzyki exaile
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish

%description -n fish-completion-%{name}
Fish completion for exaile music player.

%description -n fish-completion-%{name} -l pl.UTF-8
Dopełnianie parametrów w fish dla odtwarzacza muzyki exaile.

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%prep
%setup -q

# useless, there are bigger correspondent locales
%{__rm} po/frp.po

%build
%{__make} \
	PREFIX=%{_prefix} \
	LIBINSTALLDIR=/%{_datadir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBINSTALLDIR=/%{_datadir}

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{cy,kk,ie,ur,zh}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_sysconfdir}/xdg/exaile
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/exaile/settings.ini
%{_datadir}/%{name}
%{_datadir}/metainfo/exaile.appdata.xml
%{_datadir}/dbus-1/services/org.exaile.Exaile.service
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*x*/apps/exaile.png
%{_iconsdir}/hicolor/scalable/apps/exaile.svg
%{_mandir}/man1/exaile.1*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/%{name}

%files -n fish-completion-%{name}
%defattr(644,root,root,755)
%{fish_compdir}/%{name}.fish
