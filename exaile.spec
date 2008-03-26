# TODO:
#	package plugins/*
#	segfault on exit (python: Python/pystate.c:563: PyGILState_Ensure: Assertion `autoInterpreterState' failed)
#
Summary:	A powerful GTK+2 media player
Summary(pl.UTF-8):	Potężny odtwarzacz multimediów oparty na GTK+2
Name:		exaile
Version:	0.2.12
Release:	1
# GPL v2 in COPYING; GPL v1+ in license.txt; Artistic/Perl in lib/wmainfo.py
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.exaile.org/files/%{name}_%{version}~gutsyppa2.tar.gz
# Source0-md5:	95efa2899ea5dfd251e933c36d1849ed
URL:		http://www.exaile.org/
BuildRequires:	python-pygtk-devel >= 2.8
Requires:	python-dbus >= 0.71
Requires:	python-gstreamer
Requires:	python-mutagen
Requires:	python-pygtk-glade
Requires:	python-sqlite
Requires:	gstreamer-plugins-base >= 0.10
Requires:	gstreamer-plugins-good >= 0.10
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{python_sitearch}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/images/default_theme
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/sql
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/xl/{gui,media,panels,plugins}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec python %{_datadir}/%{name}/exaile.py $@
EOF

install mmkeys.so $RPM_BUILD_ROOT%{python_sitearch}
install exaile.1 $RPM_BUILD_ROOT%{_mandir}/man1
install exaile.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install exaile.glade $RPM_BUILD_ROOT%{_datadir}/%{name}
install equalizer.ini $RPM_BUILD_ROOT%{_datadir}/%{name}
install data/settings_meta.ini $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install lib/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
install sql/*.sql $RPM_BUILD_ROOT%{_datadir}/%{name}/sql
install xl/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/xl
install xl/gui/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/xl/gui
install xl/media/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/xl/media
install xl/panels/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/xl/panels
install xl/plugins/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/xl/plugins
install xl/plugins/*.glade $RPM_BUILD_ROOT%{_datadir}/%{name}/xl/plugins
install images/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/images
install images/default_theme/*.png \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/images/default_theme
install images/largeicon.png $RPM_BUILD_ROOT%{_pixmapsdir}
install exaile.desktop $RPM_BUILD_ROOT%{_desktopdir}

cd po
for d in */LC_MESSAGES; do
	install -d $RPM_BUILD_ROOT%{_localedir}/$d
	install $d/exaile.mo $RPM_BUILD_ROOT%{_localedir}/$d
done
cd ..

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc changelog
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/exaile.py
%{_datadir}/%{name}/exaile.glade
%attr(755,root,root) %{python_sitearch}/mmkeys.so
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/settings_meta.ini
%{_datadir}/%{name}/equalizer.ini
%{_datadir}/%{name}/images
#{_datadir}/%{name}/plugins
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.py
%dir %{_datadir}/%{name}/sql
%{_datadir}/%{name}/sql/*.sql
%dir %{_datadir}/%{name}/xl
%{_datadir}/%{name}/xl/*.py
%dir %{_datadir}/%{name}/xl/gui
%{_datadir}/%{name}/xl/gui/*.py
%dir %{_datadir}/%{name}/xl/media
%{_datadir}/%{name}/xl/media/*.py
%dir %{_datadir}/%{name}/xl/panels
%{_datadir}/%{name}/xl/panels/*.py
%dir %{_datadir}/%{name}/xl/plugins
%{_datadir}/%{name}/xl/plugins/*.py
%{_datadir}/%{name}/xl/plugins/plugins.glade
%{_desktopdir}/*.desktop
%{_mandir}/man1/exaile.1*
%{_pixmapsdir}/*
