Name: moblin-session
Summary: Moblin User Experience Startup Scripts
Group: Graphical desktop/Other
Version: 0.13
License: GPLv2
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch0: moblin-session-0.13-path.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: telepathy-mission-control

%description
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .session

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std

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
%{_datadir}/xsessions/moblin.desktop
