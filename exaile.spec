Summary:	A powerful GTK+2 media player
Summary(pl):	Pot�ny odtwarzacz multimedi�w oparty na GTK+2
Name:		exaile
Version:	0.2.8
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.exaile.org/files/%{name}_%{version}.tar.gz
# Source0-md5:	a07d5acdebbc42a72e297963f5aec249
Patch0:		%{name}-python-2.5.patch
Patch1:		%{name}-FHS.patch
URL:		http://www.exaile.org/
BuildRequires:	python-pygtk-devel >= 2.8
Requires:	python-dbus >= 0.71
Requires:	python-gstreamer
Requires:	python-mutagen
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

%description -l pl
Exaile to odtwarzacz multimedi�w maj�cy by� podobny do AmaroKa, ale
dla GTK+2. ��czy wiele dobrych cech AmaroKa (i innych odtwarzaczy
multimedi�w).

Niekt�re mo�liwo�ci to:
- automatyczne pobieranie ok�adki albumu
- obs�uga du�ych bibliotek
- pobieranie tekst�w utwor�w
- informacje o wykonawcy/albumie z wikipedii
- obs�uga last.fm
- opcjonalna obs�uga iPoda (przy zainstalowanym pakiecie python-gpod)
- wbudowana przegl�darka katalog�w shoutcast�w
- playlisty z zak�adkami
- czarna lista �cie�ek
- �ci�ganie tabulatur gitarowych z fretplay.com
- przesy�anie �cie�ek odtworzonych na iPodzie do last.fm

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
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
