Summary:	A powerful GTK2 media player
Name:		exaile
Version:	0.2.5
Release:	1
Source0:	http://www.exaile.org/files/%{name}_%{version}.tar.gz
# Source0-md5:	f700d561e3cf756bcdcf4c006b132d51
Patch0:		%{name}-python-2.5.patch
License:	GPL
Group:		Applications/X11
URL:		http://www.exaile.org/
BuildRequires:	python-pygtk-devel >= 2.8
Requires:	python-dbus >= 0.71
Requires:	gstreamer-plugins-base >= 0.10
Requires:	gstreamer-plugins-good >= 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exaile is a media player aiming to be similar to KDE's AmaroK, but for
gtk2. It incorporates many of the cool things from AmaroK (and other
media players).

Some of the features are:
- automatic fetching of album art
- handling of large libraries
- lyrics fetching
- artist/album information via the wikipedia
- last.fm support
- optional iPod support (assuming you have python-gpod installed).
- builtin shoutcast directory browser
- tabbed playlists
- blacklisting of tracks
- downloading of guitar tabs from fretplay.com
- submitting played tracks on the iPod to last.fm

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_menudir}

%{__make}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/exaile.py
%{_datadir}/%{name}/exaile.glade
%{_datadir}/%{name}/mmkeys.so
%{_datadir}/%{name}/images
%{_datadir}/%{name}/po
%{_datadir}/%{name}/sql
%{_datadir}/%{name}/xl
%{_desktopdir}/*
%{_pixmapsdir}/*
