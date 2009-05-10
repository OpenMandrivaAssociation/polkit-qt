Name:           polkit-qt
Version:        0.9.2
Summary:        Assists in the Recovery and Prevention of Repetitive Strain Injury
Release:        %mkrel 3
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.rsibreak.org
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         polkit-qt-0.9.2-fix-link.patch
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  polkit-devel
Requires:       kdebase4-runtime

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
%_kde_libdir/libpolkit-qt-core.so.%{libpolkit_qt_core_major}*

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
%_kde_libdir/libpolkit-qt-gui.so.%{libpolkit_qt_gui_major}*


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
%_kde_libdir/pkgconfig/polkit-qt-core.pc
%_kde_libdir/pkgconfig/polkit-qt-gui.pc
%_kde_libdir/pkgconfig/polkit-qt.pc
%_kde_includedir/PolicyKit/polkit-qt
%_kde_libdir/libpolkit-qt-core.so
%_kde_libdir/libpolkit-qt-gui.so

#-----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build

%cmake_kde4
%make


%install
rm -rf %buildroot
cd build
make DESTDIR=%buildroot install
cd ..

%clean
rm -rf %{buildroot}

