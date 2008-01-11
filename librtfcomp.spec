Name:		librtfcomp
Version:	1.1
Release:	%mkrel 3

%define 	major 0
%define		libname	%mklibname rtfcomp %major

Summary:	Library to read and write compressed RTF files
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
License:	GPL
Group:		System/Libraries
URL:		http://synce.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/synce/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel python-pyrex

%description
Can decompress and recompress compressed RTF and convert from 
UTF8 to RTF for use in things like the AirSync protocols

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Can decompress and recompress compressed RTF and convert from 
UTF8 to RTF for use in things like the AirSync protocols

%package -n	%{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	python-%{libname}
Summary:	Python bindings for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}

%description -n	python-%{libname}
This package contains the python bindings for %{name}.

%prep
%setup -q

%build
%configure2_5x --program-prefix=rtfcomp-
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/rtfcomp/*.h
%{_libdir}/%{name}.a
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la

%files -n python-%{libname}
%defattr (-,root,root)
%{py_platsitedir}
