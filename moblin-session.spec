Name: moblin-session
Summary: Moblin User Experience Startup Scripts
Group: Graphical desktop/Other
Version: 0.13
License: GPLv2
URL: https://www.moblin.org
Release: %mkrel 4
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch0: moblin-session-0.13-path.patch
Patch1: moblin-session-0.13-gconf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: telepathy-mission-control
Requires: moblin-ux-settings

%description
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .session
%patch1 -p1 -b .gconf
cat > 10moblin <<EOF
NAME=Moblin
DESC=Moblin Desktop Environment
EXEC=%{_sysconfdir}/xdg/moblin/xinitrc
SCRIPT:
exec %{_sysconfdir}/xdg/moblin/xinitrc
EOF

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_datadir}/xsessions/moblin.desktop
install -d %{buildroot}%{_sysconfdir}/X11/wmsession.d
install -m755 10moblin %{buildroot}%{_sysconfdir}/X11/wmsession.d/
chmod 755 %{buildroot}%{_sysconfdir}/xdg/moblin/xinitrc

%find_lang %{name}

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
	if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
		mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
	fi
done

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/startmoblin
%{_sysconfdir}/xdg/moblin/xinitrc
%{_sysconfdir}/X11/wmsession.d/10moblin
