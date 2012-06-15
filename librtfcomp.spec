Name:		librtfcomp
Version:	1.2
Release:	1

%define 	major 0
%define		libname	%mklibname rtfcomp %major

Summary:	Library to read and write compressed RTF files
License:	GPL
Group:		System/Libraries
URL:		http://synce.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/synce/SynCE/librtfcomp/%{name}-%{version}.tar.gz
BuildRequires:	python-devel python-pyrex

%description
Can decompress and recompress compressed RTF and convert from 
UTF8 to RTF for use in things like the AirSync protocols.

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
Provides:	python-%{name}

%description -n	python-%{libname}
This package contains the python bindings for %{name}.

%prep
%setup -q

%build
%configure2_5x --program-prefix=rtfcomp- \
	       --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{libname}-devel
%{_includedir}/rtfcomp/*.h
%{_libdir}/%{name}.so

%files -n python-%{libname}
%{py_platsitedir}
