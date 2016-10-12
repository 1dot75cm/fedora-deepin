Name:           deepin-gettext-tools
Version:        1.0.3
Release:        1%{?dist}
Summary:        Deepin Gettext Tools

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       python2 gettext
#BuildRequires:  

Provides:       %{name}

#%global debug_package %{nil}

%description
Deepin Gettext Tools


%prep
%autosetup %{version}.tar.gz#%{name}

%build
%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

find -iname "*.py" | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

sed -e 's/sudo cp/cp/' -i src/generate_mo.py
sed -e 's/qmake/qmake-qt5/' -e '/lupdate/d' -i Makefile

%install
make DESTDIR="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_prefix}/lib/*


%changelog
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.3-1
- Initial package build