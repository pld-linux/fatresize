Summary:	Resize an FAT16/FAT32 volume non-destructively
Summary(pl.UTF-8):	Niedestrukcyjna zmiana rozmiaru wolumenów FAT16/FAT32
Name:		fatresize
Version:	1.0.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fatresize/%{name}-%{version}.tar.bz2
# Source0-md5:	3bfac57c0801d33ad39e740841e6441e
URL:		http://sourceforge.net/projects/fatresize/
BuildRequires:	parted-devel >= 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fatresize is a command line tool for non-destructive resizing of
FAT16/FAT32 file systems. It is based on the GNU Parted library. The
main target of the project is to be used with the EVMS FAT plugin.

%description -l pl.UTF-8
fatresize to działające z linii poleceń narzędzie do niedestrukcyjnej
zmiany rozmiaru systemów plików takich jak FAT16/32. Oparte jest na
bibliotece parted. Głównym przeznaczeniem tego projektu jest używanie
go z wtyczką FAT EVMS-a.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/*
