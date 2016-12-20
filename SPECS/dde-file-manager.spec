Name:           dde-file-manager
Version:        1.3.4
Release:        1%{?dist}
Summary:        Deepin File Manager

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-tool-kit gtk2 deepin-shortcut-viewer file qt5-qtsvg libsecret gsettings-qt poppler-cpp deepin-tool-kit qt5-qtx11extras ffmpegthumbnailer polkit-gnome polkit-qt5-1
BuildRequires:  qt5-qttools-devel libsecret-devel file-devel poppler-cpp-devel gtk2-devel gsettings-qt deepin-tool-kit qt5-qtsvg-devel qt5-qtx11extras-devel ffmpegthumbnailer-devel polkit-devel polkit-qt5-1-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin File Manager


%prep
%autosetup %{version}.tar.gz#%{name}

%build
sed -i 's/lrelease/lrelease-qt5/g' dde-file-manager-lib/generate_translations.sh
sed -i 's/qmake/qmake-qt5/g' vendor/prebuild

qmake-qt5 QMAKE_CFLAGS_ISYSTEM= PREFIX=%{_usr}
make

%install
make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*
%{_sysconfdir}/xdg/autostart/*
%{_libdir}/*
%{_includedir}/*
%{_sysconfdir}/dbus-1/system.d/*


%changelog
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.4-1
- Update package to 1.3.4
* Mon Oct 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.3-1
- Update package to 1.3.3
* Mon Oct 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.3-1
- Initial package build