Summary:	A powerful GTK2 media player
Name:		exaile
Version:	0.2.5b
Release:	1
Source0:	http://www.exaile.org/files/%{name}_%{version}.tar.gz
# Source0-md5:	1e8439c85536ce83d05a0b281a918f91
######		Unknown group!
License:	GPL
Group:		Applications/X11
URL:		http://www.exaile.org/
BuildRequires:	python-pygtk-devel >= 2.0
Requires:	dbus-python >= 0.71
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
%{_datadir}/%{name}/
%{_desktopdir}/*
%{_pixmapsdir}/*
%_menudir/%{name}
