%define name	somaplayer
%define version 0.5.3
%define release %mkrel 3
%define major	0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

%define build_plf 0
%{?_with_plf: %global build_plf 1}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Music player for MP3, Ogg, wav, audio CDs, MP3 streams, and Ogg streams
Group:		System/Servers
License:	GPL
URL:		https://www.somasuite.org/somaplayer.php
Source:		http://soma.realityhacking.org/src/%{name}-%{version}.tar.gz
Patch:      somaplayer-fix-format-errors.patch
BuildRequires:	pkgconfig
BuildRequires:	libopenssl-devel
BuildRequires:	confuse-devel
BuildRequires:	libcdda-devel
BuildRequires:	libshout-devel
BuildRequires:	libmad-devel
BuildRequires:	libid3-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libsndfile-devel
BuildRequires:	gtk+2-devel
BuildRequires:	zlib-devel
%if %build_plf
BuildRequires:	liblame-devel
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
somaplayer is music player for MP3, Ogg, wav, audio CDs, MP3 streams, and Ogg
streams. It is able to use the appropriate sound drivers or demons or to stream
directly to an Icecast server (Icecast2 or SHOUTcast) or to encode in MP3 and
Ogg Vorbis. It also acts as a sound daemon that is able to accept connections
from other somaplayers or any other sound player (xmms, mpg123, and others)
thanks to a special wrapper.

%if %build_plf
The PLF build provide additional support mp3, which is covered by software
patents
%endif

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}somaplayer0-devel < 0.5.2-9

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n %name-%version
%patch -p1

%build
%configure2_5x --disable-ao
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean 
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h

