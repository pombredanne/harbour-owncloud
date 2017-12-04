# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-owncloud

# >> macros
%define debug_package %{nil}
%define __requires_exclude ^libqwebdav|libnemonotifications-qt5.*$
%define __provides_exclude_from ^%{_datadir}/.*$
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    ownCloud
Version:    0.5.2
Release:    1
Group:      Qt/Qt
License:    GPLv2
URL:        https://github.com/beidl/harbour-owncloud
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-owncloud.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Unofficial NextCloud/ownCloud client for SailfishOS

%package daemon
Summary:   NextCloud/ownCloud background task for automatic camera backups

%description daemon
Nextcloud/ownCloud background task for automatic camera backups

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files daemon
%defattr(755,root,root,-)
%{_bindir}/%{name}-daemon
%{_bindir}/%{name}-permissiond
%defattr(-,root,root,-)
/usr/lib/systemd/user/%{name}-daemon.service
/usr/lib/systemd/user/%{name}-permissiond.service
%{_datadir}/nemo-transferengine/plugins/
/usr/lib/nemo-transferengine/plugins/libowncloudshareplugin.so
/usr/lib/qt5/qml/com/github/beidl/harbourowncloud/libharbourowncloudqmlplugin.so
/usr/lib/qt5/qml/com/github/beidl/harbourowncloud/qmldir

# >> files
# << files

%post daemon
/bin/systemctl-user enable harbour-owncloud-daemon.service >/dev/null 2>&1 || :
/bin/systemctl-user enable harbour-owncloud-permissiond.service >/dev/null 2>&1 || :
/bin/systemctl-user restart harbour-owncloud-daemon.service >/dev/null 2>&1 || :
/bin/systemctl-user restart harbour-owncloud-permissiond.service >/dev/null 2>&1 || :
