Summary:	A powerful GTK+2 media player
Summary(pl):	Potê¿ny odtwarzacz multimediów oparty na GTK+2
Name:		exaile
Version:	0.2.5
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.exaile.org/files/%{name}_%{version}.tar.gz
# Source0-md5:	f700d561e3cf756bcdcf4c006b132d51
Patch0:		%{name}-python-2.5.patch
URL:		http://www.exaile.org/
BuildRequires:	FHS-fix
BuildRequires:	python-pygtk-devel >= 2.8
Requires:	python-dbus >= 0.71
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
Exaile to odtwarzacz multimediów maj±cy byæ podobny do AmaroKa, ale
dla GTK+2. £±czy wiele dobrych cech AmaroKa (i innych odtwarzaczy
multimediów).

Niektóre mo¿liwo¶ci to:
- automatyczne pobieranie ok³adki albumu
- obs³uga du¿ych bibliotek
- pobieranie tekstów utworów
- informacje o wykonawcy/albumie z wikipedii
- obs³uga last.fm
- opcjonalna obs³uga iPoda (przy zainstalowanym pakiecie python-gpod)
- wbudowana przegl±darka katalogów shoutcastów
- playlisty z zak³adkami
- czarna lista ¶cie¿ek
- ¶ci±ganie tabulatur gitarowych z fretplay.com
- przesy³anie ¶cie¿ek odtworzonych na iPodzie do last.fm

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/exaile.py
%{_datadir}/%{name}/exaile.glade
# FIXME: move ELF to %{_libdir}
%attr(755,root,root) %{_datadir}/%{name}/mmkeys.so
%{_datadir}/%{name}/images
%{_datadir}/%{name}/po
%{_datadir}/%{name}/sql
%{_datadir}/%{name}/xl
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
