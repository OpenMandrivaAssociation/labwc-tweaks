Name:           labwc-tweaks
Version:        0~git.20251101.0
Release:        1
Summary:        GUI Configuration app for labwc
License:        BSD-3-Clause AND GPL-2.0-only
URL:            https://github.com/labwc/labwc-tweaks
Source:         https://github.com/labwc/labwc-tweaks/archive/refs/heads/master.tar.gz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       labwc

%description
labwc-tweaks is a GUI configuration application for the labwc Wayland compositor

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt

%files -f %{name}.lang
%license LICENSE BSD-3-Clause
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/labwc_tweaks.appdata.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_kab.qm
