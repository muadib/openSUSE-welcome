Name:           korora-welcome
Version:        18.0
Release:        1%{?dist}
Summary:        Korora welcome utility

License:        GPLv2+
URL:            http://kororaproject.org
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       python-simplejson pygobject3

%description
The Korora Welcome utility provides a simple interface for accessing all
the relevant information for a new user of Korora.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}

cp -a data/* %{buildroot}%{_datadir}/%{name}
cp -a icons/* %{buildroot}%{_datadir}/icons/hicolor/
install -p -m 644 korora-welcome.desktop %{buildroot}%{_datadir}/applications/korora-welcome.desktop
install -p -m 755 korora-welcome %{buildroot}%{_bindir}/korora-welcome

# validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/korora-welcome.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/korora-welcome
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/korora-welcome.desktop

%changelog
* Fri Mar 15 2013 Ian Firns <firnsy@kororaproject.org> - 0.18.0-1
- Initial version.
