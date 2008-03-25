Summary:	A powerful GTK+2 media player
Summary(pl.UTF-8):	Potężny odtwarzacz multimediów oparty na GTK+2
Name:		exaile
Version:	0.2.12
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.exaile.org/files/%{name}_%{version}~gutsyppa2.tar.gz
# Source0-md5:	95efa2899ea5dfd251e933c36d1849ed
Patch0:		%{name}-python-2.5.patch
Patch1:		%{name}-FHS.patch
URL:		http://www.exaile.org/
BuildRequires:	python-pygtk-devel >= 2.8
Requires:	python-dbus >= 0.71
Requires:	python-gstreamer
Requires:	python-mutagen
Requires:	python-pygtk-glade
Requires:	python-sqlite
Requires:	gstreamer-plugins-base >= 0.10
Requires:	gstreamer-plugins-good >= 0.10
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
#%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/exaile.py
%{_datadir}/%{name}/exaile.glade
%attr(755,root,root) %{python_sitearch}/mmkeys.so
%{_datadir}/%{name}/images
%{_datadir}/%{name}/po
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/sql
%{_datadir}/%{name}/xl
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
