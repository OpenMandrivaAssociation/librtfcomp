Name:		librtfcomp
Version:	1.2
Release:	2

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


%changelog
* Fri Jun 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2-1
+ Revision: 805839
- version update 1.2

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 1.1-8mdv2011.0
+ Revision: 438734
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.1-7mdv2009.1
+ Revision: 319653
- rebuild with python 2.6

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 1.1-6mdv2009.0
+ Revision: 250443
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 16 2008 Emmanuel Andry <eandry@mandriva.org> 1.1-4mdv2008.1
+ Revision: 153760
- add provides

* Fri Jan 11 2008 Emmanuel Andry <eandry@mandriva.org> 1.1-3mdv2008.1
+ Revision: 148723
- add missing provides

* Fri Jan 11 2008 Emmanuel Andry <eandry@mandriva.org> 1.1-2mdv2008.1
+ Revision: 148716
- use program-prefix to avoid conflict with coreutils
- provide python package

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jun 30 2007 Emmanuel Andry <eandry@mandriva.org> 1.1-1mdv2008.0
+ Revision: 46162
- Import librtfcomp

