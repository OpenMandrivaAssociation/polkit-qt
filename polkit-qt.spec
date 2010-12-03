Name:           polkit-qt
Version:        0.9.3
Summary:        Library that allows developer to access PolicyKit API
Release:        %mkrel 2
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.kde.org/
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  polkit-devel
BUildRequires:  qt4-devel
BuildRequires:  cmake
BuildRequires:  automoc4

%description
Polkit-qt is a library that allows developer to access PolicyKit 
API with a nice Qt-style API

#-----------------------------------------------------------------------------

%define libpolkit_qt_core_major 0
%define libpolkit_qt_core %mklibname polkit-qt-core %{libpolkit_qt_core_major}

%package -n %libpolkit_qt_core
Summary: Polkit-Qt core library
Group: System/Libraries

%description -n %libpolkit_qt_core
Polkit-Qt core library.

%files -n %libpolkit_qt_core
%defattr(-,root,root)
%_libdir/libpolkit-qt-core.so.%{libpolkit_qt_core_major}*

#-----------------------------------------------------------------------------

%define libpolkit_qt_gui_major 0
%define libpolkit_qt_gui %mklibname polkit-qt-gui %{libpolkit_qt_gui_major}

%package -n %libpolkit_qt_gui
Summary: Polkit-Qt core library
Group: System/Libraries

%description -n %libpolkit_qt_gui
Polkit-Qt core library.

%files -n %libpolkit_qt_gui
%defattr(-,root,root)
%_libdir/libpolkit-qt-gui.so.%{libpolkit_qt_gui_major}*

#-----------------------------------------------------------------------------

%package   devel
Summary:   Devel stuff for polkit-Qt
Group:     Development/KDE and Qt
Requires:  %libpolkit_qt_core = %version
Requires:  %libpolkit_qt_gui = %version

%description  devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%defattr(-,root,root)
%_libdir/pkgconfig/polkit-qt-core.pc
%_libdir/pkgconfig/polkit-qt-gui.pc
%_libdir/pkgconfig/polkit-qt.pc
%_includedir/PolicyKit/polkit-qt
%_libdir/libpolkit-qt-core.so
%_libdir/libpolkit-qt-gui.so

#-----------------------------------------------------------------------------

%prep
%setup -q

%build

%cmake_qt4
%make


%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

